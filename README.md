This projects shows how you can produce and consume data into a Kafka cluster, for this case we are using  python ```faker``` library which will help us generate new data after every 30 seconds. 

Caveat: If you are using cloud storage or pc to get this data before streaming, this is an endless loop. 


**Python Faker Code that generates  "name", "address", "message", and created_on" data:**

```python
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
    
```