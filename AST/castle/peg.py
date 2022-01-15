import logging; logger = logging.getLogger(__name__)

from ._base import AST_BASE, ID, IDError

class PEG (AST_BASE):                                                   # abstract
    """Base class of all PEG classes"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MixIn_value_attribute:
    """With this MixIn PEG-classes get the ``.value`` property"""

    def __init__(self, *, value=None, **kwargs):
        super().__init__(**kwargs)
        logger.debug(f'{type(self).__name__}:: value:={value}:{type(value)}')
        self._value=value

    @property
    def value(self):
        logger.debug(f'{type(self).__name__}:: @property={self._value}')
        return self._value


class MixIn_expr_attribute:
    """With this MixIn PEG-classes get the ``.expr`` property"""

    def __init__(self, *, expr=None, **kwargs):
        super().__init__(**kwargs)
        self._expr = expr

    @property
    def expr(self):
        return self._expr

##
## Note: When using TypeHints with PEG-classes; the clases
##       should be defined "above" the typehints uses them
##       This defines (largely/partly) the order of classes.
##

class Terminal(MixIn_value_attribute, PEG): pass                        # abstract
class StrTerm(Terminal): pass
class RegExpTerm(Terminal): pass

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
        ID.validate_or_raise(name)
        super().__init__(**kwargs)
        self.name = name
        self.expr = expr
        logger.debug(f'{type(self).__name__}:: expr:={expr}:{type(expr)}')
        logger.debug("\t" + "; ".join(f'{c}:{type(c)}' for c in expr))

class Grammar(NonTerminal):
    def __init__(self, *,
                 rules: list[Rule]=None,
                 settings: list[Setting]=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.rules = rules
        self.settings = settings


class Group(Expression): pass                                           # abstract --  Note: Do not Group for  '(' ...')';  that's a Sequence!!
class UnorderedGroup(MixIn_expr_attribute, Group):                      # It looks like a Quantity, but is a group
    """See a set (aka "group") of expressions that **all** have to be matched, but the **order** is a don't care.

       Possible an extension of Arpeggio (see: https://textx.github.io/Arpeggio/stable/grammars/), possible a generic one."""

class Quantity(MixIn_expr_attribute, Expression):                                             # abstract
    """An expression with Quantification; like optional, or repetition. The subclasses defines which Quantification"""


class Sequence(MixIn_value_attribute, Expression):
    """A _list_ of expressions; can be of length=1"""
    # __init__ (see MixIn) sets self._value; assuming it is a list

    def __len__(self):       	return len(self._value)
    def __getitem__(self, n):	return self._value[n]


class OrderedChoice(Expression):pass                                    # It a an set of alternatives

class Optional(Quantity):pass
class ZeroOrMore(Quantity):pass
class OneOrMore(Quantity):pass


class Predicate(MixIn_expr_attribute, Expression): pass                 # abstract
class AndPredicate(Predicate): pass
class NotPredicate(Predicate): pass
