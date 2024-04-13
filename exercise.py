##exercise class
class Exercise():
    def __init__(self, name, muscle):
        self.name = name
        self.muscle = muscle

##workout class  
class Workout():
    def __init__(self, list_of_exercises):
        self.list_of_exercises = list_of_exercises
    
    def create_workout(quiz_responses_tuple):
        return None



## testing section
ex1 = Exercise("bench press", "chest")
ex2 = Exercise("pull up", "back")
ex3 = Exercise("bicep curl", "bicep")

exList = [ex1, ex2, ex3]

newWorkout = Workout(exList)

for item in newWorkout.list_of_exercises:
    print("{} {}".format(item.name, item.muscle))

