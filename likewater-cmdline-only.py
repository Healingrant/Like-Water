import re
import random
#import pickle

# Pulls three (3) Random Phrase from 'phrases-general-[version].csv'.

userInput = ''
yinyang = ''
yangyin = ''
fo = ['']
genfile = open("phrases-general-v0.1.6.csv", "r")
yinfile = open("phrases-yin-v0.1.1.csv", "r")
yangfile = open("phrases-yang-v0.1.1.csv", "r")


def phraseOutput (userInput):
	if userInput == yinyang:
		with yinfile as source:
			lines = [line for line in source]
		fo = random.sample(lines, 3)
		with yangfile as source:
			lines = [line for line in source]
		fo2 = random.sample(lines, 3)
		print fo[0], fo2[0]
	
	else:
		with userInput as source:
			lines = [line for line in source]
		fo = random.sample(lines, 3)
		print fo[0]
	
def main():
	userInput = input("Enter Command (genfile, yinfile, yangfile, or yinyang:")
#	if userInput == yinyang:
		
#	elif userInput == yangyin:
#		print phraseOutput(yangfile), phraseOutput(yinfile)
#	else:
	print phraseOutput(userInput)

main()

# # # # # # # # # #
# save to file?
# with open("new_file.csv", "wb") as sink:
# sink.write("\n".join(random_choice))






