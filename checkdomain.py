print("##     ## ########  ######## ##    ##  #######  ########  ########")
print(" ##   ##  ##     ## ##       ##   ##  ##     ## ##     ## ##")       
print("  ## ##   ##     ## ##       ##  ##   ##     ## ##     ## ##")      
print("   ###    ########  ######   #####    ##     ## ##     ## ######")   
print("  ## ##   ##   ##   ##       ##  ##   ##     ## ##     ## ##")       
print(" ##   ##  ##    ##  ##       ##   ##  ##     ## ##     ## ##")       
print("##     ## ##     ## ######## ##    ##  #######  ########  ########")
print('')

import urllib
while True:
	u = raw_input("Input domain: ")
	u1 = u.replace("http://www.","").replace("https://www.","").replace("/","")
	u2 = "http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=%s" % u1
	c = urllib.urlopen(u2)
	c1 = c.read()
	c2 = int(c1.count("still available"))
	if c2 == 1:
		print "Domain %s is still available" % u1
	else:
		print "Domain %s has already been registered" % u1
	print ""
	raw_input("Enter to check another domain!")
	print""