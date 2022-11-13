from utils import *

print_rules()
cities = get_cities_data()
used_cities = []

first_city = get_first_city(cities)
used_cities.append(first_city)
print(f'Первый город - {first_city}')
last_letter = get_last_letter(first_city)

word_count = 0

while True:
    print(f'Введите город на букву {last_letter.upper()}')
    user_city = input().capitalize()

    if user_city == 'Стоп':
        break

    elif user_city == 'Подсказка':
        print(get_prompt(last_letter, cities, used_cities))

    elif is_city(user_city, cities):

        if user_city[0] != last_letter.upper():
            print(f'Этот город не начинается на букву {last_letter.upper()}')

        elif is_used_city(user_city, used_cities):
            print('Этот город уже был')

        else:
            used_cities.append(user_city)
            word_count += 1

            # Ход компьютера
            new_last_letter = get_last_letter(user_city)
            prog_city = get_city(new_last_letter, cities, used_cities)
            used_cities.append(prog_city)
            print(f'\n{prog_city}')

            last_letter = get_last_letter(prog_city)

    else:
        print('Это не город')

print(f'\nИгра окончена! Вы написали {word_count} городов!')
