import quiz, exercise, weight_loss_plan
from quiz import *
from exercise import *
from weight_loss_plan import *



def startDecision():
    decision = input("Would you like to plan a workout or get weight loss tips.\n\ta. workout\n\tb. weight loss\n")
    return True, decision

def endDecision():
    decision = input("Would you like to go back to the beginning or end the program.\n\ta. Go back\n\tb. end program\n")
    if decision=="a":
        return True
    else:
        return False
def main():
    go = True
    while (go == True):
        go, decision = startDecision()
        if decision == "a":

            response_tuple = do_quiz()
            df = pandas.read_csv('exercise_database.csv')
            newWorkout = Workout()
            parameters = Workout.get_parameters(response_tuple)
            newWorkout.create_workout(df, parameters)
            for i, item in enumerate (newWorkout.list_of_exercises, start=1):
                print("{}. {} for {}".format(i, item.name, item.muscle))
            go = endDecision()
        else:
            print("weight loss stuff here")
            response = weight_quiz()
            generate_plan(response)
            go = endDecision()




if __name__ == "__main__":
    main()
