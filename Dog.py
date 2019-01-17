class Dog:

    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
ace = Dog("Ace", 3)
baxter = Dog("Baxter", 7)
apollo = Dog("Apollo", 4)

print("{} is {} and {} is {}.".format(ace.name, ace.age, baxter.name, baxter.age))

def get_biggest_number():
    biggest_number = max(philo.age, mikey.age, ace.age, baxter.age, apollo.age)
    return biggest_number
print("The oldest dog is {} years old.".format(get_biggest_number()))

