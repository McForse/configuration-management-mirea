from Person import Person
from Log import Log


class Trainer(Person):

    def __init__(self, name, surname, age, id_number, position):
        super(Trainer, self).__init__(name, surname, age)
        Log.CRE("Создан экземпляр класса Trainer")
        self.__id_number = id_number
        self.__position = position
        self.__schedule = {}

    def add_training_to_schedule(self, data, time):
        if data in self.__schedule:
            Log.ERR("Тренировка уже есть в расписании")
            print("{} already exists in schedule".format(data))
        else:
            Log.INF("Тренировка добавлена")
            self.__schedule[data] = time

    def edit_training_in_schedule(self, data, time):
        if data in self.__schedule.keys():
            Log.INF("Тренировка изменена в расписании")
            self.__schedule[data] = time
        else:
            Log.ERR("Тренировка не найдена")
            print("{} not found in schedule".format(data))

    def remove_training_in_schedule(self, data):
        if data in self.__schedule.keys():
            Log.INF("Тренировка удалена из расписания")
            del self.__schedule[data]
        else:
            Log.ERR("Тренировка не найдена")
            print("{} not found in schedule".format(data))

    def get_training_schedule(self, data):
        if data in self.__schedule:
            return self.__schedule[data]
        else:
            Log.ERR("Тренировка не найдена")
            print("{} not found in schedule".format(data))

    def get_schedule(self):
        Log.INF("Тренировка получена")
        return "Trainer id: {}, Schedule: {}".format(self.__id_number, self.__schedule)

    def print_schedule(self):
        Log.INF("Расписание распечатано")
        print(self.get_schedule())

    def __str__(self):
        return super(Trainer, self).__str__() + ", Id number: {}, Position: {}".format(self.__id_number, self.__position)


# тестирование
if __name__ == '__main__':
    print("Trainers:")
    trainer2 = Trainer("Irina", "Popova", 21, 1, "Dance trainer")
    trainer1 = Trainer("Ivan", "Ivanov", 32, 2, "Fitness trainer")
    trainer3 = Trainer("Peter", "Petrov", 30, 3, "Swimming trainer")

    print(trainer1.__str__())
    print(trainer2.__str__())
    print(trainer3.__str__())

    trainer1.add_training_to_schedule("01.05.2020", "16:00")
    trainer1.add_training_to_schedule("02.05.2020", "19:00")
    trainer1.add_training_to_schedule("03.05.2020", "19:00")
    trainer2.add_training_to_schedule("01.05.2020", "11:00")
    trainer3.add_training_to_schedule("01.05.2020", "09:00")
    print("\nTrainers schedule:")
    trainer1.print_schedule()
    trainer2.print_schedule()
    trainer3.print_schedule()

    trainer1.remove_training_in_schedule("01.05.2020")
    trainer1.remove_training_in_schedule("02.05.2020")
    trainer1.remove_training_in_schedule("03.05.2020")
    print("\nAfter removing all trainings for trainer 1:")
    trainer1.print_schedule()
    trainer2.print_schedule()
    trainer3.print_schedule()

    trainer2.edit_training_in_schedule("01.05.2020", "19:00")
    trainer3.edit_training_in_schedule("01.05.2020", "22:00")
    print("\nAfter editing all time in schedule:")
    trainer1.print_schedule()
    trainer2.print_schedule()
    trainer3.print_schedule()

    print("\nOperations with errors:")
    trainer1.remove_training_in_schedule("01.05.2020")
    trainer2.edit_training_in_schedule("02.05.2020", "19:00")
    trainer3.add_training_to_schedule("01.05.2020", "22:00")
