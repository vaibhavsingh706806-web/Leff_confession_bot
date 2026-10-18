import os
import http.server
import socketserver
import threading
import telebot

# 1. Render ke liye web server
PORT = int(os.environ.get("PORT", 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Leff Bot is running 24/7!")

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# 2. Seedha yahan apna BotFather wala token aur channel username daal de!
TOKEN = "8721256256:AAGNg7gIw9ZjOsW15UqBOgmTjtiHtIeZO0k"  # Jaise: "123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ"
CHANNEL_USERNAME = "@LeffConfessions"        # Apna channel username daal de

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
bot.infinity_polling(timeout=10, long_polling_timeout=5)
