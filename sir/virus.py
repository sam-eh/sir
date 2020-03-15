"""This files provides a simple representation of the probability of recovering from a virus in discrete number of days"""
import numpy.random as npr

class Virus(object):
    """disease object to model number of days infectitious without symptoms and number of days to recover"""
    def __init__(self, p_recover, p_symptoms, p_infect, name="generic"):
        self.p_recover = p_recover
        self.p_symptoms = p_symptoms
        self.p_infect = p_infect
        self.name = name
    
    def __str__(self):
        return self.name

    def recovered(self, days):
        if npr.binomial(days, self.p_recover) >= 1:
            return True
        else:
            return False

    def symptomatic(self, days):
        if npr.binomial(days, self.p_symptoms) >= 1:
            return True
        else:
            return False

    def infect(self, susceptible):
        return npr.binomial(susceptible, self.p_infect)

class Covid19(Virus):
    def __init__(self):
        super().__init__(p_recover=0.05, p_symptoms=0.1, p_infect=0.0002, name="COVID-19")