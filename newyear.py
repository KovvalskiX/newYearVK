import vk_api
import time
from random import randint

silent = False

def mode():
    askmode = input("[НАСТРОЙКА] Выводить лог в консоль? (Y/N) ")
    global silent
    if askmode == "y" or askmode == "Y":
        return;
    elif askmode == "n" or askmode == "N":
        silent = True
        return;
    else:
        mode()

mode()

def wait():
    if time.gmtime(time.time()).tm_sec != 0:
        time.sleep(0.5)
        wait()
    else: return;
if silent==False:print("[LOG] Жду следующей минуты для корректного отображения.")
wait()
if silent==False:print("[LOG] Запущено. Импортирую модули.")

session = vk_api.VkApi(token=input("Токен с правами friends, status, offline: "))
session._auth_token()

if silent==False:print("[LOG] Авторизация...")

vk = session.get_api()
if silent==False:print("[LOG] Успех!")

n = time.gmtime(input("Введите 31.12.ГОД 23:59:59 в формате Timestamp: "))
if silent==False:print("[LOG] Таймер установлен на " + n + ", запускаю цикл")
def tonewyear():
    ost = "🎄"+str(n.tm_mday - time.gmtime(time.time()).tm_mday) + " д. " + str(n.tm_hour - time.gmtime(time.time()).tm_hour) + " ч. " + str(n.tm_min - time.gmtime(time.time()).tm_min) + " мин.🎄"
    vk.status.set(text=ost,group_id="")
    if silent==False:print("[LOG] Установлен новый статус: " + ost + "\n[LOG] Жду 30 секунд.")
    time.sleep(30)
    friend()
def friend():
    frnds = list(vk.friends.get(fields="online",name_case="nom").items())
    rn=randint(0,frnds[0][1])
    if silent==False:print("[LOG] Рандомный друг №" + str(rn))
    ost = "🎲⭐" + frnds[1][1][rn]["first_name"] + ' ' + frnds[1][1][rn]["last_name"]+"⭐🎲"
    vk.status.set(text=ost,group_id="")
    if silent==False:print("[LOG] Установлен новый статус: " + ost + "\n[LOG] Жду 30 секунд.")
    time.sleep(30)
    tonewyear()
tonewyear()
