    def guess_my_year_of_birth():
        my_birthday = 31
        my_answer = 0
        while my_answer != my_birthday:
            input("Enter a guess: ")
            int(input(my_answer))
            if my_answer != my_birthday:
                print("Incorrect Guess :(! Guess again")

    print("Wow!!! Correct Guess :)!")
