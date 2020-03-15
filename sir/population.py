from person import Person
from virus import Virus, Covid19

class Population(object):
    """population represnts a grouping of person records"""
    def __init__(self, pop_size=10000):
        self.pop = [Person() for i in range(0,pop_size)]

    def __str__(self):
        summary = self.get_numTypes()
        return f"susceptible: {summary['s']}\ninfected: {summary['i']}\nrecovered: {summary['r']}"

    def get_numTypes(self):
        ret = {"s": 0, "i": 0, "r": 0}
        for person in self.pop:
            person_type = person.get_type()
            if person_type == "s":
                ret["s"] += 1
            elif person_type == "i":
                ret["i"] += 1
            elif person_type == "r":
                ret["r"] += 1
        return ret
    
    def get_infectedPersons(self):
        """returns a list of infected persons objects in the population"""
        infected_persons = list()
        for person in self.pop:
            if person.get_type() == "i":
                infected_persons.append(person)
        return infected_persons

    def get_susceptiblePersons(self):
        """returns a list of susceptible persons objects in the population"""
        susceptible_persons = list()
        for person in self.pop:
            if person.get_type() == "s":
                susceptible_persons.append(person)
        return susceptible_persons

    def get_recoveredPersons(self):
        """returns a list of susceptible persons objects in the population"""
        recovered_persons = list()
        for person in self.pop:
            if person.get_type() == "r":
                recovered_persons.append(person)
        return recovered_persons
    
    def get_activeInfectedPersons(self):
        """returns a list of persons objects who are infected and have not quarantined themselves"""
        activeInfected_persons = list()
        for person in self.pop:
            if (person.get_type() == "i") & (person.get_quarantined() == False):
                activeInfected_persons.append(person)
        return activeInfected_persons

    def infect_pop(self, day):
        """simulates infecting of a population based on virus carried by individual persons records"""
        active_infected = self.get_activeInfectedPersons()
        susceptible_persons = self.get_susceptiblePersons()
        for carrier in active_infected:
            virus = carrier.infect()
            try:
                current_susceptible = len(susceptible_persons)
                num_infected = min(virus.infect(current_susceptible), current_susceptible)
            except AttributeError:
                # somehow the infected person does not have a virus attribute set; we need to change this person record to be more accurate
                carrier.reset()
            else:
                num_removed = 0
                while num_removed < num_infected:
                    person_infected = susceptible_persons.pop()
                    person_infected.infected(day, type(virus))
                    num_removed += 1
            if len(susceptible_persons) == 0:
                return
    
    def quarantine_pop(self, day):
        """simulates active carriers becoming symptomatic and quarantining themselves to prevent infecting others"""
        active_infected = self.get_activeInfectedPersons()
        if len(active_infected) == 0:
            print("no carriers are actively infected")
            return
        for carrier in active_infected:
            carrier.quarantine(day)

    def recover_pop(self, day):
        """simulates infected people recovering (and becoming no longer infectious)"""
        infected = self.get_infectedPersons()
        if len(infected) == 0:
            print("no population members are infected")
            return
        for carrier in infected:
            carrier.recover(day)