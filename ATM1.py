from abc import ABCMeta, abstractmethod

class Repository(metaclass=ABCMeta):
    users = {'Mark': {'password': 1234, 'amount': 1000}}

    @abstractmethod
    def checking(self):
        pass

    @abstractmethod
    def withdraw_money(self):
        pass

    @abstractmethod
    def eject_card(self):
        pass


class User(Repository):
    def __init__(self, password):
        if str(self) in Repository.users.keys():
            if password == Repository.users[str(self)]['password']:
                print('change operation')
        else:
            raise TypeError('try again')

    def checking(self):
            pass

    def withdraw_money(self):
            pass

    def eject_card(self):
            pass

Mark = User(int(input("your password: ")))