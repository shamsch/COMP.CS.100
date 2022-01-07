"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Project: accesscontrol, program template
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}

class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """
        #declaring the constructors and an empty list
        self.__id=id
        self.__name=name
        self.__access=[]


    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """
        #carrying out the printing task
        print(f"{self.__id}, {self.__name}, access: ", end="")
        str=""
        for val in sorted(self.__access): #sorting the acesscodes in alphabatical order
            str= str + val + ", "
        x= str.rstrip(", ")
        print(x)


    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """
        #getting the name
        return self.__name


    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        #the first to if and elif can be shortened it's basically checking if the new accesscode is already there
        if new_access_code in DOORCODES.keys():
            if self.check_access(new_access_code):
                pass
            else:
                self.__access.append(new_access_code)
        elif new_access_code in self.returnAccessList():
            pass
        else:
            self.__access.append(new_access_code)



    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        #checking the access right
        found= False
        if DOORCODES[door]==[]: #doors which don't have any accesscode
            for val in self.__access:
                if val==door:
                    found= True
        elif door in self.__access:  #if the door is already in access
            found=True
        else:
            for access in DOORCODES[door]: #iterating over the DOOR dictionary and checking if one of the acess code can grant acess to this particular door
                for val in self.__access:
                    if val==access:
                        found= True

        if found: #returing appropriate response
            return True
        else:
            return False


    def returnAccessList(self):
        """
        returns the access list of self object
        """
        #self made method
        return self.__access

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added to this card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        add= card.returnAccessList()
        for element in add: #makes sures if only unique elements are added aka no repettion
            if element not in self.__access:
                self.__access.append(element)

    def checkAndDelete(self):
        """
        This method deletes redundant door names from the access list if there is an access code that has right to that particular door
        """
        for ele in self.__access:
            if ele in DOORCODES.keys(): #only checking door names, not access codes
                if self.check_access(ele): #checking if there is access to the door (it is implemented in the main function in such a way that it doesn't delete everytime, circumventing the obvious)
                    self.__access.remove(ele)
                else:
                    pass


# TODO: Implement helper functions here.

def listOfAllValues(dict):
    """
    This function is used to generate a list of all unique values inside a nested list-dictionary
    """
    str=[]
    for val in dict.values():
       for ele in val:
              if ele not in str:
                  str.append(ele)
    return str


def main():
    objectDict={}
    allAccessCode= listOfAllValues(DOORCODES) #getting all unique accesscode from the DOOR dict
    try:
        file = open("accessinfo.txt", mode="r") #reading fill data
        for file_line in file:
            file_line = file_line.rstrip()
            data_str= file_line.split(";") #breaking the data apart
            id=data_str[0]
            name=data_str[1]
            access=data_str[2]
            accessCodes = access.split(",") #breaking the accesscode apart
            x = Accesscard(id, name) #creating the object
            for ele in accessCodes: #passing the access code into the object
                x.add_access(ele)
            objectDict[id] = x #storing the object in a dict with respect to its ID
        file.close() #good practice?
    except:
        print("Error: file cannot be read.")
        return #error handeling


    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            for val in sorted(objectDict.keys()): #showing all the card info by retreving the object from the dict, sorting to meet the condition
                objectDict[val].info()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            if card_id not in objectDict.keys():
                print("Error: unknown id.") #error
            else:
                objectDict[card_id].info() #showing just one card info


        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]

            if card_id not in objectDict.keys():
                print("Error: unknown id.") #error cases
            elif door_id not in DOORCODES.keys():
                print("Error: unknown doorcode.")
            elif objectDict[card_id].check_access(door_id):
                print(f"Card {card_id} ( {objectDict[card_id].get_name()} ) has access to door {door_id}") #has access
            else:
                print(f"Card {card_id} ( {objectDict[card_id].get_name()} ) has no access to door {door_id}") #has no acess with the help of the method

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            if card_id not in objectDict.keys():
                print("Error: unknown id.") #error cases
            elif access_code not in allAccessCode and access_code not in DOORCODES.keys():
                print("Error: unknown accesscode.")
            elif access_code in objectDict[card_id].returnAccessList():
                pass #if already in access makes no effect
            else:
                objectDict[card_id].add_access(access_code) #adding
                if access_code in allAccessCode: #circumventing the obvious case of deleting everytime by using it only when the new access is an access code itself
                    objectDict[card_id].checkAndDelete()



        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            if card_id_to not in objectDict.keys() or card_id_from not in objectDict.keys():
                print("Error: unknown id.") #error case
            else:
                objectDict[card_id_to].merge(objectDict[card_id_from]) #merging using the prebuilt method

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


#ciao thanks for reading, i know this program could have been made simpler but i did it on a hurry

if __name__ == "__main__":
    main()

