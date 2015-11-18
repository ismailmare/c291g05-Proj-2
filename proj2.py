# Assignment:           Mini Project 1
# Due Date:             October, 27 2015
# Name:                 Ismail Mare, Janice Loo, Preyanshu Kumar
# Unix ID:              imare, jloo, preyansh
# StudentID:            1388973, 1359624, 1395321
# Lecture Section:      B1
# Instructor:           Davood Rafiei
#---------------------------------------------------------------
#

#importing necessary libraries
import sys
import datetime
import math
import random
import time
import string
import sys






#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
def pterms():
	file=open('file.txt','r')
	target = open('pterms.txt','w')
	review=0
	a=0
	list_words=['']*5
	for line in file:
		
		if 'product/title:' in line:
			a=0
			line=line[len('product/title '):]
			list_words=['']*50
			review+=1
			for char in line:
				if char.isalnum()==True:
					list_words[a]+=str(char)
				else:
					a=a+1
			for word in list_words:
				if len(word)>=3:
					word=word.lower()+str(',')+str(review)+'\n'
					target.write(word)
	file.close()
	target.close()


def reviews():

	target = open('reviews.txt', 'w')
	f=open('file.txt','r')

	review=1

	for line in f:
		
		if 'product/productId:' in line:
			target.write(str(review))
			review=review+1
			target.write(',')
			target.write(str((line[len('product/productId: '):])).rstrip('\n'))
			target.write(',')

		if 'product/title:' in line: 
			target.write(str('"'+line[len('product/title: '):].rstrip('\n')+'"'))
			target.write(',')

		if 'product/price:' in line:
			target.write(line[len('product/price: '):].rstrip('\n'))
			target.write(',')

		if 'review/usrID:' in line:
			target.write(line[len('review/usrID: '):].rstrip('\n'))	
			target.write(',')

		if 'review/profileName:' in line:
			target.write(str('"'+line[len('review/profileName: '):].rstrip('\n')+'"'))
			target.write(',')

		if 'review/helpfulness:' in line:
			target.write(line[len('review/helpfulness: '):].rstrip('\n'))
			target.write(',')

		if 'review/score:' in line:
			target.write(line[len('review/score: '):].rstrip('\n'))	
			target.write(',')

		if 'review/time:' in line:
			target.write(line[len('review/time: '):].rstrip('\n'))
			target.write(',')

		if 'review/summary:' in line:
			target.write(str('"'+line[len('review/summary: '):].rstrip('\n')+'"'))
			target.write(',')	

		if 'review/text:' in line:
			temp=str('"'+line[len('review/text: '):].rstrip('\n')+'"'+'\n')
			target.write(temp)


	target.close()
	f.close()
	return

def rterms():
	
	target = open('rterms.txt', 'w')
	f=open('file.txt','r')
	newword=''
	review=0

	for line in f:
		if 'review/summary:' in line:
			line=line[len('review/summary '):]
			review+=1
			line_array=line.split()
			for words in line_array: 
				word=''
				for char in words:
					if char.isalnum()==True:
						word+=str(char)
					else:
						newword=word
						word=''
						if len(newword)>=3:
							newword=newword.lower()+str(',')+str(review)+'\n'
							target.write(newword)
				if len(word)>=3:
					word=word.lower()+str(',')+str(review)+'\n'
					target.write(word)

		elif 'review/text:' in line:
			line=line[len('review/text: '):]
			line_array=line.split()
			for words in line_array:
				word=''
				for char in words:
					if char.isalnum()==True:
						word+=str(char)
					else:
						newword=word
						word=''
						if len(newword)>=3:
							newword=newword.lower()+str(',')+str(review)+'\n'
							target.write(newword)
				if len(word)>=3:
					word=word.lower()+str(',')+str(review)+'\n'
					target.write(word)
				
	target.close()
	f.close()

	return 


def scores():
	target = open('scores.txt', 'w')
	f=open('file.txt','r')
	review=0

	for line in f:
		if 'review/score:' in line:
			review+=1
			line=line[len('review/score: '):].rstrip('\n')
			word=line+str(',')+str(review)+'\n'
			target.write(word)

	target.close()
	f.close()

	return
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
#PHASE 1
def phase1():
	reviews()
	pterms()
	rterms()
	scores()





#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
#PHASE 2


def phase2():
	return 

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------










#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
#PHASE 3


def phase3():
	return 

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------



def main():
	#	This is an example of reading file from stdin and printing contents
	org_file = open(sys.argv[1])
	replaced_file = open('file.txt','w')

	for line in org_file:
		line=line.replace('"','&quot;')
		line=line.replace("\"","\\")
		replaced_file.write(line)
	org_file.close()
	replaced_file.close()

	phase1()
	return


main()



