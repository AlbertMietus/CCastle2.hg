# Castle/CCastle RPy Writer — Context & Design Summary
# (C) Albert Mietus, 2026. Part of Castle/CCastle project
note:: Mostly generated claude as a summary of discussions

---

## 1. Project Context & Goals

**Castle** is a new programming language (under development). It has a compiler with plug-able modules like:
- caste-aigr: AIGR (Abstract Intermediate Graph Representation) — the IR of the compiler
- `castle-RPy-writer`
  - generates RPython code from AIGR
  - using RPython translator — translates RPython to C

The goal is **fast generated C code**, via RPython's translator and optimiser.
Castle is ambitious: "the best language ever" — it will have all conveniences of all known languages.
Design is work-in-progress; the AIGR is the contract between compiler phases.

---

## 2. Architecture Overview

### Key packages (namespace packages, PEP 420):
- `castle-aigr` → `castle/aigr/`, `castle/aigr_extra/`
- `castle-RPy-writer` → `castle/writers/RPy/`, `castle/writers/RPy_buildin/`

### Key classes in the writer:
- `Renderer(Visitor)` — main entry point, `visit_<AIGRType>()` methods
- `Portray` — dumb name converter (prefixes, string mappings). Auxiliary to Renderer.
- `PortrayType` — maps AIGR types to RPython `CC_B_*` names. Auxiliary to Renderer.
- `Machinery` — facade for pluggable code generation strategies
- `Bundler` — facade for argument packing/unpacking (NEW, see below)
- `NativeBundler` — concrete `*args/**kwargs`-style implementation of `Bundler`
- `Walker(Visitor)` — walks AIGR subnodes
- `IDRef` — resolves AIGR ID references to RPython names

### RPy_buildin (handwritten RPython, never generated):
- `CC_B_Component` — base class for all Castle elements/components
- `CC_B_ComponentClass` — descriptor with dispatch table (dict: str → callable)
- `CC_B_ComponentInterface` — describes the interface of a component
- `CC_B_Value` and subclasses — argument value wrappers (see below)

---

## 3. Calling Convention Design

### The dispatch table pattern:
```python
cc_S_Credible_HelloWorld_std['CC_P_std_invoke'](main_elm, args, kwargs)
```
- `cc_S_*` is a dict (str → callable) — effectively a vtable
- String keys are **always compile-time constants** — RPython eliminates hash lookup
- Every callable in the table has the **same signature**: `(element, args, kwargs)`
- `args` and `kwargs` carry the actual arguments uniformly

### Performance conclusions (from reasoning + small experiments):
- String-keyed dict ≈ int-keyed dict in performance (RPython constant-folds string keys)
- No need for vtable-rewrite optimiser — RPython handles it
- The `kwargs` dict allocation on every call IS worth optimising (future optimiser)
- RPython's annotator is better at type inference than anything we'd build in AIGR
- Cast in `CC_B_*.__init__` (e.g. `int(v)`) is zero-cost when RPython proves it unnecessary

---

## 4. CC_B_Value Hierarchy

File: `castle/writers/RPy_buildin/buildin/CC_B_Values.py`

```python
class CC_B_Value:
    """Base for all Castle argument-value wrappers. Never instantiate directly."""
    pass

class CC_B_int(CC_B_Value):
    def __init__(self, v): self.value = int(v)

class CC_B_float(CC_B_Value):
    def __init__(self, v): self.value = float(v)

class CC_B_string(CC_B_Value):
    def __init__(self, v): self.value = str(v)

class CC_B_boolean(CC_B_Value):
    def __init__(self, v): self.value = bool(v)

class CC_B_Component(CC_B_Value):
    def __init__(self, v): self.value = v   # CC_B_Component instance

class CC_B_Struct(CC_B_Value):
    def __init__(self, v): self.value = v   # CC_B_Struct instance
```

### Design decisions:
- `.value` is uniform across all subclasses (not `.intval`, `.strval` etc.)
- Cast in `__init__` is the safety net — RPython eliminates it when provably unnecessary
- Bundler never emits extra casts — trusts RPython's annotator
- At unpack time, RPython's annotator sees concrete subclass → no `int|float` union

### Corresponding AIGR types (`castle/aigr/types.py`):
```python
int     = _buildinNumber('int')
float   = _buildinNumber('float')
string  = _buildin('string')
boolean = _buildin('boolean')
```
Note: `boolean` not `bool` (full name, like `string` not `str`).

### Sync test:
`pytst/d03_RPy/machinery/test_sync_Portray2buildin_names.py`
Dynamically discovers all `_buildin` types and all `CC_B_*` classes and verifies they match.
**Must pass** before any other bundler tests are meaningful.

---

## 5. Bundler Design

### Role:
`Bundler` knows the *mechanic* of bundling arguments for a call.
It does NOT know about rendering (that's `Renderer.visit()`).
It does NOT know about type names (that's `PortrayType`).
It IS stateless — no data, no lifeline.

### Two-level API:
| Level   | Pack   | Unpack   | Description                       |
|---------|--------|----------|-----------------------------------|
| Element | `box`  | `unbox`  | Wrap one value: `CC_B_int(1)`     |
| List    | `pack` | `unpack` | Assemble all: `[CC_B_int(1)], {}` |

### Class hierarchy:
```python
class Bundler(ABC):
    def __new__(cls, hint:str="", **kwargs):
        # returns NativeBundler() for now
        ...

    def box(self, value_txt:str, cc_type:aigr.types._types) -> str: ...
    def unbox(self, param:aigr.TypedParameter) -> str: ...
    def pack(self, arguments:aigr.ArgumentList,
             formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock: ...
    def unpack(self, formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock: ...

class NativeBundler(Bundler):
    """*args/**kwargs style — positional list + named dict"""
    ...
```

### Key design decisions:
- `Bundler.__new__(hint="")` selects implementation — currently always `NativeBundler`
- `Portray`/`PortrayType` are NOT passed to Bundler — internal implementation detail of `NativeBundler`
- `NativeBundler` instantiates `PortrayType` internally (class-level, stateless)
- Named args → dict (`kwargs`), positional → list (`args`)
- Reordering (when needed) belongs in the Bundler, not in `Renderer`
- Future Bundlers (JSON, network, positional-only) are independent subclasses

### Type aliases (in `castle/aigr/aid.py`):
```python
ArgumentList               = list[Argument]
TypedParameterList         = tuple[TypedParameter, ...]
OptionalArgumentList       = Optional[ArgumentList]
OptionalTypedParameterList = Optional[TypedParameterList]
```
Note: Arguments are `list` (mutable, per call-site); Parameters are `tuple` (immutable, defined once).

### Generated code types (Python 3.12+):
```python
type Boxed[T] = str    # a CC_B_*(value) expression, e.g. CC_B_int(1)
type ArgList  = str    # the full [...], {} structure
```
Basedpyright understands these; mypy support is incomplete as of early 2026.

### Current status of NativeBundler.pack:
```python
def pack(self, arguments, formal_parameters) -> TextBlock:
    pos_parts = []
    for arg, param in zip(arguments, (p for p in (formal_parameters or ()))):
        value_txt = arg.value.value if isinstance(arg.value, aigr._literal) else repr(arg.value)  # TODO: use visitor
        wrapper   = f'CC_B_{param.type.represents}'   # TODO: use PortrayType
        pos_parts.append(f'{wrapper}({value_txt})')
    return f'[{", ".join(pos_parts)}], {{}}'
```
**Two open TODOs:**
1. Replace `isinstance(arg.value, aigr._literal)` with `Renderer.visit(arg.value)`
2. Replace `f'CC_B_{param.type.represents}'` with `PortrayType.prefix(param.type)`

---

## 6. PortrayType Design

### Role:
Dumb name converter. Only knows: `aigr.types.int` → `'CC_B_int'`.
No knowledge of packing, casting, or structure.

### Implementation:
```python
class PortrayType(Visitor):
    _prefixes = ('prefix',)
    _CC_buildinType_prefix = 'CC_B_'

    def prefix(self, CC_type) -> str:
        return self._visitor(CC_type, prefix='prefix')

    def _default_prefix(self, CC_type) -> str:
        try:
            represents = CC_type.represents
        except AttributeError as e:
            assert False, f"{CC_type=} has no `.represents`"
        return f'{self._CC_buildinType_prefix}{represents}'

    def prefix_ComponentImplementation(self, CC_type):
        return 'CC_B_Component'
```

---

## 7. Naming Conventions

### RPython generated names:
| Pattern                | Example           | Meaning                          |
|------------------------|-------------------|----------------------------------|
| `CC_<name>`            | `CC_Foo`          | Generated class for Component    |
| `cc_C_<name>`          | `cc_C_Foo`        | Element (instantiated component) |
| `cc_CI_<name>`         | `cc_CI_Foo`       | Component interface              |
| `cc_S_<comp>_<port>`   | `cc_S_Foo_std`    | Event dispatch table             |
| `CC_P_<proto>_<event>` | `CC_P_std_invoke` | Key in dispatch table            |
| `CC_B_<type>`          | `CC_B_int`        | Builtin value wrapper            |

### Python/AIGR naming:
- Classes starting with `_` are abstract/mixin
- `_buildin` → built-in Castle types; `_user` → user-defined types
- `_buildinNumber` → numeric built-in types
- Type names use full words: `boolean` not `bool`, `string` not `str`
- `""` for text strings, `''` for constants (in generated code)

---

## 8. TDD Conventions (Uncle Bob style)

### The three laws:
1. No production code without a failing test
2. No more test than sufficient to fail
3. No more production code than sufficient to pass

### Test file naming:
```
test_0_<subject>.py   # smoke/sanity — does it exist?
test_1_<subject>.py   # first real behaviour
test_2_<subject>.py   # next behaviour
test_<N><letter>_...  # variant/edge case of test_N
test_sync_<A>2<B>.py  # contract/sync test between two units
```

### Test structure (BDD-style, 3 phases):
```python
def test_1a_pack_single_positional_string(bundler):
    # GIVEN
    arguments = (aigr.Argument(value=aigr.fString(value="Just a demo")),)
    formal_parameters = (aigr.TypedParameter(name='a', type=CCTypes.string),)
    expected = '[CC_B_string("Just a demo")], {}'

    # WHEN
    txt = bundler.pack(arguments=arguments, formal_parameters=formal_parameters)

    # THEN
    verify_ValidPython(txt)
    assert str(txt) == expected, f"Got {txt=}, when packing {arguments=} -- {expected=}"
```
3-phase separation (blank lines) when test is more than ~3 lines.

### Shared test infrastructure:
- `fixtures.py` — shared pytest fixtures per test directory
- `verify.py` — shared verification helpers (e.g. `verify_ValidPython`)
- `mocks.py` — test doubles, mock AIGR nodes
- `from .fixtures import bundler` — always relative import
- `from .verify import *` — always relative import

### Test doubles (Uncle Bob terminology):
- `NonBundlerStub` — concrete subclass that does NOT implement methods, to test base raises

### Assertions:
- Always include `f"..."` message on assert — make failures self-explanatory
- `try/except NotImplementedError: pass` preferred over `pytest.raises` (linter-friendly)
- `verify_ValidPython(txt)` — always call on bundler output (checks `isinstance` + `ast.parse`)

---

## 9. Open TODOs & Next Steps

### Immediate (next coding session):
1. Implement `box`/`unbox` on `Bundler` + `NativeBundler`
2. Implement `PortrayType` fully + its tests
3. Wire `PortrayType` into `NativeBundler` — replace `f'CC_B_{param.type.represents}'`
4. Wire `Renderer.visit()` into `NativeBundler` — replace `isinstance(arg.value, aigr._literal)` hack
5. Write `test_2_bundler-simple.py` tests for `CC_B_int` etc.
6. Implement `unpack` in `NativeBundler`

### Design decisions still open:
- Rename `signature` → `formal_parameters` done ✓; but `Signature` type alias still in some places
- `ArgumentList`/`TypedParameterList` — move to `aigr.aid` done ✓
- `Boxed[T]`/`ArgList` typed string aliases — agreed, not yet implemented
- Split `Bundler.pack` into `box` + `pack` — agreed, not yet refactored
- `PortrayType` — new file `portray_type.py` alongside `portray.py`

### Future optimisers (separate packages, read/write AIGR):
1. **Positional-args optimiser** — resolve named args to positional slots, flat array, no kwargs dict
2. **Vtable-rewrite optimiser** — dict dispatch → Python class dispatch (probably not needed)

### Known technical debt:
- `visit_Call` in `Renderer` has HACK comment for `self.` prefix on method calls
- `_pack_argList` on `Renderer` should be fully replaced by `Bundler.pack`
- `Machinery` needs `self.arg_bundler = Bundler(hint)` wired in
- `RPy_buildin` import path in `_file_header` has `XXX ToDo`

---

## 10. Key Design Principles Established

1. **Trust the AIGR** — it's validated before the writer runs; writer can assert, not re-validate
2. **Trust RPython** — its annotator is better at type inference than anything we'd build
- Cast in `__init__` is zero-cost when RPython proves it unnecessary
3. **Trust the C compiler** — don't second-guess `gcc`/`clang -O2`
4. **SOLID + TDD** — every new class gets independent tests; Red→Green→Refactor
5. **Portray is dumb** — only string/name conversion, no logic
6. **Bundler owns the mechanic** — not Renderer, not Portray
7. **Stateless helpers** — Bundler, PortrayType have no state; instantiated internally
8. **String keys are fine** — RPython constant-folds them; no need for int-keyed vtable
