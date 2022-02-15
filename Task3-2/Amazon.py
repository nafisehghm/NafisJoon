from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Open Amazon and search Shoes
s=Service('E:\ChromeWebdriver\chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='https://www.amazon.com/'
browser.get(url)
print(browser.title)
browser.find_element(By.ID,'twotabsearchtextbox').send_keys('shoes')
browser.find_element(By.ID,'nav-search-submit-button').click()

#verify Shoes page loads successfully


try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'a-m-us a-aui_72554-c a-aui_accordion_a11y_role_354025-c a-aui_killswitch_csa_logger_372963-c a-aui_launch_2021_ally_fixes_392482-c a-aui_pci_risk_banner_210084-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c a-meter-animate'))


finally:
    print("Page loaded")

#Select a shoe

browser.find_element(By.PARTIAL_LINK_TEXT, 'Loafer Flat').click()

#verify selection

try:
    element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Loafer Flat'))


finally:
    print("Selection Verified")



