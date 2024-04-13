def quiz():
    goal = input("What is the goal of this workout?\n\ta. Get stronger\n\tb. Lose weight\n\tc. Athleticism\n\td. Overall Health\n")
    time = input("How much time can you commit to the workout?\n\ta. <30 min\n\tb. 30-60 min\n\tc. 1-2 hours\n\td. >2 hours\n")
    primary_muscle = input("What primary muscle group do you want to target?\n\ta. Chest\n\tb. Back\n\tc. Legs\n\td. Arms\n\te. Core\n\tf. Whole body\n")
    secondary_muscle = input("What secondary muscle group do you want to target\n\ta. Chest\n\tb. Back\n\tc. Legs\n\td. Arms\n\te. Core\n\tf. Whole body\n")
    experience = input("What is your experience level with working out?\n\ta. Beginner\n\tb. Intermediate\n\tc. Advanced\n")
    return goal, time, primary_muscle, secondary_muscle, experience

g, t, p, s, e = quiz()
print("{}{}{}{}{}".format(g,t,p,s,e))

