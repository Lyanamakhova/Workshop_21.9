# Yеобходимо написать программу, которая позволит составить список гостей. 
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def get_guest(self):
        return f'{self.name} {self.surname}, г. {self.city}'

client_1 = Client('Иван','Петров','Москва',50)
client_2 = Client('Владимир','Зайцев','Кострома',50)
client_3 = Client('Олеся','Янина','Новосибирск',50)

guest_list = [client_1, client_2, client_3]

for guest in guest_list:
    print(guest.get_guest())
