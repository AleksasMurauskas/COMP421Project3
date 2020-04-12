import psycopg2
import sys
import pandas as pd
import matplotlib.pyplot as plt





#if __name__ == "__main__":


def main():
	#connect to database
	passw = "Cinema2078"
	#print("please enter the password for cs421g78:")
	#pw= str(input())
	connection = psycopg2.connect(user="cs421g78",
		password=passw,
		host="comp421.cs.mcgill.ca",
		port="5432",
		database="cs421")
	print("Wlecome to the CinemaClub Databse Interace")
	print("")
	display_menu()

	while(1): #infinite loop for user inputs 
		use_in= str(input())
		if(int(use_in)==0): #prompted menu to be displayed  
			display_menu()
		if(int(use_in)==10): # prompted exit 
			exit_prog()
		if(int(use_in)==1):
			processOne()
		if(int(use_in)==2):
			processTwo()
		if(int(use_in)==3):
			processThree()
		if(int(use_in)==4):
			processFour()
		if(int(use_in)==5):
			processFive()


def processOne():
	print("placeholder1")

def processTwo():
	print("placeholder2")

def processThree():
	print("placeholder3")


def processFour():
	print("placeholder4")

def processFive():
	print("placeholder5")




def exit_prog():
	#close connection to database
	conn = None
	print("Exiting Program")
	sys.exit()


def display_menu():
	print("-----------------Program Menu-----------------")
	print("Enter the associted number to begin a process:")	
	print("0: Redisplay Menu")
	print("1: Query 1")
	print("2: Query 2")
	print("3: Query 3")
	print("4: Query 4")
	print("5: Query 5")
	print("10: Exit Program")


main()
