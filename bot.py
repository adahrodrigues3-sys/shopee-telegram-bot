
import os
import requests

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def enviar_mensagem(texto):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Configure os segredos do Telegram no GitHub.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    resposta = requests.post(
        url,
        json={"chat_id": TELEGRAM_CHAT_ID, "text": texto},
        timeout=20
    )
    print("Resposta do Telegram:", resposta.text)
resposta.raise_for_status()

if __name__ == "__main__":
    enviar_mensagem(
        "🤖 Bot de ofertas preparado! A integração com a Shopee será configurada depois da aprovação da API."
    )
