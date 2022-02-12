from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython


def peg_grammar(): 	return rules, EOF
def rules(): 		return OneOrMore([parse_rule, setting])
def parse_rule():	return rule_name, '<-', expression, ";"

def expression():	return sequence, op_alternative
def sequence():		return OneOrMore(single_expr)
def single_expr():	return [ rule_crossref, term, group, predicate ], op_quantity

def op_alternative():   return Optional( '|' , expression )
def op_quantity(): 	return Optional([ '?' , '*' , '+' , '#' ])

def term():		return [ str_term, regex_term ]
def group():		return '(', expression, ')'
def predicate():	return ['&','!'], single_expr

def str_term():		return [  (S3,   str_no_s3,  S3),
                                  (D3,   str_no_d3,   D3),
                                  (S1,   str_no_s1,   S1),
                                  (D1,   str_no_d1,   D1)  ]
def regex_term():	return [  (RE,   re_no_slash, RE),
                                  (REs3, str_no_s3,   S3),
                                  (REd3, str_no_d3,   D3),
                                  (REs1, str_no_s1,   S1),
                                  (REd1, str_no_d1,   D1)  ]

def rule_name():	return ID
def rule_crossref():	return ID
def ID():        	return _(r"[a-zA-Z_]([a-zA-Z_]|[0-9])*")

def re_no_slash():	return _(r"((\\/)|[^\/])*")
def str_no_s1():	return _(r"((\\')|[^'\n])*")                    # Does NOT match multiline -- note 'multiline=False' is not the same
def str_no_d1():	return _(r'((\\")|[^"\n])*')                    # idem
def str_no_s3():	return _(r"([^']|('[^'])|(''[^']))*")           # ALLOW multiline
def str_no_d3():	return _(r'''([^"]|("[^"])|(""[^"]))*''')       # idem

def setting():		return setting_name, '=', value, ';'
def setting_name():	return ID
def value():            return [ str_term, regex_term, number, setting_xref ]
def number():		return [ complex_lit, float_lit, int_lit ]
def setting_xref():	return ID
def complex_lit():	return _(r"([0-9](\.[0-9]*)?)[+-][iIjJ]([0-9](\.[0-9]*)?)")
def float_lit():	return _(r"[0-9]\.[0-9]+")
def int_lit():		return _(r"[1-9][0-9]*")


S1 = "'"
D1 = '"'
S3 = "'''"
D3 = '"""'
RE   = '/'
REs1 = _(r"[rR]'")
REd1 = _(r'[rR]"')
REs3 = _(r"[rR]'''")
REd3 = _(r'[rR]"""')

def comment():		return "//", _(".*\n")


