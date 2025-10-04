import json
import urllib.request
import requests
from datetime import datetime, date
from json import JSONEncoder
from typing import Any

person_data = {
    "name": "Selim",
    "age": 29,
    "city": "Zurich",
}

json.dumps(person_data, indent=4)
print(json.dumps(person_data, indent=4))
with open("person.json", "w") as file:
    json.dump(person_data, file, indent=4)


# Desearialization
json_data = '{"name": "Selim", "age": 29}'
person = json.loads(json_data)
type(person)
print(person)

i = 10
for i in range(10):
    print(i)
#############################

url = "https://www.andybek.com/api/data/persons"
with urllib.request.urlopen(url) as response:
    response_data = response.read().decode("utf-8")

type(response_data)
json_data = json.loads(response_data)
type(json_data)

# This is better way of handling requests.It automatically converts into python objet.

#############################

response = requests.get(url)
response.json()
type(response.json())
raw_data = {"name": "Selim"}
# This is serializing the data to json str automatically. Otherwise, we had to dump to json.
# requests.post(a_url, json=raw_data)

#############################


raw_date_with_date = {"name": "Selim", "birthday": datetime.date(1996, 1, 4)}


class CustomEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, date):
            return o.isoformat()
        # This behaviour is already necessary to pass the "o" to JSONEncoder class.
        return super().default(o)


json.dumps(raw_date_with_date, cls=CustomEncoder)


############################# User Defined Serilization
class Person:
    def __init__(self, name, born) -> None:
        self.name = name
        self.born = born

    @property
    def age(self):
        """The  age property."""
        return datetime.now().year - self.born


john = Person("John", 1996)
json.dumps(john.__dict__)
john.name
john.born
john.age


def custom_serialize(obj):
    if isinstance(obj, Person):
        return {
            "name": obj.name,
            "age": obj.age,
        }
    raise TypeError("object is not serializeable")


json.dumps(john, default=custom_serialize)

############################# Challange

challangeURL = "https://www.andybek.com/api/data/books"
originalFile = "person-original.json"
cleanedFile = "person-cleaned.json"
response = requests.get(challangeURL)
books_data = response.json()

with open(originalFile, "w") as f:
    json.dump(books_data, f, indent=4)

for book in books_data:
    del book["rank"]
    del book["release_date"]

with open(cleanedFile, "w") as f:
    json.dump(books_data, f, indent=2)
