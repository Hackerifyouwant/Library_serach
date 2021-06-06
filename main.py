from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


url = 'https://coborrow.lib.nctu.edu.tw/newust/index.php?&pds_handle=6620211217502274153222964504565&calling_system=primo'
username = "109263017"
password = "Hu_91012"
select_school = "4"

driver = webdriver.Chrome(ChromeDriverManager().install())

def login(search):
    driver.get(url)
    driver.maximize_window()  # 最大化視窗


    driver.find_element_by_name("input_userid_hidden").send_keys(username)
    driver.find_element_by_name("input_password").send_keys(password)

    select = Select(driver.find_element_by_name('school_id'))

    select.select_by_value(select_school)

    driver.find_element_by_name("loginclear").click()

    driver.switch_to_alert().accept() 
    #driver.close()
    get_page_informatrion(search)

def get_page_informatrion(search):

    url = 'http://opac.lib.ncu.edu.tw/search*cht/Y?SEARCH=' + search + '&SORT=D'
    script = 'window.open("'+url+'");'
    driver.execute_script(script)

    url = 'https://library.ym.edu.tw/search*cht/a?searchtype=t&searcharg=' + search + '&SORT=D&searchscope=7&submit.x=23&submit.y=14'
    script = 'window.open("'+url+'");'
    driver.execute_script(script)    

    url = 'https://webpac.lib.nctu.edu.tw/F/GNE9AIMJL5RV3S9TV25T7DXGS9GL6IH6LACCJ7RTL5GBQY594N-07012?func=find-b&find_code=WTI&request=' + search +'&local_base=TOP01&adjacent=1'
    script = 'window.open("'+url+'");'
    driver.execute_script(script)

    url = 'https://webpac.lib.nthu.edu.tw/F/G7A4GQDXD6HV5IQDRHHAIGHDF6PV44EVJYUUFT9UAYEYTMU6DA-17529?func=find-b&find_code=WRD&request=' + search + '&local_base=TOP01&adjacent=1'
    script = 'window.open("'+url+'");'
    driver.execute_script(script)

    

search = input("輸入你想查詢的書目: ")
login(search)
