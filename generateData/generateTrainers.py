import requests

def generate_trainers():
    trainers_url = "http://127.0.0.1:8000/trainers/"

    data1 = {"name": "Dimitri", "birthdate": "2024-01-11"}
    data2 = {"name": "Jeremie", "birthdate": "2024-02-11"}
    data3 = {"name": "Thibault", "birthdate": "2024-03-11"}

    requests.post(trainers_url, json = data1)
    print("dresseur 1 : ", data1)
    requests.post(trainers_url, json = data2)
    print("dresseur 2 : ", data2)
    requests.post(trainers_url, json = data3)
    print("dresseur 3 : ", data3)


generate_trainers()