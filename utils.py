import json
import random

CITIES_DATA_FILE = 'cities.json'


def get_cities_data():
    """
    Загружает базу данных городов из файла cities.json
    :return: база городов (список словарей)
    """
    with open(CITIES_DATA_FILE, encoding='utf-8') as file:
        cities = json.load(file)

    return cities


def is_city(city: str, cities_data: list):
    """
    Проверяет является ли введенное пользователем слово городом
    :param city: город игрока
    :param cities_data: база городов
    :return: True or False
    """
    return city in cities_data[city[0]]


def is_used_city(city: str, used_cities: list):
    """
    Проверяет был ли город пользователя в игре
    :param city: город пользователя
    :param used_cities: база городов
    :return: True or False
    """
    return city in used_cities


def get_last_letter(word: str):
    """
    Позволяет получить последнюю букву города, за исключением букв, на которых нет городов
    :param word: город
    :return: последняя буква
    """
    bad_letters = ['ё', 'ъ', 'ы', 'ь', 'й', 'ц']

    if word[-1] not in bad_letters:
        return word[-1]

    else:
        for i in range(2, len(word)):
            if word[-i] not in bad_letters:
                return word[-i]


def get_city(letter: str, cities_data: list, used_cities):
    """
    Позволяет получить город из базы данных, которого не было в игре, на нужную букву
    :param letter: первая буква нужного города
    :param cities_data: база городов
    :param used_cities: список использованных городов
    :return: город
    """
    letter = letter.upper()

    while True:
        city = random.choice(cities_data[letter])
        if city not in used_cities:
            return city


def get_prompt(letter: str, cities_data: list, used_cities: list):
    """
    Позволяет получить подсказку, если пользователь не знает города
    :param letter: буква, на которую нужен город
    :param cities_data: база городов
    :param used_cities: список использованных городов
    :return: город
    """
    letter = letter.upper()

    while True:
        city = random.choice(cities_data[letter])
        if city not in used_cities:
            return city


def print_rules():
    """
    Выводит правила игры
    """
    print('Добро пожаловать в игру города')
    print('Цель игры - поочереди  называть российские города на последнюю букву последнего города')
    print('Для того, чтобы закончить игру, введите "стоп"')
    print('Если нужна подсказка - напишите слово "подсказка"\n')


def get_first_city(cities: list):
    """
    Позволяет получить первый город для начала игры
    :param cities: база городов
    :return: рандомный город
    """
    city_letter = random.choice(list(cities.keys()))
    return random.choice(cities[city_letter])
