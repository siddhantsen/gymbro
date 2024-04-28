import exercise, quiz
from quiz import do_quiz
from exercise import Exercise, Workout


def main():
    emptyList = []
    newWorkout = Workout(emptyList)
    response_tuple = do_quiz()
    
    parameters = newWorkout.get_parameters(response_tuple)
    l = newWorkout.create_workout(newWorkout, parameters)
    
    

if (__name__ == "main"):
    main()

