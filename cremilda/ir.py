import sidekick as sk 


class Expr(sk.Union):
    Atom = sk.opt(object)
    FCall = sk.opt(name=str, fargs=list)
    Symbol = sk.opt(str)


class Stmt(sk.Union):
    Assign = sk.opt(name=str, value=Expr)
    FDef = sk.opt(name=str, args=list, body=list)
    Return = sk.opt(Expr)
