import arpeggio

from castle.ast import peg

import logging;logger = logging.getLogger(__name__)
from typing import Union

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
#NO_VISITOR_NEEDED: visit_op_quantity		-- handled in visit_single_expr
#NO_VISITOR_NEEDED: visit_op_alternative	-- handled in visit_expression
#NO_VISITOR_NEEDED: visit_complex_lit		-- handled in visit_number
#NO_VISITOR_NEEDED: visit_float_lit		-- handled in visit_number
#NO_VISITOR_NEEDED: visit_int_lit		-- handled in visit_number
#NO_VISITOR_NEEDED: visit_value



class PegVisitor(arpeggio.PTNodeVisitor):
    def _logstr_node_children(self, node, children):
        return f'>>{node}<< children[{len(children)}] >>' + ", ".join(f'{c}:{type(c).__name__}' for c in children) + '<<'

    def visit_str_term(self, node, children):
        return peg.StrTerm(value=node[1], parse_tree=node)

    def visit_regex_term(self, node, children):
        return peg.RegExpTerm(value=node[1], parse_tree=node)

    def visit_rule_name(self, node, children):
        return peg.ID(name=str(node), parse_tree=node)

    def visit_rule_crossref(self, node, children):
        return peg.ID(name=str(node), parse_tree=node)

    def visit_parse_rule(self, node, children):                               #  Name '<-' expression ';'
        return peg.Rule(name=children[0],expr=children[1], parse_tree=node)


    def visit_single_expr(self, node, children):                        #  [ rule_crossref, term, group, predicate ],  op_quantity
        token_2_class = {'?': peg.Optional,
                         '*': peg.ZeroOrMore,
                         '+': peg.OneOrMore,
                         '#': peg.UnorderedGroup}

        if len(children) == 1: #  No Optional part
            logger.debug(f'visit_single_expr==1:: {getattr(children[0], "name", children[0])}:{type(children[0])}')
            return children[0]

        elif len(children) == 2: #  Optional part
            logger.debug(f'visit_single_expr==2::Got: {children[0]}, {children[1]}')
            expr = children[0]
            token = str(children[1])
            quantum_cls = token_2_class.get(token)
            if quantum_cls:
                ast=quantum_cls(expr=expr, parse_tree=node)
                logger.debug(f'visit_single_expr==2::Pass: {quantum_cls}(expr={expr})')
                return ast
            else:
                raise QuantityError(f"token '{token}' not recognised")
        else: # #children not in (1,2)
            raise  NotImplementedError("visit_single_expr, len>2")      # -- Is this possible?


    # expression <- sequence, op_alternative; op_alternative <- ('|' expression)?
    def visit_expression(self, node, children) -> Union[peg.Sequence,  peg.OrderedChoice]:
        logger.debug('visit_expression::' + self._logstr_node_children(node, children))
        if len(children) == 1: #Only sequence
            return children[0]
        elif len(children) == 2: # So, having 1 or more alternatives in children[1]
            # In all cased a (single) OrderedChoice with a list of alternatives should be returned.
            if isinstance(children[1], peg.OrderedChoice):
                alternatives = [children[0]] + [alt for alt in children[1]]
            else:
                alternatives = children
            return peg.OrderedChoice(children = alternatives, parse_tree=node)
        else:
            raise NotImplementedError("visit_expression, len>2")


    # OneOrMore(single_expr)
    def visit_sequence(self, node, children) -> peg.Sequence:
        logger.debug(f'visit_sequence::{self._logstr_node_children(node, children)}')
        return peg.Sequence(value=children, parse_tree=node)


    def visit_predicate(self, node, children):
        token_2_predicate = {'&': peg.AndPredicate,
                             '!': peg.NotPredicate}
        logger.debug(f'visit_predicate:: >>{node}<< #children={len(children)}')

        if len(children) == 2:
            token = children[0]
            cls = token_2_predicate.get(token)
            if cls:
                ast = cls(expr=children[1], parse_tree=node)
                return ast
            else:
                raise PredicateError(f"token '{token}' not recognised")
        else:
            raise  NotImplementedError("visit_predicate, len!=2")      # -- Is this possible?


    def visit_rules(self, node, children):                              # Mix of `ParseRule`(s)`Setting`(s) ; will be sorted out n `Grammar`
        logger.debug('visit_rules::' + self._logstr_node_children(node, children))
        return peg.Rules(children=children[:], parse_tree=node)


    def visit_peg_grammar(self, node, children):
        rules=children[0]
        logger.debug('visit_peg_grammar::' + self._logstr_node_children(node, children) + f'rules:: {rules}')
        parse_rules = peg.ParseRules(children=[r for r in rules if isinstance(r, peg.Rule)] )
        settings      = peg.Settings(children=[r for r in rules if isinstance(r, peg.Setting)] )
        assert len(rules) == len(parse_rules) + len(settings), f'Number of parse_rules ({len(parse_rules)}) and settings ({len(settings)}), does not match total: {len(rules)}'
        return peg.Grammar(rules=parse_rules, settings=settings, parse_tree=node)


    def visit_setting_name(self, node, children):
        return peg.ID(name=str(node), parse_tree=node)

    def visit_number(self, node, children):
        return peg.Number(value=str(node), parse_tree=node)

    def visit_setting_xref(self, node, children):
        return peg.ID(name=str(node), parse_tree=node)

    def visit_setting(self, node, children):
        logger.debug('visit_setting::' + self._logstr_node_children(node, children))
        return peg.Setting(name=children[0], value=children[1] , parse_tree=node)
