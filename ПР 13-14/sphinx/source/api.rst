Руководство разработчика
========================

.. automodule:: main
	:members:

Классы
######

.. automodule:: Person

.. autoclass:: Person
	:members:

	.. automethod:: __init__
	.. automethod:: __str__

.. automodule:: Client

.. autoclass:: Client
	:members:

	.. automethod:: __init__
	.. automethod:: __str__

.. automodule:: Trainer

.. autoclass:: Trainer
	:members:

	.. automethod:: __init__
	.. automethod:: __str__


**Класс Gym**

.. automodule:: Gym

.. autoclass:: Gym
	:members:

	.. automethod:: __init__
	.. automethod:: __len__
	.. automethod:: __getitem__
	.. automethod:: __delitem__
	.. automethod:: __setitem__
	.. automethod:: __add__
	.. automethod:: __sub__
	.. automethod:: __str__

Графики наследования классов
############################

.. inheritance-diagram:: Client
.. inheritance-diagram:: Trainer

UML-диаграмма наследования классов
##################################

.. uml::

    skinparam shadowing false
    skinparam monochrome true

    class Person {
      # name
      # surname
      # age
      + __str__()
    }
    class Client {
      - ticket_id
      - training_log
      + get_training(key)
      + get_training_log()
      + print_training_log()
      + __str__()
    }
    class Trainer {
      - id_number
      - position
      - schedule
      + add_training_to_schedule(data, time)
      + edit_training_in_schedule(data, time)
      + remove_training_in_schedule(data)
      + get_training_schedule(data)
      + get_schedule()
      + print_schedule()
      + __str__()
    }

    Client -up-> Person
    Trainer -up-> Person