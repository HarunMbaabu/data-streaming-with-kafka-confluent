import time
from faker import Faker

fake = Faker()

def get_registered_users():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "message": fake.text(),
        "created_on": fake.year()
    }


while True:
    user = get_registered_users()
    print(user) 
    time.sleep(30) 