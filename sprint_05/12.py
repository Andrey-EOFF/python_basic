# Task 12
# Напишите функцию f12 которая принимает строку и возвращает:
# еслих входящая строка 'http' или 'https' то возвращает строку 'url'
# если входящая строка '@' то возвращает 'email'
# если входящая строка 'ftp' то возвращает 'ftp'
# во всех остальных случаях - возвращает пустую строку

def f12(input_string):
    if input_string == 'http' or input_string == 'https':
        return 'url'
    elif input_string == '@':
        return 'email'
    elif input_string == 'ftp':
        return 'ftp'
    else:
        return ''

print(f12('http'))