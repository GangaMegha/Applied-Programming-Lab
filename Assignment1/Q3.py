import re

with open("input.dat",'r') as f:				#open input file input.dat
	contents=f.read()				#read from the input file input.dat usig file pointer f

contents=contents.lower()						#converting the string to lowercase inorder to avoid incorrect frequency due to case-sensitivity
contents=re.sub('[^a-z ]+', '', contents)	#keeping only alphabets and space in the string
words=contents.split()							#splitting string into words
d={}											#declaring an empty dictionary
for w in words :								#Building the dictionary by iterating through the words
	if w in d :			#if word present in the dictionary						
		d[w]+=1			#increment the frequency
	else :				#if word not already present in the dictionary
		d[w]=1			#add new word to dictionary

for key in sorted(d) :#.iteritems() :	#iterate through the dictionary
    print key, d[key]				#print the word and its curresponding frequency
