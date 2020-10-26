import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json2 = json.dumps(person, indent=4, sort_keys=True)

# Writing in file
with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)

# Reading json
with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)