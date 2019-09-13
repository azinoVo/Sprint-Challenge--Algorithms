'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word, count = 0):

    # Counter to accumulate the number of occurrences as they happen
    occurrences = count

    # First two letters that we are checking
    piece = word[0:2]
    print("word", word)
    print("pieces", piece)
    print("occurrences", occurrences)
    
    # Base Case and returns the number of occurrences
    # End at conclusion of word
    if len(word) == 2:
        if word == "th":
            occurrences = count + 1
            print("FINAL", occurrences)
            return occurrences
        else:
            print("FINAL", occurrences)
            return occurrences

    # Function Calling itself slowly reaching the base case
    elif len(word) > 2:
        if piece == "th":
            # Check if letters are "th", increment, and repeat the function
            occurrences = count + 1
            print("***", occurrences)
            # Step by one letter at a time, cutting off the letter behind it each time
            count_th(word[1:], occurrences)
        else:
            count_th(word[1:], occurrences)
    else:
            pass

count_th("abcthxyz", 0)