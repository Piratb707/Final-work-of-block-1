# Язык Python

# Функция выборакоротких слов.
def short_strings(strings):
    short_strings = [] # Массив для хранения коротких слов
    for string in strings:
        if len(string) <= 3:  # Проверка длинны слова
            short_strings.append(string) # При проходе проверки слово добавляется в конечный словарь
    return short_strings

initial_array = ['собака', '2', 'дом', '666', 'Евгений']
result = short_strings(initial_array)
print(result)
