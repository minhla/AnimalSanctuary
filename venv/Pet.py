class Pet:
    def __init__(self, id, type, breed, vaccinated, neutered, microchip, reason, arriveDate, departDate, destination, address):
        self.id = id
        self.type = type
        self.breed = breed
        self.vaccinated = vaccinated
        self.neutered = neutered
        self.microchip = microchip
        self.reason = reason
        self.arriveDate = arriveDate
        self.departDate = departDate
        self.destination = destination
        self.address = address
        self.print_all = id + "," + type + "," + breed +","+ vaccinated +","+ neutered +","+ microchip + "," +reason+","+ arriveDate + "," + departDate \
                                                + "," + destination + "," + address
        self.print_once = "Sanctuary Identification: "+ id + "," +" Type: "+ type + "," " Breed: "+ breed + "," +" Vaccinated: "+ vaccinated + "," +" Neuteured: "+\
                          neutered + "," +" Microchip: "+ microchip + "," +" Reason for Admission: "+ reason+ ", "+"Date of Admission: "+arriveDate + "," +\
                          "Date of Departure: "+departDate + "," +"Destination: "+ destination + "," +"Destination Adddress: "+ address