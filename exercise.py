import pandas

##exercise class
class Exercise():
    def __init__(self, name, muscle):
        self.name = name
        self.muscle = muscle

##workout class  
class Workout():
    def __init__(self, list_of_exercises):
        self.list_of_exercises = list_of_exercises
    
    def create_workout(quiz_responses_tuple=None):
        exerciseData = pandas.read_csv('exercise_database.csv')
        print(exerciseData['exercise'])
        return None
    
    def sortDataByMuscle(dataframe, muscle_group):
        df = dataframe[dataframe['muscle'] == muscle_group]
        return df
    
    def sortDataDifficulty(dataframe, difficulty):
        df = dataframe[dataframe['difficulty'] == difficulty]
        return df
    def pickRandomWorkout(dataframe, muscle_group, difficulty):
        sortedOnce = Workout.sortDataByMuscle(dataframe, muscle_group)
        sortedTwice = Workout.sortDataDifficulty(sortedOnce, difficulty)

        random_row = sortedTwice.sample(n=1)
        name = random_row['exercise']
        muscle = random_row['muscle']
        
        item = Exercise(name, muscle)

        print("{} {}".format(item.name, item.muscle))
        
        



## testing section
ex1 = Exercise("bench press", "chest")
ex2 = Exercise("pull up", "back")
ex3 = Exercise("bicep curl", "bicep")

exList = [ex1, ex2, ex3]

newWorkout = Workout(exList)

for item in newWorkout.list_of_exercises:
    print("{} {}".format(item.name, item.muscle))

df = pandas.read_csv('exercise_database.csv')
Workout.create_workout()
Workout.pickRandomWorkout(df, "chest", "beginner")

