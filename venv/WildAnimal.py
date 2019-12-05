class WildAnimal:
    def __init__(self, id, type, vaccinated, reason, arriveDate, departDate, destination, address):
        self.id = id
        self.type = type
        self.vaccinated = vaccinated
        self.reason = reason
        self.arriveDate = arriveDate
        self.departDate = departDate
        self.destination = destination
        self.address = address
        self.print_once = "Sanctuary Identification: "+ id +", "+"Type: "+ type +","+" Vaccinated: "+ vaccinated +","+" Reason for Admission: "+ reason \
                         +","+" Date of Arrival: "+ arriveDate +","+" Date of Departure: "+ departDate +","+" Destination: "+ destination \
                         +","+" Destination Address"+ address
        self.print_all = id + ", " + type + "," + vaccinated + ","+ reason \
                          + "," + arriveDate + "," + departDate + "," + destination \
                          + "," + address