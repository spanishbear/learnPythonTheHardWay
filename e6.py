#Bind x with the print statement and formatted variable
x = "There are %d types of people." % 10
# Bind binary with the string binary
binary = "binary"
# Bind do_not with the string don't 
do_not = "don't"
# Bind y with the string statement and 2 formatted variable
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y 

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of.."
e = "a string with a right side."

print w + e
