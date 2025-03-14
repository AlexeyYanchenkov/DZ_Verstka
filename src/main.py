from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import urllib.request

# Настройки сервера
HOST = "localhost"
PORT = 8080

# Путь к HTML-файлу
HTML_FILE = "contact.html"

# URL удаленного репозитория
REMOTE_HTML_URL = "https://raw.githubusercontent.com/AlexeyYanchenkov/DZ_Verstka/main/contact.html"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обработка всех GET-запросов, возвращает contact.html"""

        # Если HTML-файла нет – скачиваем
        if not os.path.exists(HTML_FILE):
            print(f"Файл {HTML_FILE} не найден. Скачиваем из репозитория.")
            try:
                urllib.request.urlretrieve(REMOTE_HTML_URL, HTML_FILE)
                print(f"Файл {HTML_FILE} успешно загружен!")
            except Exception as e:
                print(f"Ошибка загрузки HTML-файла: {e}")
                self.send_error(500, "Ошибка сервера")
                return

        try:
            # Читаем HTML-файл
            with open(HTML_FILE, "r", encoding="utf-8") as f:
                content = f.read()

            # Отправляем ответ
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))

        except FileNotFoundError:
            self.send_error(404, "Файл не найден")

        except Exception as e:
            print(f"Ошибка сервера: {e}")
            self.send_error(500, "Ошибка сервера")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyServer)
    print(f"Сервер запущен: http://{HOST}:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Сервер остановлен.")