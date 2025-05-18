# Generated from D:\PPL_Finance_Chatbot_01\Finance.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FinanceParser import FinanceParser
else:
    from FinanceParser import FinanceParser

# This class defines a complete listener for a parse tree produced by FinanceParser.
class FinanceListener(ParseTreeListener):

    # Enter a parse tree produced by FinanceParser#program.
    def enterProgram(self, ctx:FinanceParser.ProgramContext):
        pass

    # Exit a parse tree produced by FinanceParser#program.
    def exitProgram(self, ctx:FinanceParser.ProgramContext):
        pass


    # Enter a parse tree produced by FinanceParser#userInput.
    def enterUserInput(self, ctx:FinanceParser.UserInputContext):
        pass

    # Exit a parse tree produced by FinanceParser#userInput.
    def exitUserInput(self, ctx:FinanceParser.UserInputContext):
        pass


    # Enter a parse tree produced by FinanceParser#salaryInput.
    def enterSalaryInput(self, ctx:FinanceParser.SalaryInputContext):
        pass

    # Exit a parse tree produced by FinanceParser#salaryInput.
    def exitSalaryInput(self, ctx:FinanceParser.SalaryInputContext):
        pass


    # Enter a parse tree produced by FinanceParser#categoriesInput.
    def enterCategoriesInput(self, ctx:FinanceParser.CategoriesInputContext):
        pass

    # Exit a parse tree produced by FinanceParser#categoriesInput.
    def exitCategoriesInput(self, ctx:FinanceParser.CategoriesInputContext):
        pass


    # Enter a parse tree produced by FinanceParser#category.
    def enterCategory(self, ctx:FinanceParser.CategoryContext):
        pass

    # Exit a parse tree produced by FinanceParser#category.
    def exitCategory(self, ctx:FinanceParser.CategoryContext):
        pass


    # Enter a parse tree produced by FinanceParser#command.
    def enterCommand(self, ctx:FinanceParser.CommandContext):
        pass

    # Exit a parse tree produced by FinanceParser#command.
    def exitCommand(self, ctx:FinanceParser.CommandContext):
        pass


    # Enter a parse tree produced by FinanceParser#spendCommand.
    def enterSpendCommand(self, ctx:FinanceParser.SpendCommandContext):
        pass

    # Exit a parse tree produced by FinanceParser#spendCommand.
    def exitSpendCommand(self, ctx:FinanceParser.SpendCommandContext):
        pass


    # Enter a parse tree produced by FinanceParser#changeCommand.
    def enterChangeCommand(self, ctx:FinanceParser.ChangeCommandContext):
        pass

    # Exit a parse tree produced by FinanceParser#changeCommand.
    def exitChangeCommand(self, ctx:FinanceParser.ChangeCommandContext):
        pass


    # Enter a parse tree produced by FinanceParser#addCommand.
    def enterAddCommand(self, ctx:FinanceParser.AddCommandContext):
        pass

    # Exit a parse tree produced by FinanceParser#addCommand.
    def exitAddCommand(self, ctx:FinanceParser.AddCommandContext):
        pass


    # Enter a parse tree produced by FinanceParser#deleteCommand.
    def enterDeleteCommand(self, ctx:FinanceParser.DeleteCommandContext):
        pass

    # Exit a parse tree produced by FinanceParser#deleteCommand.
    def exitDeleteCommand(self, ctx:FinanceParser.DeleteCommandContext):
        pass


    # Enter a parse tree produced by FinanceParser#resetCommand.
    def enterResetCommand(self, ctx:FinanceParser.ResetCommandContext):
        pass

    # Exit a parse tree produced by FinanceParser#resetCommand.
    def exitResetCommand(self, ctx:FinanceParser.ResetCommandContext):
        pass



del FinanceParser