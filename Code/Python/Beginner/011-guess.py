import random
R = random.randrange(1,100)

print "Guess a number between 1 and 100!"
N = input("Enter a number : ")
i = 1
while (N!=R):
    if N>R:
        print "Too big... try again"
    else:
        print "Too small.. try again"
    N = input("Enter a number: ")
    i=i+1
print "You got it in", i, "tries"
