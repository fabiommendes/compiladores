import sidekick as sk 


class Expr(sk.Union):
    Atom = sk.opt(object)
    BinOp = sk.opt(op=str, left=Expr, right=Expr)
    FCall = sk.opt(name=str, fargs=list)


class Stmt(sk.Union):
    Assign = sk.opt(name=str, expr=Expr)

# Expressions
Atom = Expr.Atom
BinOp = Expr.BinOp
FCall = Expr.FCall

# Statements
Assign = Stmt.Assign
