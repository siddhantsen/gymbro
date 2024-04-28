import quiz, exercise
from quiz import *
from exercise import *
"""
The test file will contain sample inputs for the quiz file. 
It will call the functions in the same order that the final production will. 
It will also include the same returned print statements with the information for the user. 

"""



##testing quiz
response_tuple = do_quiz()
print(response_tuple)


## testing workout stuff section

exList = []
newWorkout = Workout()



df = pandas.read_csv('exercise_database.csv')

parameters = Workout.get_parameters(response_tuple)
newWorkout.create_workout(df, parameters)
for item in newWorkout.list_of_exercises:
    print("{} {}".format(item.name, item.muscle))

print("**********************")
## sample for test
workout2 = Workout()
sample_response = ('a', 'b', 'c', 'd', 'b')
sample_parameters = Workout.get_parameters(sample_response)
workout2.create_workout(df, sample_parameters)
for ex in workout2.list_of_exercises:
    print("{} {}".format(ex.name, ex.muscle))


