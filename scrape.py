from time import sleep
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com')
        



def get_username(browser, person_name):
    search_input = WebDriverWait(browser, 1000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']"))
    )
    search_input.clear()
    search_input.send_keys(person_name)
    sleep(3)

    usernames = []
    names = []
    verified_unames = []
    keys = []

    user_elements = browser.find_elements(By.CSS_SELECTOR, "span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")
    name_elements = browser.find_elements(By.CSS_SELECTOR, "span.x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft")
    for i in user_elements:
        usernames.append(i.text)
    
    for n in name_elements:
        names.append(n.text)
    
    for name in names:
        list_from_name = name.split()
        lisname_csv = person_name.split()
        result = all(element in lisname_csv for element in list_from_name)
        keys.append(result)

    for username, key in zip(usernames, keys):
        if key == True:
            verified_unames.append(username)

    return verified_unames, names
   
# Function to read data from CSV file
def csv_to_list(file_path):
    data_list = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:
            data_list.append(row)
    return data_list

# csv file with names, addresses, and schools in different columns
file_path = 'csv_file_with_info.csv'
actual_data = csv_to_list(file_path)

browser = webdriver.Chrome()
browser.implicitly_wait(5)

HomePage(browser)
# input username, password
LoginPage(browser).login("johndoe_100123", "Johndoe1001")
notnow_button = browser.find_element(By.CSS_SELECTOR, "div._ac8f")
notnow_button.click()
not_now2_button = browser.find_element(By.CSS_SELECTOR, "button._a9--._a9_1")
not_now2_button.click()
search_button = browser.find_element(By.CSS_SELECTOR, "a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd[href='#'][role='link'][tabindex='0']")
search_button.click()

usernames = []
address = []
matched_results = {}

for person in actual_data:
    person_name, person_address, person_school = person
    userlist, names = get_username(browser, person_name)
    if userlist:
        person_name_list = person_name.split()  # Convert person_name to a list
        for user, name in zip(userlist, names):
            name_list = name.split()  # Convert name to a list
            if all(elem in person_name_list for elem in name_list):
                address.append(person_address)
                usernames.append([user, name])

data_dict = {item[0]: item[1] for item in usernames}
for username, name in data_dict.items():
    profile_url = f"https://www.instagram.com/{username}/"
    browser.get(profile_url)

    try:
        bio_element = browser.find_element(By.XPATH, "//h1[contains(@class, '_aacl')]")
        name_element = browser.find_element(By.CSS_SELECTOR, "span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")

    except NoSuchElementException:
        continue
    for y in address:
        search_string = y
        bio_text = bio_element.text.lower()
        name_text = name_element.text
        # if search_string in bio_text:

    matched_results[username] = name_text

print(matched_results)
filename = 'possible_leads.csv'

# Open the CSV file in write mode
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    writer.writerow(['Instagram Username', 'Person Name'])
    for username, name in matched_results.items():
        writer.writerow([username, name])

print(f"CSV file '{filename}' created successfully.")

browser.close()
