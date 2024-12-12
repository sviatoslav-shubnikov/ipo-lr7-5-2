import json

with open('dump.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


numb = input("Введите номер квалификации: ")

found = False

print("\n=============== Результат поиска ===============")

specialty = 0

for item in data:
    if item['model'] == 'data.skill'  and item['fields']['code']==numb:

        print(f"{item['fields']['code']} >> Квалификация {item['fields']['title']}")
        specialty = item['fields']['specialty']
        found = True
        
for item in data:
    if item['model'] == 'data.specialty':

        specialty_pk = item['pk']

        if specialty == specialty_pk:

            print(f"{item['fields']['code']} >> Специальность {item['fields']['title']}")

if not found:
    print("============== Не найдено ===============")