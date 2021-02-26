from selenium import webdriver

import time

browser = webdriver.Firefox()

browser.get("https://www.instagram.com/")
time.sleep(2)

idm = browser.find_element_by_name("username")
passw = browser.find_element_by_name("password")


# write your user name and password to logn and pas areas.
logn = ""
pas = ""
idm.send_keys(logn)
passw.send_keys(pas)

buton = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
buton.click()

#login part completed.
time.sleep(7)
browser.get("https://www.instagram.com/"+logn+"/")
time.sleep(5)
options = browser.find_elements_by_css_selector(".Y8-fY ")
followers_part = options[1]
followers_part.click()
time.sleep(3)

editor = """
toscroll = document.querySelector(".isgrP");
toscroll.scrollTo(0, toscroll.scrollHeight);
var cc=toscroll.scrollHeight;
return cc;

"""


#scroll events
cc = browser.execute_script(editor)
match=False
while(match==False):
    lastCount = cc
    time.sleep(2)
    cc = browser.execute_script(editor)
    if lastCount == cc:
        match=True
time.sleep(5.5)
lastlist = []
followers1 = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

#text file operations
for eleman in followers1:
    lastlist.append(eleman.text)

with open("allfollowers.txt","w",encoding = "UTF-8") as file:
    for follower in lastlist:
        file.write(follower+"\n")
        
    

browser.close()
