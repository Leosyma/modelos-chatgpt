# Bibliotecas
import openai
from dotenv import load_dotenv, find_dotenv

# Carrega a chave da API
_ = load_dotenv(find_dotenv())

# Conecta com o chatgpt
client = openai.Client()

# Função para geracao de texto
def geracao_texto(mensagens):
    # Define os parametros do modelo
    resposta = client.chat.completions.create(
        messages=mensagens,
        model='gpt-3.5-turbo-0125',
        temperature=0,
        max_tokens=1000,
        stream=True,
    )

    # Gera a resposta e salva
    print('Assistant: ', end='')
    texto_completo = ''
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    print()
    
    mensagens.append({'role': 'assistant', 'content': texto_completo})
    return mensagens


if __name__ == '__main__':

    print('Bem-vindo ao chatBot com Python')
    mensagens = []
    # Interface para fazer a pergunta
    while True:
        input_usuario = input('User: ')
        mensagens.append({'role': 'user', 'content': input_usuario})
        mensagens = geracao_texto(mensagens)

