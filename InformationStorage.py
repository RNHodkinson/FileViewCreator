# Boiler plate Python..:: Information to Array ::..

import os
import os.path
import glob


while(True):
	print("Welcome :)\n1) View files\n2) Input to file list")
	welChoice = input(":")
	if(welChoice == '1' or welChoice == '2'):
		if(welChoice == '1'):
			os.system("clear")
			print("Your Files Are:\n")
			
			fileList = glob.glob('*.txt')
			for filei in fileList:
				print('%d ). %s'%(fileList.index(filei),filei))

			
			numSel = True
			while(numSel):
				print("\nselect file by \'Number\' to open\nor ctrl+z to quit")
				numSelected = input(":")
				try:
					numSelected = int(numSelected)
				except:
					print("not a Number try again")
					continue
				if(numSelected > len(fileList)):
					print("Not on the list try again")
					continue
				else:
					os.system('gedit %s'%(fileList[numSelected]))
					break
		else:
			os.system("clear")
			print("What would you like to name the file?")
			fName = input(":")
			os.system("gedit %s"%(fName))
			break
	else:
		print("Try again with NUMBER 1 or 2")
	break

