from flask import Flask, Response
import requests

app = Flask(__name__)

CONTACTS_HTML_URL = "https://raw.githubusercontent.com/AlexeyYanchenkov/DZ_Verstka/main/Html/contact.html"

def get_contacts_page():
    """Загружает HTML-страницу 'Контакты' из удалённого репозитория"""
    try:
        print(f"Загружаем: {CONTACTS_HTML_URL}")  # Логирование запроса
        response = requests.get(CONTACTS_HTML_URL)
        response.raise_for_status()
        print("HTML загружен успешно!")  # Подтверждение загрузки
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка загрузки: {e}")  # Вывод ошибки
        return f"<h1>Ошибка загрузки страницы: {e}</h1>"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    """Возвращает страницу 'Контакты' на любой GET-запрос"""
    html_content = get_contacts_page()
    return Response(html_content, mimetype="text/html")

if __name__ == "__main__":
    print("Запуск сервера...")
    app.run(host="0.0.0.0", port=8080, debug=True)