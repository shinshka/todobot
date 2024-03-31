import sys

import requests

token = '6803792823:AAHcezYfCtEFtB05-t_nJGvZKTn3w1V8LDk'

request = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={sys.argv[1]}&text={sys.argv[2]}"
requests.get(request)
