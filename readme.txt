1. Brief description
I want to make a workout tool that has a vast database of different exercises and muscle groups.
The user is able to upload their workouts and the program will make suggestions to improve the workout. 
Further, the program can design workouts using the responses to a simple 3-5 question quiz that outlines the user's goals, lifestyle, and experience.

2. Function description
    1. Create workout Function 
        - Program asks the user a few questions that it uses to design a workout.
        - program will use a large database of exercises to combine them into the ideal workout. 
        - potentially will use AI learning model to find patterns in existing workouts. 
    2. Workout suggestions
        - In the program there exists the Workout class which has exercise attributes
        - The suggestion function will take a workout object as an input and use a trained model to make reccomendations on the workout
    3. Workout quiz
        - questions will be asked to the user like years of lifting experience, time commitment, and goals (weight loss/gain)
        - will pass the results to the create workout function
