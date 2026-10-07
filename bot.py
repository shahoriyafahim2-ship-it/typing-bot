import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

BOT_TOKEN = "7983467690:AAG9DRuUzoSjhGO9GpN4t7wAc1NvMxffbHI"

WORDS = ["bangladesh", "telegram", "typing", "speed", "game", "python", "github", "render", "keyboard", "challenge"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am Typing Bot!\n"
        "Type /typing to start the game!"
    )

async def typing_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = random.choice(WORDS)
    context.user_data['current_word'] = word
    await update.message.reply_text(f"Type this: *{word}*\n\nSend this word to check your speed!", parse_mode="Markdown")

async def check_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'current_word' in context.user_data:
        if update.message.text.strip() == context.user_data['current_word']:
            await update.message.reply_text("Correct! Great speed! Use /typing to play again.")
            del context.user_data['current_word']

def main():
    token = os.environ.get("BOT_TOKEN", BOT_TOKEN)
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("typing", typing_game))
    app.add_handler(CommandHandler("type", typing_game))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_word))
    app.run_polling()

if __name__ == "__main__":
    main()
