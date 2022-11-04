# class Film:
#     def __init__(self, janr, country, osenka):
#         self.janr = janr
#         self.country = country
#         self.osenka = osenka

#     def __str__(self):
#         return f'{self.janr}, {self.country}, {self.osenka}'

# forsaj = Film('komedia', 'USA', '5.5')
# print(forsaj)







# class Monkey:
#     max_age = 12
#     loves_bananas = True

#     def climb(self):
#         print('I am climbing the tree')

# m1 = Monkey()
# print(m1.max_age)
# print(m1.loves_bananas)
# m1.climb()

# m2 = Monkey()
# print(m2.max_age)
# print(m2.loves_bananas)
# m2.climb()



class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, num):
        self.num = num

    def __str__(self):
        return f'через {self.num} лет, будет {self.age + self.num} лет'

p = Person('John', 23, 'male') 
print(p)
p.calculate_age(23)
print(p)
