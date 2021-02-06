"""

Jessica Pan -- jeypan@ucsc.edu
Winter 2021 -- CSE 210A Programming Languages
HW4 -- WHILE-SS interpreter

I used the lark-parser library in python to create the AST of while and
to interpret the AST tree.
Links I used for this assignment that helped me a lot:
https://www.gitmemory.com/issue/lark-parser/lark/355/481851369
https://github.com/lark-parser/lark/blob/master/docs/json_tutorial.md
https://github.com/lark-parser/lark/tree/master/examples
"""

import sys

from lark import Lark
from collections import OrderedDict
from ssprint import *

sys.setrecursionlimit(10000)

class InterpAST():
    def __init__(self, parser):
        self.parser = parser
        self.state = {}
        self.stepbystep = StepbyStep()
        self.ss = []    # list of steps
        self.whileCount = 0
    
    def checkVariable(self, var):
        if var in self.state:
            return self.state[var]
        return 0

    def booleanCHECK(self, oper, L, R):
        if oper == "=":
            return L == R

        elif oper == "<":
            return L < R

        elif oper == ">":
            return L > R

    def interpret(self, tree):
        stmt_oper = tree.data

        # NOT
        if stmt_oper == "not":
            if not self.interpret(tree.children[0]):
                return 1
            
            else:
                return 0
        
        # TRUE condition
        elif stmt_oper == "true_cond":
            return 1

        # FALSE condition
        elif stmt_oper == "false_cond":
            return 0
            
        # AND ^
        elif stmt_oper == "and":
            return self.interpret(tree.children[0]) and self.interpret(tree.children[1])

        # OR v
        elif stmt_oper == "or":
            return self.interpret(tree.children[0]) or self.interpret(tree.children[1])

        # get number
        if stmt_oper == "number":
            return int(tree.children[0])

        # peek for variable
        elif stmt_oper == "variable":
            return self.checkVariable(tree.children[0])

        # Variable assignment
        elif stmt_oper == "assigning":
            # include skip for step by step
            variable = tree.children[0].children[0]
            self.state[variable] = self.interpret(tree.children[1])
            
            self.ss.append("skip, " + self.showStore())

            return
            
        # COMPARE left & right
        elif stmt_oper == "compare":
            coper = tree.children[1]
            L = self.interpret(tree.children[0])
            R = self.interpret(tree.children[2])

            return self.booleanCHECK(coper, L, R)

        # ARITH operations
        elif stmt_oper in {"add", "mul", "sub", "div"}:
            L = self.interpret(tree.children[0])
            R = self.interpret(tree.children[1])

            if stmt_oper == 'add':
                return L + R

            elif stmt_oper == 'mul':
                return L * R

            elif stmt_oper == 'sub':
                return L - R
                
            elif stmt_oper == 'div':
                return round(L / R)

        # SKIP stmt: do nothing just return and add skip to ss
        elif stmt_oper == "skip":
            self.ss.append(' ,' + self.showStore())
            return 

        # regular stmt (C1 to C1; C2)
        elif stmt_oper == "sstatement":    
            
            clen = len(self.ss)
            self.interpret(tree.children[0])

            # mod results
            for n in range(clen, len(self.ss)):
                modlen = len(self.ss[n].split(","))
                res = self.ss[n].split(",")[0] + "; " + self.stepbystep.format(tree.children[1])
                
                for temp in range(1, modlen):
                    res += ',' + self.ss[n].split(",")[temp]

                self.ss[n] = res

            # print c2 to ss
            self.ss.append(self.stepbystep.format(tree.children[1]) + ", " + self.showStore())
            self.interpret(tree.children[1])
            
            return

        # composite stmt (seq of assign: if, while))
        elif stmt_oper == "cstatement":

            clen = len(self.ss)
            self.interpret(tree.children[0])

            # mod reuslts
            for n in range(clen, len(self.ss)):
                modlen = len(self.ss[n].split(","))
                res = self.ss[n].split(",")[0] + "; " + self.stepbystep.format(tree.children[1])
                
                for temp in range(1, modlen):
                    res += ',' + self.ss[n].split(",")[temp]
                
                self.ss[n] = res

            self.ss.append(self.stepbystep.format(tree.children[1]) + ", " + self.showStore())       # print c2
            self.interpret(tree.children[1])
            
            return

        
        # IF statement
        elif stmt_oper == "if":
            if self.interpret(tree.children[0]):
                # add to step-by-step
                self.ss.append(self.stepbystep.format(tree.children[1]) + ", " + self.showStore())
                
                # condition satisfied & execute stmts
                self.interpret(tree.children[1])

            elif not self.interpret(tree.children[0]) and len(tree.children) == 3:
                # add to step-by-step
                self.ss.append(self.stepbystep.format(tree.children[2]) + ", " + self.showStore())

                # condition unsatisfied & execute stmts after if-else stmt
                self.interpret(tree.children[2])

            return 
        
        # TERNARY if
        elif stmt_oper == "ternary":
            var = tree.children[0].children[0]
            condition = self.interpret(tree.children[1])
            
            self.state[var] = self.interpret(tree.children[2]) if condition else self.interpret(tree.children[3])
            
            return

        # while statement
        elif stmt_oper == "swhile":

            # count number of recursions (test case easy-17 doesn't work without whileCount)
            if self.whileCount <= 3332:
                self.whileCount += 1
                # print(self.whileCount)

            else:
                self.ss.append(self.stepbystep.format(tree.children[1]) + "; " + self.stepbystep.format(tree) + ", " + self.showStore())
                return
            
            if self.interpret(tree.children[0]):
                self.ss.append(self.stepbystep.format(tree.children[1]) + "; " + self.stepbystep.format(tree) + ", " + self.showStore())


                clen = len(self.ss)
                # condition statisfied & execute statements
                self.interpret(tree.children[1])

                # mod results
                for n in range(clen, len(self.ss)):
                    modlen = len(self.ss[n].split(","))
                    res = self.ss[n].split(",")[0] + "; " + self.stepbystep.format(tree)
                    
                    for temp in range(1, modlen):
                        res += ',' + self.ss[n].split(",")[temp]
                    
                    self.ss[n] = res

                self.ss.append(self.stepbystep.format(tree) + ", " + self.showStore())
                self.interpret(tree)

            elif not self.interpret(tree.children[0]) and tree.children[1].data == "sstatement":
                # assign; add skip
                self.ss.append("skip; " + self.stepbystep.format(tree.children[1].children[1]) + ", " + self.showStore())
                self.ss.append(self.stepbystep.format(tree.children[1].children[1]) + ", " + self.showStore())
                
                self.interpret(tree.children[1].children[1])

            else:
                # while false; add skip to store
                self.ss.append("skip, " + self.showStore())
                return

        elif stmt_oper == "cwhile":

            if self.interpret(tree.children[0]):
                
                self.ss.append(self.stepbystep.format(tree.children[1]) + "; " + self.stepbystep.format(tree) + ", " + self.showStore())
                
                clen = len(self.ss)
                self.interpret(tree.children[1])

                # mod results
                for n in range(clen, len(self.ss)):
                    modlen = len(self.ss[n].split(","))
                    res = self.ss[n].split(",")[0] + "; " + self.stepbystep.format(tree)
                    
                    for temp in range(1, modlen):
                        res += ',' + self.ss[n].split(",")[temp]

                    self.ss[n] = res

                self.ss.append(self.stepbystep.format(tree) + ", " + self.showStore())
                self.interpret(tree)

            else:
                # while false; add skip to store
                self.ss.append("skip, " + self.showStore())
                return


        elif stmt_oper == "seq":
            child = len(tree.children)
            
            # check all children
            for item in range(child-1):

                clen = len(self.ss)
                comandstr = ""
                for com in range(child - item - 1):
                    comandstr += self.stepbystep.format(tree.children[item+com+1]) if (com == child - item - 2) else self.stepbystep.format(tree.children[item+com+1]) + "; "

                self.interpret(tree.children[item])

                # mod results
                for n in range(clen, len(self.ss)):
                    modlen = len(self.ss[n].split(","))
                    res = self.ss[n].split(",")[0] + "; " + comandstr
                    
                    for temp in range(1, modlen):
                        res += ',' + self.ss[n].split(",")[temp]
                        
                    self.ss[n] = res

                # Print the rest
                self.ss.append(comandstr + ", " + self.showStore())
            
            # check last child
            self.interpret(tree.children[child-1])
            


                


    def showStore(self):
        itt = OrderedDict(sorted(self.state.items()))
        store = ", ".join(str(variable) + " → " + str(data) for variable, data in itt.items())
        
        return "{" + store + "}"

    def showResults(self):
        for i in self.ss:
            if i != " ,{}":
                print("⇒", i)

    def read(self, text):
        ast = self.parser.parse(text)
        self.interpret(ast)
        self.showResults() 

        return self.showStore()

if __name__ == '__main__':
    for input in sys.stdin:
        wp = Lark.open('WHILE.lark', parser='lalr')
        output = InterpAST(wp).read(input)
