from sys import argv
from os.path import exists

script, fromFile, toFile = argv

inData = open(fromFile).read() 
open(toFile, 'w').write(inData)

#Meh.  One line is too messy - fuck that