"""
This program:
-Allows the user to pick to text files to compare
-Displays the 10 most frequent words in each text
-Displays the 10 most distinctive words in each text relative to the other
-Displays a given word in context

Author: XXXXXXXXXXX
Date: 22 November 2017
"""
from filemenu import *

def main():

    # User selects from menu of text files (functions are from filemenu.py)
    folder = "../texts"
    files = list_files(folder)
    choice_1 = menu_selection(files, "Enter choice for the 1st corpus: ")
    choice_2 = menu_selection(files, "Enter choice for the 2nd corpus: ")
    corpus_1 = files[choice_1]
    corpus_2 = files[choice_2]

    # Process the texts from the source files to form a list of the cleaned
    #   version of the text (i.e. lowercase and no punctuation)
    cleaned_text_list_1 = file_clean(corpus_1)
    cleaned_text_list_2 = file_clean(corpus_2)
    print()

    # Create list of word counts for each corpus
    word_counts_1 = word_counter(cleaned_text_list_1)
    word_counts_2 = word_counter(cleaned_text_list_2)
    wc1_copy = word_counts_1[:]     # Make copies for use in distinct function
    wc2_copy = word_counts_2[:]

    # Display 10 most frequent words in each corpus
    word_frequency(cleaned_text_list_1, word_counts_1, corpus_1)
    print()
    word_frequency(cleaned_text_list_2, word_counts_2, corpus_2)
    print()

    # Display 10 most distinctive words of each text in relation to the other
    distinct(cleaned_text_list_1, cleaned_text_list_2, wc1_copy, wc2_copy,
        corpus_1, corpus_2)
    print()

    # Ask user for word to find in context and display every instance of the
    #   word in context until the user enters nothing at the prompt
    quit = False
    while not quit:
        word = input("Choose a word to see it in context: ")
        print()
        if word == "":
            quit = True
        else:
            word_context(word, corpus_1, cleaned_text_list_1)
            print("-"*40)
            word_context(word, corpus_2, cleaned_text_list_2)
            print()

# ------------------------------------------------------------------------------
def file_clean(corpus):
    """
    Reads file, uses line_cleaner function, and returns a list of the
    cleaned file text
    """
    infile = open(corpus, "r")
    cleaned_text_list = []
    for line in infile:
        cleaned_text_list.extend(line_cleaner(line))
    infile.close()

    return cleaned_text_list

# ------------------------------------------------------------------------------
def line_cleaner(text):
    """
    Cleans text and returns a list of the cleaned text
    """
    text = text.lower()                 # Converts line to lowercase version
    text_ch_count = len(text)
    cleaned_s = ""                      # String version of cleaned text
    for n in range(text_ch_count):
        ch = text[n]
        if ch.isalpha() or ch.isdigit():
            cleaned_s += ch
        else:                       # Replaces non-alphanumeric characters with
            cleaned_s += " "        #   spaces
    clean_line = cleaned_s.split()

    return clean_line

# ------------------------------------------------------------------------------
def word_counter(cleaned_text_list):
    """
    Taking a list of cleaned text, creates a list of words and their
    respective word counts
    """
    counts = []
    for item in cleaned_text_list:
        i, low = binary_search(counts, item)
        if i == -1:                         # If word is not yet in counts,
            counts.insert(low, [item, 1])   #   add word and word count to
        else:                               #   to counts at index = low
            counts[i][1] += 1           # If the word is in counts,
                                        #   add 1 to the word's count
    return counts

# ------------------------------------------------------------------------------
def word_frequency(cleaned_text_list, word_counts, corpus):
    """
    Displays the 10 most frequent words in given text
    """
    # Sorts in order from lowest to highest frequency
    lst = word_counts
    l = len(lst)
    for i in range(1, l):    # Insertion sort
        elt = lst[i]
        j = i-1
        # if not at the start of the list and items are out of order
        while (j >= 0) and (elt[1] < lst[j][1]):
            lst[j+1] = lst[j]
            j=j-1
        while (j >= 0) and (elt[0] < lst[j][0]):
            lst[j+1] = lst[j]
            j=j-1
        lst[j+1] = elt

    # Display 10 most frequent words and their respective counts
    print("The 10 most frequent words in %s are:" %(corpus))
    print()
    print("%-10s| %s" %("Frequency", "Word"))
    print("%10s|%s" %(10*"-", 30*"-"))
    n = l - 1
    while (n > l - 11) and (n >= 0):
        table_entry_s = ("%9d | %s" %(lst[n][1],
            lst[n][0]))
        print(table_entry_s)
        n -= 1

    return

# ------------------------------------------------------------------------------
def distinct(cleaned_text_list_1, cleaned_text_list_2, wc1_copy, wc2_copy,
    corpus_1, corpus_2):
    """
    -Calculates frequency scores for each word using freq_score function
    -Calculates distinctiveness scores for each word found in both texts
    -Displays 10 most distinctive words of each text in relation to the other
    """
    # Calculate frequency scores; mutate word count lists
    freq_score(wc1_copy, cleaned_text_list_1)
    freq_score(wc2_copy, cleaned_text_list_2)

    # Create list of shared words and their distinctiveness scores
    d_score_list = []
    for item in wc1_copy:
        word = item[0]
        i, low = binary_search(wc2_copy, word)
        if i != -1:
            score = item[1] / wc2_copy[i][1]
            d_score_list.append([word, score])

    # Sort from lowest to highest distinctiveness score
    l = len(d_score_list)
    for i in range(1, l):
        elt = d_score_list[i]
        j = i-1
        # if not at the start of the list and items are out of order
        while (j >= 0) and (elt[1] < d_score_list[j][1]):
            d_score_list[j+1] = d_score_list[j]
            j=j-1
        while (j >= 0) and (elt[0] < d_score_list[j][0]):
            d_score_list[j+1] = d_score_list[j]
            j=j-1
        d_score_list[j+1] = elt

    # Display 10 most distinctive words of corpus_1 relative to corpus_2
    print("The 10 most prevalent words in %s\n relative to %s:"
        %(corpus_1, corpus_2))
    print()
    print("%8s| %s" %("Score ", "Word"))
    print("%8s|%s" %(7*"-", 30*"-"))
    n = l - 1
    while (n > l - 11) and (n >= 0):
        table_entry_s = ("%7.2f | %s" %(d_score_list[n][1],
            d_score_list[n][0]))
        print(table_entry_s)
        n -= 1
    print()

    # Display 10 most distinctive words of corpus_2 relative to corpus_1
    print("The 10 most prevalent words in %s\n relative to %s:"
        %(corpus_2, corpus_1))
    print()
    print("%8s| %s" %("Score ", "Word"))
    print("%8s|%s" %(7*"-", 30*"-"))
    n = 0
    while (n < l) and (n < 10):
        score = 1/d_score_list[n][1]
        table_entry_s = ("%7.2f | %s" %(score,
            d_score_list[n][0]))
        print(table_entry_s)
        n += 1

    return

# ------------------------------------------------------------------------------
def freq_score(word_counts, cleaned_text_list):
    """
    Mutates word_counts (copied list) by replacing word counts with frequency
    scores
    """
    text_length = len(cleaned_text_list)
    for item in word_counts:
        score = item[1]/text_length
        item[1] = score

    return

# ------------------------------------------------------------------------------
def word_context(word, corpus, cleaned_text_list):
    """
    Displays a given word in context (i.e. displays the four words preceding
    and following the word in every instance in which the word occurs)
    """
    print("Here are the occurences of '%s' in %s:" %(word, corpus))
    print(40*"-")
    text_length = len(cleaned_text_list)
    start = 0
    i = linear_search(cleaned_text_list, start, word)
    if i != -1:
        count = 0
        while i != -1 and start < text_length:
            ante_s = ""
            post_s = ""
            if i < 4 and i <= text_length - 5:  # Too close to beginning
                ante_start = 0
                post_end = i + 5
            elif i < 4 and i > text_length - 5: # Too close to beginning
                ante_start = 0                          #   and end
                post_end = text_length
            elif i > 4 and i > text_length - 5: # Too close to end
                ante_start = i - 4
                post_end = text_length
            else:                           # Goldilocks
                ante_start = i - 4
                post_end = i + 5

            for index in range(ante_start, i):
                ante_s += cleaned_text_list[index] + " "
            for index in range(i + 1, post_end):
                post_s += cleaned_text_list[index] + " "

            print("%36s%s %s" %(ante_s, word, post_s))
            start = i + 1
            count += 1      # Avoids having to make another copy of counts list
            i = linear_search(cleaned_text_list, start, word)
        print()
        print("The word '%s' occurs (%d) times in the text." %(word, count))

    else:
        print("The word '%s' does not occur in the text." %(word))

    return

# ------------------------------------------------------------------------------
def linear_search(lst, start, target):
    """
    Modified linear_search function
    """
    position = start                # Allows for different starting positions
    while position < len(lst):
        if lst[position] == target:
            return position
        position += 1
    return -1

# ------------------------------------------------------------------------------
def binary_search(lst, target):
    """
    -Modified binary_search function
    -List must be sorted
    -Returns low in addition to middle (found) or -1 (not found) for use in
    word_counter function in textinfo program
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        middle = int((low + high)/2)
        if target == lst[middle][0]:    # Allows for use with counts, a list of
            return middle, low          #   lists
        elif target > lst[middle][0]:
            low = middle + 1
        else: # too low
            high = middle -1
    return -1, low

# ------------------------------------------------------------------------------

main()
