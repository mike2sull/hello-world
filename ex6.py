#Variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not) #StringInString 1

print x
print y

print "I said: %r." % x  #StringInString 2
print "I also said: '%s'" % y #StringInString 3

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #StringInString 4

w = "This is the left side of..."
e = "a string with a right side."

print w + e #Concatenate two strings together