from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython

def peg_grammar(): 	return OneOrMore(rule), EOF
def rule():		return rule_name, '<-', ordered_choice, ";"
def ordered_choice():	return sequence, ZeroOrMore('|', sequence)
def sequence():		return ZeroOrMore(prefix)
def prefix():           return Optional(['&','!']), suffix
def suffix():		return expression, Optional([ '?' , '*' , '+' , '#' ])
def expression():       return [ regex_term, str_term, ('(', ordered_choice, ')'), rule_crossref]
def rule_crossref():	return rule_name
def rule_name():	return ID
def regex_term():	return [\
                                (RE,   re_no_slash, RE),
                                (REs3, str_no_s3,   S3),
                                (REd3, str_no_d3,   D3),
                                (REs1, str_no_s1,   S1),
                                (REd1, str_no_d1,   D1)
                                ]
def str_term():		return [\
                                (S3, str_no_s3, S3),
                                (D3, str_no_d3, D3),
                                (S1, str_no_s1, S1),
                                (D1, str_no_d1, D1)
                                ]

def ID():        	return _(r"[a-zA-Z_]([a-zA-Z_]|[0-9])*")

def re_no_slash():	return _(r"((\\/)|[^\/])*")

def str_no_s1():	return _(r"((\\')|[^'\n])*")                    # Does NOT match multiline -- note 'multiline=False' is not the same
def str_no_d1():	return _(r'((\\")|[^"\n])*')                    # idem
def str_no_s3():	return _(r"([^']|('[^'])|(''[^']))*")           # ALLOW multiline
def str_no_d3():	return _(r'''([^"]|("[^"])|(""[^"]))*''')       # idem

S1 = "'"
D1 = '"'
S3 = "'''"
D3 = '"""'
RE   = '/'
REs1 = _(r"[rR]'")
REd1 = _(r'[rR]"')
REs3 = _(r"[rR]'''")
REd3 = _(r'[rR]"""')



def comment():          return "//", _(".*\n")

