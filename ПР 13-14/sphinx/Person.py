from Log import Log


class Person:

    def __init__(self, name, surname, age):
        Log.CRE("Создан экземпляр класса Person")
        self.__name = name
        self.__surname = surname

        try:
            self.__age = int(age)

            if not 0 <= age <= 100:
                raise ValueError("age from 0 to 100")
        except ValueError as error:
            Log.ERR("Возраст должен быть в пределах от 0 до 100")
            print("Error:", error)

    def __str__(self):
        output_str = "Name: {}, Surname: {}, Age: {}".format(self.__name, self.__surname, self.__age)
        return output_str


# тестирование
if __name__ == '__main__':
    person = Person("Ivan", "Ivanov", 20)
    print(person.__str__())

    print("\nOperations with errors:")
    person = Person("Ivan", "Ivanov", -1)