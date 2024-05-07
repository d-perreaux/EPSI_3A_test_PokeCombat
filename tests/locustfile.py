'''Test de charge avec un Get et un Post'''

from locust import HttpUser, task, between

class MyUser(HttpUser):
    '''
    Définit le wait_time entre chaque user
    '''
    wait_time = between(5, 15)  # Temps d'attente entre les requêtes, en secondes

    @task
    def create_trainer(self):
        '''
        Test de post trainers
        '''
        data = {"name": "Sacha Touille", "birthdate": "1991-12-13"}
        self.client.post("/trainers/", json=data)

    @task
    def gettrainer(self):
        '''
        Test de get Trainers
        '''
        self.client.get("/trainers/1")
