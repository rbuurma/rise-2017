"""
Author: XXXXXXXXXXXXXX
Date: 11/15/17-11/24/17
"""
import filemenu

def main():
    s = '''
     This program:
     1. Lets you choose two out of the texts given
     2. Compares the words in the two texts and displays the ten most
        'distinctive' ones (or the words that are more likely to appear in
        in one text than in the other)
     3. Presents the ten most frequent words in each separate text
     4. Allows you to choose a word to see the context in which it is seen in
        each text
     To get started, you may want to try austen_emma.txt and
     austen_northanger_abber.txt'''
    print(s)
    print()

    folder = "../texts"
    file_list = filemenu.list_files(folder)

    frst_file = getFile("Enter the choice for the 1st corpus: ", file_list)
    scnd_file = getFile("Enter the choice for the 2nd corpus: ", file_list)

    w1 = getList(frst_file)
    c1 = getCounts(w1)
    c1_alpha = c1[:] #will be used for context()

    w2 = getList(scnd_file)
    c2 = getCounts(w2)
    c2_alpha = c2[:] #will be used for context()

    distinctive(w1, w2, c1, c2, frst_file, scnd_file)

    printTenMostFrequent(c1, frst_file)
    printTenMostFrequent(c2, scnd_file)

    word = " "
    while word != "": #if user presses enter, loop ends
        print()
        word = input("Enter a word to see it in context. Press enter to quit. ")

        context(c1_alpha, w1, word, frst_file)
        context(c2_alpha, w2, word, scnd_file)
        print()

#-----------------------functions are in order of use--------------------------#
def getFile(prompt, file_list):
    '''Takes a prompt and the list of files as parameters. Returns the file.
        filemenu.menu_selection() is called within getFile().
    '''

    chosen = filemenu.menu_selection(range(len(file_list)), prompt)
    the_file = file_list[chosen]

    return the_file

#------------------------------------------------------------------------------#
def getList(file_name):
    '''Returns a list of the words in the file in lowercase and no punctuation.
         stripLine() is called within getList().
    '''

    word_file = open(file_name, "r")

    words = [] #init
    for line in word_file:
        line = stripLine(line)
        line = line.split()

        for word in line:
            words.append(word)

    return words

#------------------------------------------------------------------------------#
def stripLine(line):
    '''Returns a version of the line containing no punctuation and lowercase.
         Is called within getList().
    '''

    new_string = "" #init
    line = line.lower()

    for ch in line:
        if ch.isalpha():
            new_string += ch
        else:
            new_string += " "
         #elif ch != "'": #some words have apostrophes
         #    new_string += "

    return new_string

#------------------------------------------------------------------------------#
def getCounts(lst):
    '''Returns a sorted array containing [the words in <lst>, counts].
         indexSearch() is called within getCounts().
    '''

    c = [] #init

    for word in lst:
        i = indexSearch(c, word) #correct place of word in sorted list

        try:
            if c[i][0] == word:
                    c[i][1] += 1
            else:
                c.insert(i, [word, 1])

        except IndexError:
                c.append([word, 1])

    return c

#------------------------------------------------------------------------------#
def indexSearch(lst, word):
    '''Returns the correct place for <word> in sorted list <lst>.
         Is called within getCounts().
    '''

    if len(lst) == 0:
        return 0

    low = 0
    high = len(lst)-1
    while low <= high:
        mid = int((low + high)/2)

        if word == lst[mid][0]:
            return mid
        elif word > lst[mid][0]:
            low = mid+1
        else: #bottom half
            high = mid-1

    return low

#------------------------------------------------------------------------------#
def distinctive(w1, w2, c1, c2, file1, file2):
    '''Calculates and prints the ten most 'distinctive' words in two texts.
         Is called in main().
    '''

    len1 = len(w1)
    len2 = len(w2)
    scores = []

    for i in range(len(c1)):
        if c1[i][0] in w2:
            i2 = indexSearch(c2, c1[i][0])
            ratio = (c1[i][1]/len1) / (c2[i2][1]/len2)

            k = indexSearch(scores, c1[i][0])
            scores.insert(k, [c1[i][0], ratio])

    sortByCount(scores)
    printMostDistinctive(scores, file1, False)
    printMostDistinctive(scores, file2, True)

#------------------------------------------------------------------------------#
def printMostDistinctive(s, file_name, inversion):
    '''Prints the ten most 'distinctive' words in a text.
         Is called in distinctive().
    '''

    if len(s) < 10:
        loops = len(s)
    else:
        loops = 10

    print()
    print("Ten most distinctive words in the file %s:" %(file_name))
    print()

    print("%10s %26s" %("Word", "Dist. Score"))
    if not inversion:
        for k in range(loops):
            i = len(s)-k-1
            print("(#%2d) %-15s %15.2f" %(k+1, s[i][0], s[i][1]))

    elif inversion:
        for k in range(loops):
            print("(#%2d) %-15s %15.2f" %(k+1, s[k][0], 1/s[k][1]))

#------------------------------------------------------------------------------#
def printTenMostFrequent(c, file_name):
    '''Prints the ten most frequent words in a text.
         Is called in main().
    '''

    sortByCount(c)

    print()
    print("The ten most frequent words in %s are:" %(file_name))
    print()

    print("%10s %16s" %("Word", "Frequency"))
    for k in range(1, 11):
        print("(#%2d) %-10s %10d" %(k, c[len(c)-k][0], c[len(c)-k][1]))

#------------------------------------------------------------------------------#
def sortByCount(lst):
    '''Sorts the array by the count or the distinctiveness score.
         Is called within printTenMostFrequent() and distinctive().
    '''

    for current in range(1, len(lst)):
        stored_value = lst[current]
        before = current - 1

        while (before >= 0) and (stored_value[1] < lst[before][1]):
            lst[before + 1] = lst[before]
            before -= 1
        lst[before + 1] = stored_value

#------------------------------------------------------------------------------#
def context(c, w, word, file_name):
    '''Prints the frequency and the context in which word appears in the text.
         formatContext() is called within context().
    '''

    index_found = indexSearch(c, word) #index where word is found

    try:
        frequency = c[index_found][1]

    except IndexError:
        frequency = c[index_found-1][1]

    word_in_text = False

    if word == c[index_found][0]:
        word_in_text = True #loop runs
    elif word != "":
        print()
        print("That word is not present in %s!" %(file_name))
        print()

    times_found = 0

    while word_in_text and frequency != times_found:
        print()
        print("The word %s is seen %d in %s." %(word, frequency, file_name))
        print()

        for i in range(len(w)):
            if w[i] == word:
                context = formatContext(i, w)
                print(context)
                print()

                times_found += 1

#------------------------------------------------------------------------------#
def formatContext(i, w):
    '''Formats phrase so context looks neat. Takes index of the word to find the
         four previous and next words. Returns the line of context.
         Is called within context().
    '''

    before_txt = ""
    context = ""
    space = " "

    if i < 5: #beginning of list
        context = "%40s" %(before_txt)

        for k in range(5):
            context += space + w[i+k]

    elif i > (len(w)-5): #end of list
        for k in range(4):
            before_txt += space + w[(i+k)-4]

        context = "%40s" %(before_txt)

        for k in range(i, len(w)): #from i to end of list
            context += space + w[k]

    else: #neither beginning nor end of list
        for k in range(4):
            before_txt += space + w[(i+k)-4]

        context = "%40s" %(before_txt)

        for k in range(5):
            context += space + w[i+k]

    return context

#------------------------------------------------------------------------------#
main()
