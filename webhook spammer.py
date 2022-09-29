import pyautogui
from dhooks import Webhook

Webhook1 = pyautogui.prompt(text='enter webhook url here:', title= 'webhook spammer by londonplayz')

hook = Webhook(Webhook1)

MassageToSpam = pyautogui.prompt(text='what massage you want to spam(It @everyone bta', title= 'webhook spammer by londonplayz')
while True:
    hook.send((MassageToSpam) + "@everyone")