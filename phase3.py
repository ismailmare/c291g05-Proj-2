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
		data=re.sub('[^0-9a-zA-Z_]',' ',data)
		data=data.lower()
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

	#locate cursor where price is (4)
	#if v.startswith(price):
		#if rID not in list:
			#list.append()
	
	
	
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
		data=re.sub('[^0-9a-zA-Z_]',' ',data)
		data=data.lower()
		if text in data:
			list.append(key.decode("utf-8"))
		iter=curs_rw.next()

	#try and use _.startswith('word') helps a lot
	#A = 'heloobelonie'
	#if A.startswith('heloobelonie'):
	#print(A)



	curs_rw.close()
	database_rw.close()
	return




 

def score_search(score,sign,value):
	database_sc = db.DB()
	database_sc.open("sc.idx") #I changed it to use the scores index
	curs_sc=database_sc.cursor()

	#NOTe: .get() only retrieving the value (rID)
	#I'm not sure if we need to do while loop because i think when we use get() it should list all of them
	#iter = cur.first()
	#if database.get(db'score') not in list:
	#	list.append()
	#iter = cur.next()
	iter = curs_sc.first()
	value=float(value)
	while iter:
		data=iter[1]
		key=iter[0]
		key = key.decode("utf-8")
		key = float(key)
		data = data.decode("utf-8")
		if sign =='>':
			if key>value:
				list.append(data)
		elif sign =='<':
			if key<value:
				list.append(data)
		elif sign =='=':
			if key==value:
				list.append(data)
		iter=curs_sc.next()


	curs_sc.close()
	database_sc.close()
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
			command=query[i]
			if 'p:' in command:
				update_list()
				command=command[len('p:'):]
				product_search(command)
			elif 'r:' in command:
				update_list()
				command=command[len('r:'):]
				review_search(command)
			elif 'pprice' in command:
				update_list()
				price_search(command,query[i+1],query[i+2])
			elif 'rdate' in command:
				update_list()
				date_search(command,query[i+1],query[i+2])
			elif 'rscore' in command:
				update_list()
				if len(command)> len('rscore'):
					sign=command[len('rscore'):len(command)-1]
					value=command[len('rscore')+1:len(command)]
					command='rscore'
					score_search(command,sign,value)
				else:
					score_search(command,query[i+1],query[i+2])
			elif '%' in command:
				update_list()
				command=command.split('%')
				command=command[0]
				part_search(command)
			else:
				if ((len(command)>=3) and (command.isalnum()==True)):
					update_list()
					full_search(command)
			list=set(list)
			list=sorted(list)
			if len(command)>1:
				check()


		if len(new_list)==0:
			new_list=sorted(new_list)
			new_list=list
		iter=curs_rw.first()
		print(new_list)
		while iter:
			data = iter[1]
			key=iter[0]
			if key.decode("utf-8") in new_list:
				print('\n')
				data=data.decode("utf-8")
				data=data.split('"')
				print("product/productId: %s" %data[0])
				print("product/title: %s" %data[1])
				price=data[2].split(',')
				print("product/price: %s" %price[1])
				print("review/userId: %s" %price[2])
				print("review/profileName: %s" %data[3])
				stuff=data[4].split(',') 
				print("review/helpfulness: %s" %stuff[1])
				print("review/score: %s" %stuff[2])
				print("review/time: %s" %stuff[3])
				print("review/summary: %s" %data[5])
				print("review/text: %s" %data[7])				
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
