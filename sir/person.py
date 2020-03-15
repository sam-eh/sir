from virus import Virus, Covid19

class Person(object):
    """base class for a person"""

    def __init__(self):
        """set parameters for what we would expect from an individual
            type indicates:
                s: susceptible
                i: infectious
                r: recovered"""
        self.type = "s" 
        self.quarantined = False
        self.dayOfInfect = None
        self.virus = None

    def __str__(self):
        return f"\ntype:{self.type} | quarantined: {self.quarantined} | day infected: {self.dayOfInfect} | virus: {self.virus}"

    def get_type(self):
        return self.type
   
    def get_quarantined(self):
        return self.quarantined

    def get_dayOfInfect(self):
        return self.dayOfInfect

    def get_virus(self):
        return self.virus

    def reset(self):
        self.type = "s"
        self.quarantined = False
        self.dayOfInfect = None
        self.virus = None

    def infect(self):
        """returns the virus to infect if the individual is not quarantined and is infected"""
        if (self.type == "i") & (self.quarantined == False):
            return self.virus
        else:
            return None

    def infected(self, day, virus=Covid19):
        if self.type == "s":
            self.type = "i"
            self.dayOfInfect = day
            self.virus = virus()

    def quarantine(self, day):
        if (self.type == "i") & (self.quarantined == False):
            if self.virus.symptomatic(day - self.get_dayOfInfect()):
                self.quarantined = True

    def recover(self, day):
        if self.type == "i":
            if self.virus.recovered(day - self.get_dayOfInfect()):
                self.type = "r"