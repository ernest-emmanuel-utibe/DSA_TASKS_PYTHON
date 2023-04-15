def print_word_ventures():
    word_ventures = "VENTURES"
    count = 0
    for letter in word_ventures:
        if count % 2 == 0:
            print()
        print(letter, end=' ')
        count = count + 1
    print()


if __name__ == "__main__":
    print(print_word_ventures())
