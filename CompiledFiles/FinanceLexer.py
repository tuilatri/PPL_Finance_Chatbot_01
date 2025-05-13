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
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\7\6\66")
        buf.write("\n\6\f\6\16\69\13\6\3\7\6\7<\n\7\r\7\16\7=\3\7\3\7\6\7")
        buf.write("B\n\7\r\7\16\7C\7\7F\n\7\f\7\16\7I\13\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\6\rX\n\r\r\r")
        buf.write("\16\rY\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\3\2\6\4\2C\\c|\5\2\62;C\\c|\3")
        buf.write("\2\62;\5\2\13\f\17\17\"\"\2a\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\"\3\2\2\2\7&\3\2\2\2")
        buf.write("\t-\3\2\2\2\13\63\3\2\2\2\r;\3\2\2\2\17J\3\2\2\2\21N\3")
        buf.write("\2\2\2\23P\3\2\2\2\25R\3\2\2\2\27T\3\2\2\2\31W\3\2\2\2")
        buf.write("\33\34\7E\2\2\34\35\7j\2\2\35\36\7c\2\2\36\37\7p\2\2\37")
        buf.write(" \7i\2\2 !\7g\2\2!\4\3\2\2\2\"#\7C\2\2#$\7f\2\2$%\7f\2")
        buf.write("\2%\6\3\2\2\2&\'\7F\2\2\'(\7g\2\2()\7n\2\2)*\7g\2\2*+")
        buf.write("\7v\2\2+,\7g\2\2,\b\3\2\2\2-.\7T\2\2./\7g\2\2/\60\7u\2")
        buf.write("\2\60\61\7g\2\2\61\62\7v\2\2\62\n\3\2\2\2\63\67\t\2\2")
        buf.write("\2\64\66\t\3\2\2\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2")
        buf.write("\2\678\3\2\2\28\f\3\2\2\29\67\3\2\2\2:<\t\4\2\2;:\3\2")
        buf.write("\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>G\3\2\2\2?A\7\60\2")
        buf.write("\2@B\t\4\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D")
        buf.write("F\3\2\2\2E?\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\16")
        buf.write("\3\2\2\2IG\3\2\2\2JK\7X\2\2KL\7P\2\2LM\7F\2\2M\20\3\2")
        buf.write("\2\2NO\7<\2\2O\22\3\2\2\2PQ\7*\2\2Q\24\3\2\2\2RS\7+\2")
        buf.write("\2S\26\3\2\2\2TU\7.\2\2U\30\3\2\2\2VX\t\5\2\2WV\3\2\2")
        buf.write("\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\b\r\2\2")
        buf.write("\\\32\3\2\2\2\b\2\67=CGY\3\b\2\2")
        return buf.getvalue()


class FinanceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ID = 5
    NUMBER = 6
    VND = 7
    COLON = 8
    LPAREN = 9
    RPAREN = 10
    COMMA = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Change'", "'Add'", "'Delete'", "'Reset'", "'VND'", "':'", 
            "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMBER", "VND", "COLON", "LPAREN", "RPAREN", "COMMA", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ID", "NUMBER", "VND", 
                  "COLON", "LPAREN", "RPAREN", "COMMA", "WS" ]

    grammarFileName = "Finance.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


