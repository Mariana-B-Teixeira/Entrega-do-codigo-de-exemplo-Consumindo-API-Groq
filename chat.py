import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def perguntar(mensagem):
    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": mensagem}
        ]
    )
    return resposta.choices[0].message.content

print("=== Chat com Groq ===")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() == "sair":
        print("Encerrando...")
        break
    resposta = perguntar(pergunta)
    print(f"IA: {resposta}\n")

    