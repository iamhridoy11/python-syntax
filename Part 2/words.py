word = ["hello", "hey", "goodbye", "yo", "yes"]
def print_upper_words(words, first, last):

    # 1, 2 For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!
    for items in words:
        print(items.upper())

    # 3, 4
    if first == "h":
        for items in range(len(words) - 3):
            print("\t", words[items].upper())
    if last == "y":
        for items in range(len(words) - 2, len(words)):
            print(words[items].upper())



print_upper_words(word, first= "h", last= "y")