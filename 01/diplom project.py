import datetime

class Person:
    def __init__(self, first_name, last_name=None, middle_name=None, birth_date=None, death_date=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def calculate_age(self):
        today = datetime.date.today()
        if self.death_date:
            age = self.death_date.year - self.birth_date.year - ((today.month, today.day) < (self.death_date.month, self.death_date.day))
        else:
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

class Database:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search_person(self, query):
        results = []
        for person in self.people:
            if query.lower() in person.first_name.lower() or query.lower() in person.last_name.lower() or query.lower() in person.middle_name.lower():
                results.append(person)
        return results

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for person in self.people:
                file.write(f"{person.first_name},{person.last_name},{person.middle_name},{person.birth_date},{person.death_date},{person.gender}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                first_name, last_name, middle_name, birth_date, death_date, gender = data
                if death_date:
                    death_date = datetime.datetime.strptime(death_date, "%d.%m.%Y").date()
                birth_date = datetime.datetime.strptime(birth_date, "%d.%m.%Y").date()
                self.people.append(Person(first_name, last_name, middle_name, birth_date, death_date, gender))

def main():
    database = Database()

    while True:
        print("\nМеню:")
        print("1. Додати нову людину")
        print("2. Пошук людини")
        print("3. Зберегти дані у файл")
        print("4. Завантажити дані з файлу")
        print("5. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище (не обов'язково): ")
            middle_name = input("Введіть по-батькові (не обов'язково): ")
            birth_date = input("Введіть дату народження у форматі dd.mm.yyyy: ")
            birth_date = datetime.datetime.strptime(birth_date, "%d.%m.%Y").date()
            death_date = input("Введіть дату смерті у форматі dd.mm.yyyy (не обов'язково): ")
            death_date = datetime.datetime.strptime(death_date, "%d.%m.%Y").date() if death_date else None
            gender = input("Введіть стать (m/f): ")
            person = Person(first_name, last_name, middle_name, birth_date, death_date, gender)
            database.add_person(person)
            print("Дані про людину додано!")

        elif choice == "2":
            query = input("Введіть рядок для пошуку: ")
            results = database.search_person(query)
            if results:
                for index, person in enumerate(results):
                    age = person.calculate_age()
                    death_info = f"Помер: {person.death_date}" if person.death_date else ""
                    print(f"{person.first_name} {person.last_name} {person.middle_name} {age} років, {person.gender}. Народився {person.birth_date}. {death_info}")
            else:
                print("Нічого не знайдено.")

        elif choice == "3":
            filename = input("Введіть ім'я файлу для збереження: ")
            database.save_to_file(filename)
            print("Дані збережено у файл.")

        elif choice == "4":
            filename = input("Введіть ім'я файлу для завантаження: ")
            database.load_from_file(filename)
            print("Дані завантажено з файлу.")

        elif choice == "5":
            print("Дякую за використання програми!")
            break

        else:
            print("Невірний вибір. Будь ласка, спробуйте ще раз.")

if __name__ == "__main__":
    main()
