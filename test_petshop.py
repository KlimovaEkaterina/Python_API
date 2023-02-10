import requests
import pytest
import allure

base_url = "https://petstore.swagger.io/v2"
url_pet_post = "/pet"
url_pet_get = "/pet/1055"

@allure.epic("Создание + проверка нового питомца (статус код 200) методом POST")
#### Создание + проверка нового питомца (статус код 200) методом POST
def test_new_pet():
    
    data = {
        "id": 1055,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Sharik",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "status": "available"
        }
    result_post = requests.post(base_url + url_pet_post, json = data)
    print (result_post.text)
    assert 200 == result_post.status_code
    if result_post.status_code == 200: # Сравнение ожидаемого статус кода с фактическим
        print("Статус код 200! Новый питомец создан. Тест прошел!")
    else:
        print("Статус код не 200! Тест провален!")
    check = result_post.json()
    id_pet = check.get("id")
    print("id", id_pet)

#### Проверка существования нового питомца (по созданному id и имени) методом GET
    print(base_url + url_pet_get)
    result_get = requests.get(base_url + url_pet_get)
    print (result_get.text)
    if result_get.status_code == 200: # Сравнение ожидаемого статус кода с фактическим
        print("Статус код 200! Новый питомец существует. Тест прошел!")
    else:
        print("Статус код не 200! Тест провален!")
    check = result_get.json()
    id_pet = check.get("id")
    name_pet = check.get("name")
    assert name_pet == "Sharik"
    if id_pet == 1055: # Сравнение созданного питомца по id
        print("ID соответствует! Тест прошел!")
    else:
        print("ID не соответствует! Тест провален!")
    if name_pet == "Sharik": # Сравнение созданного питомца по имени
        print("Имя соответствует! Тест прошел!")
    else:
        print("Имя не соответствует! Тест провален!")

@allure.epic("Изменение статуса питомца на sold (статус код 200) методом PUT")
#### Изменение статуса питомца на sold (статус код 200) методом PUT
def test_update_pet():
    data_put = {
        "id": 1055,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Sharik",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "status": "sold"
        }
    result_put = requests.put(base_url + url_pet_post, json = data_put)
    print (result_put.text)
    assert 200 == result_put.status_code
    if result_put.status_code == 200: # Сравнение ожидаемого статус кода с фактическим
        print("Статус код 200! Изменения внесены. Тест прошел!")
    else:
        print("Статус код не 200! Тест провален!")

#### Проверка внесенных изменений (статус питомца стал sold) методом GET
    result_get = requests.get(base_url + url_pet_get)
    print (result_get.text)
    if result_get.status_code == 200: # Сравнение ожидаемого статус кода с фактическим
        print("Статус код 200! Проверка изменений упешно. Тест прошел!")
    else:
        print("Статус код не 200! Тест провален!")
    check = result_get.json()
    status_pet = check.get("status")
    assert status_pet == "sold"
    if status_pet == "sold": # Сравнение измененного статуса
        print("Статус питомца соответствует! Тест прошел!")
    else:
        print("Статус питомца не соответствует! Тест провален!")

@allure.epic("Удаление питомца (проверка успешности по статус коду 200) методом DELETE")
#### Удаление питомца (проверка успешности по статус коду 200) методом DELETE
def test_delete_pet():
    result_delete = requests.delete(base_url + url_pet_get, headers = {"api_key":"special-key"})
    print (result_delete.text)
    if result_delete.status_code == 200: # Сравнение ожидаемого статус кода с фактическим
        print("Статус код 200! Удаление успешно. Тест прошел!")
    else:
        print("Статус код не 200! Тест провален!")

#### Проверка отсутствия удаленного питомца (по id и имени)  методом GET
    result_get = requests.get(base_url + url_pet_get)
    print (result_get.text)
    if result_get.status_code == 404: # Сравнение ожидаемого статус кода с фактическим
        print("Статус код 404! Удаленный питомец не существует. Тест прошел!")
    else:
        print("Статус код не 404! Тест провален!")

test_new_pet()
test_update_pet()
test_delete_pet()
