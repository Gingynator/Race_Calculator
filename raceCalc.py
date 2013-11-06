#"""This function takes inputs for time and distance, then calculates and displays 
average mile time, and mph. If the input is in km it also converts it to mph."""

def race(name, hours, minutes, seconds, km, mi): 
    if km > 0:
        if hours > 0:
            print str(name) + " ran " + str(km) + "km in " + str(hours) + " hours " + str(minutes) + " minutes and " + str(seconds) + " seconds"
        else:
            print str(name) + " ran " + str(km) + "km in " + str(minutes) + " minutes and " + str(seconds) + " seconds"
        totalseconds = float(hours) * (60*60) + (float(minutes) * 60) + float(seconds)
	average_mile_minutes = ((float(totalseconds)/float(km)) * 1.61)/60
	average_mile_seconds = (average_mile_minutes%1) * 60
	print str(int(average_mile_minutes)) + " minutes and " + str(int(average_mile_seconds)) + " seconds is the average mile time"
	total_miles = float(km) / 1.61
	mile_decimal = totalseconds / 3600.0
	mph = total_miles / mile_decimal
	print str(round(mph, 2)) + "(mph) is how fast this person ran"
    elif not km > 0 and mi > 0:
	if hours > 0:
            if mi == 26.2:
		print str(name) + " ran a marathon in " + str(hours) + " hours " + str(minutes) + " minutes and " + str(seconds) + " seconds"
	    else:
		print str(name) + " ran " + str(mi) + "mi in " + str(hours) +" hours " + str(minutes) + " minutes and " + str(seconds) + " seconds"
	else: 
	    print str(name) + " ran " + str(mi) + "mi in " + str(minutes) + " minutes and " + str(seconds) + " seconds"  
	totalseconds = float(hours) * (60*60) + (float(minutes) * 60) + float(seconds)
	average_mile_minutes = float(totalseconds) / float(mi) / 60
	average_mile_seconds = (average_mile_minutes%1) * 60
	print str(int(average_mile_minutes)) + " minutes and " + str(int(average_mile_seconds)) + " seconds is the average mile time"
	mile_decimal2 = totalseconds / 3600.0
	mph = float(mi) / float(mile_decimal2)
	print str(round(mph, 2)) + "(mph) is how fast this person ran"
    else:
	print "What are you doing? What kind of race did you run?"

#Spoof race
race ("Jimmy Hendrix", 0, 43, 30, 0, 5)
print ""
#Real race, world record for fastest marathon!
race ("Geoffrey Mutai", 2, 3, 38, 0, 26.2)
print ""

#The i-- variables are inputs that will be the arguments for the race function
iname = raw_input("enter your name: ")
print ""
yon = raw_input("were you running in km y or n?: ")
if yon is "y":
    kilnumber = raw_input("how many kilometers?: ")
    milnumber = 0
    try:
	float(kilnumber)
    except:
	print "You must enter a number"
	exit()
elif yon is "n":
    kilnumber = 0
    milnumber = raw_input("how many miles?: ")
    try:
	float(milnumber)
    except:
	print "You must enter a number"
	exit()
else:
    print "your response must be y or n"
    exit()

ihrs = raw_input("how many hours did it take you?: ")
try:
    float(ihrs)
except:
    print "You must enter a number"
    exit()

imins = raw_input("how many minutes did it take you?: ")
try:
    float(imins)
except:
    print "You must enter a number"
    exit()

isecs = raw_input("how many seconds did it take you?: ")
try:
    float(isecs)
except:
    print "You must enter a number"
    exit()

print ""

race (iname, ihrs, imins, isecs, kilnumber, milnumber)

