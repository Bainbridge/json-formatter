"""
Title: JSON-Formatter
Author: Cortlan Bainbridge (cortlan.bainbridge@gmail.com)
Version: 1.1
Description:  Makes JSONs more human readable
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

def main():
	if args.c:
		cleanDirectory()
		return
	if args.f:
		verified = checkFileName(args.f)
		if verified:
			print("File has been verified, rewritting json")
			## Begin formatting ##
			formatFileName = args.f[0:-5]+"-formatted.json"
			with open(args.f, "r") as jsonFile:
				data = json.load(jsonFile)
				with open(formatFileName,"w") as fileOut:
					fileOut.write(json.dumps(data, indent=4, sort_keys=False))
			print("File wrote to "+formatFileName+"")
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
