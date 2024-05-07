import requests
import random

def generate_pokemons():
    
    trainer_id = 0
    
    while (trainer_id < 3):
        count = 0
        trainer_id = trainer_id + 1
        pokemons_url = f"http://127.0.0.1:8000/trainers/{trainer_id}/pokemon"
        print("URL : ", pokemons_url)
        while (count < 6):
            count = count + 1
            id = random.randint(1,999)
            data = {"api_id": id, "custom_name" : f"name{id}"}
            print("data : ", data)
            requests.post(pokemons_url, json = data)


generate_pokemons()
