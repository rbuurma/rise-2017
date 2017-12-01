from filemenu import *
"""
analyzes text files, giving word frequency
"""
def main():
	folder = "../texts"
	files = list_files(folder)
	select_1 = menu_selection(files, "Enter choice for the 1st text: ")
	print("Your first selection: %s" %(files[select_1]))
	select_2 = menu_selection(files, "Enter choice for the 2nd text: ")
	print("Your second selection: %s" %(files[select_2]))
	select1 = files[select_1]
	select2 = files[select_2]
	cleanlst1 = makecleanlst(select1)
	cleanlst2 = makecleanlst(select2)
	data1 = makedata(cleanlst1)
	data1_sort = data1[:]
	data2 = makedata(cleanlst2)
	data2_sort = data2[:]
	sort(data1_sort)
	sort(data2_sort)
	print("The 10 most frequent words in %s are: " %(select1))
	disp10words(data1_sort,"Frequency")
	print("The 10 most frequent words in %s are: " %(select2))
	disp10words(data2_sort, "Frequency")
	numwords1 = len(cleanlst1)
	numwords2 = len(cleanlst2)
	dist_lst = dist(numwords1, numwords2, data1, data2)
	last10 = getlast10(dist_lst)
	print("The 10 most prevalent words in %s relative to %s are: " %(select1,select2))
	disp10words(dist_lst,"Score")
	print("The 10 most prevalent words in %s relative to %s are: " %(select2,select1))
	disp10words(last10,"Score")
	while True:
		word = input("What word do you want me to find? ")
		if word == "":			#stops if user inputs empty string
			print("Thank you for using this program.")
			break
		pos1 = context(cleanlst1, word)
		pos2 = context(cleanlst2, word)
		print("Occurences of %s in %s: " %(word,select1))
		print(20*"-")
		dispwords(cleanlst1, pos1, select1, word)	#displays all the words in context
		print("Occurences of %s in %s: " %(word,select2))
		print(20*"-")
		dispwords(cleanlst2, pos2, select2, word)

#finds words in context
def context(cleanlst, word):
	pos = []
	p = lsearch(cleanlst,word,0)	#finds the fist occurence of the word
	if p[0] == -1:					#if no word is found
		return -1
	pos += p
	while True:			#finds all occurences of the word
		p = lsearch(cleanlst,word,pos[len(pos)-1]+1)
		if p[0] == -1:
			break
		pos += p
	return pos

#prints up to ten words with corresponding value
def disp10words(list, text):
	a = 10
	b = 0
	if len(list) < 10:
		a = len(list)
	print("%-12s | Word" %(text))
	print(13*"-" + "|" + 25*"-")
	for i in range(b,a):
		print("%12f | %s" %(list[i][1],list[i][0]))

#creates a list of the least distinctive words
def getlast10(list):
	a = len(list)-1
	b = len(list)-11
	if len(list) < 10:
		b = 0
	final = []
	c = 0
	for i in range(a,b,-1):
		final.append(list[i])
		final[c][1] = 1/(final[c][1])
		c += 1
	return final

#creates a sorted list of most distinctive words
def dist(n1, n2, data1, data2):
	distlst = []
	for i in data1:
		a = bsearch(data2,i[0])
		if a[0] != -1:
			d = (i[1]/n1)/(data2[a[0]][1]/n2)
			distlst.append([i[0],d])
	sort(distlst)
	return distlst

#sorts the counts list by count instead of alphabetical order
def sort(list):
	b = 0
	while b != len(list):
		a = list[b]
		c = 0
		for i in list:
			if i[1] < a[1]:
				list[c] = a
				a = i
				list[b] = i
			c += 1
		b += 1

#makes a cleaned list of words given an input file
def makecleanlst(select):
	infile = open(select, "r")
	cleanlst = []
	for line in infile:
		clean = cleantext(line)
		cleanlst += clean.split()
	return cleanlst

#cleans text returning only lower case letters and spaces
def cleantext(line):
	clean_line = ""
	for i in line:
		if i.isalpha() == True:
			clean_line += i.lower()
		else:
			clean_line += " "
	return clean_line

#creates list of words + word count
def makedata(cleanlst):
	data = []
	for i in cleanlst:
		if len(data) != 0:
			d = bsearch(data,i)
			if d[0] >= 0:
				data[d[0]][1] += 1
			else:
				data.insert(d[1],[i,1])
		else:
			data += [[i,1]]
	return data

#finds the most used word and how often it is used
def bigword(data):
	bword = data[0]
	for i in data:
		if i[1] > bword[1]:
			bword = i
	return bword

#binary search
def bsearch(lst, item):
	low = 0
	high = len(lst) - 1
	while low <= high:
		middle = int((low + high)/2)
		if item == lst[middle][0]:
			return [middle]
		elif item > lst[middle][0]:
			low = middle + 1
		else:
			high = middle -1
	return [-1,low]

#linear search for finding words in cleanlst
def lsearch(lst, item, pos):
	while pos != len(lst):
		if lst[pos] == item:
			return [pos]
		pos += 1
	return [-1]

#displays words 4 before and 4 after a word
def dispwords(lst, poslst, select, word):
	if poslst == -1:
		print("I couldn't find %s in %s" %(word,select))
		return
	for i in poslst:
		l = ""
		r = ""
		if i < 4:
			for j in range(i):
				l += lst[j] + " "
		else:
			for j in range(4,0,-1):
				l += lst[i-j] + " "
		if i > len(lst) - 5:
			for j in range(1,len(lst)-i):
				r += lst[i+j] + " "
		else:
			for j in range(1,5):
				r += lst[i+j] + " "
		print("%35s%s %-35s" %(l,lst[i],r))
	return

main()
