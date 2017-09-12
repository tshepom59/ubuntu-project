#!/usr/bin/python3

import csv
import random

'''Write a program to randomly select an EIT to pitch an idea
# read the csv file
# put data from file in a struture that we can work with in Python (dictionary)
# print details of EIT up for a pitch
# group the eits into nexus and ubuntu classes
'''
klass = input('Enter class name: ')

while klass.lower() not in ('ubuntu', 'nexus'):
	print('Like seriously? "{}" is not a valid class name'.format(klass))
	klass = input('Enter class name: ')

no_of_pitchees = int(input('How many pitchees do you want? '))

with open('eits-2018.csv') as file_handler:
	reader = csv.DictReader(file_handler)
	# eits = [eit for eit in reader] # list comprehension
	eits = []

	for eit in reader:
		if eit['klass'].lower() == klass:
			eits.append(eit)

	for i in range(no_of_pitchees):
		pitchee = random.choice(eits)

		print("\nName: {name}\nClass: {klass}\nCountry: {country}\nGender: {gender}\n".format(**pitchee))
