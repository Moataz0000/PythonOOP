class Skills:
    def __init__(self):
        self.skills = ['python', 'machine learning', 'NNL', 'deep learning']

    def __str__(self):
        return f"my skills are --> {self.skills}"
    def __len__(self):
        return  len(self.skills)

obj = Skills()
print(obj)  
print(f'Number of skills are --> {len(obj)}')  

obj.skills.clear()
print(f'Number of skills are --> {len(obj)}')  
print(obj)
