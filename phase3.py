
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
		if text in data.decode("utf-8"):
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






def part_search(part_word):
	database_rw = db.DB()
	database_rw.open("rw.idx")
	curs_rw=database_rt.cursor()





	curs_rw.close()
	database_rw.close()

	return






def score_search(score,sign,value):
	database_rw = db.DB()
	database_rw.open("sc.idx") #I changed it to use the scores index
	curs_rw=database_rw.cursor()

	# NOTE: .get() only retrieving the value (rID)
	#I'm not sure if we need to do while loop because i think when we use get() it should list all of them
	#iter = cur.first()
	if database.get(db'score') not in list:
		list.append()
	#iter = cur.next()
	


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
	subprocess.call('rm rt.idx',shell=True)
	subprocess.call('rm pt.idx',shell=True)
	subprocess.call('rm sc.idx',shell=True)
	subprocess.call('rm rw.idx',shell=True)

	return






main()
