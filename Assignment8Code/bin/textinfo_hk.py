"""
This program uses searching techniques to search for words in a corpus and
display the most frequent word and its count. Then, this program will ask
the user to enter a word they want to know more information about and the
program will show them the occurrences of the word within context.

XXXXXXXXXXXXXXXX
11/13/17
"""
import filemenu

def main():
    folder = "../texts"
    files = filemenu.list_files(folder)
    print("To get started, you may want to try austen_emma.txt")
    print("and austen_northanger_abbey.txt")

    for i in range(2):
        if i == 0:
            n = "1st"
            text0 = filemenu.menu_selection(files, "Enter choice for the "
            + n + " text: ")
            print("Your selection: %s" % (files[text0]))
            title0 = files[text0]
        else:
            n = "2nd"
            text1 = filemenu.menu_selection(files, "Enter choice for the "
            + n + " text: ")
            print("Your selection: %s" % (files[text1]))
            title1 = files[text1]

    cleantext0 = processText(title0)
    count0 = countWords(cleantext0,title0)
    cleantext1 = processText(title1)
    count1 = countWords(cleantext1,title1)

    distinctiveWords(cleantext0,cleantext1,count0,count1,title0,title1)
    distinctiveWords(cleantext1,cleantext0,count1,count0,title1,title0)

    done = False
    while done == False:
        contextword = input("What word do you want to see in context?: ")
        if contextword == "":
            done = True
        else:
            for i in range(2):
                if i == 0: # looks to see if word is in text
                    here = linearSearch(contextword, cleantext0)
                    if here == True:
                        print("Here are the occurances of", contextword, "in",
                        title0, ": ")
                        print("------------------------------------")
                        contextWords(contextword, cleantext0)
                        print("------------------------------------")
                    else:
                        print("Here are the occurances of", contextword, "in",
                        title0, ": ")
                        print("------------------------------------")
                        print("The word '", contextword,
                        "' does not occur in this text")
                        print("------------------------------------")
                else:
                    here = linearSearch(contextword, cleantext1)
                    if here == True:
                        print("Here are the occurances of", contextword, "in",
                        title1, ": ")
                        print("------------------------------------")
                        contextWords(contextword, cleantext1)
                        print("------------------------------------")
                    else:
                        print("Here are the occurances of", contextword, "in",
                        title1, ": ")
                        print("------------------------------------")
                        print("The word '", contextword,
                        "' does not occur in this text")
                        print("------------------------------------")
#-------------------------------------------------------------------------------
def processText(title):
    """opens text file, lowercases it, turns numbers and non-letter characters
    into spaces, then returns the clean file in the form of a list"""
    inf = open(str(title), "r")
    cleanfile = []
    for line in inf:
        cleanline = ""
        for ch in line:
            alphacheck = ch.isalpha()
            if alphacheck == True:
                ch = ch.lower()
                cleanline = cleanline + ch
            else:
                newch = " "
                cleanline = cleanline + newch
        cleanline = cleanline.split()
        cleanfile.extend(cleanline)
    return cleanfile
#-------------------------------------------------------------------------------
def countWords(cleantext,title):
    """receives the clean text (a list), counts each of the words in the text,
    puts this data in a list as follows: ['word', # of times it occurs].
    Prints a chart of the 10 most frequent words in the text"""
    counts = [] # a lists of lists
    for i in cleantext:
        ans_list = binarySearch(i, counts)
        idx = ans_list[0] # the position of where the word should be in list
        found = ans_list[1] # either True or False
        if found == True:
            counts[idx][1] = counts[idx][1] + 1
        else:
            counts.insert(idx,[i, 1])
    sortedcounts = bubbleSort(counts)

    print("The 10 most frequent words in", title, "are: ")
    print("Frequency | Word")
    print("----------|-------------------------")
    length = len(sortedcounts)
    for i in range(length-1,length-11,-1):
        print("%5s %5s %5s" % (sortedcounts[i][1], "|", sortedcounts[i][0]))
    return counts
#-------------------------------------------------------------------------------
def bubbleSort(list1):
    """receives list of words in novel and amount of times they occur, bubble
    sorts this list by frequency or score of words and puts it in a new list.
    Returns that list"""
    done = False
    while not done:
        nswaps = 0
        for i in range(len(list1) - 1):
            if list1[i][1] > list1[i+1][1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
                nswaps = nswaps + 1
        if nswaps == 0:
            done = True
    # now the list is sorted by number of times a word occurs
    return list1
#------------------------------------------------------------------------------
def binarySearch(x,L):
    """use bin search, returns either the index of the word and True or the low
    of where the word should be and False"""
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (high + low)//2
        if x == L[mid][0]:
            return [mid, True]
        elif x < L[mid][0]:
            high = mid - 1
        else:
            low = mid + 1
    # if we get here, not found
    return [low, False]
#-------------------------------------------------------------------------------
def distinctiveWords(p_cleantext,s_cleantext,p_counts,s_counts, p_title, s_title):
    """is given a text and finds the top 10 most distinctive words in one
    text relative to the other, prints a chart of this data"""
    n0 = len(p_cleantext)
    n1 = len(s_cleantext)
    distinctiveness = []
    for pair in p_counts:
        ans_list = distinctivebinarySearch(pair[0],s_counts)
        idx = ans_list[0]
        s_frequency = ans_list[1]
        here = ans_list[2]
        if here == "found":
            p_score = pair[1]/n0
            s_score = s_frequency/n1
            score = p_score / s_score
            distinctiveness.append([pair[0],score])
    sorteddistinctive = bubbleSort(distinctiveness)

    print("The 10 most prevalent words in", p_title, "relative to", s_title,"are: ")
    print("Score       | Word")
    print("------------|-------------------")
    length = len(distinctiveness)
    if length < 10:
        for i in range(length-1,-1,-1):
            print("%11.1f %s %-5s" % (sorteddistinctive[i][1], "|", sorteddistinctive[i][0]))
    else:
        for i in range(length-1,length-11,-1):
            print("%11.1f %s %-5s" % (sorteddistinctive[i][1], "|", sorteddistinctive[i][0]))
#------------------------------------------------------------------------------
def distinctivebinarySearch(x,L):
    """ is given a word and the counts list, returns if that word is found and
    if it is returns its index and the frequency of the word"""
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (high + low)//2
        if x == L[mid][0]:
            return [mid, L[mid][1], "found"]
        elif x > L[mid][0]:
            low = mid + 1
        else:
            high = mid - 1
    # if we get here, not found
    return ["", "", "not found"]
#-------------------------------------------------------------------------------
def linearSearch(word, text):
    """ is given a word and a text. Searches for word in text and returns True
    if it is found and False if it is not"""
    done = False
    while not done:
        for i in text:
            if i == word:
                done = True
                return True
        # if we get here, word is not in cleantext
        done = True
        return False
#-------------------------------------------------------------------------------
def contextWords(contextword, cleantext):
    """is given the word the user wants to know more about, prints everytime
    the word occurs in the text including the 4 words before and the 4 words
    after that word """
    indexes = contextlinearSearch(contextword, cleantext) # this is a list
    for i in indexes:
        string1 = str(cleantext[i-4] + " " + cleantext[i-3] + " " +
        cleantext[i-2] + " "+ cleantext[i-1])
        string2 = str(cleantext[i+1] + " " + cleantext[i+2] + " " +
        cleantext[i+3] + " " + cleantext[i+4])
        print("%30s %s %-30s" % (string1, cleantext[i], string2))
#------------------------------------------------------------------------------
def contextlinearSearch(contextword, cleantext):
    """finds all the places where that word is in the text and returns a list
    of the indexes of that word"""
    placesfound = []
    for i in range(len(cleantext)):
        if cleantext[i] == contextword:
            placesfound.append(i)
    return placesfound

main()
