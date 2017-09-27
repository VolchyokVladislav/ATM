from abc import ABCMeta, abstractmethod

class Repository(metaclass=ABCMeta):
    users = {'Mark': {'password': 1234, 'amount': 1000}}

    def Checking(self):
        print('your amount:', self.users['Mark']['amount'])

    def withdraw_money(self):
        sum1 = input('enter sum: ')
        if int(sum1) <= self.users['Mark']['amount']:
            self.users['Mark']['amount'] -= int(sum1)
            print('Take your money:', int(sum1))
        else:
            print('No money')

    def eject_card(self):
        print('Take your card')

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
        elif int(number) == 2:
            return self.withdraw_money()
        elif int(number) == 3:
            return self.eject_card()





Mark = Check(int(input('password: ')))
Mark.test()