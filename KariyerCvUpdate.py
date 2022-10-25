from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from gtts import gTTS 
import os


#cd "C:\Program Files\Google\Chrome\Application"
#chrome.exe --remote-debugging-port=3487 --user-data-dir="C:\...................\Selenium\chromeProfile2"

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:3487")
driver=webdriver.Chrome(executable_path="C:\\Users\\........................Selenium\\chromedriver.exe",chrome_options=opt)


# driver.get('https://www.kariyer.net/tum-ozgecmisler/')
# time.sleep(5)

tts = gTTS(text='日本語があまり話せない', lang='ja')
tts = gTTS(text='日本語があまり話せない .............. 私は日本語をほとんど知りません', lang='ja')
tts.save("6.mp3")
os.system("6.mp3")






Cv1 = '/html/body/div[1]/div/div/div[3]/div/div/div/nav/div[1]/div/div[2]/span/div[1]/div[2]/div/div/a[1]'
Cv2 = '/html/body/div[1]/div/div/div[3]/div/div/div/nav/div[1]/div/div[2]/span/div[2]/div[2]/div/div/a[1]'

click=1

while True:

    driver.find_element_by_xpath(Cv1).click()
    print(f"clicked   1---- {click}")
    # os.system("1.mp3")
    time.sleep(127)

    driver.find_element_by_xpath(Cv2).click()
    print(f"clicked   2---- {click}")
    # os.system("2.mp3")
    time.sleep(257)

    click=click+1
    os.system("6.mp3")
    
    if click>333:
        print(time.localtime())
        break
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")
# os.system("4.mp3")