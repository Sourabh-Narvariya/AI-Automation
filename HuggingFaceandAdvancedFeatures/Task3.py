import nest_asyncio
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from google import genai

nest_asyncio.apply()

GEMINI_API_KEY = "GEMINI_API_KEY"
TOKEN = "TELEGRAM_BOT_TOKEN"
BOT_USERNAME = "@kunj_bot"

client = genai.Client(api_key=GEMINI_API_KEY)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm kunj bot powered by Gemini. Ask me anything.")

async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a message and I'll answer using Gemini AI.")

def get_response(text: str) -> str:
    try:
        if not text.strip():
            return "Please send some text."
        response = client.models.generate_content(model="gemini-2.5-flash", contents=text)
        return getattr(response, "text", "Could not generate response.")
    except Exception as e:
        return f"Error: {e}"

async def handle_msg(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_type = update.message.chat.type
    
    if chat_type == "group" and BOT_USERNAME not in text:
        return
    
    text = text.replace(BOT_USERNAME, "").strip() if BOT_USERNAME in text else text
    response = get_response(text)
    print(f"User ({update.message.chat.id}): {text}\nBot: {response[:100]}")
    await update.message.reply_text(response)

async def error(update, ctx):
    print(f"Error: {ctx.error}")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))
    app.add_error_handler(error)
    print("Bot polling...")
    await app.run_polling(poll_interval=3)

asyncio.run(main())
