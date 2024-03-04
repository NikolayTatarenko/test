from openpyxl import Workbook
import csv

wb = Workbook()
ws = wb.active

with open('data.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        del row[2]
        ws.append(row)

# Сохраняем Excel-файл
wb.save('data.xlsx')

print("Дані збережені у файлі 'data.xlsx'")
