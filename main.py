import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from config import HTML_DIR

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс, описывающий работу сервера. Дочерний класс класса BaseHTTPRequestHandler."""

    def do_GET(self):
        """Метод, обрабатывающий GET запросы."""
        with open(os.path.join(HTML_DIR, "contacts.html"), mode="r", encoding="utf-8") as file:
            data = file.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        """Метод, обрабатывающий POST запросы."""
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        print(str(body))
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped")
