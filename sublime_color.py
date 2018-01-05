# Tested + passed.
# Working as of 01/03/18
# needs  tweaking.

import fileinput
import os
from datetime import datetime
import time


sublime_dir = '/home/developer/Desktop/github scripts'	# Your sublime dIrectory.

def dawn_mode():	# this function activates dawn mode: bright color.
	s = open("Preferences.txt").read()	# reads the sublime preferences file.
	s = s.replace('dusk', 'dawn')		# replaces the theme: dark to light.
	f = open("Preferences.txt", 'w')		# opens preferences file in write mode.
	f.write(s)				# writes the changes to the file.
	f.close()				# closes the file to prevent memory leakage.					
	print('[+]Dawn Mode Activated')	

def dusk_mode():
	s = open("Preferences.txt").read()
	s = s.replace('dawn', 'dusk')
	f = open("Preferences.txt", 'w')
	f.write(s)
	f.close()
	print('[+]Dusk Mode Activated')



def main():	# main function. responsible for selecting any
	current_time = datetime.now().time()	# functions above. Dependent on time.
	if current_time.hour == 19 and current_time.minute == 48:
		dawn_mode()
		print(current_time)
	else:
		dusk_mode()
		print(current_time)

main()
