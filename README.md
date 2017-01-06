# webseurity
python code for web security
#!/usr/bin/env python

import mechanize
from bs4 import BeautifulSoup



def banner():
	print "##################################"
	print " This is mechanize class"
	print "#################################"


def browser():
	print " #############################"
	print " For Form Field "
	print "##############################"
	br=mechanize.Browser()
	cookies=mechanize.CookieJar()
	br.set_cookiejar(cookies)
	br.set_handle_robots(False)
	#br.set_all_readonly(False)
	print " Browser 1"
	br.open('http://www.facebook.com')
	for form in br.forms():
		print form

	print "########################"
	print "links"
	print "######################"
	#for link in br.links():
	#	print link.text+ ':' + link.url
	
	br.select_form(nr=0) # first form 
	br.form["email"]="reality_subash@hotmail.com"
#	br.click_link(id="next")
	#br.submit()
	br.form["pass"]="sub@sh@12"
	
#	#br.select_form(nr=1) # second form
	#br.click_link(id='signIn')
	br.submit()
	print br.response().read()
	#print "#####################"
	#print " response after click "
	#print "###################"
	#html= br.response().read()
	#ls=BeautifulSoup(html,'lxml')
	#for link in ls.find_all('a'):
	#	print link.get('href')
	#print ls.title
	print "############################"
	print "Browser 2"
	print "############################"
	br1=mechanize.Browser()
	br1.set_handle_robots(False)
	br1.set_cookiejar(cookies)
	br1.open('http://www.facebook.com')
	print br1.title()	

	

banner()
browser()
