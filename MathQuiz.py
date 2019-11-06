# Math Quiz
#Miguel Villareal
#9-20-17
#002



'#This variable asks the user what level they'
'#would like to do.( beginner, intermediate, or advanced)'
choice = input("What level would you like your quiz \n\
to be(beginner, intermediate, or advanced): ")
'#This function is used if the user picks the beginner level.'
if choice == "beginner":
    '#This import function imports the random function.'
    from random import randint
    questions = int(input("How many questions would you like: "))
    correct = 0
    for i in range (questions):
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        prod = n1 + n2

        ans = input("What is %d plus %d? " % (n1, n2))
        '#this function occurs if the user answers the problem correct.'
        if int(ans) == prod:
            print(" That is correct! \n")
            correct = correct + 1
        else:
            print("Sorry, the answer is %d.\n " % prod)

        n3 = randint(1, 10)
        n4 = randint(1, 10)
        subt = n3 - n4

        ans = input("What is %d minus %d? " % (n3, n4))
        '#this function occurs if the user answers the problem correct.'
        if int(ans) == subt:
            print(" That is correct! \n")
            correct = correct + 1
        else:
            print ("Sorry, the answer is %d . \n " % subt)

    print("\nI asked you" ' questions ' " questions.\n\
You got %d of them right." % correct)
elif choice == "intermediate":
    '#This import function imports the random function.'
    from random import randint
    questions = int(input("How many questions would you like: "))
    correct = 0
    for i in range(questions):
        n1 = randint(1, 25)
        n2 = randint(1, 25)
        prod = n1 * n2
        ans = input("What is %d times %d? " % (n1, n2))
        '#this function occurs if the user answers the problem correct.'
        if int(ans) == prod:
            print(" That is correct! \n")
            correct = correct + 1
        else:
            print(" Sorry, the answer is %d.\n" % prod)
        n3 = randint(1, 25)
        n4 = randint(1, 25)
        dvd = n3 // n4
        ans = input("What is %d divided by %d? " % (n3, n4))
        '#this function occurs if the user answers the problem correct.'
        if int(ans) == dvd:
            print(" That is correct! \n")
            correct = correct + 1
        else:
            print("Sorry, the answer is %d.\n" % dvd)

    print("\nI asked you" ' questions ' " questions.\n\
    You got %d of them right." % correct)
elif choice == "advanced":
    correct = 0
    for i in range(4):
        n1 = 5
        n2 = 7
        prod = n1 - n2**2
        ans = input("What is %d minus %d squared?" % (n1, n2))
        '#this function occurs if the user answers the problem correct.'
        if int(ans) == prod:
            print(" That is correct! \n")
            correct = correct + 1
        else:
            print(" Sorry, the answer is %d.\n" % prod)
        n3 = 4
        n4 = 2
        prod = n3**2 + n4*3
        ans = input("What is %d squared plus %d times 3? " % (n3, n4))
        '#this function occurs if the user answers the problem correct.'
        if int(ans) == prod:
            print(" That is correct! \n")
            correct = correct + 1
        else:
            print("Sorry, the answer is %d.\n" % prod)
        n5 = 6
        n6 = 7
        prod = -n5 + n2**3
        ans = input("What's negative % d plus % d to\n\
        the third power?" % (n5, n6))
        '#this function occurs if the user answers the problem correct.'
        if int(ans) == prod:
            print(" That is correct! \n")
            correct = correct + 1
        else:
            print(" Sorry, the answer is %d.\n" % prod)
        n7 = 4
        n8 = 1
        prod = abs(n7) * n8 + 3
        ans = input("What is the absolute value\n\
        of %d times %d plus 3? " % (n3, n4))
        '#this function occurs if the user answers the problem correct.'
        if int(ans) == prod:
            print(" That is correct! \n")
            correct = correct + 1
        else:
            print("Sorry, the answer is %d.\n" % prod)
'#This print statement shows the amount of problems the user answered correct.'
print("\nI asked you 4 questions.  You got %d of them right." % correct)
