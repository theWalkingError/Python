# Dictionary
dic_1 = {'name': 'Andrew'}

print(dic_1['name'])

dic_2 = dict()

# dic_3 = dict.fromkeys()

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(key, " - ", users[key])




def func(*args): # неопределенное количество параметров в виде кортежа
    return args


def function(**args): # неопределенное количество параметров в виде словаря
    return args