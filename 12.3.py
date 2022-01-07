"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""


class Character:
    def __init__(self, charcter):
        self.__character=charcter
        self.__name={}

    def give_item(self, item):
        if item not in self.__name.keys():
            self.__name[item]=0

        self.__name[item]+=1

    def remove_item(self,item):
        self.__name[item]-=1
        if self.__name[item]==0:
            self.__name.pop(item)

    def printout(self):
        print(f"Name: {self.get_name()}")
        if not self.__name:
            print("  --nothing--")
        else:
            for val in sorted(self.__name.keys()):
                print(f"  {self.__name[val]} {val}")

    def get_name(self):
        return self.__character

    def has_item(self, item):
        if item in self.__name.keys():
            return True
        else:
            return False

    def how_many(self,item):
        if item not in self.__name.keys():
            x=0
        else:
            x= int(self.__name[item])
        return x


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
