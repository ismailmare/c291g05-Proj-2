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
from bsddb3 import db





#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
def pterms():
	file=open('file.txt','r')
	target = open('pterms.txt','w')
	review=0
	newword=''
	review=0

	for line in file:
		if 'product/title:' in line:
			line=line[len('product/title '):]
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


def db_load_prep(filename):
	target=open(filename,'r')
	write=(filename.split('.'))[0]+"_load"+".txt"
	write1=open(write,'w')
	for line in target:
		second_half=''
		contents=line.split(',')
		write1.write(contents[0])
		write1.write('\n')
		for i in range(1,len(contents)):
			second_half+=contents[i]
		write1.write(second_half)
	target.close()
	write1.close()
	return




def db_load_prep_reviews(filename):
	target=open(filename,'r')
	write=(filename.split('.'))[0]+"_load"+".txt"
	write1=open(write,'w')
	for line in target:
		second_half=''
		contents=line.split(',')
		write1.write(contents[0])
		write1.write('\n')
		for i in range(1,len(contents)):
			if i > 1:
				second_half+=","+contents[i]
			else:
				second_half+=contents[i]
		write1.write(second_half)
	target.close()
	write1.close()



def phase2():
	subprocess.call('sort rterms.txt | uniq -u',shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	subprocess.call('sort pterms.txt | uniq -u',shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	subprocess.call('sort scores.txt | uniq -u', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

	database_rw = db.DB()
	database_pt = db.DB()
	database_rt = db.DB()
	database_sc = db.DB()

	database_sc.set_flags(db.DB_DUP) 

	database_rw.open("rw.rdx",None,db.DB_HASH,db.DB_CREATE)
	database_pt.open("pt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	database_rt.open("rt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	database_sc.open("sc.rdx",None,db.DB_BTREE,db.DB_CREATE)

	db_load_prep("scores.txt") #Now files loaded for db called: scores_load.txt
	db_load_prep("pterms.txt") #Now files loaded for db called: pterms_load.txt
	db_load_prep("rterms.txt") #Now files loaded for db called: rterms_load.txt
	db_load_prep_reviews("reviews.txt") #Now files loaded for db called: reviews_load.txt

	curs_rw=database_rw.cursor()
	subprocess.call('db_load -f reviews_load.txt -T -t hash rw.rdx',shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

	#test#################
	#iter = curs_rw.first()
	#while iter:
	#	print(iter)
	#	iter=curs_rw.next()
	######################

	curs_rw.close()
	database_rw.close()

	curs_rt=database_rt.cursor()
	subprocess.call('db_load -f rterms_load.txt -T -t btree rt.rdx',shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	
	#test#################
	#iter = curs_rt.first()
	#while iter:
	#	print(iter)
	#	iter=curs_rt.next()
	######################

	curs_rt.close()
	database_rt.close()

	curs_pt=database_pt.cursor()
	subprocess.call('db_load -f pterms_load.txt -T -t btree pt.rdx',shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	
	#test#################
	#iter = curs_pt.first()
	#while iter:
	#	print(iter)
	#	iter=curs_pt.next()
	######################

	curs_pt.close()
	database_pt.close()

	curs_sc=database_sc.cursor()
	subprocess.call('db_load -f scores_load.txt -T -t btree sc.rdx',shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	
	#test#################
	#iter = curs_sc.first()
	#while iter:
	#	print(iter)
	#	iter=curs_sc.next()
	######################

	curs_sc.close()
	database_sc.close()

	return 

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------










#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
#PHASE 3

def review_search(text):
	database_rt = db.DB()
	database_rt.open("rt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	curs_rt=database_rt.cursor()






	curs_rt.close()
	database_rt.close()
	return


#Preyanshu
def product_search(text):
	database_pt = db.DB()
	database_pt.open("pt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	curs_pt=database_rt.cursor()
        #product_list=[]
        iter = curs_rt.first()
	while iter:
		print(iter)
		iter=curs_rt.next()
                if text in iter[1]:
                        print(iter[1])



	curs_pt.close()
	database_pt.close()
	return

def full_search(text):
	database_rt = db.DB()
	database_rt.open("rt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	curs_rt=database_rt.cursor()
	database_pt = db.DB()
	database_pt.open("rt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	curs_pt=database_pt.cursor()




	curs_rt.close()
	database_rt.close()
	curs_pt.close()
	database_pt.close()	

	return




def price_search(price,sign,value):
	#need to read in price in database
	database_rw = db.DB()
	database_rw.open("rt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	curs_rw=database_rw.cursor()





	curs_rw.close()
	database_rw.close()

	return





def date_search(command,sign,date):

	return






def part_search(part_word):
	database_rt = db.DB()
	database_rt.open("rt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	curs_rt=database_rt.cursor()
	database_pt = db.DB()
	database_pt.open("rt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	curs_pt=database_pt.cursor()




	curs_rt.close()
	database_rt.close()
	curs_pt.close()
	database_pt.close()	

	return






def score_search(score,sign,value):
	database_rw = db.DB()
	database_rw.open("rw.rdx",None,db.DB_BTREE,db.DB_CREATE)
	curs_rw=database_rw.cursor()






	curs_rw.close()
	database_rw.close()
	return





def phase3():
	global query
	while True:
		query=input("\nPlease enter your Query, (q) to quit: ")
		print('\n')
		if query=='q':
			break
		query=query.split()
		for i in range(len(query)):
			command=query[i]
			if 'p:' in command:
				product_search(command)
			elif 'r:' in command:
				review_search(command)
			elif 'pp' in command:
				price_search(command,query[i+1],query[i+2])
			elif 'rdate' in command:
				date_search(command,query[i+1],query[i+2])
			elif 'rscore' in command:
				score_search(command,query[i+1],query[i+2])
			elif '%' in command:
				part_search(command)
			else:
				full_search(command)


	print("\nHave a nice day!\n")
	
	return 

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
# Main()


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
	phase2()
	phase3()

	return






main()



