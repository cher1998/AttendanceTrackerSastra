import time
from selenium import webdriver
import cv2
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome("F:\Softwares\chromedriver.exe", chrome_options=options)
driver.get("http://webstream.sastra.edu/sastrapwi")
regd_no=driver.find_element_by_id("txtRegNumber")
regd_no.send_keys("119004124")
regd_no.send_keys()
dob=driver.find_element_by_id("txtPwd")
dob.send_keys("14091997")
time.sleep(4)
driver.save_screenshot("capta.png")
img = cv2.imread("capta.png")
crop_img = img[205:250, 400:575]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
print "enter captcha"
capta_answer=raw_input()
captcha_id=driver.find_element_by_id("answer")
captcha_id.send_keys(capta_answer)
x_path_1='//*[@id="frmLogin"]/table/tbody/tr[3]/td/table/tbody/tr[6]/td/input[1]'
driver.find_element_by_xpath(x_path_1).click() 
x_path_2='//*[@id="masterdiv"]/div[13]/a'
driver.find_element_by_xpath(x_path_2).click()
time.sleep(2)
x_path_3='//*[@id="form01"]/table[1]/tbody/tr[12]/td[4]'
tot_bunks=int(driver.find_element_by_xpath(x_path_3).text)
if tot_bunks<80:
    msg="you can bunk "+str(80-tot_bunks)+" more hours in total"
    print msg
else:
    print "you are screwed"

str_fin_sub=' '
for sub_name_index in range(3,12):
    str_call='//*[@id="form01"]/table[1]/tbody/tr['+str(sub_name_index)+']/td[2]'
    sub_name=driver.find_element_by_xpath(str_call).text
    str_call='//*[@id="form01"]/table[1]/tbody/tr['+str(sub_name_index)+']/td[6]'
    sub_bunk=int(driver.find_element_by_xpath(str_call).text)
    if sub_bunk<80:
        str_fin_sub=str_fin_sub+' '+sub_name+","
print "moniter your attendance in"+str_fin_sub        
driver.quit()