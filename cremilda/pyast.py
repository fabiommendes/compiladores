import sidekick as sk 


class Expr(sk.Union):
    Number = sk.opt(int)
    BinOp = sk.opt(op=str, left=Expr, right=Expr)
    FCall = sk.opt(name=str, fargs=list)


Number = Expr.Number
BinOp = Expr.BinOp
FCall = Expr.FCall