import argparse
import re
import os

parser = argparse.ArgumentParser(description="""Finds all TV-shows with same name as the first
        parameter and puts them into the folder specified in the second parameter""")
parser.add_argument('show', help='Name of the show to sort')
parser.add_argument('folder', help='Path to and the of the folder to contain the show')
args = parser.parse_args()

s = args.show
x = s.replace(' ', '.')
for root, dirs, files in os.walk('dl'):
    for f in files:
        found = re.search(x + '.(S([0-9][0-9]))*', f, re.I)
		season = "Season " + found.group(2)
		print(f, "season: ", season)
        if found != None:
            if not os.path.exists(args.folder):
                os.makedirs(args.folder)
            print(os.path.join(os.path.abspath(root),f))
            os.rename(os.path.join(os.path.abspath(root),f), os.path.join(args.folder,f))    
