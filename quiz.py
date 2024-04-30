def do_quiz():
    ## question 1
    response_validity = False

    while (response_validity == False):
        acceptable = ['a', 'b', 'c', 'd']
        goal = input("What is the goal of this workout?\n\ta. Get stronger\n\tb. Lose weight\n\tc. Athleticism\n\td. Overall Health\n")
        if (goal in acceptable):
            response_validity = True
            break
        print("************************\nInvalid input. Try again\n************************")

    ## question 2
    response_validity = False

    while (response_validity == False):
        acceptable = ['a', 'b', 'c', 'd']
        time = input("How much time can you commit to the workout?\n\ta. <30 min\n\tb. 30-60 min\n\tc. 1-2 hours\n\td. >2 hours\n")
        if (time in acceptable):
            response_validity = True
            break
        print("************************\nInvalid input. Try again\n************************")
        

    ## question 3
    response_validity = False

    while (response_validity == False):
        acceptable = ['a', 'b', 'c', 'd']
        primary_muscle = input("What primary muscle group do you want to target?\n\ta. Chest\n\tb. Back\n\tc. Legs\n\td. Arms\n")
        if (primary_muscle in acceptable):
            response_validity = True
            break
        print("************************\nInvalid input. Try again\n************************")

    ## question 4
    response_validity = False

    while (response_validity == False):
        acceptable = ['a', 'b', 'c', 'd']
        secondary_muscle = input("What secondary muscle group do you want to target\n\ta. Chest\n\tb. Back\n\tc. Legs\n\td. Arms\n")
        if (secondary_muscle in acceptable):
            response_validity = True
            break
        print("************************\nInvalid input. Try again\n************************")

    ## question 5
    response_validity = False

    while (response_validity == False):
        acceptable = ['a', 'b', 'c']
        experience = input("What is your experience level with working out?\n\ta. Beginner\n\tb. Intermediate\n\tc. Advanced\n")
        if (experience in acceptable):
            response_validity = True
            break
        print("************************\nInvalid input. Try again\n************************")
        

    
    response_tuple = (goal, time, primary_muscle, secondary_muscle, experience)
    return response_tuple



