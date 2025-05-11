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
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\3\2\3\2\3\2\3\2\3\2\5\2\26\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16")
        buf.write("\2\2\2-\2\25\3\2\2\2\4\27\3\2\2\2\6\37\3\2\2\2\b\"\3\2")
        buf.write("\2\2\n%\3\2\2\2\f(\3\2\2\2\16*\3\2\2\2\20\26\5\4\3\2\21")
        buf.write("\26\5\6\4\2\22\26\5\b\5\2\23\26\5\n\6\2\24\26\5\f\7\2")
        buf.write("\25\20\3\2\2\2\25\21\3\2\2\2\25\22\3\2\2\2\25\23\3\2\2")
        buf.write("\2\25\24\3\2\2\2\26\3\3\2\2\2\27\30\7\n\2\2\30\31\7\3")
        buf.write("\2\2\31\32\7\13\2\2\32\33\7\4\2\2\33\34\7\f\2\2\34\35")
        buf.write("\7\r\2\2\35\36\7\5\2\2\36\5\3\2\2\2\37 \7\6\2\2 !\5\16")
        buf.write("\b\2!\7\3\2\2\2\"#\7\7\2\2#$\5\16\b\2$\t\3\2\2\2%&\7\b")
        buf.write("\2\2&\'\7\n\2\2\'\13\3\2\2\2()\7\t\2\2)\r\3\2\2\2*+\7")
        buf.write("\n\2\2+,\7\4\2\2,-\7\f\2\2-.\7\r\2\2./\7\5\2\2/\17\3\2")
        buf.write("\2\2\3\25")
        return buf.getvalue()


class FinanceParser ( Parser ):

    grammarFileName = "Finance.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'('", "')'", "'Change'", "'Add'", 
                     "'Delete'", "'Reset'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'VND'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CATEGORY", "DESCRIPTION", "AMOUNT", "CURRENCY", "WS" ]

    RULE_command = 0
    RULE_addExpense = 1
    RULE_changeCategory = 2
    RULE_addCategory = 3
    RULE_deleteCategory = 4
    RULE_resetCommand = 5
    RULE_categoryChange = 6

    ruleNames =  [ "command", "addExpense", "changeCategory", "addCategory", 
                   "deleteCategory", "resetCommand", "categoryChange" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    CATEGORY=8
    DESCRIPTION=9
    AMOUNT=10
    CURRENCY=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpense(self):
            return self.getTypedRuleContext(FinanceParser.AddExpenseContext,0)


        def changeCategory(self):
            return self.getTypedRuleContext(FinanceParser.ChangeCategoryContext,0)


        def addCategory(self):
            return self.getTypedRuleContext(FinanceParser.AddCategoryContext,0)


        def deleteCategory(self):
            return self.getTypedRuleContext(FinanceParser.DeleteCategoryContext,0)


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
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FinanceParser.CATEGORY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.addExpense()
                pass
            elif token in [FinanceParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.changeCategory()
                pass
            elif token in [FinanceParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.addCategory()
                pass
            elif token in [FinanceParser.T__5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.deleteCategory()
                pass
            elif token in [FinanceParser.T__6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 18
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


    class AddExpenseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATEGORY(self):
            return self.getToken(FinanceParser.CATEGORY, 0)

        def DESCRIPTION(self):
            return self.getToken(FinanceParser.DESCRIPTION, 0)

        def AMOUNT(self):
            return self.getToken(FinanceParser.AMOUNT, 0)

        def CURRENCY(self):
            return self.getToken(FinanceParser.CURRENCY, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_addExpense

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpense" ):
                listener.enterAddExpense(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpense" ):
                listener.exitAddExpense(self)




    def addExpense(self):

        localctx = FinanceParser.AddExpenseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_addExpense)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(FinanceParser.CATEGORY)
            self.state = 22
            self.match(FinanceParser.T__0)
            self.state = 23
            self.match(FinanceParser.DESCRIPTION)
            self.state = 24
            self.match(FinanceParser.T__1)
            self.state = 25
            self.match(FinanceParser.AMOUNT)
            self.state = 26
            self.match(FinanceParser.CURRENCY)
            self.state = 27
            self.match(FinanceParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChangeCategoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def categoryChange(self):
            return self.getTypedRuleContext(FinanceParser.CategoryChangeContext,0)


        def getRuleIndex(self):
            return FinanceParser.RULE_changeCategory

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChangeCategory" ):
                listener.enterChangeCategory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChangeCategory" ):
                listener.exitChangeCategory(self)




    def changeCategory(self):

        localctx = FinanceParser.ChangeCategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_changeCategory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(FinanceParser.T__3)
            self.state = 30
            self.categoryChange()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddCategoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def categoryChange(self):
            return self.getTypedRuleContext(FinanceParser.CategoryChangeContext,0)


        def getRuleIndex(self):
            return FinanceParser.RULE_addCategory

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddCategory" ):
                listener.enterAddCategory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddCategory" ):
                listener.exitAddCategory(self)




    def addCategory(self):

        localctx = FinanceParser.AddCategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_addCategory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(FinanceParser.T__4)
            self.state = 33
            self.categoryChange()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteCategoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATEGORY(self):
            return self.getToken(FinanceParser.CATEGORY, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_deleteCategory

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteCategory" ):
                listener.enterDeleteCategory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteCategory" ):
                listener.exitDeleteCategory(self)




    def deleteCategory(self):

        localctx = FinanceParser.DeleteCategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deleteCategory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(FinanceParser.T__5)
            self.state = 36
            self.match(FinanceParser.CATEGORY)
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
        self.enterRule(localctx, 10, self.RULE_resetCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(FinanceParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoryChangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATEGORY(self):
            return self.getToken(FinanceParser.CATEGORY, 0)

        def AMOUNT(self):
            return self.getToken(FinanceParser.AMOUNT, 0)

        def CURRENCY(self):
            return self.getToken(FinanceParser.CURRENCY, 0)

        def getRuleIndex(self):
            return FinanceParser.RULE_categoryChange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategoryChange" ):
                listener.enterCategoryChange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategoryChange" ):
                listener.exitCategoryChange(self)




    def categoryChange(self):

        localctx = FinanceParser.CategoryChangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_categoryChange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(FinanceParser.CATEGORY)
            self.state = 41
            self.match(FinanceParser.T__1)
            self.state = 42
            self.match(FinanceParser.AMOUNT)
            self.state = 43
            self.match(FinanceParser.CURRENCY)
            self.state = 44
            self.match(FinanceParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





