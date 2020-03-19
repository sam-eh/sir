from random import randint
import matplotlib.pyplot as plt
from population import Population

"""main file for attempting to simulate a SIR curve"""

# for each population on each day:
#        simulate those infected showing symptoms and quarantining themselves
#        simulate infecting of pop by active infected persons
#        report out the SIR numbers
day = 1
my_pop = Population()
# choose 3 people to infect initially
initial_infect = my_pop.get_susceptiblePersons()[0:2]
for person in initial_infect:
    person.infected(day)

day_results = {"s":[], "i":[], "r":[]}
result = my_pop.get_numTypes()
day_results["s"].append(result["s"])
day_results["i"].append(result["i"])
day_results["r"].append(result["r"])

days_list = [0]
day_countdown = 5

while True:
    while day_countdown > 0:
        print(f"-----\nday: {day}")
        my_pop.infect_pop(day)
        my_pop.quarantine_pop(day)
        my_pop.recover_pop(day)
        result = my_pop.get_numTypes()
        day_results["s"].append(result["s"])
        day_results["i"].append(result["i"])
        day_results["r"].append(result["r"])
        days_list.append(day)
        day += 1
        day_countdown -= 1

    # plot current item
    fig, ax = plt.subplots(figsize=(14,7))
    s = ax.scatter(days_list, day_results["s"], c="blue")
    i = ax.scatter(days_list, day_results["i"], c="red")
    r = ax.scatter(days_list, day_results["r"], c="green")
    ax.set_title(f"Simulation of Population Infection/Recovery Over {day} Days")
    ax.get_xaxis().set_label("Day")
    ax.get_yaxis().set_label("Population Count")
    ax.legend((s, i, r), ('Susceptible', 'Infected', 'Recovered'))
    plt.show()

    # assess if should continue with simulation
    keep_going = input("Continue with 5 next days of simulation? y/n\n")
    if keep_going == "n":
        break;
    else:
        day_countdown = 5