import requests
import json
import jsonpath

url = "http://localhost:4000/subscriptions"


def test_add():
    # Добавление новой подписки (post запрос)
    file = open('user.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, json_input)
    assert response.status_code == 200
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    assert len(id[0]) == 24


def test_add_wrong_email():
    # Добавление новой подписки с неправильным email
    file = open('user2.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, json_input)
    assert response.status_code == 200
    response_json = json.loads(response.text)
    error = jsonpath.jsonpath(response_json, 'error')
    assert error[0] == "ValidationError (SubscriptionModel:None) (Invalid email address: tesfdsfsu: ['email'])"


def test_add_wrong_data():
    # Отправка неправильных данных в post запрос
    response = requests.post(url, "It's a wrong data.")
    assert response.status_code == 400


def test_get():
    # Тестирование get
    response = requests.get(url)
    assert response.status_code == 200
    response_json = json.loads(response.text)
    if len(response_json) < 1:
        return
    assert None != response_json[0].get('email')
    assert None != response_json[0].get('name')
    assert None != response_json[0].get('comment')
    assert None != response_json[0].get('created_at')
    assert None != response_json[0].get('expired_at')


def test_delete():
    # Тестирование delete запроса
    response = requests.delete(url)
    assert response.status_code == 200
    response_json = json.loads(response.text)
    assert None != response_json.get('removed')


"""test_add()
test_add_wrong_email()
test_add_wrong_data()
test_get()
test_delete()"""
