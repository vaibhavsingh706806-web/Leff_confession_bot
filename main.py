import os
import http.server
import socketserver
import threading
import telebot

# Debugging: Dekhte hain Render kya-kya environment variables bhej raha hai
print("DEBUG - Available Env Keys:", list(os.environ.keys()))

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

TOKEN = os.environ.get("8721256256:AAGNg7gIw9ZjOsW15UqBOgmTjtiHtIeZO0k")
CHANNEL_USERNAME = os.environ.get("@LeffConfessions")

if not TOKEN:
    print("ERROR: BOT_TOKEN is missing!")
    exit(1)

bot = telebot.TeleBot(TOKEN)
confession_counter = 1

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✨ Welcome to Leff. Send your confession:")

@bot.message_handler(func=lambda message: True)
def handle_confession(message):
    global confession_counter
    try:
        bot.send_message(CHANNEL_USERNAME, f"Confession #{confession_counter}: {message.text}")
        bot.reply_to(message, "✅ Sent successfully!")
        confession_counter += 1
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

print("Leff Bot Live Ho Gaya Hai!")
bot.infinity_polling(timeout=10, long_polling_timeout=5)
