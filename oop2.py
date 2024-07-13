from abc import ABCMeta, abstractmethod


 
class Programming(metaclass=ABCMeta):
    
    @abstractmethod
    def has_oop(self):
        pass


class Python(Programming):
    @property
    def has_oop(self):
        return 'yes'


class Cpp(Programming):
    @property
    def has_oop(self):
        return 'no'       
    



obj = Python()

print(obj.has_oop)