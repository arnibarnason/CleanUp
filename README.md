# CleanUp
This script can be placed and run in any folder containing shows that need to be sorted.

The to run the script you need to type ./clean.py and then you place the two parameters.
The first parameter is the name of the show to be sorted and the second is the name and path of the folder it should be placed in after sorting.
The script will then find all shows containing the name as the start of the file name (if the name of the show is not at the beginning of the filename, the show does not deserve to be sorted) and place them into the specified folder and there it will be placed into a folder named after the show, then a folder named after the season of the show and finally the show file it self.
The script should also remove all .txt, .nfo, dat files associated with the files to be moved and then remove all empty folders

Example of usage (after placing the script in the downloads folder to be sorted): ./clean.py "how i met YOUR Mother" "~/Shows"

