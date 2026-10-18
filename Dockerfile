FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Dummy web server port export taaki Render Web Service free chal sake
EXPOSE 8080
CMD python -c "import http.server, socketserver, threading; threading.Thread(target=lambda: socketserver.TCPServer(('', 8080), http.server.SimpleHTTPRequestHandler).serve_forever(), daemon=True).start()" && python main.py
