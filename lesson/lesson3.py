# Наследование - Инкапсуляция - Полиморфизм - Абстракция
from abc import ABC, abstractmethod

class Animal(ABC):


    # Декоратор # @abstractmethod
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return print("Gaf Gaf")

    def move(self):
        return print('run')
dog = Dog()
dog.make_sound()

# Nikita.kg
# Twilio.com


class OTPService(ABC):


    @abstractmethod
    def sms_send(self, phone):
        pass


class NikitaOTP(OTPService):


    def sms_send(self, phone):
        phone = input("Введите тел в формате +7xxx xx xx xx xx")

