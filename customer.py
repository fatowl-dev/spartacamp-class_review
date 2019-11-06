class Customer:
    def __init__(self, first_name: str, family_name: str, age: int):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + ' ' + self.family_name

    def entry_fee(self):
        if self.age <= 3:
            return 0
        if self.age < 20:
            return 1000
        if self.age < 65:
            return 1500
        if self.age < 75:
            return 1200
        return 500

    def info_csv(self, sep: str = ','):
        cells = [self.first_name + ' ' + self.family_name, str(self.age), str(self.entry_fee())]
        return sep.join(cells)

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
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# fee = ken.entry_fee()  # 1000 という値を返す
# print(fee)
#
# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# fee = tom.entry_fee() # 1500 という値を返す
# print(fee)
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# fee = ieyasu.entry_fee() # 1200 という値を返す
# print(fee)

# C-4
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# csv = ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す
# print(csv)
#
# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# csv = tom.info_csv()  # "Tom Ford,57,1500" という値を返す
# print(csv)
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# csv  =ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
# print(csv)

# C-5
# ikura = Customer(first_name='Ikura', family_name='Namino', age=2)
# print(ikura.entry_fee())

# C-6
# namihei = Customer(first_name='Namihei', family_name='Isono', age=76)
# print(namihei.entry_fee())

# C-7 C-8
# タブ
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
csv = ken.info_csv(sep='\t')  # "Ken Tanaka 15  1000" という値を返す
print(csv)

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
csv = tom.info_csv('\t')  # "Tom Ford   57  1500" という値を返す
print(csv)

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
csv  =ieyasu.info_csv('\t')  # "Ieyasu  Tokugawa    73  1200" という値を返す
print(csv)

# パイプ
csv = ken.info_csv(sep='|')  # "Ken Tanaka|15|1000" という値を返す
print(csv)
csv = tom.info_csv(sep='|')  # "Tom Ford|57|1500" という値を返す
print(csv)
csv  =ieyasu.info_csv(sep='|')  # "Ieyasu Tokugawa|73|1200" という値を返す
print(csv)

