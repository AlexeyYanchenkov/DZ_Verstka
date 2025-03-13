from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from src.config import file_contact_html  # Убедись, что путь правильный

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обработка GET-запросов"""
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        try:
            # Проверяем, существует ли HTML-файл
            if not os.path.exists(file_contact_html):
                raise FileNotFoundError

            # Читаем содержимое HTML-файла
            with open(file_contact_html, "r", encoding="utf-8") as f:
                content = f.read()

            # Отправляем успешный ответ
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))

        except FileNotFoundError:
            # Если файл не найден – отправляем 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"<h1>ZALUPA</h1>")

        except Exception as e:
            # Ловим другие ошибки
            print(f"Ошибка сервера: {e}")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"<h1>Oshibka servera</h1>")


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")