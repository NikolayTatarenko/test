first_var = input("Введіть перший рядок: ")
second_var = input("Введіть другий рядок: ")
third_var = input("Введіть третій рядок: ")
fourth_var = input("Введіть четвертий рядок: ")

with open('example.txt', 'w') as file:
    file.write(f"{first_var}\n{second_var}\n")

with open ('example.txt', 'a') as file:
    file.write(f"{third_var}\n{fourth_var}")
