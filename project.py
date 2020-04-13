import psycopg2
import sys
import pandas as pd
import matplotlib.pyplot as plt


def main():

	movieIndexQuery= """CREATE INDEX employeeNames ON Employee(name);"""

	#connect to database
	passw = "Cinema2078"
	#print("please enter the password for cs421g78:")
	#pw= str(input())
	connection = psycopg2.connect(user="cs421g78",
		password=passw,
		host="comp421.cs.mcgill.ca",
		port="5432",
		database="cs421")
	print("Welcome to the CinemaClub Databse Interace")
	print("")
	display_menu()

	while(1): #infinite loop for user inputs 
		print("Input:", end=" ")
		use_in= str(input())
		if(use_in==""):
			print("Invalid Input, please try again")
			continue
		elif(int(use_in)==0): #prompted menu to be displayed  
			display_menu()
		elif(int(use_in)==10): # prompted exit 
			exit_prog(connection)
		elif(int(use_in)==1):
			processOne(connection)
		elif(int(use_in)==2):
			processTwo()
		elif(int(use_in)==3):
			processThree()
		elif(int(use_in)==4):
			processFour()
		elif(int(use_in)==5):
			processFive()
		else:
			print("Invalid Input, please try again")


def processOne(connection): #Make a New Employee
	

	print("What is their name?")
	#new_name= input()
	new_name= "Aleks"
	print("What is their address?")
	#new_add= input()
	new_add= "3434 St. Famille" 
	print("What is their new email?")
	#new_email= input()
	new_email= "avm@avm.ca"
	new_add= "3434 St. Famille" 
	print("Where do they work? please enter a cid")
	#new_cid= input()
	new_cid= "1461"
	print("What is new employeeID?")
	#new_eid= input()
	new_eid= "11111"
	print("What is their starting salary?")
	#new_sal= input()
	new_sal= "500000"
	Query ="""INSERT INTO employee (eid, cid, name, email, salary, address) VALUES ('"""
	Query_with_val = Query+new_eid+"', '"+new_cid+"', '"+new_name+"', '"+new_email+"','"+new_sal+"', '"+new_add
	Query_end="');"
	Query_fin = Query_with_val+Query_end
	#dat1 = pd.read_sql_query(Query_fin, connection)
	c = connection.cursor()
	c.execute(Query_fin)
	print(Query_fin)

def processTwo(): #What movie titles are screening on this date
	print("placeholder2")
	print("What is the date you would like to select")
	#in_date =input()
	in_date ="1919-06-26"
	query = """select name from screening s, movie m where s.movieid = m.movieid and date ='1919-06-26'"""
	q_input = """select name from screening s, movie m where s.movieid = m.movieid and date ="""
	q_fin = q_input+"'"+in_date+"';"

	dat1 = pd.read_sql_query(query, connection)
	dat1.set_index(['Movie Titles'])
	print("Movie Titles:\n")
	print(dat1.head())


def processThree(): #How many times has this item sold
	print("placeholder3")

def processFour(): # How many Items has a customer purchased
	print("placeholder4")

def processFive(): 
	print("placeholder5")
	print("What is the id of the ")




def exit_prog(connection):
	#close connection to database
	connection = None
	print("Exiting Program")
	sys.exit()


def display_menu():
	print("-----------------Program Menu-----------------")
	print("Enter the associted number to begin a process:")	
	print("0: Redisplay Menu")
	print("1: Create a new Employee")
	print("2: What movie screenings are on this date")
	print("3: Query 3")
	print("4: Query 4")
	print("5: Query 5")
	print("10: Exit Program")

main()
