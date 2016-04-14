"""
Title: JSON-Formatter
Author: Cortlan Bainbridge (bainbric@uni.edu)
Version: 1.0
Description:  Makes JSONs more human readable (adds whitespacing with depth)
"""
import json
import sys
import argparse
import os
import glob

#Arguments
parser = argparse.ArgumentParser(description="Make a JSON human readable")
parser.add_argument('-f', action="store",required=False,help="Specifiy a file name")
parser.add_argument('-c', action="store_true",required=False,help="Cleans the directory of all formatted JSONs")
args = parser.parse_args()

TAB = "\t"
NL = "\n"

def main():
	if args.c:
		cleanDirectory()
		return
	if args.f:
		verified = checkFileName(args.f)
		if verified:
			print("File has been verified, rewritting json")
			## Begin formatting ##
			depth = 0
			fileO = open(args.f,"r")
			fileOut = open(args.f[0:-5]+"-formatted.json","w")
			fileContents = fileO.readlines()
			for line in fileContents:
				index = 0
				for character in line:
					if character=="{":
						if depth==0:
							fileOut.write("\t"*depth+character)
						else:
							fileOut.write("\n")
							fileOut.write("\t"*depth+character)
						depth += 1
					elif character==",":
						fileOut.write(character)
						fileOut.write("\n")
					elif character=="}":
						depth -= 1
						fileOut.write("\n"+"\t"*depth+character)
					elif character=="\"":
						if depth==0:
							fileOut.write(character)
						else:
							if line[index+1]==":":
								fileOut.write(character)
							elif line[index-1]=="{":
								fileOut.write("\n"+("\t"*depth)+character)
							elif line[index+1]==",":
								fileOut.write(character)
							elif line[index+1]=="}":
								fileOut.write(character)
							else:
								fileOut.write("\t"*depth+character)						
					else:
						fileOut.write(character)
					index += 1
			fileO.close()
			fileOut.close()
			print("File wrote to "+args.f[0:-5]+"-formatted.json")
	else:
		print("ERROR: You need to specify a file name")

def checkFileName(fileName):
	fileName1 = fileName.split(".")
	if fileName1[-1]!="json":
		return False
	else:
		if os.path.isfile(fileName):
			return True
		else:
			print("File doesn't exist")
	return False

def cleanDirectory():
	counter = 0
	files = glob.glob(os.getcwd()+"\*")
	print("Cleaning the directory of past update scripts...")
	for specificFile in files:
		specificFileSplit = specificFile.split("/")
		if "formatted.json" in specificFileSplit[-1]:
			os.remove(specificFile)
			print("Removed "+specificFile)
			counter += 1
	print("    Removed "+str(counter)+" formatted jsons.")

main()