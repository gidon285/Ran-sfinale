import os

def sniffing():
    if os.path.exists("save.pcap"):
        os.remove("save.pcap")
    os.system('sudo wireshark -k -Y http -w /tmp/save.pcap')

sniffing()




























# def get_clear_browsing_button(driver):
#     """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
#     return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


# def clear_cache(driver, timeout=2):
#     """Clear the cookies and cache for the ChromeDriver instance."""
#     # navigate to the settings page
#     driver.get('chrome://settings/clearBrowserData')

#     # wait for the button to appear
#     wait = WebDriverWait(driver, timeout)
#     wait.until(get_clear_browsing_button)
    
#     # click the button to clear the cache
#     # get_clear_browsing_button(driver).click()
#     driver.find_element_by_xpath('//*[@id="clearBrowsingDataConfirm"]').click()
    

#     # wait for the button to be gone before returning
#     wait.until_not(get_clear_browsing_button)

# from selenium.webdriver.remote.webelement import WebElement
# def js():
#     return driver.execute_script("return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")

# # driver = webdriver.ChromeOptions()
# # driver.get("chrome://settings/clearBrowserData")
# # wait = WebDriverWait(driver, 10)
# # clearButton = driver.execute_script("return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog')")

# # #click on the clear button now
# # time.sleep(3)
# # clearButton.click()
#   command = ['echo','done!']
#     process = subprocess.Popen(command, stdout=subprocess.PIPE)
#     process.communicate()