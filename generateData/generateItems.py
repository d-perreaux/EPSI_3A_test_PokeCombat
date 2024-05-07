import requests
import random

base_url = "https://pokeapi.co/api/v2"

def get_item_name(item_id):
    response = requests.get(f"{base_url}/item/{item_id}", timeout=10)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        return name
    else:
        return "item non trouvé"  
    
def get_item_description(item_id):
    response = requests.get(f"{base_url}/item/{item_id}", timeout=10)
    if response.status_code == 200:
        data = response.json()
        description = data["effect_entries"][0]["short_effect"]
        return description
    else:
        return "item non trouvé"

def generate_items():
    
    trainer_id = 0
  
    while (trainer_id < 3):
        count = 0
        trainer_id = trainer_id + 1
        items_url = f"http://127.0.0.1:8000/trainers/{trainer_id}/item"
        print("URL : ", items_url)
        nb_item_trainer = random.randint(1,5)
        print(f"Nombre d'item de trainer{trainer_id} : {nb_item_trainer}")
        
        while (count < nb_item_trainer):
            count = count+1
            id = random.randint(1, 999)
            print("id : ", id)
            name = get_item_name(id) #item 866 error 404
            
            while (name == "item non trouvé"):
                id = random.randint(1, 999)
                name = get_item_name(id) 
                
            description = get_item_description(id)
            data = {"name": name, "description" : description}
            requests.post(items_url, json = data)
            print(data)
    

generate_items()
    