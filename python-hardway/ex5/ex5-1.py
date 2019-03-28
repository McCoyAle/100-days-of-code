
name = 'Alexandra McCoy'
age = 31
height = 66 # inches
cm_height = height * 2.54
weight = 161 # lbs
kil_weight = weight * 0.453592
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She is also %d cm, if we convert inches." %cm_height
print "She's %d pounds heavy." % weight
print "If we convert pounds to kilos, she is %d kilos." % kil_weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky. Try to get it correct.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
