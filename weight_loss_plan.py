def weight_quiz():
    current_weight = int(input("What is your current weight in pounds:\n"))
    height = int(input("What is your height in inches:\n"))
    age = int(input("What is your age:\n"))
    exercise_level = input("What is your exercise level:\n\ta. sedentary\n\tb. lightly active (exercise 2-3 times per week)\n\tc. moderately active (exercise 4-5 times per week)\n\td. very active (exercise 6-7 times per week)")
    goal_weight = int(input("What is your goal weight in pounds: \n"))
    timeline = int(input("In how many weeks do you want to lose this weight:\n"))
    response_tuple = (current_weight, height, age, exercise_level, goal_weight, timeline)
    return response_tuple

    
def get_basal_metabolic_rate(response_tuple):
    current_weight, height, age, exercise_level, goal_weight, timeline = response_tuple
    basal_metabolic_rate = ((9.99 * current_weight) / 2.212) + (6.25 * height * 2.5) - (4.92 * age) + 5
    basal_metabolic_rate = round(basal_metabolic_rate, 1)
    return basal_metabolic_rate

def get_calories_burned_through_activity(response_tuple):
    additional_cals = 0
    current_weight, height, age, exercise_level, goal_weight, timeline = response_tuple
    if (exercise_level == "a"):
        additional_cals = 300
    elif (exercise_level == "b"):
        additional_cals = 500
    elif (exercise_level == "c"):
        additional_cals = 700
    elif (exercise_level == "d"):
        additional_cals = 1000
    return additional_cals

def generate_plan(response_tuple):
    current_weight, height, age, exercise_level, goal_weight, timeline = response_tuple
    total_burned = get_calories_burned_through_activity(response_tuple) + get_basal_metabolic_rate(response_tuple)
    weight_difference = current_weight - goal_weight
    total_deficit = weight_difference * 3500
    daily = round(total_deficit / (timeline*7), 2)
    daily_eat = round((total_burned - daily), 2)
    print("In order to lose {} pounds in {} weeks, we recommend eating at a daily {} calorie deficit".format(weight_difference, timeline, daily))
    print("This means that at your calculated burn rate of {}, you should eat {} calories per day".format(total_burned, daily_eat))
    

    



