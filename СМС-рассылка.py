'''class Queue:
    def __init__(self, *queue):
        self.queue = queue

    def append(self, *values):
        self.queue = (*self.queue, *values)

    def copy(self):
        return Queue(*self.queue)

    def pop(self):
        if self.queue:
            el = self.queue[0]
            self.queue = self.queue[1:]
            return el
        return

    def extend(self, new_queue):
        self.queue = (*self.queue, *new_queue.queue)

    def next(self):
        return self.queue[1:]

    def __add__(self, other):
        return Queue(*(self.queue + other))

    def __iadd__(self, other):
        self.extend(other)

    def __eq__(self, values):
        return self.queue == values.queue

    def __rshift__(self, n):
        return Queue(*self.queue[n:])

    def __str__(self):
        return '[' + ' -> '.join([str(i) for i in self.queue]) + ']'


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep='\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)'''


class Person:
    def __init__(self, name: str, patronymic: str, surname: str, phones: dict):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.phones = phones

    def get_phone(self):
        return self.phones['private'] if 'private' in self.phones.keys() else None

    def get_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def get_work_phone(self):
        return self.phones['work'] if 'work' in self.phones.keys() else None

    def get_sms_text(self):
        return (f'Уважаемый {self.name} {self.patronymic}! '
                f'Примите участие в нашем беспроигрышном конкурсе для физических лиц')


class Company:
    def __init__(self, name: str, type: str, phones: dict, *workers):
        self.name = name
        self.type = type
        self.phones = phones
        self.workers = workers

    def get_phone(self):
        if 'contact' in self.phones.keys():
            return self.phones['contact']
        for i in self.workers:
            if 'work' in i.phones.keys():
                return i.phones['work']
        return

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return (f'Для компании {self.name} есть супер предложение! '
                f'Примите участие в нашем беспроигрышном конкурсе для {self.type}')


def send_sms(*args):
    for i in args:
        if i.get_phone():
            print(f'Отправлено СМС на номер {i.get_phone()} с текстом: {i.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {i.get_name() if type(i) == Person else i.get_name()}')


person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
