from abc import ABCMeta, abstractmethod

class Repository(metaclass=ABCMeta):
    users = {'Mark': {'password': 1234, 'amount': 1000}}

    def Checking(self):
        print(self.users['Mark']['amount'])


class Check(Repository):
    def __init__(self, password):
        global number
        if password == Repository.users['Mark']['password']:
            print('change operation: \n 1)Checking \n 2)withdraw_money \n 3)eject_card')
            number = input('your number: ')
        else:
            raise TypeError('try again')

    def test(self):
        if int(number) == 1:
            return self.Checking()




Mark = Check(int(input('password: ')))
print(Mark.test())