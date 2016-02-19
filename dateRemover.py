import json
import sys
import argparse
import os

parser = argparse.ArgumentParser(description="Make a JSON human readable")
parser.add_argument('-f', action="store",required=False,help="Specifiy a file name")
args = parser.parse_args()

def main():
	if args.f:
		fileRead = open(args.f,"r")
		fileWrite = open(args.f[0:-5]+"-dr.json","w")
		for line in fileRead:
			if "time" not in line:
				fileWrite.write(line)
		fileWrite.close()
		fileRead.close()







main()