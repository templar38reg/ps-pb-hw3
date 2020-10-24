account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'} #словарь аккаунтов

account = [account1, account2, account3, account4] #список аккаунтов

user1 = {'name': 'Иван', 'age': 20, 'account': [account1]}
user2 = {'name': 'Петр', 'age': 25, 'account': [account2]}
user3 = {'name': 'Ольга', 'age': 18, 'account': [account3]}
user4 = {'name': 'Анна', 'age': 27, 'account': [account4]} #словарь пользователей

user_list = [user1, user2, user3, user4] #список пользователей
user_age = sum(sub['age'] for sub in user_list) # переменная подсчёта суммы возраста всех пользователей 

key = input('Введите ключ (name или account): ') # значение вводимого ключа необходимо имя или аккаунт
try:
    print(f'Значение ключа {key.lower()} для юзера 1 = {user1[key.lower()]}')
    print(f'Значение ключа {key.lower()} для юзера 2 = {user2[key.lower()]}')
    print(f'Значение ключа {key.lower()} для юзера 3 = {user3[key.lower()]}')
    print(f'Значение ключа {key.lower()} для юзера 4 = {user4[key.lower()]}') # используем введённый ключ, чтобы он совпал с ключом из наших словарей пользователей
except:
    print('Введенный ключ не найден')

user_input = input('Введите порядковый номер: ') # номер пользователя
try:  
    print(f'Данные по юзеру №: {user_list[int(user_input) - 1]["name"]}')
    print(f'имя: {user_list[int(user_input) - 1]["name"]}')
    print(f'возраст: {user_list[int(user_input) - 1]["age"]}')
    print(f'логин: {account[int(user_input) - 1]["login"]}')
    print(f'пароль: {account[int(user_input) - 1]["password"]}') # аналогично с ключом имя\аккаунт, только вызываем необходимые нам данные из различных словарей
    
except:
    print('Пользователь с указанным номером не найден')

ordinal = input('Введите номер пользователя, которого нужно переместить в конец: ')
pop_user = user_list.pop(int(ordinal) - 1)
print(f'Кого переместили: {pop_user["name"]}')
print(f'Список до изменения: {user1, user2, user3, user4}')
user_list.append(pop_user)
print(f'Список после изменения: {user_list}')
print(f'Средний возраст пользователей: {user_age / len(user_list)}') # используем переменную возраста и делим на общее число их
