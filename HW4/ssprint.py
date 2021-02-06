# This transforms the AST into a nicer format when we print out step by step

from lark import tree, Lark

class StepbyStep(object):
    def __init__(self):
        self.map_oper = {"add": "+", 
                    "mul":"*", 
                    "sub": "-", 
                    "div": "/", 
                    "and": "∧", 
                    "or": "∨"}
        

    def format(self, tree):
        stmt_oper = tree.data

        if stmt_oper == "not":
            return "¬" + self.format(tree.children[0])
        

        elif stmt_oper == "true_cond":
            return "true"
        

        elif stmt_oper == "false_cond":
            return "false"    
        

        elif stmt_oper == "number":
            return str(int(tree.children[0]))
        

        elif stmt_oper == "variable":
            return tree.children[0]


        elif stmt_oper == "assigning":
            return tree.children[0].children[0] + " := " + self.format(tree.children[1])


        elif stmt_oper in {"add", "mul", "sub", "div", "and", "or"}:
            return "(" + self.format(tree.children[0]) + self.map_oper[stmt_oper] + self.format(tree.children[1]) + ")"


        elif stmt_oper == "compare":
            return "(" + self.format(tree.children[0]) + tree.children[1] + self.format(tree.children[2]) + ")"


        elif stmt_oper == "sstatement":
            return self.format(tree.children[0]) + "; " + self.format(tree.children[1])


        elif stmt_oper == "if":
            return "if " + self.format(tree.children[0]) + " then { " + self.format(tree.children[1]) + " } else { " + self.format(tree.children[2]) + " }"
        

        elif stmt_oper in {"cwhile", "swhile"}:
            return "while " + self.format(tree.children[0]) + " do { " + self.format(tree.children[1]) + " }"
        

        elif stmt_oper == "seq":
            seq = ""
            for temp in range(len(tree.children)):
                seq += self.format(tree.children[temp]) + "; " if temp != len(tree.children) - 1 else self.format(tree.children[temp])

            return seq
