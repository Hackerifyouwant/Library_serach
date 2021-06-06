from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

def get_page_informatrion(search):
    url = 'http://opac.lib.ncu.edu.tw/search*cht/Y?SEARCH=' + search + '&SORT=D'
    script = 'window.open("'+url+'");'
    driver.execute_script(script)

    url = 'https://library.ym.edu.tw/search*cht/a?searchtype=t&searcharg=' + search + '&SORT=D&searchscope=7&submit.x=23&submit.y=14'
    script = 'window.open("'+url+'");'
    driver.execute_script(script)

    url = 'https://webpac.lib.nthu.edu.tw/F/?func=find-b&find_code=WRD&request=' + search + '&local_base=TOP01&adjacent=1'
    script = 'window.open("'+url+'");'
    driver.execute_script(script)

    url = 'https://webpac.lib.nctu.edu.tw/F/?func=find-b&find_code=WTI&request=' + search + '&local_base=TOP01&adjacent=1'
    script = 'window.open("'+url+'");'
    driver.execute_script(script)


search = input("輸入你想查詢的書目: ")
get_page_informatrion(search)


