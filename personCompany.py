class Person:
    def __init__(self, first_name, second_name, last_name, dict_phones: dict):
        self.phones = dict_phones
        self.FIO = [first_name, second_name, last_name]

    def get_phone(self):
        return self.phones.get('private')

    def get_name(self):
        return " ".join(self.FIO)

    def get_work_phone(self):
        return self.phones.get('work')

    def get_sms_text(self):
        return f"Уважаемый {self.FIO[0]} {self.FIO[1]}! Примите участие в нашем беспроигрышном конкурсе для физических лиц!"


class Company():
    def __init__(self, company_name, type_company, phone_number: dict, *args: Person):
        self.worker_list = list(args)
        self.company_name = company_name
        self.type = type_company
        self.phones_company = phone_number

    def get_name(self):
        return self.company_name

    def get_phone(self):
        if not self.phones_company.get("contact") == None:
            return self.phones_company.get("contact")
        else:
            for worker in self.worker_list:
                if not worker.get_work_phone() == None:
                    return worker.get_work_phone()
            return None

    def get_sms_text(self):
        return f"Для компании {self.company_name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.type}!"


def send_sms(*args):
    for el in args:
        if not el.get_phone() == None:
            print(f"Отправлено СМС на номер {el.get_phone()} с текстом: {el.get_sms_text()}")
        else:
            print(f'Не удалось отправить сообщение абоненту: {el.get_name()}')

#Пример 1

# person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
# person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
# person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
# person4 = Person("John", "Unknown", "Doe", {})
# company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
# company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
# company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
# send_sms(person1, person2, person3, person4, company1, company2, company3)

#Пример 2

person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
