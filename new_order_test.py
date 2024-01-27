# Ксения Никифорова, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


# Функция создания нового заказа
def create_new_order(body):
    return requests.post(configuration.MAIN_URL + configuration.CREATE_NEW_ORDER,
                         json=body)


order_track = create_new_order(data.new_order_body).json()["track"]


# Функция получения заказа по треку
def get_order(order_track):
    return requests.get(configuration.MAIN_URL + configuration.GET_ORDER + str(order_track))


def test_get_order():
    response = create_new_order(data.new_order_body)
    track = response.json()["track"]
    data_order = get_order(order_track)
    assert data_order.status_code == 200

