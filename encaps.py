# puclic , protected, private


class Member:
    def __init__(self, name):
        self.__name = name # Private 

    def say_hello(self):
        return f'Hello {self.__name}'  

    # private method
    def __fuck(self):
        return f'fuck {self.__name}'  
    
    # seter mehtod
    def get_name(self):
        return self.__name
     
    # geter method
    def set_name(self, new_name):
        self.__name = new_name
    



one = Member('Mezo')
# print(one._Member__name) # access private att
# print(one._Member__fuck()) # access private method



print(one.get_name())

print(one.set_name('Moataz'))