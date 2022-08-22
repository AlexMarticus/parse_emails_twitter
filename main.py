import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def scroll_and_retirn_emails(n):
    emails = []
    driver.execute_script(f"window.scrollTo(0, {1080 * n});")
    time.sleep(5)
    for i in range(1, 13):
        try:
            a = driver.find_element(by=By.XPATH,
                                    value=f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                          f'2]/div/div/section/div/div/div[{str(i)}]').text
        except:
            break
        if '@gmail.com' in a:
            for j in a.split():
                if '@gmail.com' in j:
                    if j[0] in """><.,/?!@#$%^&*()_+-={}[]":'""":
                        j = j[1:]
                    if j[-1] in """><.,/?!@#$%^&*()_+-={}[]":'""":
                        j = j[:-1]
                    emails.append(j)
                    break
    return emails


option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotification.enabled', False)
option.set_preference('media.volume_scale', '0.0')
option.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) '
                                                    'Gecko/20100101 Firefox/97.0')
driver = webdriver.Firefox(options=option)
driver.get('https://twitter.com/sendbeatsbot')
print('Зарегистрируйтесь, после чего нажмите Enter')
input()
driver.get('https://twitter.com/sendbeatsbot')
n_emails = int(input('Введите кол-во почт: '))
time.sleep(10)
start_time = time.time()
emails = set()
try:
    for i in range(10000):
        for p in scroll_and_retirn_emails(i):
            emails.add(p)
            if len(emails) >= n_emails:
                print('Готово! Сейчас отправлю в телеграм')
                break
        print(f"Записано почт: {len(emails)}")
except:
    pass
url1 = "https://api.telegram.org/bot5482242421:AAEuN-wuEryNH-oyime_Fw0roQ7WZeutFVc/sendMessage?"
r1 = requests.post(url1, data={'chat_id': 'телеграм id человека', "text": '\n'.join(emails)})
if r1.status_code != 200:
    print('Ошибка в отправке почт в телеграм. Пропишу их здесь.')
    print('\n'.join(emails))

print(f'Время выполнения: {time.time() - start_time}')
