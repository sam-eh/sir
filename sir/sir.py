from random import randint
import matplotlib.pyplot as plt
from population import Population

"""main file for attempting to simulate a SIR curve"""

# for each population on each day:
#        simulate those infected showing symptoms and quarantining themselves
#        simulate infecting of pop by active infected persons
#        report out the SIR numbers

days = 30
day = 1
# just running this for a single population; eventually could benefit from simulating populations where individuals travel between
my_pop = Population()
# choose 3 people to infect initially
initial_infect = my_pop.get_susceptiblePersons()[0:2]
for person in initial_infect:
    person.infected(day)
day_results = []
day_results.append(my_pop.get_numTypes())
while day <= days:
    print(f"-----\nday: {day}")
    my_pop.infect_pop(day)
    my_pop.quarantine_pop(day)
    my_pop.recover_pop(day)
    day_results.append(my_pop.get_numTypes())
    # print(f"\n{my_pop}")
    day += 1

susceptible, infected, recovered = [], [], []
for result in day_results:
    susceptible.append(result["s"])
    infected.append(result["i"])
    recovered.append(result["r"])

days_list = [i for i in range(0,days+1)]

fig, ax = plt.subplots(figsize=(14,7))
s = ax.scatter(days_list, susceptible, c="blue")
i = ax.scatter(days_list, infected, c="red")
r = ax.scatter(days_list, recovered, c="green")
ax.set_title(f"Simulation of Population Infection/Recovery Over {days} Days")
ax.get_xaxis().set_label("Day")
ax.get_yaxis().set_label("Population Count")
ax.legend((s, i, r), ('Susceptible', 'Infected', 'Recovered'))
plt.show()