from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8591560606:AAFVP5a-s0qioTRBg8B3UTN8waKMu8qwZFM"

movies = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Kino nomini yoz 🎬")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for name in movies:
        if name in text:
            await update.message.reply_text("Topildi 🎬 yuboryapman...")
            await update.message.reply_video(movies[name])
            return

    await update.message.reply_text("Topilmadi 😕")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, search))

    print("Bot ishga tushdi 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()



