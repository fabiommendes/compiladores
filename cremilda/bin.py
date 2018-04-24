from .lexer import lexer
from .parser import parser
from .compiler import compile_ast
from .emitter import generate_python_code


def main(argv):
    filename = argv[1]

    with open(filename) as F:
        src = F.read()

    # Pipeline básico de um compilador    
    tokens = lexer(src)
    ast = parser(tokens)
    ir = compile_ast(ast)
    py_src = generate_python_code(ir)

    # Imprime o resultado na tela
    print(py_src)