import re
from random import choice, paretovariate
from time import sleep
from unidecode import unidecode


# -------------------------------------------------------------------------------
# Interface de interação com chatbots
# -------------------------------------------------------------------------------

def interact(chatbot, ctx=None, intro=None):
    """Chama o chatbot em loop passando o contexto inicial."""

    # Mensagem opcional no início
    if intro is not None:
        respond(intro)

    while True:
        try:
            msg = input('> ')
        except KeyboardInterrupt:
            print()
            msg = ''

        if not msg:
            if input('sair? (S/n) ').lower() in 's':
                break

        ctx, reply = chatbot(ctx, clean(msg))
        respond(reply)


def replay(msgs, chatbot, ctx=None, intro=None):
    """
    Executa interação de forma não-interativa. Útil para testes.
    """
    if intro is not None:
        respond(intro)

    for msg in msgs:
        print('>', msg)
        ctx, reply = chatbot(ctx, clean(msg))
        respond(reply)


def respond(msg):
    for c in msg:
        print(c, end='', flush=True)
        if c == '\n':
            sleep(0.2)
        
        sleep((paretovariate(5) - 1)/ 5)
    print('\n', flush=True)
    sleep(0.4)


def clean(x):
    return unidecode(x.lower())


# -------------------------------------------------------------------------------
# Chatbots
# -------------------------------------------------------------------------------

def yell_bot(ctx, msg):
    """
    Bot que responde gritando de volta ao usuário.
    """
    return ctx, msg.upper() + '!!!'


def eq(expected, reply, to=None):
    """
    Retorna reply se entrada do usuário for exatamente igual ao valor 
    de msg.
    """

    expected = expected.lower()

    def eq_bot(ctx, msg):
        if msg.lower() == expected:
            return output(ctx, to, reply)
        return ctx, ''

    return eq_bot


def has(words, reply, to=None):
    """
    Retorna reply se entrada do usuário contiver
    alguma das palavras em words.
    """

    words = [w.lower() for w in words]

    def has_bot(ctx, msg):
        msg = msg.lower()
        if any(w in msg for w in words):
            return output(ctx, to, reply)
        return ctx, ''

    return has_bot


def always(reply, to=None):
    """
    Sempre retorna a mesma mensagem.
    """

    def bot(ctx, msg):
        return output(ctx, to, reply)
    return bot


def neverbot(msg, ctx):
    """
    Bot que nunca é selecionado
    """
    return ctx, ''

    
def regex(pattern, reply, to=None):
    """
    Função captura padrão e passa o dicionário de valores 
    para o output
    """
    search = re.compile(pattern).search
    
    def match_bot(ctx, msg):
        m = search(msg)
        if m:
            return output(ctx, to, reply, m.groupdict())
        else:
            return ctx, ''
        
    return match_bot


# Normaliza saídas.
def output(curr_ctx, ctx, reply, data=None):
    """
    Normaliza o padrão de saída:

    * Se ctx for None, escolhe curr_ctx. 
    * Se reply for uma função, utiliza reply()
    * Se for conjunto, lista ou tupla, sorteia elemento aleatorio
    * Se data for dado, formata string com dicionário de
      valores.
    """

    ctx = curr_ctx if ctx is None else ctx
    if callable(reply):
        reply = reply()
    elif isinstance(reply, (tuple, list, set)):
        reply = choice(list(reply))
    if data is not None:
        reply = reply.format(**data)
    return ctx, reply


# -------------------------------------------------------------------------------
# Composição de chatbots
# -------------------------------------------------------------------------------

def compose(*bots):
    """Cria chatbot que retorna a primeira interação bem sucedida 
    na lista de bots fornecidas."""

    def bot(ctx, msg):
        for bot in bots:
            ctx_, msg_ = bot(ctx, msg)
            if msg_:
                return ctx_, msg_
        return ctx, ''

    return bot


def if_msg(cond, bot, else_=neverbot):
    """
    Executa bot somente se função fornecida for avaliada como True na
    entrada do usuário.
    """
    def if_bot(ctx, msg):
        if cond(msg):
            return bot(ctx, msg)
        return else_(ctx, msg)
    return bot


def if_ctx(cond, bot, else_=neverbot):
    """
    Executa bot somente se função fornecida for avaliada como True no
    contexto atual.
    """
    def if_bot(ctx, msg):
        if cond(ctx):
            return bot(ctx, msg)
        return else_(ctx, msg)
    return bot


def story(name, *bots):
    """
    Cria uma história linear.

    Nenhuma parte da história pode ser capturada por uma
    regra anterior.
    """

    def bot(ctx, msg):
        if ctx and ctx.startswith(name + ':'):
            idx = int(ctx.partition(':')[-1])
            _, reply = bots[idx](ctx, msg)

            if reply:
                if idx == len(bots) - 1:
                    return None, reply
                return f'{name}:{idx + 1}', reply
            return None, ''
        else:
            ctx, reply = bots[0](ctx, msg)
            if reply:
                return f'{name}:1', reply
            return ctx, ''

    return bot


# Funções auxiliares para utilizar em if_ctx, if_msg
def one_of(*opts):
    return lambda x: x in opts


def has_one_of(*opts):
    return lambda x: any(a in x for x in opts)


def has_all_of(*opts):
    return lambda x: all(a in x for x in opts)


# -------------------------------------------------------------------------------
# Programa principal
# -------------------------------------------------------------------------------

def main_bot():
    """
    Cria e retorna o bot principal
    """
    return yell_bot


if __name__ == '__main__':
    # Escolhemos o chatbot e iniciamos o loop de interação

    # 1 - deixar a interrogacao e a virgula opcionais
    # 2 - capturar qualquer mensagem que comece com oi, ou olá, ou ola
    #
    # ... - passar no teste de turing...
    interact(main_bot())
