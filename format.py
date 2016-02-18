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

#Arguments
parser = argparse.ArgumentParser(description="Make a JSON human readable")
parser.add_argument('-f', action="store",required=False,help="Specifiy a file name")
args = parser.parse_args()

TAB = "\t"
NL = "\n"

def main():
	if args.f:
		verified = checkFileName(args.f)
		if verified:
			print("File has been verified, rewritting emails")
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
							fileOut.write(character)
						else:
							fileOut.write("\n")
							fileOut.write("\t"*depth+character)
						depth += 1
					elif character==",":
						fileOut.write(character)
						fileOut.write("\n")
					elif character=="}":
						depth -= 1
						fileOut.write(character)
					elif character=="\"":
						if depth==0:
							fileOut.write(character)
						else:
							if line[index+1]==":":
								fileOut.write(character)
							elif line[index-1]=="{":
								fileOut.write(character)
							elif line[index+1]==",":
								fileOut.write(character)
							elif line[index+1]=="}":
								fileOut.write(character)
							else:
								fileOut.write("\t"*depth+character)						
					else:
						fileOut.write(character)
					index += 1
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

main()