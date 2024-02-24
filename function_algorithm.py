
def check_func(user_number):
    # Перевіряємо, чи введене значення є числом
    if user_number.replace('.', '', 1).replace(',', '', 1).lstrip('-').isdigit():
        number = float(user_number.replace(',', '.'))
        if number == 0:
            return "Ви ввели нуль"
        elif number < 0:
            return f"Ви ввели від'ємне {'дробове' if '.' in user_number else 'ціле'} число: {number}"
        else:
            return f"Ви ввели позитивне {'дробове' if '.' in user_number else 'ціле'} число: {int(number)}"
    else:
        return "Ви ввели неправильне число: " + user_number

while True:
    user_input = input("Введіть число або 'вихід', 'exit', 'quit', 'e' або 'q': ").lower()
    if user_input in ['вихід', 'exit', 'quit', 'e', 'q']:
        break
    else:
        result = check_func(user_input)
        print(result)