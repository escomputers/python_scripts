#!/bin/python3

import mysql.connector
import pandas


def main():
	colnames = ['Name', 'Phone']
	data = pandas.read_csv('contacts.csv', names=colnames)
	nomi = data.Name.tolist()
	recapiti = data.Phone.tolist()
	
	#convert each item in list into integer
	recapiti_converted = ([str(item) for item in recapiti])
	
	#remove spaces inside each string item in list
	recapiti_cleaned = ([s.replace(' ', '') for s in recapiti_converted])
	
	mydb = mysql.connector.connect(
	host="127.0.0.1",
	user="test",
	password="11111111111",
	database="testing"
	)
	mycursor = mydb.cursor()
	
	values_to_insert = list(zip(nomi,recapiti_cleaned))
	#CREATE A TABLE NAMED phonebook WITH 2 COLUMNS name and phone
	query = "INSERT INTO phonebook (name, phone) VALUES " + ",".join("(%s,%s)" for _ in values_to_insert)
	flattened_values = [item for sublist in values_to_insert for item in sublist]
	mycursor.execute(query, flattened_values)
	
	mydb.commit()
	mycursor.close()
		
if __name__ == '__main__':
	main()

