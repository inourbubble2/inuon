# 크롤링을 하는 부분
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from pyvirtualdisplay import Display
# import logger
import logging


class Crawl:
    def __init__(self, id, pw):
        self.logger = logging.getLogger(__name__)

        self.display = Display(visible=0, size=(1920, 1080))
        self.display.start()
        self.logger.info("Starting display")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome('./chromedriver',
                                       chrome_options=chrome_options)
        self.uname = id
        self.pword = pw
        self.hakbeon = int(id[0:4])

    def __del__(self):
        self.driver.close()

    def login(self):
        self.driver.implicitly_wait(3)
        self.logger.info("Start to login to cyber.inu.ac.kr")
        self.driver.get('https://cyber.inu.ac.kr/login.php')
        self.driver.find_element_by_id('input-username').send_keys(self.uname)
        self.driver.find_element_by_id('input-password').send_keys(self.pword)
        self.driver.find_element_by_xpath(
            '//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[2]/form/div[2]/input').click()

        self.driver.implicitly_wait(3)
        if self.driver.current_url == 'https://cyber.inu.ac.kr/login.php':
            self.logger.error("Login failed")
            return False
        self.logger.info("Login sucessfully")
        return True

    def get_info(self):
        self.logger.info("Getting info of the student")

        self.driver.get('http://cyber.inu.ac.kr')
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        dept = soup.find('p', {'class': 'department'})
        name = soup.find('li', {'class': 'user_department hidden-xs'})

        if dept and name:
            self.logger.info(name.text + ', ' + dept.text)
            return name.text, dept.text
        else:
            return None

    def get_class(self):
        self.logger.info("Getting courses of the student")

        result = list()
        courses_a = list()
        sems = [10, 11, 20, 21]
        sem_ts = ['1학기', '여름학기', '2학기', '겨울학기']

        self.driver.get('http://cyber.inu.ac.kr/local/ubion/user/')

        for year in range(self.hakbeon, datetime.today().year+1):
            for i in range(0, 4):
                self.driver.get('http://cyber.inu.ac.kr/local/ubion/user/?year='
                                + str(year) + '&semester=' + str(sems[i]))
                html = self.driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                courses_a = soup.find_all('a', {'class': 'coursefullname'})

                if len(courses_a) > 0:
                    sem_t = sem_ts[i]
                    for course in courses_a:
                        course_name = course.text[0:len(course.text) - 13]
                        course_code = course.text[len(course.text) - 11:len(course.text) - 1]
                        result.append([year, sem_t, course_name, course_code])
        self.logger.info(str(result))
        return result


