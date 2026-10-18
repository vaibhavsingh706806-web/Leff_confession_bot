import os
import telebot

TOKEN = os.environ.get("8721256256:AAGNg7gIw9ZjOsW15UqBOgmTjtiHtIeZO0k")
CHANNEL_USERNAME = os.environ.get("@leffconfession")

bot = telebot.TeleBot(TOKEN)
confession_counter = 1

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "✨ Welcome to Leff.\n\n"
        "Yahan apne dil ki baat, secrets ya confessions bina kisi darr ke bhejo.\n\n"
        "🔒 Privacy Guarantee: Aapka naam aur identity 100% hidden rahegi!\n\n"
        "👇 Apna message yahan type karke bhejo:"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_confession(message):
    global confession_counter
    user_text = message.text
    
    post_text = (
        f"✦ LEFF CONFESSION #{confession_counter}\n"
        f"────────────────────────\n\n"
        f"💬 \"{user_text}\"\n\n"
        f"────────────────────────\n"
        f"🕊️ Anonymous Submission"
    )

    try:
        bot.send_message(CHANNEL_USERNAME, post_text)
        bot.reply_to(
            message, 
            f"✅ Aapka confession successfully channel par post ho gaya hai!\n\n"
            f"👉 Check here: {CHANNEL_USERNAME}"
        )
        confession_counter += 1
    except Exception as e:
        bot.reply_to(message, f"❌ Error: Message post nahi ho paya.\nDetails: {e}")

print("Leff Bot Live Ho Gaya Hai!")
bot.infinity_polling()
