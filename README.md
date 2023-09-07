# InstaAutoBot
AutoBot For Instagram Automations v1.3 beta
Free open source script, only for education and research purpse
Use this script as your resposability

Before open Run.py, Install necessary packages by using pip
- selenuim
- tqdm
- webdriver

#Features
- Auto send bulk DM instgram messages to bulk users list
- Auto trying again code
- Notification by telegram api

#Use InstaAutoBot
1-
open Run.py, write your instagram usrname and pasword (Better to not use your personal one)
my_username = 'your ID'
my_password = 'your Pass'
2-
Choose how much attepttry when failed to execute some line of code
triesParam = 5
3-
Fill the file users.txt with list of user you want to send message to (Line by line)
Fill the file messages.txt with list of messages you want to send (Line by line) the bot with choose randomly one message per user
4- 
Integrate your telegram Bot to receive messsage and updates whene script is running, edit telegram_api.py

Thank you
