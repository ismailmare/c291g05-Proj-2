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
import subprocess
import re
from bsddb3 import db





#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

def pterms():
	file=open('file.txt','r')
	target = open('pterms.txt','w')
	review=0
	newword=''

	for line in file:
		if 'product/title:' in line:
			line=line[len('product/title '):]
			review+=1
			strippedList=re.sub('[^0-9a-zA-Z_]',' ',line)
			#pattern = re.compile('([^\s\w]|_)+')
			#strippedList = pattern.sub(' ', line)
			strippedList=strippedList.split()
			for word in strippedList:
				if len(word)>=3:
					newword=word.lower()+str(',')+str(review)+'\n'
					target.write(newword)
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
	file=open('file.txt','r')
	target = open('rterms.txt','w')
	review=1
	newword=''
	read=False
	read1=False

	for line in file:
		if 'review/summary' in line:
			read= True
			line=line[len('review/summary '):]
			strippedList=re.sub('[^0-9a-zA-Z_]',' ',line)
			#pattern = re.compile('([^\s\w]|_)+')
			#strippedList = pattern.sub(' ', line)
			strippedList=strippedList.split()
			for word in strippedList:
				if len(word)>=3:
					newword=word.lower()+str(',')+str(review)+'\n'
					target.write(newword)

		if 'review/text' in line:
			read1= True
			line=line[len('review/text '):]
			strippedList=re.sub('[^0-9a-zA-Z_]',' ',line)
			#pattern = re.compile('([^\s\w]|_)+')
			#strippedList = pattern.sub(' ', line)
			strippedList=strippedList.split()
			for word in strippedList:
				if len(word)>=3:
					newword=word.lower()+str(',')+str(review)+'\n'
					target.write(newword)
		if (read==True) and (read1==True):
			review+=1
			read=False
			read1=False

	file.close()
	target.close()



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


def main():
	#	This is an example of reading file from stdin and printing contents
	try:
		org_file = open(sys.argv[1])
	except:
		print("\n"+"Input file not provided!"+"\n")
		return
	replaced_file = open('file.txt','w')

	for line in org_file:
		line=line.replace('"','&quot;')
		line=line.replace("\\","\\\\")
		replaced_file.write(line)
	org_file.close()
	replaced_file.close()

	phase1()

	return






main()
