# Consumindo a API da Groq com Python
Desafio do curso de IA Generativa do SENAI: 

Agora vamos criar um sistema de chatbot usando a infraestrutura da AWS e os sistemas de IA generativa da Groq com Llama.

Primeiro vamos criar uma VM no console da AWS buscando a criação de um EC2. Clicando no menu principal depois em computação e por fim EC2.

Coleção de exemplos práticos em Python consumindo a API da **Groq** com o modelo `llama-3.3-70b-versatile`, demonstrando desde chamadas simples até engenharia de prompt com persona (`system` prompt) e manutenção de histórico de conversa.

## Scripts Incluídos

1. **`chat.py` — Chat Básico com a Groq**
   Exemplo direto de interação via terminal enviando a pergunta do usuário (`role: "user"`) para o modelo `llama-3.3-70b-versatile` e exibindo a resposta.

2. **`exercicioIronica.py` — Personalidade com System Prompt**
   Demonstra o uso do `SYSTEM_PROMPT` (`role: "system"`) para definir o comportamento e tom de voz da IA (uma assistente sarcástica e irônica que ainda assim entrega a resposta correta ao final).

3. **`atendenteSAC.py` — Atendente Virtual com Memória de Conversa (SAC Energia Mais)**
   Implementa um agente de atendimento estruturado para a empresa fictícia **Energia Mais**, mantendo o histórico completo da conversa (`historico`) entre turnos para conduzir o cliente passo a passo na abertura de um chamado.

## Pré-requisitos

- Python 3.8+
- Chave de API da [Groq](https://console.groq.com/)

## Como executar

1. Instale a biblioteca da Groq:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute qualquer um dos scripts desejados:
   ```bash
   python chat.py
   # ou
   python exercicioIronica.py
   # ou
   python atendenteSAC.py
   ```
   Digite `sair` a qualquer momento no terminal para encerrar a conversa.
