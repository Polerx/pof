import requests,time,colorama,json,random,string
from colorama import Fore,init
init()
import certifi
import urllib3
urllib3.disable_warnings()


print('''
By Rayan al-Juhani 
ig @h_p
''')



class report:
    def __init__(self):
        self.session = requests.Session()
        self.site_key = "6Ldt4CkUAAAAAJuBNvKkEcx7OcZFLfrn9cMkrXR8"
        self.url = "https://support.snapchat.com/"
        self.contents = open('config.json', 'r',encoding="latin-1",errors='ignore')
        self.data = json.load(self.contents)
        self.API_KEY = self.data['api_key']
        self.user = self.data['user']
        self.message = self.data['message']
        self.email = self.data['email']


    def captcha(self):
        try:
            captcha_id = self.session.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(self.API_KEY, self.site_key, self.url)).text.split('|')[1]
            recaptcha_answer = self.session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(self.API_KEY, captcha_id)).text
            print(Fore.White+"[Response] captcha solving...")
            while 'CAPCHA_NOT_READY' in recaptcha_answer:
                time.sleep(5)
                recaptcha_answer = self.session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(self.API_KEY, captcha_id)).text
            recaptcha_answer = recaptcha_answer.split('|')[1]
            return recaptcha_answer
        except Exception as e:
            print(e)


    def email_gen(self):
        ran = ('').join(random.choices(string.ascii_letters + string.digits, k=8))
        email = ran+"flaah9991@gmail.com"
        return email
   
    
    def report(self):
        emails = self.email_gen()
        answer1 = self.captcha()
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Host":"support.snapchat.com",
            "Accept-Encoding":"gzip, deflate",
            "Cookie":"sc_at=v2|H4sIAAAAAAAAAE3GyREAIQgEwIiowuUazQY8ojD4/dqvjk/SsJNE6pCWgnKa08qjfaXE5LpNeTRDdw8D7lP+AR74ykdAAAAA",
            "Content-Type":"text/plain;charset=UTF-8"
        }
        data ='''key=ts-all-abuse-1&field-24394115=FALAH&field-24335325={}&field-24380496=There+is+no&field-24389845=cf-all-abuse-1-reportee-over-18&field-24335443={}&field-24335453=cf-all-abuse-1-reported-unknown&field-22808619={}&g-recaptcha-response={}&answers=5153567363039232,5657146641350656,5659936423936000,5701645388218368'''.format(self.email,self.user,self.message,answer1)
        send_report = self.session.post("https://support.snapchat.com/en-US/api/v2/send",data=data,headers=headers , verify=False)
		
        if send_report.status_code==200:
            print(Fore.GREEN+"[Requests] Done {}".format(self.user))		
        else:
            print(Fore.RED+"[Error] لا يمكن إرسال التقرير")

if __name__ == "__main__":
    while True:
        start = report()
        start.report()
