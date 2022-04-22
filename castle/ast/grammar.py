import logging; logger = logging.getLogger(__name__)

from ._base import AST_BASE, ID, IDError

import typing

class PEG (AST_BASE):                                                   # abstract
    """Base class of all Grammer-rule (using a PEG) classes"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MixIn_value_attribute:
    """With this MixIn PEG-classes get the ``.value`` property"""

    def __init__(self, *, value=None, **kwargs):
        logger.debug(f'{self._typeName(self)}.MixIn_value_attribute:: value:=' +
                     ('[[' +', '.join(f'{v}:{type(v).__name__}' for v in value) + ']]') if isinstance(value, list) else f's>>{value}<<')
        super().__init__(**kwargs)
        self._value=value

    @property
    def value(self):
        logger.debug(f'{self._typeName(self)}:: @value={self._value}')
        return self._value


class MixIn_expr_attribute:
    """With this MixIn PEG-classes get the ``.expr`` property"""

    def __init__(self, *, expr=None, **kwargs):
        logger.debug(f'{self._typeName(self)}.MixIn_expr_attribute:: expr:={self._valType(expr)}')
        super().__init__(**kwargs)
        self._expr = expr

    @property
    def expr(self):
        logger.debug(f'{self._typeName(self)}:: @expr={self._expr}')
        return self._expr


class MixIn_children_tuple:
    """With this MixIn PEG-class get the ``.children`` property; and sequence-alike methods"""
    def __init__(self, *, children, **kwargs):
        logger.debug(f'{self._typeName(self)}.MixIn_children_tuple:: children[{len(children)}]:=' +
                     ('[[' +', '.join(f'{c}:{type(c).__name__}' for c in children) + ']]') if isinstance(children, list) else f's>>{children}<<')
        super().__init__(**kwargs)
        self._children = tuple(children)

    def __len__(self):
        return len(self._children)
    def __getitem__(self, key):
        return self._children[key]
    def __iter__(self): return self._children.__iter__()
    def __str__(self):
        return f"<{type(self).__name__}.MixIn_children_tuple:{len(self)}[" + ",".join(str(c) for c in self) + "]>"

##
## Note: When using TypeHints with PEG-classes; the clases
##       should be defined "above" the typehints uses them
##       This defines (largely/partly) the order of classes.
##

class Terminal(MixIn_value_attribute, PEG): pass                        # abstract
class StrTerm(Terminal): pass
class RegExpTerm(Terminal): pass
class Number(Terminal):                                            # Value is stored as a string
    def __str__(self):                                             # mostly for debugging
        return f'<"{self.value}">'

class Markers(PEG): pass                                                # abstract
class EOF(Markers): pass                                                # XXX Todo ## singleton?

class NonTerminal(PEG): pass                                            # abstract
class Expression(NonTerminal): pass                                     # abstract


class Setting(PEG):
    def __init__(self, *,
                 name: ID,
                 value,
                 **kwargs):
        ID.validate_or_raise(name)
        super().__init__(**kwargs)
        self.name = name
        self.value = value


class Rule(NonTerminal):
    def __init__(self, *,
                 name: ID, expr:Expression=None,
                 **kwargs):
        logger.debug(f'{self._typeName(self)}: name={self._valType(name)}, expr={self._valType(expr)}')
        if expr:
            logger.debug("\t" + "; ".join(f'{c}:{type(c)}' for c in expr))
        if not isinstance(name, ID): raise TypeError(f'Rule-name {name} is not of type ID')
        super().__init__(**kwargs)
        self.name = name
        self.expr = expr

class Rules(MixIn_children_tuple, PEG): pass                            # generic: ParseRules or Settings or Mix
class ParseRules(Rules): pass
class Settings(Rules): pass


class Grammar(NonTerminal):
    def __init__(self, *,
                 all_rules: typing.Sequence[Rule],
                 **kwargs):
        super().__init__(**kwargs)
        self._all_rules = Rules(children=all_rules) # store `all_rules` in once, to be able to remember the order
        self.parse_rules  = ParseRules( children=[r for r in self._all_rules if isinstance(r, Rule)] )
        self.settings = Settings( children=[r for r in self._all_rules if isinstance(r, Setting)] )
        assert len(all_rules) == len(self.parse_rules) + len(self.settings)


class Group(Expression): pass                                           # abstract --  Note: Do not Group for  '(' ...')';  that's a Sequence!!


class UnorderedGroup(MixIn_expr_attribute, Group):                      # It looks like a Quantity, but is a group
    """A set (aka "group") of expressions that **all** have to be matched, but the **order** is a don't care.

       Possible an extension of Arpeggio (see: https://textx.github.io/Arpeggio/stable/grammars/), possible a generic one."""


class Quantity(MixIn_expr_attribute, Expression):                                             # abstract
    """An expression with Quantification; like optional, or repetition. The subclasses defines which Quantification"""


class Sequence(MixIn_children_tuple, Expression):
    """A sequence of expressions; can be of length=1"""
    # __init__ (see MixIn) sets self._children; assuming it is a list

    def __str__(self): # mostly for debugging
        return "Seq{{" + " ; ".join(f"{c}" for c in self) + "}}"


class OrderedChoice(MixIn_children_tuple, Expression):                  # A | B | C | ...  the order is relevant
    """OC: A _tuple_ of alternative expressions"""

    def __str__(self): # mostly for debugging
        return "OC{{" + " | ".join(f"{c}" for c in self._children) + "}}"

class Optional(Quantity):pass
class ZeroOrMore(Quantity):pass
class OneOrMore(Quantity):pass

class Predicate(MixIn_expr_attribute, Expression): pass                 # abstract
class AndPredicate(Predicate): pass
class NotPredicate(Predicate): pass

