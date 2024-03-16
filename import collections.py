import collections

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_pet = {}
    new_pet_id = last + 1
    new_pet_name = input("Введите имя питомца: ")
    new_pet_type = input("Введите вид питомца: ")
    new_pet_age = int(input("Введите возраст питомца: "))
    new_pet_owner = input("Введите имя владельца: ")
    new_pet = {new_pet_id: {"Имя питомца": new_pet_name, "Вид питомца": new_pet_type, "Возраст питомца": new_pet_age, "Имя владельца": new_pet_owner}}
    pets.update(new_pet)
    print("Питомец успешно добавлен!")

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return 'года'
    else:
        return 'лет'

def pets_list():
    print("Список питомцев:")
    for pet in pets.values():
        for pet_info in pet.values():
            print(f"Имя питомца: {pet_info['Имя питомца']}")
            print(f"Вид питомца: {pet_info['Вид питомца']}")
            print(f"Возраст питомца: {pet_info['Возраст питомца']} {get_suffix(pet_info['Возраст питомца'])}")
            print(f"Имя владельца: {pet_info['Имя владельца']}")
            print()

def read():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    if pet:
        print(f"Это {pet['Имя питомца']} по кличке '{pet['Имя питомца'].split()[-1]}'.")
        print(f"Вид питомца: {pet['Вид питомца']}.")
        print(f"Возраст питомца: {pet['Возраст питомца']} {get_suffix(pet['Возраст питомца'])}.")
        print(f"Имя владельца: {pet['Имя владельца']}.")
    else:
        print("Питомец с таким ID не найден.")

def update():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    if pet:
        pet_name = input("Введите новое имя питомца: ")
        pet_type = input("Введите новый вид питомца: ")
        pet_age = int(input("Введите новый возраст питомца: "))
        pet_owner = input("Введите новое имя владельца: ")
        pets[ID] = {pet_name: {"Вид питомца": pet_type, "Возраст питомца": pet_age, "Имя владельца": pet_owner}}
        print("Информация о питомце успешно обновлена!")
    else:
        print("Питомец с таким ID не найден.")

def delete():
    ID = int(input("Введите ID питомца: "))
    if ID in pets.keys():
        del pets[ID]
        print("Запись о питомце успешно удалена!")
    else:
        print("Питомец с таким ID не найден.")

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}

command = ""
while command != 'stop':
    command = input("Введите команду (create, read, update, delete, list, stop): ")
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Программа остановлена.")
    else:
        print("Неизвестная команда.")