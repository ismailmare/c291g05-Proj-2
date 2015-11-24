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


	database_rw.open("rw.idx",None,db.DB_HASH,db.DB_CREATE)
	database_pt.open("pt.idx",None,db.DB_BTREE,db.DB_CREATE)
	database_rt.open("rt.idx",None,db.DB_BTREE,db.DB_CREATE)
	database_sc.open("sc.idx",None,db.DB_BTREE,db.DB_CREATE)

	#db_load_prep("scores.txt") #Now files loaded for db called: scores_load.txt
	#db_load_prep("pterms.txt") #Now files loaded for db called: pterms_load.txt
	#db_load_prep("rterms.txt") #Now files loaded for db called: rterms_load.txt
	#db_load_prep_reviews("reviews.txt") #Now files loaded for db called: reviews_load.txt

	curs_rw=database_rw.cursor()
	#subprocess.call('db_load -f reviews_load.txt -T -t hash rw.idx',shell=True)
	subprocess.call('cat reviews.txt |./perl_script.pl | db_load -T -t hash rw.idx',shell=True)
	#test#################
	#iter = curs_rw.first()
	#while iter:
	#	print(iter)
	#	iter=curs_rw.next()
	######################

	curs_rw.close()
	database_rw.close()

	curs_rt=database_rt.cursor()
	#subprocess.call('db_load -f rterms_load.txt -T -t btree rt.idx',shell=True)
	subprocess.call('cat rterms.txt |./perl_script.pl | db_load -T -t btree rt.idx',shell=True)
	#test#################
	#iter = curs_rt.first()
	#while iter:
	#	print(iter)
	#	iter=curs_rt.next()
	######################

	curs_rt.close()
	database_rt.close()

	curs_pt=database_pt.cursor()
	#subprocess.call('db_load -f pterms_load.txt -T -t btree pt.idx',shell=True)
	subprocess.call('cat pterms.txt |./perl_script.pl | db_load -T -t btree pt.idx',shell=True)
	#test#################
	#iter = curs_pt.first()
	#while iter:
	#	print(iter)
	#	iter=curs_pt.next()
	######################

	curs_pt.close()
	database_pt.close()

	curs_sc=database_sc.cursor()
	#subprocess.call('db_load -f scores_load.txt -T -t btree sc.idx',shell=True)
	subprocess.call('cat scores.txt |./perl_script.pl | db_load -T -t btree sc.idx',shell=True)
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




# Main()


def main():
	phase2()
	return






main()
