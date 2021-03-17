from lark import Lark, Transformer, v_args


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
"""

@v_args(inline=True)    # Affects the signatures of the methods
class Interpret(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float


if __name__ == '__main__':
    arith_parser = Lark(arith, parser='lalr', transformer=Interpret())
    interp = arith_parser.parse
    
    while True:
        s = input('> ')
        if s == "q":
            break

        print(interp(s), "\n")
