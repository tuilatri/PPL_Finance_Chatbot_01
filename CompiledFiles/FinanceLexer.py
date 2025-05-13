# Generated from D:\PPL_Finance_Chatbot_01\Finance.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\7\t<\n\t\f\t\16\t?\13\t\3\n\6\nB\n\n")
        buf.write("\r\n\16\nC\3\13\6\13G\n\13\r\13\16\13H\3\13\3\13\3\13")
        buf.write("\3\13\7\13O\n\13\f\13\16\13R\13\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\6\rY\n\r\r\r\16\rZ\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\7\4\2C\\c|")
        buf.write("\6\2\62;C\\aac|\6\2\"\"\62;C\\c|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3")
        buf.write("\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13(\3")
        buf.write("\2\2\2\r,\3\2\2\2\17\63\3\2\2\2\219\3\2\2\2\23A\3\2\2")
        buf.write("\2\25F\3\2\2\2\27S\3\2\2\2\31X\3\2\2\2\33\34\7<\2\2\34")
        buf.write("\4\3\2\2\2\35\36\7*\2\2\36\6\3\2\2\2\37 \7+\2\2 \b\3\2")
        buf.write("\2\2!\"\7E\2\2\"#\7j\2\2#$\7c\2\2$%\7p\2\2%&\7i\2\2&\'")
        buf.write("\7g\2\2\'\n\3\2\2\2()\7C\2\2)*\7f\2\2*+\7f\2\2+\f\3\2")
        buf.write("\2\2,-\7F\2\2-.\7g\2\2./\7n\2\2/\60\7g\2\2\60\61\7v\2")
        buf.write("\2\61\62\7g\2\2\62\16\3\2\2\2\63\64\7T\2\2\64\65\7g\2")
        buf.write("\2\65\66\7u\2\2\66\67\7g\2\2\678\7v\2\28\20\3\2\2\29=")
        buf.write("\t\2\2\2:<\t\3\2\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2")
        buf.write("\2\2>\22\3\2\2\2?=\3\2\2\2@B\t\4\2\2A@\3\2\2\2BC\3\2\2")
        buf.write("\2CA\3\2\2\2CD\3\2\2\2D\24\3\2\2\2EG\t\5\2\2FE\3\2\2\2")
        buf.write("GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2IP\3\2\2\2JK\7\60\2\2KL")
        buf.write("\t\5\2\2LM\t\5\2\2MO\t\5\2\2NJ\3\2\2\2OR\3\2\2\2PN\3\2")
        buf.write("\2\2PQ\3\2\2\2Q\26\3\2\2\2RP\3\2\2\2ST\7X\2\2TU\7P\2\2")
        buf.write("UV\7F\2\2V\30\3\2\2\2WY\t\6\2\2XW\3\2\2\2YZ\3\2\2\2ZX")
        buf.write("\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\b\r\2\2]\32\3\2\2\2\b")
        buf.write("\2=CHPZ\3\b\2\2")
        return buf.getvalue()


class FinanceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    CHANGE = 4
    ADD = 5
    DELETE = 6
    RESET = 7
    CATEGORY = 8
    DESCRIPTION = 9
    AMOUNT = 10
    CURRENCY = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'('", "')'", "'Change'", "'Add'", "'Delete'", "'Reset'", 
            "'VND'" ]

    symbolicNames = [ "<INVALID>",
            "CHANGE", "ADD", "DELETE", "RESET", "CATEGORY", "DESCRIPTION", 
            "AMOUNT", "CURRENCY", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "CHANGE", "ADD", "DELETE", "RESET", 
                  "CATEGORY", "DESCRIPTION", "AMOUNT", "CURRENCY", "WS" ]

    grammarFileName = "Finance.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


