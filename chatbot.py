"""
Chatbot é uma função que recebe uma string e retorna uma string de resposta.
"""
import random
import re


#
# Chatbots
#
def yell_chatbot(msg):
    "Um chatbot que simplesmente repete a entrada do usuário"
    return msg.upper() + '!'


def make_regex_chatbot(regex_map, fallback='desculpe, não entendi...'):
    r"""
    Chatbot baseado em regex. Recebe um mapa entre regex e funções responsáveis
    por lidar com o padrão de regex correspondente.

    >>> chatbot = make_regex_chatbot({
    ...     r'oi, tudo bem\?': oneof(
    ...         'tudo bem!', 
    ...         'sim, e com você?'
    ...     ),
    ...     r'qual o seu nome\?': cte('Bot-o'),
    ...     r'meu nome é (?P<name>\w*)\.?': (
    ...         lambda match: 'oi {name}'.format(**match.groupdict())
    ...     ),
    ... })
    """
    regex_map = {re.compile(k): v for k, v in regex_map.items()}

    def chatbot(msg):
        for regex, handler in regex_map.items():
            match = regex.fullmatch(msg)
            if match:
                return handler(match)
        return fallback

    return chatbot


#
# Loop principal de interação
#
def interact(chatbot):
    "Chama o chatbot em loop"

    while True:
        try:
            msg = input('> ')
        except KeyboardInterrupt:
            print()
            msg = ''

        if not msg:
            if input('sair? (s/n) ').lower() == 's':
                break

        print(chatbot(msg), end='\n\n')


#
# Funções auxiliares
#
def cte(value):
    return lambda *args: value


def oneof(*options):
    return lambda *args: random.choice(options)


if __name__ == '__main__':
    # Escolhemos o chatbot e iniciamos o loop de interação
    chatbot = yell_chatbot

    interact(chatbot)
