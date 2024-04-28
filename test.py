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


## testing workout stuffsection

exList = []
newWorkout = Workout()

for item in newWorkout.list_of_exercises:
    print("{} {}".format(item.name, item.muscle))


df = pandas.read_csv('exercise_database.csv')
responses = ('a', 'a', 'a', 'a', 'a')
parameters = Workout.get_parameters(responses)
newWorkout.create_workout(df, parameters)


