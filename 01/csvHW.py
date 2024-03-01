import json
import csv
import random

# Зчитуємо дані з JSON-файлу
with open("data.json", "r") as json_file:
    data = json.load(json_file)


# Генеруємо випадковий номер телефону
def generate_phone_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])


# Відкриваємо CSV-файл для запису
with open("дані.csv", "w", newline="", encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["ID", "Ім'я", "Вік", "Телефон"])

    # Записуємо дані для кожного запису з JSON
    for id, details in data.items():
        name, age = details
        phone_number = generate_phone_number()
        writer.writerow([id, name, age, phone_number])

print("Дані успішно записані у файл: дані.csv")