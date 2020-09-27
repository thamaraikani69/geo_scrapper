#.................................om sivaya nama.............................#


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys
#import datetime
from datetime import datetime
from bs4 import BeautifulSoup

class geo_address:

        def __init__(self):
            chromedriver = 'C:\\chromedriver.exe'
            #chromedriver = 'C:\\Users\\thama\\Desktop\\chromedriver\\chromedriver.exe'
            self.browser = webdriver.Chrome(chromedriver)

            self.query=input("what you want to search only company ex(hospital in madurai)")
            #self.output_file_name=input("give out file name")
            #self.query='surgical in madurai'
            #browser.get('https://www.google.com')
            self.browser.get('https://www.google.com/search?safe=active&rlz=1C1CHBD_enIN808IN808&tbm=lcl&ei=AonJXKCKFc-R9QOKmruwAg&q='+self.query)
            time.sleep(3)
            geo_address.check(self)

        def check(self):
            try:
                wrong_sentace=self.browser.find_element_by_xpath('//*[@id="fprsl"]')
                wrong_sentace.is_displayed()
                wrong_sentace.click()
                geo_address.google_map(self)
            except:
                geo_address.google_map(self)

        def google_map(self):
            #map_zoom_out_click
            map_zoom_out = self.browser.find_element_by_xpath('//*[@id="lu_pinned_rhs"]/div/div/div[3]/div/button[2]/div').click()
            time.sleep(2)

            #google_bottom_page_number_check
            page=2
            #count_the_address_list
            self.s_no=1
            time.sleep(5)
            while True:

                try:

                    #google_bottom_page_number_click
                    page_no=self.browser.find_element_by_xpath('//*[@id="rl_ist0"]/div[2]/div/table/tbody/tr/td['+str(page)+']')

                    page_no.is_displayed()
                    page_no.click()
                    time.sleep(5)

                    for i in range(1,20):

                        try:
                            #first_address_in_the_list_click
                            site_link=self.browser.find_element_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div['+str(i)+']/div/div[3]/div/a[1]')

                            site_link.is_displayed()
                            site_link.click()
                            geo_address.link(self)
                        except:

                            ##first_address_in_the_list_click
                            time.sleep(2)
                            site_link1 = self.browser.find_element_by_xpath('//*[@id="rl_ist0"]/div[1]/div[4]/div['+str(i)+']/div/div[2]/div/a[1]')
                            site_link1.is_displayed()
                            site_link1.click()
                            geo_address.link(self)

                    #bottom_page_count_increase
                    page=page+1

                except :
                    self.file.close()
                    exit()


        def link(self):
                time.sleep(3)
                try:
                    try:
                        #delete_list=["Hours:"""]
                        heading = self.browser.find_element_by_class_name("SPZz6b")
                        
                        hos_names=heading.is_displayed()
                        filter1=heading.text
                        filter2=filter1.replace('Directions',"")
                        filter3=filter2.replace('Save',"")
                        filter4=filter3.replace('\n',"")
                        hos_namess=filter4.replace('Website',"")

                        self.hos_name=(str(self.s_no) + ": " +"NAME: "+hos_namess )
                        print(self.hos_name)

                        self.s_no += 1
                        time.sleep(3)
                    except:
                        heading = self.browser.find_element_by_class_name(
                            'SPZz6b')
                        hos_names = heading.is_displayed()
                        hos_names = heading.text
                        filter1=heading.text
                        filter2=filter1.replace('Directions',"")
                        filter4=filter3.replace('\n',"")
                        hos_namess=filter4.replace('Website',"")
                        self.hos_name = (str(self.s_no) + ": " + "NAME: " + hos_namess)
                        self.s_no += 1
                        time.sleep(3)
                except:
                    self.hos_name = ('none')

                try:
                    address_link = self.browser.find_element_by_xpath("//span[@class='LrzXr']")
                    self.address=address_link.text.replace(" ", "")
                    #print(self.address)
                except:
                    self.address = ('no address')


                try:
                    mobile_number_link=self.browser.find_element_by_xpath("//span[@class='LrzXr zdqRlf kno-fv']")
                    self.mobile_number=mobile_number_link.is_displayed()
                    self.mobile_number=mobile_number_link.text
                    #print(self.mobile_number)
                except:
                    self.mobile_number=('no mobile number')




                try:
                    try:
                        webside_link = self.browser.find_element_by_xpath('//*[@id="akp_tsuid3"]/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/a')
                        

                        self.website=webside_link.get_attribute('href')
                        #print(self.website)
                    except:
                        webside_link = self.browser.find_element_by_xpath(
                            '//*[@id="akp_tsuid3"]/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/a')
                        
                        self.website = webside_link.get_attribute('href')
                        # print(self.website)
                except:
                    self.website=("no website link")

                geo_address.output(self)



        def output(self):

            list.append(self.hos_name+'\n')
            list.append('address:'+self.address+'\n')
            list.append("Phone No:" + self.mobile_number+'\n')
            list.append("website:"+self.website + "\n\n")
            #print(list)
            self.file=open(self.query+".txt","w+",encoding='utf-8')
            for adress in list:
              self.file.write((adress))



if __name__ == '__main__':
    list = []
    geo_address()
