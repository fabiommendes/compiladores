from exam import parse, grammar
from sys import path
from lark import LexError
import pytest
import json

path.insert(0, ".")


@pytest.fixture(
    params=["-1", "42", "3.14", "true", "false", "null", '"string"', '"some string?"']
)
def atomic(request):
    return request.param


@pytest.fixture(params=["[1, 2, 3]", "[1, [2, [3, []]]]", "[]"])
def array(request):
    return request.param


@pytest.fixture(params=['{"foo": "bar"}', '{"foo": {"bar": 42}}', "{}"])
def obj(request):
    return request.param


class TestExamples:
    def test_valores_atomicos(self, atomic):
        assert parse(atomic) == grammar.parse(atomic)

    def test_arrays(self, array):
        assert parse(array) == grammar.parse(array)

    def test_objetos(self, obj):
        assert parse(obj) == grammar.parse(obj)

    def test_remove_colchete_final(self):
        assert parse('{"x": []}') == {"x": []}
        assert parse('{"x": [1]}') == {"x": [1]}

    def test_remove_chave_final(self):
        assert parse("[{}]") == [{}]
        assert parse('[{"x": 1}]') == [{"x": 1}]

    def teste_complexo(self):
        src = """
        {
            "name": "Fulano da Silva",
            "age": 20,
            "languages": [
                "Python",
                "Javascript",
                "Haskell"
            ]
        }
        """
        assert parse(src) == grammar.parse(src) == json.loads(src)



class TestInvalid:
    def invalid(self, src):
        with pytest.raises((ValueError, SyntaxError, LexError)):
            result = parse(src)
            print("In:", src)
            print("Out:", result)

    def test_rejeita_virgula_no_fim_da_lista(self):
        self.invalid("[1, 2,]")

    def test_rejeita_virgula_no_fim_do_objeto(self):
        self.invalid('{"x": 1, "y": 2,}')

    def test_rejeita_chaves_que_nao_sao_strings(self):
        self.invalid("{foo: 42}")
        self.invalid("{null: 42}")
        self.invalid("{42: 42}")

    def test_nao_aceita_valores_com_tokens_sobrando(self):
        self.invalid('1 2')
        self.invalid('[] 2')
        self.invalid('true false null')

    def test_rejeita_lista_sem_virgula_entre_itens(self):
        self.invalid('[1 2]')
        self.invalid('{"foo": "bar" "baz": "zaz"}')

    def test_rejeita_par_sem_dois_pontos(self):
        self.invalid('{"foo" "bar"}')
        self.invalid('{"foo", "bar"}')
        