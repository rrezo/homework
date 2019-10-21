# Implement 2 classes, the first one is Boss and the second one is Worker
# Worker has a property 'boss' which value must be an instance of Boss
# You can reassign this value, but you should check whether the new value
# is Boss. Each Boss has a list of his own workers. You should implement
# a method which allows you to add workers to a Boss. You're not allowed
# to add instances of Boss class to workers list!
# You can refactor the existing code.
#
# id_ - is just a random unique integer


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = set()

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.add(worker)
        else:
            print("Boss instance can't be added to workers list")

    def remove_worker(self, worker):   #called automatically when the worker
        self.workers.remove(worker)    #reassignes a new boss

    def __repr__(self):
        return self.name


class Worker(Boss):
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        super().__init__(id_, name, company)
        self._boss = boss
        boss.add_worker(self)   #automaticcally adds worker to boss' list

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if not isinstance(value, Worker):
            self._boss.remove_worker(self)   #removes previous boss's worker
            value.add_worker(self)
        else:
            print('This person is not a Boss instance')

    def __repr__(self):
        return self.name


boss1 = Boss(101, 'Steve', 'Apple')
boss2 = Boss(102, 'John', 'Apple')

worker1 = Worker(501, 'Sue', 'Apple', boss1)
worker2 = Worker(502, 'Victoria', 'Apple', boss1)
worker3 = Worker(502, 'Tim', 'Apple', boss1)

print('\nAdd workers to boss list check:\n')

boss1.add_worker(worker1)
boss1.add_worker(boss2)
boss1.add_worker(worker2)
boss2.add_worker(worker2)

print("Boss's workers list:", boss1.workers, sep=' ')
print("Worker's boss:", worker1.boss, sep=' ')

print("\nCheck change worker's boss:\n")

worker1.boss, worker2.boss, worker3.boss = boss1, boss1, boss1

print("Worker's boss:", worker1.boss, sep=' ')
print("Boss's workers list:", boss1.name, boss1.workers, sep=' ')
print("Boss's workers list:", boss2.name, boss2.workers, sep=' ')

worker2.boss = boss2
worker3.boss = boss2
worker3.boss = worker1
print("Boss's workers list:", boss1.name, boss1.workers, sep=' ')
print("Boss's workers list:", boss2.name, boss2.workers, sep=' ')


# Write a class TypeDecorators which has several methods for converting
# results of functions to a specified type (if it's possible):
# methods:
#   - to_int
#   - to_str
#   - to_bool
#   - to_float
#
# Don't forget to use @wraps

from functools import wraps

class TypeDecorators:

    @staticmethod
    def to_int(func):
        def wrapper(*args):
            return int(func(*args))
        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(*args):
            return bool(func(*args))
        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(*args):
            return str(func(*args))
        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True

print(do_nothing('25'))
print(do_something('True'))






