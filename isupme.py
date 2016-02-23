#Deverloped by Xrekode
#February 23rd 2016

print("##     ## ########  ######## ##    ##  #######  ########  ########")
print(" ##   ##  ##     ## ##       ##   ##  ##     ## ##     ## ##")       
print("  ## ##   ##     ## ##       ##  ##   ##     ## ##     ## ##")      
print("   ###    ########  ######   #####    ##     ## ##     ## ######")   
print("  ## ##   ##   ##   ##       ##  ##   ##     ## ##     ## ##")       
print(" ##   ##  ##    ##  ##       ##   ##  ##     ## ##     ## ##")       
print("##     ## ##     ## ######## ##    ##  #######  ########  ########")
print('')
import urllib
import time
#Main
u = raw_input('Input domain: ')
u1 = u.replace("http://","").replace("https://","")
u2 = "http://www.isup.me/%s" % u1
print "Crt+C to stop"
while True:
	c = urllib.urlopen(u2)
	c1 = c.read()
	up = int(c1.count("It's just you"))
	if up == 1:
		print "This site is up"
	else:
		print "This site is down"
	time.sleep(4)