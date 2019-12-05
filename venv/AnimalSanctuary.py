import csv
from Pet import Pet
from WildAnimal import WildAnimal
from Treatment import Treatment


class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None  # reference to the next node
        self.pref = None  # refernce to the previous node


class DoublyLinkedList:

    def __init__(self):  # when a new instance of the DLL is created, there is nothing in it
        self.start_node = None

    def initListWA(self):
        with open('wildanimals.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for col in csv_reader:
                tempAnimal = WildAnimal(col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7])
                wildanimals.insert(tempAnimal)

    def initListPet(self):
        with open('pets.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for col in csv_reader:
                tempPet = Pet(col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10])
                pets.insert(tempPet)

    def initListTreatment(self):
        with open('treatment.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for col in csv_reader:
                tempTreat = Treatment(col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7])
                treatment.insert(tempTreat)

    def insert(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def addNewEntryWA(self):
        id = input("Sanctuary Identification: ")
        type = input("Type: ")
        vacc = input("Vaccinated (Yes or No): ")
        adm = input("Reason for admission: ")
        arr = input("Date of arrival: ")
        dep = input("Date of departure(if available): ")
        dest = input("Destination: ")
        destadd = input("Destination address: ")
        tempAnimal = WildAnimal(id, type, vacc, adm, arr, dep, dest, destadd)
        wildanimals.insert(tempAnimal)
        # add the new entry to the csv file
        row = [id, type, vacc, adm, arr, dep, dest, destadd]
        with open('wildanimals.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

    def addNewEntryPet(self):
        id = input("Sanctuary Identification: ")
        type = input("Type: ")
        bre = input("Breed: ")
        vacc = input("Vaccinated (Yes or No): ")
        neut = input("Neutered: ")
        mic = input("Microchip number: ")
        rea = input("Reason for admission: ")
        adm = input("Reason for admission: ")
        arr = input("Date of arrival: ")
        dep = input("Date of departure(if available): ")
        dest = input("Destination: ")
        destadd = input("Destination address: ")
        tempAnimal = WildAnimal(id, type, vacc, adm, arr, dep, dest, destadd)
        wildanimals.insert(tempAnimal)
        # add the new entry to the csv file
        row = [id, type, vacc, adm, arr, dep, dest, destadd]
        with open('pets.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

    def addNewEntryTreatment(self):
        id = input("Sanctuary Identification: ")
        surg = input("Surgery: ")
        surgDate = input("Surgery Date: ")
        medic = input("Medication: ")
        medstart = input("Medication Start: ")
        medfinish = input("Medication Finish: ")
        abuse = input("Responsible for Abuse: ")
        abandon = input("Responsible for Abandoning: ")
        tempTreatment = Treatment(id, surg, surgDate, medic, medstart, medfinish, abuse, abandon)
        treatment.insert(tempTreatment)
        row = [id, surg, surgDate, medic, medstart, medfinish, abuse, abandon]
        with open('treatment.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

    def searchbyID(self, value):
        flag = False
        n = self.start_node
        head = n
        tail = n  # initialize the tail
        while tail.nref is not None:  # find the real tail
            tail = tail.nref
        while head is not tail:
            if head.item.id == value or tail.item.id == value:
                flag = True
                break
            else:
                head = head.nref
                tail = tail.pref
        if flag:
            if head.item.id == value:
                return head.item
            else:
                return tail.item
        else:
            return None

    def removeDuplicate(self):  # this method is only used for the list of abandoners and abusers
        # Checks whether list is empty
        if (self.start_node == None):
            return
        else:
            # Initially, current will point to head node
            n = self.start_node
            while n is not None:
                # index will point to node next to current
                index = n.nref
                while index is not None:
                    if (n.item == index.item):
                        # Store the duplicate node in temp
                        temp = index
                        # index's previous node will point to node next to index thus, removes the duplicate node
                        index.pref.nref = index.nref
                        if index.nref is not None:
                            index.nref.pref = index.pref
                            # Delete duplicate node by making temp to None
                        temp = None
                    index = index.nref
                n = n.nref

    def generateList(self, type):
        if self.start_node is None:
            print("List has no entry")
        else:
            if type == "Cat" or type == "Dog":
                n = self.start_node
                while n is not None:
                    if (n.item.type == type) and (n.item.vaccinated == 'Yes') and (n.item.neutered == 'Yes') and (
                            n.item.microchip != '') \
                            and not (n.item.destination):
                        print(n.item.print_all, " ")
                    n = n.nref
            elif type == "Abuse":
                n = self.start_node
                n = n.nref
                while n is not None:
                    if n.item.abuse:
                        abuser.insert(n.item.abuse)
                    n = n.nref
                abuser.removeDuplicate()
                abuser.sortNodes()
                abuser.traverse()
            elif type == "Abandon":
                n = self.start_node
                n = n.nref
                while n is not None:
                    if n.item.abandon:
                        abandoner.insert(n.item.abandon)
                    n = n.nref
                abandoner.removeDuplicate()
                abandoner.sortNodes()
                abandoner.traverse()
            elif type == "ReturnWA":
                n = self.start_node
                while n is not None:
                    if (n.item.reason.lower == "lost" and not n.item.destination \
                            and treatment.crossCheck(n.item.id)):
                        returner.insert(n.item.id)
                    n = n.nref

            elif type == "ReturnPet":
                n = self.start_node
                while n is not None:
                    if n.item.reason.lower() not in ['abandoned', 'abused',
                                                     'stray'] and not n.item.destination and n.item.vaccinated == "Yes":
                        returner.insert(n.item.id)
                    n = n.nref

    def crossCheck(self, id):  # check if an ID is in the Treatment file and if yes, has its medication finished or not
        n = self.start_node
        flag = False
        while n is not None:
            if n.item.id == id and n.item.medicFinish:
                flag = True
            n = n.nref
        return flag

    def sortNodes(self):
        if self.start_node is None:
            return;
        else:
            current = self.start_node
            while current.nref is not None:
                index = current.nref
                while index is not None:
                    if (current.item > index.item):
                        temp = current.item
                        current.item = index.item
                        index.item = temp
                    index = index.nref
                current = current.nref

    def traverse(self):
        if self.start_node is None:
            print("List has no entry")
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def enterDetails(self, type):
        if self.start_node is None:
            print("List has no entry")
        else:
            if type == "surgery":
                ans = input("Type in the ID of the entry you want to enter surgery details: ")
                if "WA" in ans.upper():
                    wildanimals.searchbyID(ans)
                elif "P" in ans.upper():
                    pets.searchbyID(ans)

    def enterSurgery(self, sid, surgery, surgeryDate):
        row_index = 0
        row = []
        n = self.start_node
        while n is not None:
            if n.item.id == sid and n.item.surgery is not None:
                n.item.surgery = surgery
                n.item.surgeryDate = surgeryDate
                row = [n.item.id, n.item.surgery, n.item.surgeryDate, n.item.medic, n.item.medicStart,
                       n.item.medicFinish, n.item.abuse, n.item.abandon]
                break
            row_index += 1
            n = n.nref

        print(row)  # for debugging purposes
        print(row_index)  # for debugging purposes
        with open('treatment.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            lines[row_index] = row
        with open('treatment.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        readFile.close()
        writeFile.close()

    def editAbuser(self, sid, name):
        n = self.start_node
        row_index = 0
        row = []
        while n is not None:
            if n.item.id == sid:
                n.item.abuse = name
                row = [n.item.id, n.item.surgery, n.item.surgeryDate, n.item.medic, n.item.medicStart, n.item.medicFinish, n.item.abuse, n.item.abandon]
                break
            row_index += 1
            n = n.nref
        print(row)  # for debugging purposes
        print(row_index)  # for debugging purposes
        with open('treatment.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            lines[row_index] = row
        with open('treatment.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        readFile.close()
        writeFile.close()

    def editAbandoner(self, sid, name):
        n = self.start_node
        row_index = 0
        row = []
        while n is not None:
            if n.item.id == sid:
                n.item.abandon = name
                row = [n.item.id, n.item.surgery, n.item.surgeryDate, n.item.medic, n.item.medicStart, n.item.medicFinish, n.item.abuse, n.item.abandon]
                break
            row_index += 1
            n = n.nref
        print(row)  # for debugging purposes
        print(row_index)  # for debugging purposes
        with open('treatment.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            lines[row_index] = row
        with open('treatment.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        readFile.close()
        writeFile.close()

    def enterNeuteuring(self, id, value):
        row = []
        row_index = 0
        n = self.start_node
        while n is not None:
            if n.item.id == id and n.item.reason is not 'Lost':
                n.item.neutered = value
                row = [n.item.id, n.item.type, n.item.breed, n.item.vaccinated, n.item.neutered, n.item.microchip, \
                       n.item.reason, n.item.arriveDate, n.item.departDate, n.item.destination, n.item.address]
                break
            row_index += 1
            n = n.nref
        print(row)  # for debugging purposes
        print(row_index)  # for debugging purposes
        with open('pets.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            lines[row_index] = row
        with open('pets.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        readFile.close()
        writeFile.close()

    def enterMicrochip(self, id, value):
        n = self.start_node
        row = []
        row_index = 0
        while n is not None:
            if n.item.id == id and not n.item.microchip and not n.item.destination:
                n.item.microchip = value
                row = [n.item.id, n.item.type, n.item.breed, n.item.vaccinated, n.item.neutered, n.item.microchip, \
                       n.item.reason, n.item.arriveDate, n.item.departDate, n.item.destination, n.item.address]
                break
            row_index += 1
            n = n.nref
        print(row)  # for debugging purposes
        print(row_index)  # for debugging purposes
        with open('pets.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            lines[row_index] = row
        with open('pets.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        readFile.close()
        writeFile.close()

    def editDeparture(self, id, date, destination, address):
        n = self.start_node
        row = []
        row_index = 0
        while n is not None:
            if n.item.id == id and not n.item.destination:
                n.item.departDate = date
                n.item.destination = destination
                n.item.address = address
                if "WA" in n.item.id:
                    row = [n.item.id, n.item.type, n.item.vaccinated, n.item.reason, n.item.arriveDate, \
                           n.item.departDate, n.item.destination, n.item.address]
                    break
                if "P" in n.item.id:
                    row = [n.item.id, n.item.type, n.item.breed, n.item.vaccinated, n.item.neutered, \
                           n.item.microchip, n.item.reason, n.item.arriveDate, n.item.departDate, n.item.destination,
                           n.item.address]
                    break
            row_index += 1
            n = n.nref
        print(row)  # for debugging purposes
        print(row_index)  # for debugging purposes
        if "P" in n.item.id:
            with open('pets.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines[row_index] = row
            with open('pets.csv', 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
            readFile.close()
            writeFile.close()
        if "WA" in n.item.id:
            with open('wildanimals.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines[row_index] = row
            with open('wildanimals.csv', 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
            readFile.close()
            writeFile.close()


# MAIN CLASS
# create the blank lists
wildanimals = DoublyLinkedList()
pets = DoublyLinkedList()
treatment = DoublyLinkedList()

# read the entries from the csv file to make a linked list
wildanimals.initListWA()
pets.initListPet()
treatment.initListTreatment()

# other linked lists
abuser = DoublyLinkedList()  # list of abusers
abandoner = DoublyLinkedList()  # list of abandoners
returner = DoublyLinkedList()  # list of pets ready to be returned to owner

while True: #main program loop
    ans = input("""
    What would you like to do? 
    1. Create a new entry
    2. Find data about an animal
    3. Generate a kind of list (Choose specific later)
    4. Edit/Enter new data
    5. Exit\n
    """)
    if ans == "1":
        ans = input("""
        Do you want to add a new entry for wild animal or pet?
        1. Wild animal
        2. Pet
        """)
        if ans == "1":
            wildanimals.addNewEntryWA()
        if ans == "2":
            pets.addNewEntryPet()
    elif ans == "2":
        ans = input("Type in the Pet/Wild Animal ID you want to look for:")
        if "WA" in ans:
            result = wildanimals.searchbyID(ans)
            print(result.print_all, " ")
        if "P" in ans:
            result = pets.searchbyID(ans)
            print(result.print_all, " ")
    elif ans == "3":
        print("""
            1. List of animal abuser
            2. List of animal abandoner
            3. List of cats ready for adoption
            4. List of dogs ready for adoption
            5. List of animals ready for return to owner
            """)
        ans = input(" ")
        if ans == "3":
            pets.generateList('Cat')
        elif ans == "4":
            pets.generateList('Dog')
        elif ans == "1":
            treatment.generateList('Abuse')
        elif ans == "2":
            treatment.generateList('Abandon')
        elif ans == "5":
            wildanimals.generateList('ReturnWA')
            pets.generateList('ReturnPet')
            returner.sortNodes()
            returner.traverse()
    elif ans == "4":
        print("""
        1. Enter details of surgery
        2. Enter details of neutering
        3. Enter microchip number
        4. Edit departure status (Date, Destination, Address)
        5. Edit details of Abuser
        6. Edit details of Abandoner
        """)
        ans = input(" ")
        if ans == "1":
            id = input("Enter the ID of the pet/wild animal you want to enter surgery details: ")
            surgeryType = input("Enter the name of the surgery: ")
            surgeryDate = input("Enter the date of surgery: ")
            treatment.enterSurgery(id, surgeryType, surgeryDate)
        elif ans == "2":
            id = input("Enter the ID of the pet you want to enter neuteuring details: ")
            statusNeuteur = input("Enter the status of neuteuring: ")
            pets.enterNeuteuring(id, statusNeuteur)
        elif ans == "3":
            id = input("Enter the ID of the pet you want to enter microchip details: ")
            microchipID = input("Enter microchip ID: ")
            pets.enterMicrochip(id, microchipID)
        elif ans == "4":
            id = input("Enter the ID of the pet/wild animal you want to edit the status: ")
            date = input("Enter the date of departure: ")
            desti = input("Enter destination designated: ")
            addr = input("Enter the destination address: ")
            if "WA" in id:
                wildanimals.editDeparture(id, date, desti, addr)
            if "P" in id:
                pets.editDeparture(id, date, desti, addr)
        elif ans == "5":
            id = input("ID of the wild animal/pet: ")
            name = input("Enter name of abuser: ")
            treatment.editAbuser(id,name)
        elif ans == "6":
            id = input("ID of the wild animal/pet: ")
            name = input("Enter name of abandoner: ")
            treatment.editAbandoner(id,name)


    elif ans == "5":
        print("\n Goodbye")
        exit()
    elif ans != "":
        print("\n Not Valid Choice. Try again")

