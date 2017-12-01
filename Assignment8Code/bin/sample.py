"""
A sample solution that a student in CS21 might be able to write

Requires python3
"""


"""
The basic strategy for counting words is as follows:
Create a list of lists called 'counts'. Each sublist in 'counts'
is a [word, count] pair representing how often the word occurred.

For each word in the text, use a modified binary search function
to first try and find the word in 'counts'. If it appears, increment
the count in the sublist. If it does not appear, insert it into the
list.

This is similar to the "modifiedBS" function from Spring
2013 Lab 8, "Author Detection"
"""



from os.path import isfile
from os import listdir
from operator import itemgetter
import re 

'''
# This function would be provided but would need to be modified

def binary_search(element, lst):
	"""
	Performs binary search for an element in a list.
	Returns the index at which the element is found or None.

	If there are multiple copies of the target element in the
	list, returns the index of the first copy found.
	"""
	left = 0
	right = len(lst) - 1
	middle = (right + left)//2

	while left <= right:
		middle = (right + left)//2
		if lst[middle] == element: # we found it
			return middle
		elif element < lst[middle]: # middle was too big
			right = middle - 1
		else:  # middle was too small
			left = middle + 1

	return None
'''

"""
Provided code
"""
def list_files(folder):
	"""
	Given a folder/directory name, print the .txt files
	in the directory and return them in a list.
	"""
	print("Here are the files in the text folder:")
	txt_files = []
	all_files = listdir(folder)
	for i in range(len(all_files)):
		file = all_files[i]
		if file.endswith('.txt'):
			print('[%2d] %s' % (i, file))
			txt_files.append('%s/%s' % (folder, file))
	print()
	return txt_files


"""
Begin student-written code
"""
def menu_selection(choices, prompt):
	"""
	Present the user with a prompt asking for a choice from a 
	list of choices verify that the selection is correct. Expects
	a numerical input.
	"""
	while True:
		choice = input(prompt)
		if not choice.isdigit():
			print("Only integers are accepted, try again.")
		else:
			choice = int(choice)
			if choice >= 0 and choice < len(choices):
				return choice
			else:
				print("That selection is out of range, try again.")

	return choice

def get_words_from_file(filename):
	"""
	Given the name of a file, return the words in the file in the order
	they appear in the file.

	A word is defined to be a sequence of capital and lower case letters.
	Hyphenated words are unhyphenated (e.g. son-in-law -> son in law).
	Apostrophes also break apart words (e.g. mother's -> mother s). We could
	change this behavior but doing this break-up allows a better accounting
	for the word (e.g. mother).
	"""
	all_words = []
	infile = open(filename, encoding='latin1')
	for line in infile:
		# We would have to give them this line or pre-tokenize the texts.
		# Unfortunately it also includes the empty string so we have to
		# remove that below.
		words = re.split('[^A-Za-z]+', line) #this line would need to be provided
		for word in words:
			if word != '':
				if word.islower(): #throw away words that aren't lowercase
					all_words.append(word)

	return all_words


def binary_update(counts, word):
	"""
	Input: A list of [word,count] representing word counts and a word
	to update.
	Returns: None; the counts list is modified.

	If the word is already in the counts list, add one to the count.

	If the word is not yet in the counts list, insert the word list
	into counts list with an initial count of 1.
	"""
	if len(counts) == 0:
		counts.append([word, 1])
		return

	right = len(counts)-1
	left = 0

	while right >= left:
		middle = (right+left)//2
		if counts[middle][0] == word: # we found it, update it
			counts[middle][1] += 1
			return
		elif word < counts[middle][0]: # middle was too big
			right = middle - 1
		else:  # middle was too small
			left = middle + 1

	# if we didn't find it, add it.
	if counts[middle][0] < word:
		counts.insert(middle+1, [word, 1])
	else:
		counts.insert(middle, [word, 1])


def binary_search(counts, word):
	"""
	Input: A list of [word,count] representing word counts or word
	frequency ratios.
	Returns: the index where the word is found or None.
	"""
	left = 0
	right = len(counts) - 1

	while left <= right:
		middle = (right + left)//2
		if counts[middle][0] == word: # we found it
			return middle
		elif word < counts[middle][0]: # middle was too big
			right = middle - 1
		else:  # middle was too small
			left = middle + 1

	return None


def count_words(wordlist):
	counts = []
	for word in wordlist:
		# we could filter out non-lowercase words if we wanted
		binary_update(counts, word)
	return counts


def prevelance(counts1, counts2):
	"""
	Determine which words are most prevelant in corpus1 relative
	to corpus2.

	The algorithm used here is to calculate the percentage of the
	corpus made up by each word and show those words with the biggest
	difference in relative percentages.

	We will create a new list, similar in format to counts1 and counts2,
	with elements [word, freq_ratio] where freq_ratio is calculated
	as: (count1(word)/(size of corpus1))/(count2(word)/(size of corpus2))
	"""
	# figure out size of each corpus
	size1 = 0
	for word_count in counts1:
		size1 += word_count[1]
	size2 = 0
	for word_count in counts2:
		size2 += word_count[1]

	ratio_list = []
	for i in range(len(counts1)):
		word = counts1[i][0]
		j = binary_search(counts2, word)
		if j is not None:
			ct1 = counts1[i][1]
			ct2 = counts2[j][1]
			#if subset:   # Not defined; possible extension
			#	ct2 -= ct1
			if ct1 > 0 and ct2 > 0 and (ct1 > 5 or ct2 > 5):
				ratio = (ct1/size1) / (ct2/size2)
				ratio_list.append([word, ratio])

	ratio_list.sort(key=itemgetter(1)) #this line would need to be provided
	                                   # or they'd have to use their own sort
	return ratio_list


def display_most_common(counts, corpus):
	"""
	Display the most frequent words in the corpus.
	"""
	n = 10
	by_freq = sorted(counts, key=itemgetter(1), reverse=True) # provided or use their own
	print("The %d most frequent words in %s are:\n" % (n, corpus))
	print("Frequency | Word")
	print("----------|-------------------------")
	for i in range(n):
		print("%9d | %s" % (by_freq[i][1], by_freq[i][0]))
	print()

def display_prevelance(ratio_list, corpus1, corpus2):
	"""
	The first entries are more prevalent in corpus1. The last entries are
	most prevalent in corpus2.
	"""
	n = 10
	print("The %d most prevalent words in %s\nrelative to %s\n" % (n, corpus1, corpus2))
	print("Score  | Word")
	print("-------|-------------------------")
	for i in range(-1, -n-1, -1):
		print("%6.1f | %s" % (ratio_list[i][1], ratio_list[i][0]))
	print()

	print("The %d most prevalent words in %s\nrelative to %s\n" % (n, corpus2, corpus1))
	print("Score  | Word")
	print("-------|-------------------------")
	for i in range(n):
		print("%6.1f | %s" % (1/ratio_list[i][1], ratio_list[i][0]))

	print()

def display_kwic(text, word):
	"""
	Create a concordance for all occurences of word in the text.
	"""
	n = 4  # window size

	# pad the corpus with n spaces on either end
	padded = [' ']*n + text + [' ']*n

	found = False
	for i in range(len(padded)):
		if padded[i] == word:
			found = True
			start_index = i-n
			end_index = i+n+1
			preword = ' '.join(padded[start_index:i])
			postword =' '.join(padded[i+1:end_index])
			print("%32s %s %-32s" % (preword, word, postword))

	if not found:
		print(" << %s not found in corpus >>" % (word))

def yes_no(prompt):

	while True:
		choice = input(prompt)
		choice = choice.lower()
		if choice.startswith('y') or choice.startswith('n'):
			return choice[0]
		else:
			print("Answer must begin with 'y' or 'n', try again.")


def correct_subset(counts1, counts2):
	"""
	Extra credit. Assuming counts1 represents the counts from a large 
	and counts2 represents the counts from a subset of that large corpus,
	update the counts in counts1 so they do not include the counts in
	counts2.
	"""
	for count_pair2 in counts2:
		word2 = count_pair2[0]
		count2 = count_pair2[1]
		idx1 = binary_search(counts1, word2)
		tmp = counts1[idx1][1]
		counts1[idx1][1] -= count2
		print(word2, count2, tmp, counts1[idx1][1])
		if counts1[idx1][1] == 0:
			counts1.pop(idx1)


def main():
	print("This program will identify the words that most distinguish")
	print("one text corpus from another.")
	print()

	folder = "../texts"
	files = list_files(folder)

	print("To get started, you may want to try austen_emma.txt")
	print("and austen_northanger_abbey.txt")
	print()
	corpus1_n = menu_selection(files, "Enter choice for the 1st corpus: ")
	corpus2_n = menu_selection(files, "Enter choice for the 2nd corpus: ")

	corpus1 = files[corpus1_n]
	corpus2 = files[corpus2_n]

	words1 = get_words_from_file(corpus1)
	counts1 = count_words(words1)

	words2 = get_words_from_file(corpus2)
	counts2 = count_words(words2)

	# Extra credit extension
	if yes_no("Is the 2nd corpus a subset of the 1st? ") == "y":
		correct_subset(counts1, counts2)

	display_most_common(counts1, corpus1)
	display_most_common(counts2, corpus2)

	ratio_list = prevelance(counts1, counts2)
	display_prevelance(ratio_list, corpus1, corpus2)

	see_more = "y"
	while see_more == "y":
		word = input("Choose a word to see it in context: ")

		print()
		print("Here are the occurences of %s in %s:" % (word, corpus1))
		print("------------------------------------")
		display_kwic(words1, word)
		print("------------------------------------")
		print("Here are the occurences of %s in %s:" % (word, corpus2))
		print("------------------------------------")
		display_kwic(words2, word)
		print()

		see_more = yes_no("Do you want to see more words in context? ")

	return ratio_list

res=main()