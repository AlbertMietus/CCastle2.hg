import arpeggio

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

import logging;logger = logging.getLogger(__name__)

class QuantityError(ValueError): pass
class PredicateError(ValueError): pass


#NO_VISITOR_NEEDED: visit_str_no_s1
#NO_VISITOR_NEEDED: visit_str_no_d1
#NO_VISITOR_NEEDED: visit_str_no_s3
#NO_VISITOR_NEEDED: visit_str_no_d3
#NO_VISITOR_NEEDED: visit_comment
#NO_VISITOR_NEEDED: visit_ID
#NO_VISITOR_NEEDED: visit_term
#NO_VISITOR_NEEDED: visit_re_no_slash
#NO_VISITOR_NEEDED: visit_group

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

    def visit_single_expr(self, node, children):                        #  [ rule_crossref, term, group, predicate ],  op_quantity
        if len(children) == 1: #  No Optional part
            try:
                n = f'name={children[0].name}'
            except AttributeError:
                n = f'name:{children[0]}'
            logger.debug(f'visit_single_expr==1:: {n}:{type(children[0])}')
            return children[0]
        elif len(children) == 2: #  Optional part
            logger.debug(f'visit_single_expr==2::Got: {children[0]}, {children[1]}')
            expr = children[0]
            token = str(children[1])
            quantum_cls = self.token_2_class.get(token)
            if quantum_cls:
                ast=quantum_cls(expr=expr, parse_tree=node)
                logger.debug(f'visit_single_expr==2::Pass: {quantum_cls}(expr={expr})')
                return ast
            else:
                raise QuantityError(f"token '{token}' not recognised")
        else:
            raise  NotImplementedError("visit_single_expr, len>2")      # XXX -- Is this possible?


    def visit_expressions(self, node, children):                        # OneOrMore(single_expr), Optional( '|' , expressions )
        logger.debug(f'visit_expressions:: >>{node}<< len={len(children)} children={children}:{type(children)}')
        return peg.Sequence(value=children, parse_tree=node)


    def visit_predicate(self, node, children):
        token_2_predicate = {'&': peg.AndPredicate,
                             '!': peg.NotPredicate}
        logger.debug(f'visit_predicate:: >>{node}<< len={len(children)}')

        if len(children) == 2:
            token = children[0]
            cls = token_2_predicate.get(token)
            if cls:
                ast = cls(expr=children[1], parse_tree=node)
                return ast
            else:
                raise PredicateError(f"token '{token}' not recognised")
        else:
            raise  NotImplementedError("visit_predicate, len!=2")      # XXX -- Is this possible?


