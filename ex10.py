tabbyCat = "\tI'm tabbed in." # \t inserts a tab
persianCat = "I'm split\non a line." # \n inserts a newline
backslashCat = "I'm \\ a \\ cat." #Double slash (\\) prints a single \

fatCat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#\t* creates a new bullet point in a bulleted list at the \t*

print tabbyCat
print persianCat
print backslashCat
print fatCat

thinCat = '''
Does this do the same thing as """?
It appears to!
'''

print thinCat

#Creates a little spinny thing
#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,