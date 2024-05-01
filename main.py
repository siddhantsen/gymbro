import quiz, exercise, weight_loss_plan
from quiz import *
from exercise import *
from weight_loss_plan import *
import time


def startSequence():
    print("You will be prompted with a series of questions. To answer, simply type your response and press enter.")
    time.sleep(2)
    print("For multiple choice questions, simply type the lowercase letter response and press enter.")
    time.sleep(2)
    print("In multiple choice questions, only the answer choices listed will be accepted. If there are a-d choices, 'e' will not be accepted.")
    time.sleep(2)
    print("For numbered answer questions, which will be indicated, simply type your integer answer and press enter.")
    time.sleep(2)
    print("Before beginning, we will practice these instructions.")
    time.sleep(2)

    ## practice question 1
    response_validity = False

    while (response_validity == False):
        acceptable = ['a', 'b', 'c', 'd']
        multi_choice_practice = input("What color is grass?\n\ta. blue\n\tb. green\n\tc. red\n\td. purple\n")
        if (multi_choice_practice in acceptable):
            response_validity = True
            break
        print("************************\nInvalid input. Try again\n************************")

    ## practice question 2
    response_validity = False

    while (response_validity == False):
        
        number_practice = int(input("Enter a number between 1 and 10,000:\n"))

        if (number_practice > 0 and number_practice <= 10000):
            response_validity = True
            break
        print("************************\nInvalid input. Try again\n************************")

    print("Great job! You've got the hang of it! We'll begin now. Enjoy!")
    

    
    

    


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
    startSequence()
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
    
            response = weight_quiz()
            generate_plan(response)
            go = endDecision()




if __name__ == "__main__":
    main()
