import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

historico = [
    {
        "role": "system",
        "content": """Você é um atendente virtual do SAC da empresa de energa elétrica chamada Energia Mais.
        Seu atendimento deve seguir exatamente esta ordem:
        1. Se apresentar como atendente da Energia Mais e cumprimentar o cliente
        2. Solicitar o nome completo do cliente
        3. Solicitar o endereço completo
        4. Solicitar o telefone para contato
        5. Perguntar qual é a reclamação ou solicitação
        6. Resumir todos os dados coletados e informar que o atendimento será realizado em até 3 dias úteis
        
        Seja educado. formal e empático. Colete um dado por vez, sem pressa.
        Não responda perguntas fora do contexto do atendimento da Energia Mais.
        Se o cliente fugir do assunto, redirecione gentilmente para o atendimento."""
    }
]

def perguntar(mensagem):
    historico.append({"role": "user", "content": mensagem})

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historico
    )

    conteudo = resposta.choices[0].message.content
    historico.append({"role": "assistant", "content": conteudo})
    return conteudo

print("=== Chat com Energia Mais ===")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() == "sair":
        print("Encerrando...")
        break
    resposta = perguntar(pergunta)
    print(f"IA: {resposta}\n")