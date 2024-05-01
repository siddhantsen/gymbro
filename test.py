import quiz, exercise, weight_loss_plan
from quiz import *
from exercise import *
from weight_loss_plan import *


"""
The test file will contain sample inputs for the quiz file. 
It will call the functions in the same order that the final production will. 
It will also include the same returned print statements with the information for the user. 

"""

## This first section will test the workout generation ##
### Importing/Reading the Database ###
df = pandas.read_csv('exercise_database.csv')
### Testing the create_workout_plan function ###

## list of test_tuples containing sample answers to the quiz
list_of_test_tuples = [
    ("a", "d", "c", "d", "b"), ### should give a legs and arms workout that has 8 exercises
    ("b", "a", "c", "b", "a"), ### should give a legs and back workout that has 4 exercises
    ("d", "b", "b", "a", "c"), ### should give a chest and back workout that has 6 exercises
]

### testing the functions to get a workout ###
for i, tup in enumerate(list_of_test_tuples, start=1):
    newWorkout = Workout()
    parameters = Workout.get_parameters(tup)
    newWorkout.create_workout(df, parameters)
    print("Test workout #{}\n".format(i))
    for j, item in enumerate (newWorkout.list_of_exercises, start=1):
        print("{}. {} for {}".format(j, item.name, item.muscle))
    print("\n")

print("-----------------------------------\n")
## This next section will test the weight_loss_plan generation
## list of test tuples containing sample answers to weight_loss_quiz ##
list_of_test_tuples_2 = [
    (125, 63, 19, "c", 119, 4), ## lose 6 pounds in 4 weeks
    (150, 70, 22, "b", 130, 10), ## lose 20 pounds in 10 weeks
    (200, 74, 30, "d", 190, 6), ## lose 10 pounds in 6 weeks
    
]

for i, tup in enumerate(list_of_test_tuples_2, start=1):
    print("Test Diet Plan #{}\n".format(i))
    generate_plan(tup)
    print("\n")

