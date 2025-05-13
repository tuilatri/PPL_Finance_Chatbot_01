# Generated from D:\PPL_Finance_Chatbot_01\Finance.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\6\2\33")
        buf.write("\n\2\r\2\16\2\34\3\2\3\2\3\3\3\3\5\3#\n\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\7\5+\n\5\f\5\16\5.\13\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7;\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\2\2\2T\2\32\3\2\2\2\4\"\3\2\2")
        buf.write("\2\6$\3\2\2\2\b\'\3\2\2\2\n/\3\2\2\2\f:\3\2\2\2\16<\3")
        buf.write("\2\2\2\20D\3\2\2\2\22K\3\2\2\2\24R\3\2\2\2\26U\3\2\2\2")
        buf.write("\30\33\5\f\7\2\31\33\5\4\3\2\32\30\3\2\2\2\32\31\3\2\2")
        buf.write("\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\36\3\2")
        buf.write("\2\2\36\37\7\2\2\3\37\3\3\2\2\2 #\5\6\4\2!#\5\b\5\2\"")
        buf.write(" \3\2\2\2\"!\3\2\2\2#\5\3\2\2\2$%\7\b\2\2%&\7\t\2\2&\7")
        buf.write("\3\2\2\2\',\5\n\6\2()\7\r\2\2)+\5\n\6\2*(\3\2\2\2+.\3")
        buf.write("\2\2\2,*\3\2\2\2,-\3\2\2\2-\t\3\2\2\2.,\3\2\2\2/\60\7")
        buf.write("\7\2\2\60\61\7\13\2\2\61\62\7\b\2\2\62\63\7\t\2\2\63\64")
        buf.write("\7\f\2\2\64\13\3\2\2\2\65;\5\16\b\2\66;\5\20\t\2\67;\5")
        buf.write("\22\n\28;\5\24\13\29;\5\26\f\2:\65\3\2\2\2:\66\3\2\2\2")
        buf.write(":\67\3\2\2\2:8\3\2\2\2:9\3\2\2\2;\r\3\2\2\2<=\7\7\2\2")
        buf.write("=>\7\n\2\2>?\7\7\2\2?@\7\13\2\2@A\7\b\2\2AB\7\t\2\2BC")
        buf.write("\7\f\2\2C\17\3\2\2\2DE\7\3\2\2EF\7\7\2\2FG\7\13\2\2GH")
        buf.write("\7\b\2\2HI\7\t\2\2IJ\7\f\2\2J\21\3\2\2\2KL\7\4\2\2LM\7")
        buf.write("\7\2\2MN\7\13\2\2NO\7\b\2\2OP\7\t\2\2PQ\7\f\2\2Q\23\3")
        buf.write("\2\2\2RS\7\5\2\2ST\7\7\2\2T\25\3\2\2\2UV\7\6\2\2V\27\3")
        buf.write("\2\2\2\7\32\34\",:")
        return buf.getvalue()


class FinanceParser ( Parser ):

    grammarFileName = "Finance.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Change'", "'Add'", "'Delete'", "'Reset'", 
                     "<INVALID>", "<INVALID>", "'VND'", "':'", "'('", "')'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "VND", "COLON", "LPAREN", 
                      "RPAREN", "COMMA", "WS" ]

    RULE_program = 0
    RULE_input = 1
    RULE_salaryInput = 2
    RULE_categoriesInput = 3
    RULE_category = 4
    RULE_command = 5
    RULE_spendCommand = 6
    RULE_changeCommand = 7
    RULE_addCommand = 8
    RULE_deleteCommand = 9
    RULE_resetCommand = 10

    ruleNames =  [ "program", "input", "salaryInput", "categoriesInput", 
                   "category", "command", "spendCommand", "changeCommand", 
                   "addCommand", "deleteCommand", "resetCommand" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    NUMBER=6
    VND=7
    COLON=8
    LPAREN=9
    RPAREN=10
    COMMA=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FinanceParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceParser.CommandContext)
            else:
                return self.getTypedRuleContext(FinanceParser.CommandContext,i)


        def input(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceParser.InputContext)
            else:
                return self.getTypedRuleContext(FinanceParser.InputContext,i)


        def getRuleIndex(self):
            return FinanceParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = FinanceParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.command()
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.input()
                    pass


                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FinanceParser.T__0) | (1 << FinanceParser.T__1) | (1 << FinanceParser.T__2) | (1 << FinanceParser.T__3) | (1 << FinanceParser.ID) | (1 << FinanceParser.NUMBER))) != 0)):
                    break

            self.state = 28
            self.match(FinanceParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def salaryInput(self):
            return self.getTypedRuleContext(FinanceParser.SalaryInputContext,0)


        def categoriesInput(self):
            return self.getTypedRuleContext(FinanceParser.CategoriesInputContext,0)


        def getRuleIndex(self):
            return FinanceParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)




    def input(self):

        localctx = FinanceParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_input)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FinanceParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.salaryInput()
                pass
            elif token in [FinanceParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.categoriesInput()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SalaryInputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(FinanceParser.NUMBER, 0)

        def VND(self):
            return self.getToken(FinanceParser.VND, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_salaryInput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSalaryInput" ):
                listener.enterSalaryInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSalaryInput" ):
                listener.exitSalaryInput(self)




    def salaryInput(self):

        localctx = FinanceParser.SalaryInputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_salaryInput)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(FinanceParser.NUMBER)
            self.state = 35
            self.match(FinanceParser.VND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoriesInputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def category(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceParser.CategoryContext)
            else:
                return self.getTypedRuleContext(FinanceParser.CategoryContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(FinanceParser.COMMA)
            else:
                return self.getToken(FinanceParser.COMMA, i)

        def getRuleIndex(self):
            return FinanceParser.RULE_categoriesInput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategoriesInput" ):
                listener.enterCategoriesInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategoriesInput" ):
                listener.exitCategoriesInput(self)




    def categoriesInput(self):

        localctx = FinanceParser.CategoriesInputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_categoriesInput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.category()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FinanceParser.COMMA:
                self.state = 38
                self.match(FinanceParser.COMMA)
                self.state = 39
                self.category()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FinanceParser.ID, 0)

        def LPAREN(self):
            return self.getToken(FinanceParser.LPAREN, 0)

        def NUMBER(self):
            return self.getToken(FinanceParser.NUMBER, 0)

        def VND(self):
            return self.getToken(FinanceParser.VND, 0)

        def RPAREN(self):
            return self.getToken(FinanceParser.RPAREN, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_category

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategory" ):
                listener.enterCategory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategory" ):
                listener.exitCategory(self)




    def category(self):

        localctx = FinanceParser.CategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_category)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(FinanceParser.ID)
            self.state = 46
            self.match(FinanceParser.LPAREN)
            self.state = 47
            self.match(FinanceParser.NUMBER)
            self.state = 48
            self.match(FinanceParser.VND)
            self.state = 49
            self.match(FinanceParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spendCommand(self):
            return self.getTypedRuleContext(FinanceParser.SpendCommandContext,0)


        def changeCommand(self):
            return self.getTypedRuleContext(FinanceParser.ChangeCommandContext,0)


        def addCommand(self):
            return self.getTypedRuleContext(FinanceParser.AddCommandContext,0)


        def deleteCommand(self):
            return self.getTypedRuleContext(FinanceParser.DeleteCommandContext,0)


        def resetCommand(self):
            return self.getTypedRuleContext(FinanceParser.ResetCommandContext,0)


        def getRuleIndex(self):
            return FinanceParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = FinanceParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_command)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FinanceParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.spendCommand()
                pass
            elif token in [FinanceParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.changeCommand()
                pass
            elif token in [FinanceParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.addCommand()
                pass
            elif token in [FinanceParser.T__2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.deleteCommand()
                pass
            elif token in [FinanceParser.T__3]:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.resetCommand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpendCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(FinanceParser.ID)
            else:
                return self.getToken(FinanceParser.ID, i)

        def COLON(self):
            return self.getToken(FinanceParser.COLON, 0)

        def LPAREN(self):
            return self.getToken(FinanceParser.LPAREN, 0)

        def NUMBER(self):
            return self.getToken(FinanceParser.NUMBER, 0)

        def VND(self):
            return self.getToken(FinanceParser.VND, 0)

        def RPAREN(self):
            return self.getToken(FinanceParser.RPAREN, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_spendCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpendCommand" ):
                listener.enterSpendCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpendCommand" ):
                listener.exitSpendCommand(self)




    def spendCommand(self):

        localctx = FinanceParser.SpendCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_spendCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(FinanceParser.ID)
            self.state = 59
            self.match(FinanceParser.COLON)
            self.state = 60
            self.match(FinanceParser.ID)
            self.state = 61
            self.match(FinanceParser.LPAREN)
            self.state = 62
            self.match(FinanceParser.NUMBER)
            self.state = 63
            self.match(FinanceParser.VND)
            self.state = 64
            self.match(FinanceParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChangeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FinanceParser.ID, 0)

        def LPAREN(self):
            return self.getToken(FinanceParser.LPAREN, 0)

        def NUMBER(self):
            return self.getToken(FinanceParser.NUMBER, 0)

        def VND(self):
            return self.getToken(FinanceParser.VND, 0)

        def RPAREN(self):
            return self.getToken(FinanceParser.RPAREN, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_changeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChangeCommand" ):
                listener.enterChangeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChangeCommand" ):
                listener.exitChangeCommand(self)




    def changeCommand(self):

        localctx = FinanceParser.ChangeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_changeCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(FinanceParser.T__0)
            self.state = 67
            self.match(FinanceParser.ID)
            self.state = 68
            self.match(FinanceParser.LPAREN)
            self.state = 69
            self.match(FinanceParser.NUMBER)
            self.state = 70
            self.match(FinanceParser.VND)
            self.state = 71
            self.match(FinanceParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FinanceParser.ID, 0)

        def LPAREN(self):
            return self.getToken(FinanceParser.LPAREN, 0)

        def NUMBER(self):
            return self.getToken(FinanceParser.NUMBER, 0)

        def VND(self):
            return self.getToken(FinanceParser.VND, 0)

        def RPAREN(self):
            return self.getToken(FinanceParser.RPAREN, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_addCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddCommand" ):
                listener.enterAddCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddCommand" ):
                listener.exitAddCommand(self)




    def addCommand(self):

        localctx = FinanceParser.AddCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_addCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(FinanceParser.T__1)
            self.state = 74
            self.match(FinanceParser.ID)
            self.state = 75
            self.match(FinanceParser.LPAREN)
            self.state = 76
            self.match(FinanceParser.NUMBER)
            self.state = 77
            self.match(FinanceParser.VND)
            self.state = 78
            self.match(FinanceParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FinanceParser.ID, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_deleteCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteCommand" ):
                listener.enterDeleteCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteCommand" ):
                listener.exitDeleteCommand(self)




    def deleteCommand(self):

        localctx = FinanceParser.DeleteCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_deleteCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(FinanceParser.T__2)
            self.state = 81
            self.match(FinanceParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResetCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FinanceParser.RULE_resetCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResetCommand" ):
                listener.enterResetCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResetCommand" ):
                listener.exitResetCommand(self)




    def resetCommand(self):

        localctx = FinanceParser.ResetCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_resetCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(FinanceParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





