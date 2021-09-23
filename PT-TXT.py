try:import requests,re,os
except:
	os.system('pip install requests')
	os.system('pip install re')
	print('[-] Done')
print("""
██████╗ ████████╗████████╗██╗  ██╗████████╗
██╔══██╗╚══██╔══╝╚══██╔══╝╚██╗██╔╝╚══██╔══╝
██████╔╝   ██║█████╗██║    ╚███╔╝    ██║   
██╔═══╝    ██║╚════╝██║    ██╔██╗    ██║   
██║        ██║      ██║   ██╔╝ ██╗   ██║   
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝   ╚═╝                                             
<\> @TweakPY """)
print('-'*30)
text=input("[+] Type Your Text: ")
print('-'*30)
h={
	'Host': 'leaked.wiki',
	'Cookie': 'socials=yes',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Length': '16',
	'Origin': 'https://leaked.wiki',
	'Referer': 'https://leaked.wiki/paste',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User': '?1',
	'Te': 'trailers',
	'Connection': 'close'}
d=f'pdata={text}'
try:
	req=requests.post('https://leaked.wiki/paste',headers=h,data=d)
	id=re.findall('<script type="text/javascript"> location.href = "./p/(.*?)"; </script>',req.text)[0]
	local_paste=f'https://leaked.wiki/r/{id}.txt'
	print(f'[+] Your Paste in a raw is: {local_paste}')
	print('')
	print(f'[+] Your Text is: {requests.get(local_paste).text}')
except:print('[~] Error !!')
