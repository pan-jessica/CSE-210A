from lark import Lark, Transformer, v_args
import math
import sys

arith = """
    ?start: sum
    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> sub
    ?product: atom
        | product "*" atom  -> mul
        | product "/" atom  -> div
    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | "(" sum ")"
    %import common.NUMBER
    %ignore /[\t \f]+/  // whitespace
"""

@v_args(inline=True)    # Affects the signatures of the methods
class Interpret(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float


if __name__ == '__main__':
    arith_parser = Lark(arith, parser='lalr', transformer=Interpret())
    interp = arith_parser.parse
    
    for line in sys.stdin:
        line = line.strip()
        if line == "q":
            break

        print(math.trunc(interp(line)))