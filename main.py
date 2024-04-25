from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import dotenv_values
import time

env_vars = dotenv_values()

# Get the values of USERNAME and PASSWORD variables from the dictionary
username = env_vars.get("USERNAME")
password = env_vars.get("PASSWORD")

driver = webdriver.Chrome()
driver.maximize_window()

# Scenario 1: Log in to my WordPress site.
def login_to_wordpress(username, password):
    driver.get("http://ashraful3885.unaux.com/wp-admin/index.php")
    driver.find_element(By.ID, "user_login").send_keys(username)
    driver.find_element(By.ID,"user_pass").send_keys(password)
    driver.find_element(By.ID,"wp-submit").click()

# Scenario 2: Check whether the "WP Dark Mode" Plugin is Active or not
def is_dark_mode_plugin_active():
    driver.get("http://ashraful3885.unaux.com/wp-admin/plugins.php")

    # Check if "WP Dark Mode" is present in the page source
    if "WP Dark Mode" in driver.page_source:
        activate_element = driver.find_elements(By.XPATH, "//a[@id='activate-wp-dark-mode']")
        if activate_element:
            text_content = activate_element[0].text
            if text_content == "Activate":
                activate_dark_mode_plugin()
        else:
            deactivate_element = driver.find_elements(By.XPATH, "//a[@id='deactivate-wp-dark-mode']")
            if deactivate_element:
                text_content = deactivate_element[0].text
                if text_content == "Deactivate":
                    time.sleep(5)
    else:
        install_and_activate_dark_mode_plugin()


# Scenario 3: If Active, navigate to the WP Dark Mode & continue. Otherwise, Install the Plugin and Activate it.
def install_and_activate_dark_mode_plugin():
    # Install the plugin
    driver.find_element(By.XPATH,"//a[@class='page-title-action']").click()
    driver.find_element(By.XPATH,"//input[@id='search-plugins']").send_keys("WP Dark Mode")
    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"//a[@aria-label='Install WP Dark Mode – WordPress Dark Mode Plugin for Improved Accessibility, Dark Theme, Night Mode, and Social Sharing 5.0.4 now']"))
    ).click()
    #Activate the plugin
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[@aria-label='Activate WP Dark Mode']"))).click()
    time.sleep(5)

def activate_dark_mode_plugin():
    driver.find_element(By.XPATH, "//a[@id='activate-wp-dark-mode']").click()
    time.sleep(5)

# Scenario 4: Enable Backend Darkmode
def enable_backend_darkmode():
    driver.find_element(By.XPATH, "//div[contains(text(),'WP Dark Mode')]").click()
    driver.find_element(By.XPATH,"//a[@class='nav-item-child focus:outline-none inactive']").click()
    driver.find_element(By.XPATH,"//div[@class='relative w-10 h-full rounded-full transition duration-100 bg-slate-200']").click()
    saveSetting = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//button[@class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']"))
    )
    saveSetting.click()


# Scenario 6: Navigate to the WP Dark Mode
def navigate_to_wp_dark_mode():
    driver.find_element(By.XPATH, "//div[contains(text(),'WP Dark Mode')]").click()


# Scenario 7: Change the Floating Switch Style
def change_floating_switch_style():
    driver.find_element(By.XPATH, "//div[contains(text(),'WP Dark Mode')]").click()

    driver.find_element(By.XPATH, "//h4[normalize-space()='Customization']").click()

    switchSetting = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Switch Settings']"))
    )
    switchSetting.click()

    # Scroll to a floating switch style section
    floatingSwitchStyle = driver.find_element(By.XPATH,"//h3[normalize-space()='Floating Switch Styles']")
    driver.execute_script("arguments[0].scrollIntoView();", floatingSwitchStyle)

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/section[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]").click()

    saveSetting = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']"))
    )
    saveSetting.click()


# Scenario 8: Custom Switch size & set it to 220.
def select_custom_switch_size():
    driver.find_element(By.XPATH, "//div[contains(text(),'WP Dark Mode')]").click()

    driver.find_element(By.XPATH, "//h4[normalize-space()='Customization']").click()

    switchSetting = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Switch Settings']"))
    )
    switchSetting.click()

    # Scroll to a switch customization section
    switchCustomization = driver.find_element(By.XPATH, "//div[@class='flex flex-col gap-1 text-base leading-6 text-black font-medium'][normalize-space()='Switch Customization']")
    driver.execute_script("arguments[0].scrollIntoView();", switchCustomization)

    driver.find_element(By.XPATH, "//div[@class='cursor-pointer flex items-center gap-2 py-2 transition duration-75 px-3.5 text-base font-normal leading-6 rounded-lg bg-gray-100 hover:bg-gray-200']//span[contains(text(),'Custom')]").click()
    customSize = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
    customSize.clear()
    customSize.send_keys('220')

    saveSetting = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//button[@class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']"))
    )
    saveSetting.click()


# Scenario 9: Change the Floating Switch Position
def change_floating_switch_position():
    driver.find_element(By.XPATH, "//div[contains(text(),'WP Dark Mode')]").click()

    driver.find_element(By.XPATH,"//h4[normalize-space()='Customization']").click()

    switchSetting = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Switch Settings']"))
    )
    switchSetting.click()

    # Scroll to the switch customization section
    switchCustomization = driver.find_element(By.XPATH, "//div[@class='flex flex-col gap-1 text-base leading-6 text-black font-medium'][normalize-space()='Switch Customization']")
    driver.execute_script("arguments[0].scrollIntoView();", switchCustomization)

    driver.find_element(By.XPATH, "//span[normalize-space()='Left']").click()

    saveSetting = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']"))
    )
    saveSetting.click()


# Scenario 10: Disable Keyboard Shortcut
def disable_keyboard_shortcut():
    driver.find_element(By.XPATH, "//div[contains(text(),'WP Dark Mode')]").click()

    driver.find_element(By.XPATH, "//h4[normalize-space()='Advanced']").click()

    accessibility = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Accessibility']"))
    )
    accessibility.click()

    # Scroll to a specific section
    specificSection = driver.find_element(By.XPATH, "//div[@id='wpbody']//div[5]")
    driver.execute_script("arguments[0].scrollIntoView();", specificSection)

    driver.find_element(By.XPATH,"//div[@class='relative w-10 h-full rounded-full transition duration-100 bg-blue-600']").click()

    saveSetting = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"//button[@class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']"))
    )
    saveSetting.click()


# Scenario 11: Enable Animation & set one instead default
def enable_toggle_animation():
    driver.find_element(By.XPATH, "//div[contains(text(),'WP Dark Mode')]").click()

    driver.find_element(By.XPATH, "//h4[normalize-space()='Customization']").click()

    siteAnimation = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Site Animation']"))
    )
    siteAnimation.click()

    driver.find_element(By.XPATH,"//div[@class='relative w-10 h-full rounded-full transition duration-100 bg-slate-200']").click()

    selectAnimation = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Pulse']"))
    )
    selectAnimation.click()

    saveSetting = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//button[@class='disabled:opacity-50 disabled:cursor-not-allowed inline-flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md cursor-pointer outline-none focus:outline-none hover:opacity-90 transition duration-75 bg-blue-500 text-white border border-blue-500']"))
    )
    saveSetting.click()


# Scenario 12: Validate Darkmode is working or not
def validate_darkMode():
    driver.find_element(By.XPATH,"//a[normalize-space()='My Blog']").click()

    background = driver.find_element(By.XPATH,"//h1[@class='wp-block-heading has-text-align-center has-x-large-font-size']")

    bgColor_on_normal = driver.execute_script("return window.getComputedStyle(arguments[0]).color;", background)

    driver.find_element(By.XPATH,"//div[@class='_track wp-dark-mode-ignore']//div[1]").click()
    time.sleep(5)

    bgColor_on_dark = driver.execute_script("return window.getComputedStyle(arguments[0]).color;", background)

    if bgColor_on_normal != bgColor_on_dark:
        print("Dark Mode is working on the frontend.")
    else:
        print("Dark Mode is not working on the frontend.")


try:
    login_to_wordpress(username, password)
    is_dark_mode_plugin_active()
    enable_backend_darkmode()
    navigate_to_wp_dark_mode()
    change_floating_switch_style()
    select_custom_switch_size()
    change_floating_switch_position()
    disable_keyboard_shortcut()
    enable_toggle_animation()
    validate_darkMode()

finally:
    driver.quit()