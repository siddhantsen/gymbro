import quiz, exercise
from quiz import *
from exercise import *

def main():
    response_tuple = do_quiz()
    df = pandas.read_csv('exercise_database.csv')
    newWorkout = Workout()
    parameters = Workout.get_parameters(response_tuple)
    newWorkout.create_workout(df, parameters)
    for item in newWorkout.list_of_exercises:
        print("{} {}".format(item.name, item.muscle))



if __name__ == "__main__":
    main()
