import os

print('''
 #     #                                  ######                              
 #  #  # ###### ###### #####              #     # ######  ####   ####  #    # 
 #  #  # #      #      #    #             #     # #      #    # #    # ##   # 
 #  #  # #####  #####  #####     #####    ######  #####  #      #    # # #  # 
 #  #  # #      #      #    #             #   #   #      #      #    # #  # # 
 #  #  # #      #      #    #             #    #  #      #    # #    # #   ## 
  ## ##  ###### ###### #####              #     # ######  ####   ####  #    # 
                                                                  By:Kair_wne                                                                             
''')

url = input('Enter the complete website URL: ')
clean_url = input('Enter the clean URL, e.g., google.com: ')
wordlist = input('Enter the path to the wordlist for directories: ')
UserAgent = input('Enter the User-Agent: ')

mirrorweb = input('Would you like to clone the web page? [yes/no] ')
if mirrorweb == "yes":
    os.system('clear')
    os.system(f'wget -m {url}')
    os.system(f'wget -m -e robots=off {url}')
else:
    print('================================================================')

brute = input('Would you like to perform a brute force on directories and files? [yes/no]')
if brute == "yes":
    os.system('clear')
    os.system(f'dirb {url} {wordlist}')
    os.system(f'gobuster dir -e -u {url} -w {wordlist} -x .php,.txt,.sql,.bkp')
    os.system(f'gobuster dir -e -u {url} -w {wordlist} -x "200,301,302,401"')
else:
    print('================================================================')

subdomain = input('Would you like to perform a subdomain brute force? [yes/no] ')
if subdomain == "yes":
    os.system('clear')
    wordlist_sub = input('Enter the path to the subdomain wordlist: ')
    os.system(f'gobuster dns -d {clean_url} -w {wordlist_sub}')
else:
    print('================================================================')

http = input('Would you like to fetch the site header? [yes/no] ')
if http == "yes":
    os.system('clear')
    os.system(f'curl -s --head {url}')
    os.system(f'curl -v -H "User-Agent: {UserAgent}" {url}')
else:
    print('================================================================')

tec = input('Would you like to identify the technologies used on the site? [yes/no] ')
if tec == "yes":
    os.system('clear')
    os.system(f'whatweb -v {clean_url}')
else:
    print('================================================================')

pagint = input('Would you like to identify pages on the internet? [yes/no] ')
if pagint == "yes":
    os.system('clear')
    ext = input('Enter the extension you are searching for: ')
    os.system(f'lynx -dump "http://google.com/search?num=100&q=site:{clean_url}+ext:{ext}" | cut -d "=" -f2 | grep ".{ext}" | egrep -v "site|google" | sed s"/...$//"g')
else:
    print('End...')
