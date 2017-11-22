# note for class
# difference between class and object
class Person:
    def __init__(self, my_age)
        self.age = my_age
me = Person(2)
# separator
me.set_last_name ("smith")
#The above is the same as the following ,but the following is not recommended
Person.set_last_name(me, "smith")

#set time to meet Ingrid on Dec 14 at 5:25 pm 