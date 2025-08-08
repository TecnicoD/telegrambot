import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Función de ruleta
def ruleta():
    numeros = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]
    return random.choice(numeros)

# Función que responde mensajes
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "hola" in texto:
        await update.message.reply_text("¡Hola! escribe (iniciar) para sacar un numero del 1 al 10.")
    elif "iniciar" in texto:
        numero = ruleta()
        await update.message.reply_text(f"🎰 Girando la ruleta...\n¡Salió el número *{numero}*!", parse_mode='Markdown')
    elif "precio" in texto:
        await update.message.reply_text("Los precios están en www.ejemplo.com 💸")
    elif "adiós" in texto:
        await update.message.reply_text("¡Chau! Que tengas un buen día 😊")
    else:
        await update.message.reply_text("No entendí eso, ¿puedes repetirlo?")

# TOKEN del bot
TOKEN = ""

# Ejecutar el bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    print("🤖 Bot encendido. Presiona Ctrl+C para detener.")
    app.run_polling()

