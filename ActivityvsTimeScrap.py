import mechanize


url = "https://www.facebook.com/login"

op = mechanize.Browser()
op.set_handle_robots(False)
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows:U:Windows NT 6.0: en-US: rv:1.9.0.6)')]

op.open(url)

"""
for i in op.forms():
        print(i)

"""
email = raw_input("Username :")
password = raw_input("Password :")

op.select_form(nr=0)
"""
<POST https://www.facebook.com/login.php?login_attempt=1 application/x-www-form-urlencoded
  <HiddenControl(lsd=AVr23Y9Imlc) (readonly)>
  <HiddenControl(display=) (readonly)>
  <HiddenControl(enable_profile_selector=) (readonly)>
  <HiddenControl(legacy_return=1) (readonly)>
  <HiddenControl(profile_selector_ids=) (readonly)>
  <HiddenControl(trynum=1) (readonly)>
  <HiddenControl(timezone=) (readonly)>
  <HiddenControl(lgnrnd=114506_j3kq) (readonly)>
  <HiddenControl(lgnjs=n) (readonly)>
  <TextControl(email=)>
  <PasswordControl(pass=)>
  <CheckboxControl(persistent=[1])>
  <HiddenControl(default_persistent=0) (readonly)>
  <SubmitControl(login=Connexion) (readonly)>>
"""
op.form["email"] = email
op.form["pass"] = password

op.submit()
print(op.title)

if op.title() != "Facebook":
    print ("Name or pass wrong")


else:
           print("")
           print("Success")

"""Scraper la facet de gauche           

import urllib
urls1=["https://www.facebook.com/belhal.karimi","https://www.facebook.com/people/Marjane-Kotity/100005725576273","https://www.facebook.com/mathieuvaloatto?fref=tl_fr_box&pnref=lhc.friends"]
urls=[]
fi = open('malefriend.csv','w')
fi.write("Lives"+";"+"Born"+";"+"Studies"+";"+"Studied" + ";" + "From" + "\n")

i=0

for i, item in enumerate(urls):
    html_content = op.open(urls[i]).read()
    """print(urls[i])
    print (html_content.title)"""
    str1 = html_content.find("_50f3\">Lives")
    str2 = html_content.find("_50f3\">Born")
    str3 = html_content.find("_50f3\">Studies")
    str4 = html_content.find("_50f3\">Studied")
    str5 = html_content.find("_50f3\">From")
    live=str(str1)
    born=str(str2)
    studies=str(str3)
    studied=str(str4)
    fr=str(str5)
    """print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str5)"""
    fi.write(live + ";" + born + ";" + studies + ";" + studied + ";" + fr + "\n")


fi.close()
"""
"""Scraper le wall directement"
urls=[]

