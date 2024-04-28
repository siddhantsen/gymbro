import pandas

##exercise class
class Exercise():
    def __init__(self, name, muscle):
        self.name = name
        self.muscle = muscle

##workout class  
class Workout():
    def __init__(self):
        self.list_of_exercises = []
    def get_parameters(quiz_responses_tuple):
        ## setting the size of the workout based on the response
        if (quiz_responses_tuple[1] == 'a'):
            size = 5
        elif (quiz_responses_tuple[1] == 'b'):
            size = 6

        elif (quiz_responses_tuple[1] == 'c'):
            size = 7

        elif (quiz_responses_tuple[1] == 'd'):
            size = 8

        ## setting the primary muscle group of the workout
        if (quiz_responses_tuple[2] == 'a'):
            primary_muscle = "chest"
        elif (quiz_responses_tuple[2] == 'b'):
            primary_muscle = "back"

        elif (quiz_responses_tuple[2] == 'c'):
            primary_muscle = "leg"

        elif (quiz_responses_tuple[2] == 'd'):
            primary_muscle = "arms"

        ## setting the secondary muscle group of the workout
        if (quiz_responses_tuple[3] == 'a'):
            secondary_muscle = "chest"
        elif (quiz_responses_tuple[3] == 'b'):
            secondary_muscle = "back"

        elif (quiz_responses_tuple[3] == 'c'):
            secondary_muscle = "leg"

        elif (quiz_responses_tuple[3] == 'd'):
            secondary_muscle = "arms"

        ## set difficulty
        if (quiz_responses_tuple[4] == 'a'):
            difficulty = 0
        elif (quiz_responses_tuple[4] == 'b'):
            difficulty = 1

        elif (quiz_responses_tuple[4] == 'c'):
            difficulty = 2
        
        parameters = (size, primary_muscle, secondary_muscle, difficulty)
        return parameters

       

    def create_workout(self, df, parameters):
        
        exerciseData = pandas.read_csv('exercise_database.csv')
        size = int(parameters[0])
        primary_muscle = parameters[1]
        secondary_muscle = parameters[2]
        difficulty = parameters[3]
        for i in range (size//2):
            item = Workout.pickRandomWorkout(exerciseData, primary_muscle, difficulty)
            self.list_of_exercises.append(item)

        for i in range (size//2):
            item = Workout.pickRandomWorkout(exerciseData, secondary_muscle, difficulty)
            self.list_of_exercises.append(item)

        
        return self.list_of_exercises
    
    
    def sortDataByMuscle(dataframe, muscle_group):
        df = dataframe[dataframe['muscle'] == muscle_group]
        return df
    

    def sortDataDifficulty(dataframe, difficulty):
        dataframe['difficulty'] = dataframe['difficulty'].astype(int)
        df = dataframe[dataframe['difficulty'] <= difficulty]
        return df
    

    def sortData(dataframe, muscle_group, difficulty):
        sortedOnce = Workout.sortDataByMuscle(dataframe, muscle_group)
        sortedTwice = Workout.sortDataDifficulty(sortedOnce, difficulty)
        
        return sortedTwice

        
    def pickRandomWorkout(dataframe, muscle_group, difficulty):
        sorted = Workout.sortData(dataframe, muscle_group, difficulty)

        random_row = sorted.sample(n=1)
        name = random_row['exercise']
        muscle = random_row['muscle']
        
        random_row_list = random_row.values.tolist()
        
        name = random_row_list[0][0]
        muscle = random_row_list[0][1]
        item = Exercise(name, muscle)
        return item
        
        
        



