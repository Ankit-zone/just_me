class Herbivore:
    def eat_plants(self):
        return "Eats plant"
class Omnivore:
    def eat_meat(self):
        return "Eat both meat and plant "
class Carnivore:
    def eat_both(self):
        return "Eat meat"
class Bear(Herbivore,Omnivore,Carnivore):
    def describe(self):
        return "Bear is an omnivore "
b=Bear()

print(b.eat_plants())
print(b.eat_meat())
print(b.eat_both())
print(b.describe())