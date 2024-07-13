class Age:
    users_count = 0
    
    @staticmethod
    def say_welcome():
        print(f'Welcome to in our system calculater.')
        print('-----------------------------------')

    @classmethod
    def show_users_count(cls):
        print('-----------------------------------')
        print(f'We have {cls.users_count} in our system.')


    def __init__(self):
        Age.say_welcome()
        self.age = int(input('Enter your age: ').strip())  
        self.choise_method()
        Age.users_count += 1

    def choise_method(self):
        print("'Month' , 'Days' , 'Hours' 'Secondes' | m or d or h or s")   
        type_of_method = str(input('Enter your choise method: ').strip().lower())
        print('------------------------Your Bill--------------------------')
        if type_of_method == 'month' or type_of_method == 'm':
            self.calc_months()
        elif type_of_method == 'days' or type_of_method == 'd':
            self.calc_days()  
        elif type_of_method == 'hour' or type_of_method == 'h':
            self.calc_hours()  
        elif type_of_method == 'seconde' or type_of_method == 's':
            self.calc_secondes()

        else:
            raise ValueError(f'Value error, "{type_of_method}". Enter valid paramerar like that ==> [m , d , h , s]')  


    def calc_months(self):
        months = self.age * 12
        print((f'You live "{months}" month.'))
        return months
    
    def calc_days(self):
        days = self.calc_months() * 356
        print(f'You live "{days}" day. ') 
        return days
    
    def calc_hours(self):
        hours = self.calc_days() * 24
        print(f'You live "{hours}" hour. ') 
        return hours
    
    def calc_secondes(self):
        secondes = self.calc_hours() * 60
        print(f'You live "{secondes}" seconde. ') 
        return secondes
           

obj = Age()
obj.show_users_count()
