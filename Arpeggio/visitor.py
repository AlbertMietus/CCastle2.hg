import arpeggio

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

import logging;logger = logging.getLogger(__name__)

class QuantityError(ValueError): pass

class PegVisitor(arpeggio.PTNodeVisitor):
    token_2_class = {'?': peg.Optional,
                     '*': peg.ZeroOrMore,
                     '+': peg.OneOrMore,
                     '#': peg.UnorderedGroup}

    def visit_str_term(self, node, children):
        return peg.StrTerm(value=node[1], parse_tree=node)

    def visit_regex_term(self, node, children):
        return peg.RegExpTerm(value=node[1], parse_tree=node)

    def visit_rule_name(self, node, children):
        return peg.ID(name=str(node), parse_tree=node)

    def visit_rule_crossref(self, node, children):
        return peg.ID(name=str(node), parse_tree=node)

    def visit_rule(self, node, children):                               #  Name '<-' expressions ';'
        return peg.Rule(name=children[0],expr=children[1], parse_tree=node)

    def visit_single_expr(self, node, children):                        #  [ rule_crossref, term, group, predicate ],  expr_quantity
        if len(children) == 1: #  No Optional part
            try:
                n = children[0].name
            except AttributeError:
                n = str(children[0])
            logger.debug(f'visit_single_expr==1:: {n}:{type(children[0])}')
            return children[0]
        elif len(children) == 2: #  Optional part
            logger.debug(f'visit_single_expr==2:: {children[0]}, {children[1]}')
            expr = children[0]
            token = str(children[1])
            quantum_cls = self.token_2_class.get(token)
            if quantum_cls:
                ast=quantum_cls(expr=expr, parse_tree=node)
                logger.debug(f'visit_single_expr==2:: {quantum_cls} {expr}')
                return ast
            else:
                raise QuantityError(f"token '{token}' not recognised")
        else:
            raise  NotImplementedError("visit_single_expr, len>2")      # XXX -- Is this possible?

    def visit_expr_quantity(self, node, children):                      # Optional([ '?' , '*' , '+' , '#' ])
        logger.debug(f'visit_expr_quantity [{len(children)}] node={node}:{type(node)}')
        return node


    def visit_expressions(self, node, children):                        # OneOrMore(single_expr), Optional( '|' , expressions )
        logger.debug(f'>>{node}<< len={len(children)} children={children}')
        return peg.Sequence(value=children, parse_tree=node)

