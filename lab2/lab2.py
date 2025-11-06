from csv import reader
import random
import xml.etree.ElementTree as ET
import time


BOOKS_FILE = 'books-en.csv'
YEAR_LIMIT_1 = 1991
YEAR_LIMIT_2 = 1995

def open_csv():
        return open(BOOKS_FILE, 'r', encoding='windows-1251')

# 1) Подсчет количества длинных записей

def count_long_titles():
    count = 0
    with open_csv() as f:
        table = reader(f, delimiter=';')
        header = next(table)
        name_index = header.index('Book-Title')
        for row in table:
            if len(row[name_index]) > 30:
                count += 1
    print(f'количество записей, у которых название больше 30 символов: {count}\n')

# 2) Поиск по автору с годом выпуска с 1991 по 1995

def search():
    search = input('Введите фамилию и имя автора:').strip()
    with open_csv() as f:
        table = reader(f, delimiter=';')
        header = next(table)
        author_index = header.index('Book-Author')
        title_index = header.index('Book-Title')
        year_index = header.index('Year-Of-Publication')

        for row in table:
            if search.lower() in row[author_index].lower():
                year = int(row[year_index])
                if YEAR_LIMIT_1 <= year <= YEAR_LIMIT_2 :
                    print(f'{row[author_index]} — {row[title_index]} ({year} год)')

# 3) Генерация ссылки

def generate_links():
    with open_csv() as f:
        table = list(reader(f, delimiter=';'))
        header = table[0]
        table = table[1:]
        author_i = header.index('Book-Author')
        title_i = header.index('Book-Title')
        year_i = header.index('Year-Of-Publication')

        chosen = random.sample(table, 20)
        with open('bibliography.txt', 'w', encoding='windows-1251') as out:
            for i, row in enumerate(chosen, start=1):
                author = row[author_i]
                title = row[title_i]
                year = row[year_i]
                line = f'{i}. {author}. {title} - {year}'
                out.write(line + '\n')
    print('файл создан\n')

# 4) Парсинг файла

def parsing():
    tree = ET.parse('currency.xml')
    root = tree.getroot()
    for val in root.findall('.//Valute'):
        if int(val.find('Nominal').text) in (10, 100):
            print(val.find('CharCode').text)

# 5) Вывод ответов

if __name__ == '__main__':
    count_long_titles()
    time.sleep(1)
    search()
    time.sleep(1)
    generate_links()
    time.sleep(1)
    parsing()