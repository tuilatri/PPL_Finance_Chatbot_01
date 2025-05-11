# Generated from D:\PPL_Finance_Chatbot_01\Finance.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FinanceParser import FinanceParser
else:
    from FinanceParser import FinanceParser

# This class defines a complete listener for a parse tree produced by FinanceParser.
class FinanceListener(ParseTreeListener):

    # Enter a parse tree produced by FinanceParser#command.
    def enterCommand(self, ctx:FinanceParser.CommandContext):
        pass

    # Exit a parse tree produced by FinanceParser#command.
    def exitCommand(self, ctx:FinanceParser.CommandContext):
        pass


    # Enter a parse tree produced by FinanceParser#addExpense.
    def enterAddExpense(self, ctx:FinanceParser.AddExpenseContext):
        pass

    # Exit a parse tree produced by FinanceParser#addExpense.
    def exitAddExpense(self, ctx:FinanceParser.AddExpenseContext):
        pass


    # Enter a parse tree produced by FinanceParser#changeCategory.
    def enterChangeCategory(self, ctx:FinanceParser.ChangeCategoryContext):
        pass

    # Exit a parse tree produced by FinanceParser#changeCategory.
    def exitChangeCategory(self, ctx:FinanceParser.ChangeCategoryContext):
        pass


    # Enter a parse tree produced by FinanceParser#addCategory.
    def enterAddCategory(self, ctx:FinanceParser.AddCategoryContext):
        pass

    # Exit a parse tree produced by FinanceParser#addCategory.
    def exitAddCategory(self, ctx:FinanceParser.AddCategoryContext):
        pass


    # Enter a parse tree produced by FinanceParser#deleteCategory.
    def enterDeleteCategory(self, ctx:FinanceParser.DeleteCategoryContext):
        pass

    # Exit a parse tree produced by FinanceParser#deleteCategory.
    def exitDeleteCategory(self, ctx:FinanceParser.DeleteCategoryContext):
        pass


    # Enter a parse tree produced by FinanceParser#resetCommand.
    def enterResetCommand(self, ctx:FinanceParser.ResetCommandContext):
        pass

    # Exit a parse tree produced by FinanceParser#resetCommand.
    def exitResetCommand(self, ctx:FinanceParser.ResetCommandContext):
        pass


    # Enter a parse tree produced by FinanceParser#categoryChange.
    def enterCategoryChange(self, ctx:FinanceParser.CategoryChangeContext):
        pass

    # Exit a parse tree produced by FinanceParser#categoryChange.
    def exitCategoryChange(self, ctx:FinanceParser.CategoryChangeContext):
        pass



del FinanceParser