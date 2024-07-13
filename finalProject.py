# Banking system using OOP

# parent class: User 
# Holds detials about an user  
# Has a function to show user details
# -------------------------------------------
# Child class: Bank 
# stores details about the account balance 
# stores details about the amount
# Allows for deposites, withdraw, view_balance



# Parent Class
class User():
    users_count = 0
    
    @classmethod
    def show_users_count(cls):
        print(f'We have {cls.users_count} users in our system.')


    def __init__(self, name ,age, gender):
        self.name = name
        self.age  = age
        self.gender = gender
        User.users_count += 1

    @property
    def show_user_details(self):
        print('Personal Details:')
        print('')
        print(f'Name: {self.name}')
        print(f'Age : {self.age}')
        print(f'Gender: {self.gender}')




# Child Class
class Bank(User):
    def __init__(self,name, age, gender):
        super().__init__(name,age, gender)
        self.balance = 0


    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount  
        print(f'Account balance has been updated: ${self.balance}')  

    def withdarw(self,amount):
        self.amount = amount
        if(self.amount > self.balance):
            print(f'Insufficient Funds | Balance Available: ${self.balance}')
        elif(self.amount < self.balance):
            self.balance = self.balance - self.amount  
            print(f'Account balance has been updated: ${self.balance}')    
        else:
            raise ValueError(f'Invalid input {self.amount}!')
    

    def view_balance(self):
        self.show_user_details
        print(f'Account balance: ${self.balance}')  
        User.show_users_count()





# Object
obj = Bank('mezo',21,'Male')
obj.deposit(100)
obj.withdarw(500)


