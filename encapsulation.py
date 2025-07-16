class public:
    def __init__(self):
        self.name="sruthi"
    def display_name(self):   #encapsulation public variable
        print(self.name)
obj=public()
obj.display_name()
print(obj.name)
###########################
class Protected:
    def __init__(self):
        self._age=30
class Subclass(Protected):
    def display_age(self):  #encapsulation protected
        print(self._age)
obj=Subclass()
obj.display_age()

##############################
class Private:
    def __init__(self):
        self.__salary=50000
    def salary(self):
        return self.__salary #encapsulation private
obj=Private()
print(obj.salary())