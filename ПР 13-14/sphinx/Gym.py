from Client import Client
from Trainer import Trainer
from Log import Log


class Gym:

    def __init__(self, address):
        Log.CRE("Создан экземпляр класса Gym")
        self.__address = address
        self.__clients = []
        self.__trainers = []

    def __str__(self):
        output_str = "Gym:\nAddress - " + str(self.__address)
        if len(self.__clients) > 0:
            output_str += "\nClients:"
            for client in self.__clients:
                output_str += "\n" + client.__str__()
        if len(self.__trainers) > 0:
            output_str += "\nTrainers:"
            for trainer in self.__trainers:
                output_str += "\n" + trainer.__str__()
        return output_str

    # метод переопределения операции + для добавления клиента
    def __add__(self, client):
        if type(client) is Client:
            Log.INF("Клиент добавлен в Gym")
            self.__clients.append(client)
        else:
            Log.ERR("Переданный объект не является Client")
            print("Object is not Client")

    # метод переопределения операции - для удаления клиента
    def __sub__(self, client):
        if type(client) is Client:
            if client in self.__clients:
                Log.INF("Клиент удалён из Gym")
                self.__clients.remove(client)
            else:
                Log.ERR("Клиента нет в Gym")
                print("Client not found in list")
        else:
            print("Object is not Client")

    def add_trainer(self, trainer):
        if type(trainer) is Trainer:
            Log.INF("Тренер добавлен в Gym")
            self.__trainers.append(trainer)
        else:
            Log.ERR("Переданный объект не является Trainer")
            print("Object is not Trainer")

    # метод получения количества тренеров функцией len
    def __len__(self):
        Log.INF("Количество тренеров получено")
        return len(self.__trainers)

    # метод получения тренеров по индексу
    def __getitem__(self, trainer_ind):
        if trainer_ind < 0 or trainer_ind >= len(self.__trainers):
            Log.ERR("Тренер по индексу {} не найден в Gym".format(trainer_ind))
            print("Trainer {} not found in list".format(trainer_ind))
        else:
            Log.INF("Тренер по индексу {} найден в Gym".format(trainer_ind))
            return self.__trainers[trainer_ind]

    # метод изменения тренера по индексу
    def __setitem__(self, key, value):
        if key < len(self.__trainers):
            Log.INF("Тренер по индексу {} изменён в Gym".format(key))
            self.__trainers[key] = value
        else:
            Log.ERR("Тренер по индексу {} не найден в Gym".format(key))
            print("Trainer with index {} not exist".format(key))

    # метод удаление тренеров по индексу
    def __delitem__(self, trainer_ind):
        if trainer_ind < 0 or trainer_ind >= len(self.__trainers):
            try:
                Log.INF("Тренер по индексу {} не найден в Gym".format(trainer_ind))
                print("Trainer {} not found in list".format(trainer_ind))
            except IndexError:
                print("Oops")
        else:
            Log.INF("Тренер по индексу {} удалён из Gym".format(trainer_ind))
            return self.__trainers.pop(trainer_ind)

    def write_to_file(self, file_name):
        try:
            with open(file_name, 'w') as f:
                f.write(gym.__str__())
                f.write("\n\n" + "Clients trainings log:")

                for client in self.__clients:
                    f.write("\n" + client.get_training_log())

                f.write("\n\n" + "Trainers trainings schedule:")

                for trainer in self.__trainers:
                    f.write("\n" + trainer.get_schedule())

                Log.INF("Содержимое объекта Gym записано в файл {}".format(file_name))
        except IOError:
            Log.ERR("Ошибка записи в файл {}".format(file_name))
            print("Can not write file {}".format(file_name))


# тестирование
if __name__ == '__main__':
    gym = Gym("Russia, Moscow, New Arbat Avenue")

    trainer1 = Trainer("Irina", "Popova", 21, 1, "Dance trainer")
    trainer2 = Trainer("Ivan", "Ivanov", 32, 2, "Fitness trainer")
    trainer1.add_training_to_schedule("01.05.2020", "16:00")
    trainer2.add_training_to_schedule("01.05.2020", "11:00")
    gym.add_trainer(trainer1)
    gym.add_trainer(trainer2)

    client1 = Client("Sergey", "Smirnov", 40, 1)
    client2 = Client("Peter", "Petrov", 30, 2)
    client1.add_training("01.05.2020", "16:00")
    client2.add_training("01.05.2020", "11:00")

    gym + client1
    gym + client2
    print(gym.__str__())

    gym.write_to_file("gym.txt")

    print("\nAfter removing the last client and last trainer:")
    gym - client2
    del gym[1]
    print(gym.__str__())

    print("\nCount of trainers: " + str(len(gym)))
    print("\nTrainer by index 0:\n" + str(gym[0]))

    print("\nEdit trainer by index 0")
    gym[0] = trainer2
    print("Trainer by index 0:\n" + str(gym[0]))

    print("\nOperations with errors:")
    gym + trainer1
    gym - trainer1
    gym.add_trainer(client1)
    gym[10]
    gym[10] = trainer2
    del gym[10]
