class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + ' ' + self.family_name

    def entry_fee(self):
        if self.age < 20:
            return 1000
        if self.age < 65:
            return 1500
        return 1200

# C-1
# ken = Customer(first_name="Ken", family_name="Tanaka")
# full_name = ken.full_name()  # "Ken Tanaka" という値を返す
# print(full_name)
#
# tom = Customer(first_name="Tom", family_name="Ford")
# full_name = tom.full_name()  # "Tom Ford" という値を返す
# print(full_name)


# C-2
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# age = ken.age  # 15 という値を返す
# print(age)
#
# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# age = tom.age # 57 という値を返す
# print(age)
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# age = ieyasu.age # 73 という値を返す
# print(age)

# C-3
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
fee = ken.entry_fee()  # 1000 という値を返す
print(fee)

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
fee = tom.entry_fee() # 1500 という値を返す
print(fee)

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
fee = ieyasu.entry_fee() # 1200 という値を返す
print(fee)

