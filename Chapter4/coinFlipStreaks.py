# Chapter 4 Coin Flip Streaks

import random

numberOfStreaks = 0
streaksPerExperiment = []
streakAverage = 0.0
howManyExperiments = 10000
for experimentNumber in range(howManyExperiments):
    # Code for list
    streak = 1
    experiment = []
    for i in range(100):
        experiment.append(str(random.randint(0, 1)))
    # print(experiment)
    # Code that checks streak
    for item in range(len(experiment)):
        if experiment[item - 1] == experiment[item]:
            streak += 1
        elif experiment[item - 1] != experiment[item]:
            streak = 1
        if streak == 6:
            numberOfStreaks += 1
            streak = 1
    streaksPerExperiment.append(numberOfStreaks / 100)
    numberOfStreaks = 0

for index, item in enumerate(streaksPerExperiment):
    #    print(
    #        "Experiment "
    #        + str(index + 1)
    #        + " the percentage of 6 flip streaks was: "
    #        + str(item * 100.0)
    #        + "%"
    #    )
    streakAverage += item
streakAverage = (streakAverage / howManyExperiments) * 100
print(
    "The average percentage of 6 flips streak from these"
    + str(howManyExperiments)
    + " experiments is... "
)
print(str(streakAverage) + "%")
