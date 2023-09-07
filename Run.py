from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
from datetime import datetime
from tqdm import tqdm
from telegrambot import tgmsg

# Timer
def timenow():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Log file
log = []

# Username and password of your instagram account:
my_username = 'your ID'
my_password = 'your Pass'
triesParam = 5
timeSleepUrlParam = random.randrange(10)
#timeSleepParam = random.randrange(5, 10)
timeSleepParam = random.randrange(2,4)

print('\033[92m' + '\033[1m' + "############################ Welcome to AutomationInstaByHamza v1.1 beta ############################")
print("Initializing... ")
tgmsg("▶️▶️▶️ Starting ◀️◀️◀️")

timestart = datetime.now()

# Username and messages lists Loading:
def read_users(path):
    try:
        with open(path, 'r') as file :
            userslist = file.read().splitlines()
        log.append(f'{timenow()} Users list Loaded Seccussfuly\n')
        return userslist
    except Exception as err:
        log.append(f'{timenow()} Error: {err}\n')
        log.append(f'{timenow()} Check {path} file if exist (Must be each users in one line)\n')
        print(err)
        quit() 

def read_messages(path):
    try:
        with open(path, 'r') as file :
            messagelist = file.read().splitlines()
        log.append(f'{timenow()} Messages list Loaded Seccussfuly\n')
        return messagelist
    except Exception as err:
        log.append(f'{timenow()} Error: {err}\n')
        log.append(f'{timenow()} Check {path} file if exist (Must be each message in one line)\n')
        print(err)
        quit()

usernames = read_users('users.txt')
if len(usernames) == 0:
    print(f"{timenow()} The Usernames list is empty") 
    quit()
messages = read_messages('messages.txt')
if len(messages) == 0:
    print(f"{timenow()} The Messages list is empty") 
    quit()

# Bot set-up
options = webdriver.ChromeOptions()
#options.add_argument("--window-size=1920,1080")
#options.add_argument("--headless")
options.add_experimental_option("detach", True)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
browser = webdriver.Chrome(options=options)

tgmsg("Bot is running...🤖")

# Authorization:
def auth(username, password):
    try:
        browser.get('https://instagram.com')
        time.sleep(10)

        print(f"{timenow()} Login In ...")

        input_username = browser.find_element(By.NAME, 'username')
        input_password = browser.find_element(By.NAME, 'password')

        enter_btn = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
    
        input_username.send_keys(username)
        time.sleep(timeSleepParam)
        input_password.send_keys(password)
        time.sleep(timeSleepParam)
        enter_btn.click()
        time.sleep(timeSleepParam)

        #Click Notification case 1
        """"
        tries = 0
        while tries < triesParam:
            try:
                notif = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                print(f"{timenow()} Logged In Successfuly")
                time.sleep(timeSleepParam)
                notif.click()
                break
            except Exception as err:
                tries += 1
                if tries == 1:
                    print(f"{timenow()} Waiting to Click Notification...")
                time.sleep(timeSleepParam)
        if tries >= triesParam:
            print(f"{timenow()} Error Timeout: Notification Popup not appeare")
            notifirst = False
        """
            
        log.append(f'{timenow()} User {username} Login Seccussfuly\n')
        print(f'{timenow()} User {username} Login Seccussfuly')
        time.sleep(timeSleepUrlParam)

    except Exception as err:
        log.append(f'{timenow()} Error: {err}\n')
        tgmsg("Error auth to instagram ❌")
        print(err)
        quit()

# SendDM:
def send_message(users, messages):
    print(f"{timenow()} Starting send DM ...")
    tgmsg("Bot is sending messages... 💬")
    NbrUsers = len(users)
    #Click Notification
    
    browser.get('https://www.instagram.com/direct/inbox/')
    tries = 0
    while tries < triesParam:
        try:
            time.sleep(timeSleepUrlParam)
            notif = browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            print(f"{timenow()} Logged In Successfuly")
            time.sleep(timeSleepParam)
            notif.click()
            break
        except Exception as err:
            tries += 1
            if tries == 1:
                print(f"{timenow()} Waiting to Click Notification...")
                time.sleep(timeSleepParam)
        if tries >= triesParam:
            print(f"{timenow()} Error Timeout: Notification Popup not appeare")
            quit()

    try:
        for user in users:
            
            time.sleep(timeSleepUrlParam)
            browser.get('https://www.instagram.com/direct/inbox/')
            
            #Click New Message
            tries = 0
            while tries < triesParam:
                try:
                    time.sleep(timeSleepUrlParam)
                    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div').click()
                    break
                except Exception as err:
                    tries += 1
                    if tries == 1:
                        print(f"{timenow()} Waiting to Click New Message...")

                    time.sleep(timeSleepParam)
            if tries >= triesParam:
                print(f"{timenow()} Error Timeout")
                quit()
			
            #Input user
            tries = 0
            while tries < triesParam:
                try:
                    userinput = browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')
                    time.sleep(timeSleepParam)
                    userinput.send_keys(user)
                    break
                except Exception as err:
                    tries += 1
                    if tries == 1:
                        print(f"{timenow()} Waiting to Input User...")

                    
                    time.sleep(timeSleepParam)
            if tries >= triesParam:
                print(f"{timenow()} Error Timeout")
                quit()

            #Select user
            tries = 0
            while tries < triesParam:
                try:
                    browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div').find_element(By.TAG_NAME, "input").click()
                    time.sleep(timeSleepParam)
                    break
                except Exception as err:
                    tries += 1
                    if tries == 1:
                        print(f"{timenow()} Waiting to Select User from list...")

                    time.sleep(timeSleepParam)
            if tries >= triesParam:
                print(f"{timenow()} Error Timeout")
                quit()

            #Button Chat User
            tries = 0
            while tries < triesParam:
                try:
                    go = browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')
                    time.sleep(timeSleepParam)
                    go.click()
                    time.sleep(timeSleepParam)
                    break
                except Exception as err:
                    tries += 1
                    if tries == 1:
                        print(f"{timenow()} Waiting to Click Chat User...")

                    time.sleep(timeSleepParam)
            if tries >= triesParam:
                print(f"{timenow()} Error Timeout")
                quit()

            #Write message
            tries = 0
            while tries < triesParam:
                try:
                    text_area = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
                    text_area.click() 
                    time.sleep(timeSleepParam)
                    messagepost = ''
                    text_area.send_keys(f"Hi {user.replace('_',' ').replace('.',' ')}\n")
                    time.sleep(timeSleepParam)
                    text_area.send_keys(f"{messagepost}\n")
                    time.sleep(timeSleepParam)
                    text_area.send_keys(random.choice(messages))
                    time.sleep(timeSleepParam)
                    break
                except Exception as err:
                    tries += 1
                    if tries == 1:
                        print(f"{timenow()} Waiting to Write Message...")

                    time.sleep(timeSleepParam)
            if tries >= triesParam:
                print(f"{timenow()} Error Timeout")
                quit()
            
            #Send Button
            tries = 0
            while tries < triesParam:
                try:
                    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').click()
                    break
                except Exception as err:
                    tries += 1
                    if tries == 1:
                        print(f"{timenow()} Waiting to Click Send Message...")

                    time.sleep(timeSleepParam)

            print(f'{timenow()} Message successfully sent to {user}')
            print(f'{timenow()} Messages to users sent: {users.index(user)+1}/{NbrUsers}')
            log.append(f'{timenow()} Messages to users sent: {users.index(user)}/{NbrUsers}')
            log.append(f'{timenow()} Message successfully sent to {user}\n')
            tgmsg(f"Message successfully sent to {user} ({users.index(user)+1}/{NbrUsers}) 📩")

            print(f'{timenow()} Please wait for next operation (This delay protect you account from getting restruction)')
            print(f'{timenow()} We advice to make the interval delay time from 10 to 20 minutes')

            delayPerMessageParam = random.randrange(600, 1200, 60)
            tgmsg(f'Next message in {delayPerMessageParam/60}min ⏳')
            for i in tqdm(range(delayPerMessageParam)):
                time.sleep(1)

        
        print(f"\n{timenow()} Congratulations, Task is complited")
        print(f"{timenow()} {NbrUsers} Messages are sent to {NbrUsers} User")
        tgmsg("Task is complited ✅")
        tgmsg(f"{NbrUsers} Message are sent to {NbrUsers} User ✅")
        print(f"{timenow()} You Will Find Details in Log file in same directory\n")
        log.append(f"{timenow()} {NbrUsers} Messages are sent to {NbrUsers} User")
        log.append(f'{timenow()} Task is complited')

    except Exception as err:
        print(err)
        log.append(f'{timenow()} Error: {err}\n')
        tgmsg("Bot is stopped because of some error ❌")
        #browser.quit()

def logger(log):
    with open('log.txt','w') as file:
        file.writelines(log)

# Starting of Script
auth(my_username, my_password)
time.sleep(random.randrange(2,4))
send_message(usernames, messages)

timeend = datetime.now()
total = str(timeend - timestart)
print(f'Total Time: {total[0]}h {total[2:3]}min')
tgmsg(f'Total Time: {total[0]}h {total[2:3]}min ⏱️')

logger(log)
browser.quit()
