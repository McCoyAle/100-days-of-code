# This line creates variable x listing number of types of people.
x = "There are %d types of people." % 10

# Creates variable called binary that is a string binary
binary = "binary"

# Creates a variable do_not that is a string don't
do_not = "don't"

# Creates a variable y that is a string and includes variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)


# Prints variables x and y to the terminal but shows the strings for both variables not the actual variable.
print x
print y

# Prints a string that includes format characters for x and y.
print "I said: %r." % x
print "I also said: '%s' ." % y

# Creates a variable hilarious that is false
hilarious = False
#Creates joke_evaluation variable, with a string that includes a formating character r.
joke_evaluation = "Isn't that joke so funny!? %r"

#Prints joke_evaluation and hilarious variables
print joke_evaluation % hilarious

#Creates two variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# Prints the two variables w and e that were previously created and concatenates them instead of printing two separate strings
print w + e
