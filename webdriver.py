from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import Select

gitlab_domain = "http://our.gitlab.com"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('lang=ko_KR')

# 유의: chromedriver를 위에서 받아준 
# chromdriver(windows는 chromedriver.exe)의 절대경로로 바꿔주세요!
# driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')

# driver.get('http://www.naver.com')
driver.get(gitlab_domain + '/users/sign_in')
driver.implicitly_wait(3)
# driver.get_screenshot_as_file('naver_main.png')

# 로그인
driver.find_element_by_id('user_login').send_keys('TEST0000')
driver.find_element_by_id('user_password').send_keys('TEST0000')
driver.find_element_by_name('commit').click()
 
time.sleep(1)

# 신규 프로젝트 생성
driver.get(gitlab_domain +'/projects/new')

time.sleep(1)


# 신규 프로젝트 이관 탭 선택
driver.find_element_by_id('import-project-tab').click()

time.sleep(2)

driver.find_element_by_css_selector('.btn.js-toggle-button.js-import-git-toggle-button').send_keys(Keys.RETURN)
print(driver.find_element_by_css_selector('.btn.js-toggle-button.js-import-git-toggle-button').text)
# driver.find_element_by_css_selector("div[class^='btn js-toggle-button js-import-git-toggle-button']")

time.sleep(3)

# 대상 : http://git.interparktour.com/R-PLATFORM/TOUR.ELK
driver.find_element_by_id('project_import_url').send_keys('http://git.interparktour.com/R-PLATFORM/project_moni')
driver.find_element_by_id('project_import_url_user').send_keys('T06055')
driver.find_element_by_id('project_import_url_password').send_keys('gusals031')
driver.find_element_by_id('project_import_url_password').send_keys(Keys.TAB + Keys.TAB + 'project_moni')
# driver.find_element_by_id('project_name').send_keys('TOUR.ELK')
# driver.find_element_by_css_selector(".form-control.input-lg[data-track-property^='project_name']").send_keys("TOUR.ELK")
# driver.find_element_by_id('s2id_project_namespace_id').send_keys('')

# div = driver.find_element_by_css_selector('.select2-container.select2.js-select-namespace.qa-project-namespace-select').click()

# option = div.find_element_by_xpath('./ul/li[. = "01"]')
# option.click()

time.sleep(5)

# 이관 버튼
# driver.find_element_by_name('commit').click()
# select = Select(driver.find_element_by_name('commit'))
# select.select_by_index(0)

# element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//form[@class='new_project']/input[@name='commit']")))
# driver.execute_script("arguments[0].click();", element)

# element2 = driver.find_element_by_xpath("//input[@type='submit' and @value='Create project']").click()
# print(element2.value)


driver.execute_script("window.scrollTo(300, document.body.scrollHeight);")


element = driver.find_element_by_xpath("//input[@name='commit']")
print(element.get_attribute('value'))
driver.execute_script("arguments[0].click();", element)
# error
# driver.find_element_by_id("saveQuestionsSection").click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='commit']"))).click()


# element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='commit']")))
# driver.execute_script("arguments[0].click();", element)

# element = driver.find_element_by_xpath("//input[@name='commit']")
# element = driver.find_element_by_xpath("//form[@class='btn btn-success project-submit']/input[0]")
# driver.execute_script("arguments[0].click();", element)
# print(element.text)


time.sleep(5)
# 종료
driver.close()

# driver.quit()

# login form
# 폼이름 new_user
# user[login]
# user[password]
