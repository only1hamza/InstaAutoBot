import requests

def tgmsg(text):
    token = ""
    chat_id = ""
    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    result = requests.get(url_req)
    if str(result) == "<Response [200]>" : print("Notification has sent to telegram")
    else: print("Error : Notification has not sent to telegram")
