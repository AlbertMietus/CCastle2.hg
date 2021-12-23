from ._base import AST_BASE, ID, IDError

class PEG (AST_BASE):                                                   # abstract
    """Base class of all PEG classes"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


##
## Note: When using TypeHints with PEG-classes; the clases
##       should be defined "above" the typehints uses them
##       This defines (largely/partly) the order of classes.
##

class Terminal(PEG):                                                    # abstract
    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)
        self.value=value


class NonTerminal(PEG): pass                                            # abstract
class Markers(PEG): pass                                                # abstract

class StrTerm(Terminal): pass
class RegExpTerm(Terminal): pass

class EOF(Markers): pass                                               # singleton?

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
                 name: ID,
                 expr :Expression=None,
                 **kwargs):
        ID.validate_or_raise(name)
        super().__init__(**kwargs)
        self.name = name
        self.expr = expr


class Grammar(NonTerminal):
    def __init__(self, *,
                 rules: list[Rule]=None,
                 settings: list[Setting]=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.rules = rules
        self.settings = settings



class ManyExpression(Expression): pass                                  # abstract
class Group(Expression):pass

class Sequence(Expression):
    """A "list of expressions; can be of length=1"""
    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)
        self.value=value
    def __len__(self):
        return len(self.value)
    def __getitem__(self, n):
        return self.value[n]


class OrderedChoice(Expression):pass
class Predicate(Expression): pass                                       # abstract

class Optional(ManyExpression):pass
class OneOrMore(ManyExpression):pass
class ZeroOrMore(ManyExpression):pass

class AndPredicate(Predicate): pass
class NotPredicate(Predicate): pass
