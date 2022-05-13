try:import requests,re
except Exception as FL:exit(FL)
print("""
██████╗ ████████╗████████╗██╗  ██╗████████╗
██╔══██╗╚══██╔══╝╚══██╔══╝╚██╗██╔╝╚══██╔══╝
██████╔╝   ██║█████╗██║    ╚███╔╝    ██║   
██╔═══╝    ██║╚════╝██║    ██╔██╗    ██║   
██║        ██║      ██║   ██╔╝ ██╗   ██║   
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝   ╚═╝                                             
        By @TweakPY - @vv1ck """)
print('-'*30)
text=input("[+] Type Your Text: ")
print('-'*30)
try:
	req=requests.post('https://leaked.wiki/paste',headers={'Host': 'leaked.wiki','Cookie': 'socials=yes','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '16','Origin': 'https://leaked.wiki','Referer': 'https://leaked.wiki/paste','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Te': 'trailers','Connection': 'close'},data=f'pdata={text}')
	id=re.findall('<script type="text/javascript"> location.href = "./p/(.*?)"; </script>',req.text)[0]
	local_paste=f'https://leaked.wiki/r/{id}.txt'
	print(f'[+] Your Paste in a raw is: {local_paste}');print('')
	print(f'[+] Your Text is: {requests.get(local_paste).text}')
except:
	try:
		problem=re.findall('''        <div class="container">
            <span class="status-reason">
                <i class="fas fa-user-times fa-2x"></i> (.*?)
            </span>
        </div>''',req.text)[0]
		if problem=='Account Suspended':print('[!] Sorry the website we use has a problem > "leaked.wiki"')
		else:print('[!] Error !!')
	except:print('[!] Error !!')
