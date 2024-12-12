import json

with open('dump.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

numb = input("Введите номер квалификации: ")

found = False

for item in data:
    if item['model'] == 'data.skill'  and item['fields']['code'] == numb:

        specialty = item['fields']['specialty']

        kval_code = item['fields']['code']
        kval_title = item['fields']['title']

        found = True


if not found:
    print("============== Не найдено ===============")


else:

    for item in data:

        if item['model'] == 'data.specialty':

            specialty_pk = item['pk']

            if specialty == specialty_pk:

                spec_code = item['fields']['code']
                spec_title = item['fields']['title']
                spec_educat = item['fields']['c_type']

    print("============== Найдено ===============")
    print(f"{spec_code} >> Специальность {spec_title}, {spec_educat}")
    print(f"{kval_code} >> Квалификация {kval_title}")
