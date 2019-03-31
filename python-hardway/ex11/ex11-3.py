print "What time is it right now?"
time = raw_input()

germ_time = int(time) + 5
eth_time = int(germ_time) + 2

print "It is %s in Germany and %s in Ethiopia." % (germ_time, eth_time)

#Attempted to print the time and convert it to German and Ethiopian time. Initially, I received an error due to not being able to
#Concatenate a string and integer object. I had to list the variables using the int() parameter to convert the raw output to an integer.
# However, I could not use 11:15 I had to use just 11. I suppose time variables will come in later chapters.
