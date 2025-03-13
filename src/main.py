# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
from src.config import file_contact_html  # Убедись, что путь к файлу правильный

# Настройки запуска сервера
hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """
    Обработчик HTTP-запросов
    """
    def do_GET(self):
        """ Обработка входящих GET-запросов """
        self.send_response(200)  # Отправка кода 200 (ОК)
        self.send_header("Content-type", "text/html; charset=utf-8")  # Указание типа контента
        self.end_headers()  # Завершение заголовков

        try:
            # Открываем HTML-файл и читаем его содержимое
            print(f"Открываю файл: {file_contact_html}")
            with open(file_contact_html, "r", encoding="utf-8") as f:
                content = f.read()
            # Отправляем HTML-контент в ответе
            self.wfile.write(content.encode("utf-8"))
        except FileNotFoundError:
            # Если файл не найден, отправляем сообщение об ошибке
            self.wfile.write(b"<h1>Zalupa</h1>")
            print("Ошибка: HTML-файл не найден!")
        except Exception as e:
            # Ловим любые другие ошибки и отправляем их клиенту
            error_message = f"<h1>Ошибка сервера: {e}</h1>"
            self.wfile.write(error_message.encode("utf-8"))

if __name__ == "__main__":
    # Запуск веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Остановка сервера
    webServer.server_close()
    print("Server stopped.")