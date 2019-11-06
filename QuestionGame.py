'#Imports Random Function to mix up the questions'
from random import shuffle
'#Our questions for the trivia game'
questions = [{"question": "What was mario's profession?",
              "answer": ["Lumberjack",
                         "Plumber",
                         "Pizza Delivery Man",
                         "Teacher"],
              "correct": 1},
             {"question": "Who is the main character of Assassin's Creed?",
              "answer": ["Lucy",
                          "Michael",
                          "Steve",
                          "Desmond",
                          "Jon"],
              "correct": 3},
             {"question": "How many ghosts are in Pacman?",
              "answer": ["1",
                         "2",
                         "3",
                         "4"],
              "correct": 3},
             {"question": "Who is the main character of Far Cry 3?",
              "answer": ["Kevin",
                          "Joann",
                          "Ronaldo",
                          "Jason"],
              "correct": 3},
             {"question": "Who is the best team in NBA 2k17?",
              "answer": ["Lakers",
                          "Bulls",
                          "Cavaliers",
                          "Warriors"],
              "correct": 3},
             {"question": "What animal is the main enemy in Donkey Kong?",
              "answer": ["cat",
                          "bunny",
                          "gorilla",
                          "horse"],
              "correct": 2},
             {"question": "What is the cat race called in Skyrim?",
              "answer": ["Khajit",
                          "Highlander Elf",
                          "Lizard Dragon",
                          "Human"],
              "correct": 0},
             {"question": "Who is Mario's brother?",
              "answer": ["Bowser",
                          "Luigi",
                          "Wario",
                          "Peach"],
              "correct": 1},
             {"question": "where did the endermen come from?",
              "answer": ["The Nether",
                          "The Forest",
                          "The Ocean",
                          "The desert"],
              "correct": 0},
             {"question": "How many lives do you get in Pacman?",
              "answer": ["1",
                          "2",
                          "3",
                          "4"],
              "correct": 2}]

'#The function in which everything is run through'


def main():
    print("Welcome to The Game Game Show!")
    print("Win Money and a NEW CAR!")
    main_menu()

'#The function that the actual game is run through'


def play_game():
    shuffle(questions)
    answer_correct = 0
    questions_given = 0
    '#The range for the amount of questions there are'
    for i in range(0, 10):
        print(questions[i]["question"], questions[i]["answer"])
        user_answer = input()
        '#Conditional statement for whether the question is right or wrong'
        if user_answer == questions[i]["answer"][questions[i]["correct"]]:
            print("Good Job! You got it right.")
            answer_correct += 1
        else:
            print("Oops! Wrong answer. Try again")
        questions_given += 1
        '#Prints out there score at the given time'
        print("Your score is", answer_correct, "out of ", questions_given)

'#Function in which the game credits are held'


def view_credits():
    print("Creators: Miguel Villareal and Jonathan Hillman\n\
          Sponsors: Game Inc. and Lets Go Studios\n\
          Date made: October 18th 2017.")

'#This function is for the main menu of our game'


def main_menu():
    option = input("Pick to PLAY game, VIEW game credits, or QUIT").lower()
    '#While loop so that once game is over it restarts'
    while (option == "play" or option == "view"):
        if option == "play":
            play_game()
        if option == "view":
            view_credits()
        option = input("pick to PLAY game, VIEW game credits, or QUIT").lower()
    '#If user chooses to quit the game will loop to menu'
    if option == "quit":
        print("Thanks for playing!")
    else:
        print("Please enter, PLAY, VIEW, or QUIT")
        main_menu()

main()
