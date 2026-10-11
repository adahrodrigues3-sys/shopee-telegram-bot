```python
import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def enviar_mensagem():
    print("Iniciando teste do bot...")

    if not TOKEN:
        print("ERRO: o segredo TELEGRAM_TOKEN não foi encontrado.")
        return

    if not CHAT_ID:
        print("ERRO: o segredo TELEGRAM_CHAT_ID não foi encontrado.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    dados = {
        "chat_id": CHAT_ID,
        "text": (
            "🤖 Teste do bot realizado!\n\n"
            "A conexão com o Telegram está funcionando."
        )
    }

    try:
        resposta = requests.post(
            url,
            json=dados,
            timeout=20
        )

        print("Código HTTP:", resposta.status_code)

        try:
            resultado = resposta.json()
        except ValueError:
            print("O Telegram retornou uma resposta não JSON.")
            print("Resposta:", resposta.text[:500])
            return

        print("Resultado do Telegram:", resultado)

        if resultado.get("ok"):
            print("SUCESSO: mensagem enviada ao Telegram!")
        else:
            print("ERRO: o Telegram recusou a mensagem.")
            print("Motivo:", resultado.get("description", "Motivo não informado"))

    except requests.RequestException as erro:
        print("ERRO DE CONEXÃO:", str(erro))


if __name__ == "__main__":
    enviar_mensagem()
```
