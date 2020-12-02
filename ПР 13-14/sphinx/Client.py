from Person import Person
from Log import Log


class Client(Person):

    def __init__(self, name, surname, age, ticket_id):
        super(Client, self).__init__(name, surname, age)
        Log.CRE("Создан экземпляр класса Client")
        self.__ticket_id = ticket_id
        self.__training_log = {}

    def add_training(self, data, time):
        if data in self.__training_log:
            Log.ERR("Тренировка уже есть в расписании")
            print("{} already exists in training log".format(data))
        else:
            Log.INF("Тренировка добавлена")
            self.__training_log[data] = time

    def get_training(self, key):
        if key in self.__training_log:
            Log.INF("Тренировка получена")
            return key + " - " + self.__training_log[key]
        else:
            Log.ERR("Тренировка не найдена")
            print("{} not found in training parameters".format(key))

    def get_training_log(self):
        Log.INF("Тренировка получена")
        return "Client id: {}, Schedule: {}".format(self.__ticket_id, self.__training_log)

    def print_training_log(self):
        Log.INF("Тренировка распечатана")
        print(self.get_training_log())

    def __str__(self):
        return super(Client, self).__str__() + ", Ticket id: {}".format(self.__ticket_id)


# тестирование
if __name__ == '__main__':
    print("Clients:")
    client1 = Client("Peter", "Petrov", 32, 1)
    client2 = Client("Ivan", "Ivanov", 22, 2)
    client3 = Client("Irina", "Smirnova", 30, 3)
    print(client1.__str__())
    print(client2.__str__())
    print(client3.__str__())

    client1.add_training("01.05.2020", "16:00")
    client2.add_training("02.05.2020", "19:00")
    client3.add_training("03.05.2020", "19:00")
    print("\nClients schedule:")
    client1.print_training_log()
    client2.print_training_log()
    client3.print_training_log()

    print("\nGet schedule training for client 1 by key 01.05.2020:")
    print(client1.get_training("01.05.2020"))

    print("\nOperations with errors:")
    client1.add_training("01.05.2020", "16:00")
    client2.get_training("01.05.2020")
