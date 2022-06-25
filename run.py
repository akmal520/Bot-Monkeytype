from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from time import sleep
from pyautogui import typewrite

opt = Options()
opt.add_argument("log-level=3")
opt.add_argument('--ignore-ssl-errors=yes')
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

bot = webdriver.Chrome(executable_path=CM().install(), options=opt, desired_capabilities=dc)

bot.get('https://monkeytype.com/')

bot.maximize_window()

wait(bot, 20).until(EC.presence_of_element_located((By.XPATH, '//div[text()="Accept all"]'))).click()

sleep(5)
words = wait(bot, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[40]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]')))
ActionChains(bot).move_to_element(words).click(words).perform()

sleep(10)
teks = wait(bot, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'word')))

bot.implicitly_wait(5)

for i in teks:
    typewrite(i.text+" ", interval=0.045)


print("SELESAI")
sleep(60)
