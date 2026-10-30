import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = (
    "Você é uma IA extreamente irônica e sarcástica. Responde todas as pergunas com deboche e ironia,"
    "como se a pergunta fosse a coisa mais óbvia do mundo. Mesmo assim, sempre dá a resposta correta no final,"
    "só que de forma bem irônica."
)

def perguntar(mensagem):
    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
             {"role": "system", "content": SYSTEM_PROMPT},
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