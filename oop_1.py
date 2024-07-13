class Members:
    #class attribute 
    not_names_allow = ['fuck', 'shit']
    user_count = 0
    @classmethod
    def show_users_count(cls):
        print(f'We have {cls.user_count} users in our system.')

    @staticmethod
    def show_logo():
        print('Welcome to in promo shop.')    
  
    def __init__(self,first_name , meddil_name , last_name , gender)-> str:
        # Object Attribute
        self.f_name = first_name
        self.m_name = meddil_name
        self.l_name = last_name
        self.gender = gender.lower()
        Members.user_count += 1


    def get_full_name(self):
        if self.f_name in Members.not_names_allow:
            raise ValueError(f'"{self.f_name}" name isn\'t allowed!')
        else:
            return (f'{self.f_name} {self.m_name} {self.l_name}')
    
    def name_with_title(self):
        
        if self.gender == 'male':
            return f'Hello, Mr.{self.f_name}'
        elif self.gender == 'female':
            return f'Hello, Miss.{self.f_name}'
        else:
            raise ValueError('Invalid Error.Please Write"Male OR Female"')
  
    def get_all_info(self):
        return (f'{self.name_with_title()}, Your Full Name Is: {self.get_full_name()}')
    

        # print(f'Users count are {count}')
    
    def delete_user(self):
        Members.user_count -= 1
        return f'User "{self.f_name}" is deleted."'

# Members.show_users_count()
member_one = Members("mezo" , 'fawzy', 'elsayed' , 'male')   
# member_one = Members("mezo" , 'fawzy', 'elsayed' , 'male')   
# member_one = Members("shit" , 'fuck', 'elsayed' , 'male')   
# Members.show_users_count()
# print(Members.get_full_name(member_one))
Members.show_logo()

