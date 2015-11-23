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
from csv import reader
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
	subprocess.call('sort rterms.txt | uniq -u',shell=True)
	subprocess.call('sort pterms.txt | uniq -u',shell=True)
	subprocess.call('sort scores.txt | uniq -u', shell=True)

	database_rw = db.DB()
	database_pt = db.DB()
	database_rt = db.DB()
	database_sc = db.DB()

	database_sc.set_flags(db.DB_DUP) 
	database_rt.set_flags(db.DB_DUP) 
	database_pt.set_flags(db.DB_DUP)


	database_rw.open("rw.rdx",None,db.DB_HASH,db.DB_CREATE)
	database_pt.open("pt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	database_rt.open("rt.rdx",None,db.DB_BTREE,db.DB_CREATE)
	database_sc.open("sc.rdx",None,db.DB_BTREE,db.DB_CREATE)

	db_load_prep("scores.txt") #Now files loaded for db called: scores_load.txt
	db_load_prep("pterms.txt") #Now files loaded for db called: pterms_load.txt
	db_load_prep("rterms.txt") #Now files loaded for db called: rterms_load.txt
	db_load_prep_reviews("reviews.txt") #Now files loaded for db called: reviews_load.txt

	curs_rw=database_rw.cursor()
	subprocess.call('db_load -f reviews_load.txt -T -t hash rw.rdx',shell=True)
	#test#################
	#iter = curs_rw.first()
	#while iter:
	#	print(iter)
	#	iter=curs_rw.next()
	######################

	curs_rw.close()
	database_rw.close()

	curs_rt=database_rt.cursor()
	subprocess.call('db_load -f rterms_load.txt -T -t btree rt.rdx',shell=True)
	
	#test#################
	#iter = curs_rt.first()
	#while iter:
	#	print(iter)
	#	iter=curs_rt.next()
	######################

	curs_rt.close()
	database_rt.close()

	curs_pt=database_pt.cursor()
	subprocess.call('db_load -f pterms_load.txt -T -t btree pt.rdx',shell=True)
	
	#test#################
	#iter = curs_pt.first()
	#while iter:
	#	print(iter)
	#	iter=curs_pt.next()
	######################

	curs_pt.close()
	database_pt.close()

	curs_sc=database_sc.cursor()
	subprocess.call('db_load -f scores_load.txt -T -t btree sc.rdx',shell=True)
	
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
	database_rt.open("rt.rdx")
	curs_rt=database_rt.cursor()

	iter = curs_rt.first()
	while iter:
		data = iter[1]
		key=iter[0]
		if text == key.decode("utf-8"):
			list.append(data.decode("utf-8"))
		iter=curs_rt.next()

	curs_rt.close()
	database_rt.close()
	return


def product_search(text):
	database_pt = db.DB()
	database_pt.open("pt.rdx")
	curs_pt=database_pt.cursor()
	iter = curs_pt.first()
	while iter:
		data = iter[1]
		key=iter[0]
		if text == key.decode("utf-8"):
			list.append(data.decode("utf-8"))
		iter=curs_pt.next()

	curs_pt.close()
	database_pt.close()
	return



def full_search(text):
	database_rw = db.DB()
	database_rw.open("rw.rdx")
	curs_rw=database_rw.cursor()

	iter = curs_rw.first()
	while iter:
		data = iter[1]
		key=iter[0]
		if text in data.decode("utf-8"):
			list.append(key.decode("utf-8"))
		iter=curs_rw.next()



	curs_rw.close()
	database_rw.close()
	return



#preyanshu
def price_search(price,sign,value):
	#The 8th query is the same as the third query except the query 
	#only returns those records where price is present and has a 
	#value less than 60. Note that there is no index on the price 
	#field; this field is checked after retrieving the candidate 
	#records using conditions on which indexes are available 
	#(e.g. terms) need to read in price in database

	database_rw = db.DB()
	database_rw.open("rw.rdx")
	curs_rw=database_rw.cursor()
	iter = curs_rw.first()
	while iter:
		key=iter[0]
		data=iter[1]
		data=data.decode("utf-8")
		data=data.split('"')
		priceitem = data[2]
		priceitem=priceitem.strip(",")
		try :
			priceitem=int(priceitem)
		except:
			iter=curs_rw.next()
		if sign =="=":
			if value == priceitem:
				list.append(key.decode("utf-8"))
				iter=curs_rw.next()

		elif sign == "<":
			if value < priceitem:
				list.append(key.decode("utf-8"))
				iter=curs_rw.next()
		elif sign == ">":
			if value >priceitem:
				list.append(key.decode("utf-8"))
				iter=curs_rw.next()
		else:
			iter=curs_rw.next()


	curs_rw.close()
	database_rw.close()

	return





def date_search(command,sign,date):
	#read in time
	#time=time.strftime("%D %H:%M", time.localtime(int(time)))
	database_rw = db.DB()
	database_rw.open("rw.rdx")
	curs_rw=database_rw.cursor()
	iter = curs_rw.first()
	while iter:
		key=iter[0]
		data=iter[1]
		data=data.decode("utf-8")
		data=data.split('"')
		tempdata=data[4]
		tempdata = tempdata.split(",")
		timestamp= tempdata[3]
		print (timestamp)
		#print(datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
)

	return






def part_search(part_word):
	database_rt = db.DB()
	database_rt.open("rt.rdx")
	curs_rt=database_rt.cursor()
	database_pt = db.DB()
	datbase_pt.open("rt.rdx")
	curs_pt=database_pt.cursor()




	curs_rt.close()
	database_rt.close()
	curs_pt.close()
	database_pt.close()	

	return






def score_search(score,sign,value):
	database_rw = db.DB()
	database_rw.open("rw.rdx")
	curs_rw=database_rw.cursor()




	curs_rw.close()
	database_rw.close()
	return

def update_list():
	global list
	if len(list)==0:
		return
	else:
		for i in list:
			new_list.append(i)
		list=[]
	return

def check():
	global new_list
	global list
	if len(new_list)==0:
		return
	update=[]
	if len(list)>=len(new_list):
		for i in list:
			if i in new_list:
				update.append(i)
	else:
		for i in new_list:
			if i in list:
				update.append(i)
	new_list=update
	list=new_list
	return

def phase3():

	database_rw = db.DB()
	database_rw.open("rw.rdx")
	curs_rw=database_rw.cursor()
	global new_list
	new_list=[]
	global list
	list=[]
	global query
	print("\nWelcome to the Query Interface\n")
	while True:
		list=[]
		new_list=[]
		query=input("\nPlease enter your Query, (q) to quit: ")
		print('\n')
		if query=='q':
			break
		query=query.split()
		for i in range(len(query)):
			update_list()
			command=query[i]
			if 'p:' in command:
				command=command[len('p:'):]
				product_search(command)
			elif 'r:' in command:
				command=command[len('r:'):]
				review_search(command)
			elif 'pprice' in command:
				price_search(command,query[i+1],query[i+2])
			elif 'rdate' in command:
				date_search(command,query[i+1],query[i+2])
			elif 'rscore' in command:
				score_search(command,query[i+1],query[i+2])
			elif '%' in command:
				part_search(command)
			else:
				if ((len(command)>=3) and (command.isalnum()==True)):
					full_search(command)
			list=set(list)
			list=sorted(list)
			check()

		iter=curs_rw.first()
		while iter:
			data = iter[1]
			key=iter[0]
			if key.decode("utf-8") in list:
				print('\n')
				print(data.decode("utf-8"))
			iter=curs_rw.next()





	print("\nHave a nice day!\n")
	curs_rw.close()
	database_rw.close()
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
	subprocess.call('rm rt.rdx',shell=True)
	subprocess.call('rm pt.rdx',shell=True)
	subprocess.call('rm sc.rdx',shell=True)
	subprocess.call('rm rw.rdx',shell=True)

	return






main()



