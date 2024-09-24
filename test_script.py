from appium import webdriver
import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
import os
import HtmlTestRunner
import time
import base64

desired_caps = dict(
    platformName='Android',
    platformVersion='13',
    automationName='UiAutomator2',
    deviceName='R3CR30SHTE',
    appPackage="kr.co.captv.pooqV2",
    appActivity="kr.co.captv.pooqV2.main.IntroActivity",
    newCommandTimeout='300',
    noReset='true',
    unicodeKeyboard= 'true'

)

#test

class Go(unittest.TestCase):

 def testcase(self):
  self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
  self.driver.close_app()

  prompt = (1000)
  for i in range(0, prompt):


   self.driver.activate_app("kr.co.captv.pooqV2")
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/tv_view_more')
   time.sleep(1)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/navigation_my').click()
   time.sleep(1)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/tv_profile_name').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="회원정보 수정"]/android.widget.TextView')
   time.sleep(1)
   self.driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="로그아웃"]/android.widget.TextView').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="로그인"]/android.widget.TextView').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/editText_id').send_keys('hwany@w.com')
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/password').send_keys('Test123!')
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/btn_log_in').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/tv_view_more')
   time.sleep(1)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/navigation_my').click()
   time.sleep(1)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/tv_profile_name').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="회원정보 수정"]/android.widget.TextView')
   time.sleep(1)
   self.driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="로그아웃"]/android.widget.TextView').click()
   self.driver.implicitly_wait(30)
   time.sleep(1)
   self.driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="로그인"]/android.widget.TextView').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/button_fake_kakao').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.EditText').send_keys('01093148010')
   time.sleep(1)
   self.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText').send_keys('Test123!@')
   self.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.widget.Button').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button').click()
   self.driver.implicitly_wait(30)
   self.driver.find_element(AppiumBy.ID,'kr.co.captv.pooqV2:id/tv_view_more')
   time.sleep(1)
   self.driver.terminate_app('kr.co.captv.pooqV2')

   #video_rawdata = self.driver.stop_recording_screen()
   #video_name = "Test" + "_" + time.strftime("%H%M%S")
   #config_root = "/Users/hwany/Desktop/"
   #filepath = os.path.join(config_root, video_name+".mp4")

   #with open(filepath,"wb+") as vd:
   #     vd.write(base64.b64decode(video_rawdata))

   print(1+i)



if __name__ == "__main__":

    reportFoler = "ReportTest"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/hwany/Desktop/"))
    unittest.main(exit=False)