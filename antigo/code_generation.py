from sidekick import opt
from types import SimpleNamespace


Node = (
    opt.Number(1)
    | opt.Name(1)
    | opt.Add(2) 
    | opt.Mul(2) 
    | opt.Div(2) 
    | opt.Sub(2)
    | opt.NameAttrib(2)
    | opt.Block(1)
    | opt.ForBlock(3)
    | opt.WhileBlock(2)
    | opt.IfBlock(2)
    | opt.EliIfBlock(2)
    | opt.ElseBlock(1)
    | opt.FunCall(2)
    | opt.FunDef(3)
)

Number, Name = Node.Number, Node.Name 
Add, Mul, Div, Sub = \
    Node.Add, Node.Mul, Node.Div, Node.Sub
NameAttrib = Node.NameAttrib
Block = Node.Block
ForBlock = Node.ForBlock


def source(ast):
    """
    Emite código python a partir da árvore sintática.
    """
    
    ctx = SimpleNamespace(tokens=[], indent=0)
    visit(ctx, ast)
    return ''.join(ctx.tokens)


def visit(ctx, ast):
    if ast.number:
        x = str(ast.number_args[0])
        ctx.tokens.append(x)
    
    elif ast.name:
        ctx.tokens.append(ast.name_args[0])

    elif ast.add:
        x, y = ast.add_args
        ctx.tokens.append('(')
        visit(ctx, x)
        ctx.tokens.append(' + ')
        visit(ctx, y)
        ctx.tokens.append(')')
    
    elif ast.mul:
        x, y = ast.mul_args
        ctx.tokens.append('(')
        visit(ctx, x)
        ctx.tokens.append(' * ')
        visit(ctx, y)
        ctx.tokens.append(')')
    
    elif ast.div:
        x, y = ast.div_args
        ctx.tokens.append('(')
        visit(ctx, x)
        ctx.tokens.append(' / ')
        visit(ctx, y)
        ctx.tokens.append(')')
    
    elif ast.sub:
        x, y = ast.sub_args
        ctx.tokens.append('(')
        visit(ctx, x)
        ctx.tokens.append(' - ')
        visit(ctx, y)
        ctx.tokens.append(')')
    
    elif ast.nameattrib:
        x, y = ast.nameattrib_args
        ctx.tokens.append(x)
        ctx.tokens.append(' = ')
        visit(ctx, y)

    elif ast.block:
        block = ast.block_args[0]
        if not block:
            block.append(Name('pass'))
        
        for node in block:
            ctx.tokens.append('    ' * ctx.indent)
            visit(ctx, node)
            ctx.tokens.append('\n')

    elif ast.forblock:
        counter, iterable, block = ast.forblock_args
        ctx.tokens.append('for ')
        visit(ctx, counter)
        ctx.tokens.append(' in ')
        visit(ctx, iterable)
        ctx.tokens.append(':\n')
        ctx.indent += 1
        visit(ctx, block)
        ctx.indent -= 1

    else:
        raise ValueError('node is not supported: %s' % ast)

# Testa o codigo
expr1 = NameAttrib('x', Add(Name('x'), Number(1)))
expr2 = NameAttrib('y', Number(42))
block = Block([expr1, expr2])
expr = ForBlock(Name('x'), Name('L'), block)

print(expr)
print(source(expr))