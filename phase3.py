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
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
#PHASE 3

def review_search(text):
	database_rt = db.DB()
	database_rt.open("rt.idx")
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
	database_pt.open("pt.idx")
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
	database_rw.open("rw.idx")
	curs_rw=database_rw.cursor()

	iter = curs_rw.first()
	while iter:
		data = iter[1]
		key=iter[0]
		data=data.decode("utf-8")
		data=data.split()
		if text in data:
			list.append(key.decode("utf-8"))
		iter=curs_rw.next()



	curs_rw.close()
	database_rw.close()
	return




def price_search(price,sign,value):
	#need to read in price in database
	database_rw = db.DB()
	database_rw.open("rw.idx")
	curs_rw=database_rw.cursor()





	curs_rw.close()
	database_rw.close()

	return





def date_search(command,sign,date):
	#read in time
	#time=time.strftime("%D %H:%M", time.localtime(int(time)))

	return






def part_search(text):
	database_rw = db.DB()
	database_rw.open("rw.idx")
	curs_rw=database_rw.cursor()

	iter = curs_rw.first()
	while iter:
		data = iter[1]
		key=iter[0]
		data=data.decode("utf-8")
		if text in data:
			list.append(key.decode("utf-8"))
		iter=curs_rw.next()



	curs_rw.close()
	database_rw.close()
	return






def score_search(score,sign,value):
	database_rw = db.DB()
	database_rw.open("rw.idx")
	curs_rw=database_rw.cursor()




	curs_rw.close()
	database_rw.close()
	return

def update_list():
	global new_
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
	for i in list:
		if i in new_list:
			update.append(i)
	new_list=update
	list=[]
	return

def phase3():
	database_rw = db.DB()
	database_rw.open("rw.idx")
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
				command=command.split('%')
				command=command[0]
				part_search(command)
			else:
				if ((len(command)>=3) and (command.isalnum()==True)):
					full_search(command)
			list=set(list)
			list=sorted(list)
			check()

		if len(new_list)==0:
			new_list=list
		iter=curs_rw.first()
		while iter:
			data = iter[1]
			key=iter[0]
			if key.decode("utf-8") in new_list:
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
	phase3()
	subprocess.call('rm rt.idx',shell=True)
	subprocess.call('rm pt.idx',shell=True)
	subprocess.call('rm sc.idx',shell=True)
	subprocess.call('rm rw.idx',shell=True)

	return






main()
