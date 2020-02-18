
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# function to take care of downloading file
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

# instantiate a chrome options object so you can set the size and headless preference
# some of these chrome options might be uncessary but I just used a boilerplate
# change the <path_to_download_default_directory> to whatever your default download folder is located
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "/home/max/test/",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="<path_to_chrome_driver>")

# change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file
download_dir = "home/max/test/"

# function to handle setting up headless download
enable_download_headless(driver, download_dir)

# launch salesforce login page
driver.get("https://login.salesforce.com")
# fill form and login
search_input = driver.find_element_by_css_selector('#main-col > div > div > div:nth-child(8) > p:nth-child(1) > a > img')
search_input.click()
# wait for report loaded
driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);

# go to report
driver.get("https://sec-b2b.my.salesforce.com/00O0K00000AoDI7")
# wait for report loaded
driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
# initialize an object to the location on the html page and click on it to download
search_input = driver.find_element_by_css_selector('.reportActions ')
search_input.click()



# go to second report
driver.get("https://sec-b2b.my.salesforce.com/00O0K00000AnxJv")
# wait for report loaded
driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
# initialize an object to the location on the html page and click on it to download
search_input = driver.find_element_by_css_selector('.reportActions')
search_input.click()



# samples
#driver.find_element_by_xpath("//input[@class='ttAH_button03']").click()
#WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ws")))
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='inputlong' and @id='identificacionUsuario']"))).send_keys("your_name")
#driver.find_element_by_xpath("//input[@id='claveConsultiva' and @name='claveConsultiva']").send_keys("your_password")
#driver.find_element_by_link_text("Entrar no NetBanco Particulares").click()
