#Deverloped by Xrekode
#February 24th 2016

print("##     ## ########  ######## ##    ##  #######  ########  ########")
print(" ##   ##  ##     ## ##       ##   ##  ##     ## ##     ## ##")       
print("  ## ##   ##     ## ##       ##  ##   ##     ## ##     ## ##")      
print("   ###    ########  ######   #####    ##     ## ##     ## ######")   
print("  ## ##   ##   ##   ##       ##  ##   ##     ## ##     ## ##")       
print(" ##   ##  ##    ##  ##       ##   ##  ##     ## ##     ## ##")       
print("##     ## ##     ## ######## ##    ##  #######  ########  ########")
print('')
#Main
import urllib
while True:
	u = raw_input("Input domain: ")
	u1 = u.replace("http://www.","").replace("https://www.","").replace("/","")
	u2 = "http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=%s" % u1
	c = urllib.urlopen(u2)
	c1 = c.read()
	c2 = int(c1.count("still available"))
	c3 = int(c1.count("has already been registered"))
	if c2 == 1:
		print "Domain %s is still available" % u1
	elif c3 == 1:
		print "Domain %s has already been registered" % u1	
	else:
		print "Domain %s was not supported" % u1
	print ""
	raw_input("Enter to check another domain!")
	print""
