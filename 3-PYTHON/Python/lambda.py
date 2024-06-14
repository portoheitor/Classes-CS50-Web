people = [
    {"name": "Heitor", "work": "Data Analyst"},
    {"name": "Louro Jose", "work": "Artist"},
    {"name": "Brad Pitu", "work": "Cachaceiro"},    
]


people.sort(key= lambda person: person["name"])

print(people)