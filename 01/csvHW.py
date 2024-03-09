import json
import csv
import random


with open("data.json", "r") as json_file:
    data = json.load(json_file)

def generate_phone_number():
    return ''.join([str(random.randint(0, 9)) for i in range(10)])


with open("data.csv", "w", newline="", encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["ID", "Ім'я", "Вік", "Телефон"])


    for id, details in data.items():
        name, age = details
        phone_number = generate_phone_number()
        writer.writerow([id, name, age, phone_number])

print("Дані записані: data.csv")