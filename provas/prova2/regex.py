import re

# BEGIN IGNORE
# (truques sujos com metaclasses do Python para habilitar a sintaxe da próxima
# seção)
class ReMeta(type):
    n_tests = -1

    def __new__(cls, name, bases, ns):
        doc = ns['__doc__']
        ok, _, fail = map(str.split, map(str.strip, doc.strip().splitlines()))
        try:
            regex = re.compile(ns['regex'])
        except KeyError:
            print('teste:', name)
            raise SystemExit('não apague o atributo "regex" da classe')
        except:
            print('teste:', name)
            raise SystemExit('regex inválida')
        
        cls.n_tests += 1
        if ns.get('enabled', True):
            print('\n%s) ' % cls.n_tests + name.replace('_', ' ').title())
            errors = 0
            for example in ok:
                if not regex.fullmatch(example):
                    errors += 1
                    print('  falha: recusou a string %r' % example)
            for example in fail:                
                if regex.fullmatch(example):
                    errors += 1
                    print('  falha: aceitou a string %r' % example)
            
            print('terminou com %s erros' % errors)

Re = type.__new__(ReMeta, 'Re', (), {})
print('INICIANDO...')   
# END IGNORE


# Classe de exemplo já respondida. Observe que existe uma lista de exemplos 
# que a regex deve aceitar, seguida por uma lista em branco e uma lista de 
# exemplos que a regex deve recusar
class testes_de_exemplo(Re):
    """
    42 10 20
    
    1.2 .1
    """
    regex = r'[0-9]+'
    enabled = True    # você pode desligar os testes de uma classe quando quiser


#
# A partir daqui é com vocês!
#
class nome_de_variável_simples_sem_letra_minúscula(Re):
    """
    foo bar foo_bar name other_name a b _

    foo1 Foo FooBar _Foo FOO foo2 2foo
    """
    regex = r''
    enabled = True


class algumas_palavras_reservadas(Re):
    """
    for def True False

    None print exec ...
    """
    regex = r''
    enabled = False         # não esqueça de ativar os testes daqui para frente!


class número_inteiro_com_sinal_opcional(Re):
    """
    1 +1 -1 42 +42 -15

    + - 4-2 42+ 4+2 ++42 -+42 +-10
    """
    regex = r''
    enabled = False


class texto_que_nao_contêm_as_letras_t_e_m_e_r(Re):
    """
    foo  42  *^*#$)@$  2018 FORA!

    golpe #$*#(e)
    """
    regex = r''
    enabled = False


class número_hexadecimal_positivo(Re):
    """
    0x0 0xFF 0x1F 0xFA32A3

    0xf FF 0x1G -0xAF
    """
    regex = r''
    enabled = False


class nome_com_a_notação_de_ponto(Re):
    """
    foo foo.bar foo.bar.baz

    .foo foo..bar foo. foo.bar. foo$foo ...
    """
    # dica: o nome é formado apenas por letras minúsculas
    regex = r''
    enabled = False


class número_inteiro_sem_zero_à_esquerda(Re):
    """
    42 1 -2 -1000 1234123 0

    01 0123 -04 -05 -0234234 -0012 0002 00 +42
    """
    regex = r''
    enabled = False


class inteiro_positivo_com_separador_de_milhares_a_cada_três_dígitos(Re):
    """
    1 42 1_000 1_324 1_234_567

    -1 1234 12_34
    """
    regex = r''
    enabled = False


# Desafio: Vale o dobro das outras!
class string_com_escape(Re):
    r"""
    "foo"  ""  "#*(FW(@$&))"  "escape\"char"
 
    "not"escaped"  "forget-to-close  forget-to-open" "str"bad
    """
    regex = r''
    enabled = False
