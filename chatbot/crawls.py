# 크롤링을 하는 부분
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

class Crawl:
    def __init__(self, id, pw):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.uname = id
        self.pword = pw
        self.hakbeon = int(id[0:4])
    
    def __del__(self):
        self.driver.close()

    def login(self):
        self.driver.implicitly_wait(3)

        self.driver.get('https://cyber.inu.ac.kr/login.php')
        self.driver.find_element_by_id('input-username').send_keys(self.uname)
        self.driver.find_element_by_id('input-password').send_keys(self.pword)
        self.driver.find_element_by_xpath(
            '//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[2]/form/div[2]/input').click()

        if self.driver.current_url == 'https://cyber.inu.ac.kr/login.php':
            return False
        return True

    def get_info(self):
        self.driver.get('http://cyber.inu.ac.kr')
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        dept = soup.find('p', {'class': 'department'})
        name = soup.find('li', {'class': 'user_department hidden-xs'})
        return {"name":name.text, "dept":dept.text}

    def get_class(self):
        result = list()
        sems = [10, 11, 20, 21]
        sem_ts = ['1학기', '여름학기', '2학기', '겨울학기']

        self.driver.get('http://cyber.inu.ac.kr/local/ubion/user/')

        for year in range(self.hakbeon, datetime.today().year+1):
            for i in range(0, 4):
                self.driver.get('http://cyber.inu.ac.kr/local/ubion/user/?year=' + str(year) + '&semester=' + str(sems[i]))
                html = self.driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                courses_a = soup.find_all('a', {'class': 'coursefullname'})

                if len(courses_a) > 0:
                    sem_t = sem_ts[i]
                    for course in courses_a:
                        course_name = course.text[0:len(course.text) - 13]
                        course_code = course.text[len(course.text) - 11:len(course.text) - 1]
                        result.append((year, sem_t, course_name, course_code))
        return result


