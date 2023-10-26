from appium import webdriver
import time

desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': 'Android API 34',
    'deviceName': 'Nexus S',
    'appPackage': 'com.android.calculator2',
    'appActivity': 'com.android.calculator2.Calculator',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

def perform_calculation():
    btn_7 = driver.find_element_by_id('com.android.calculator2:id/digit_7')
    btn_plus = driver.find_element_by_id('com.android.calculator2:id/op_add')
    btn_3 = driver.find_element_by_id('com.android.calculator2:id/digit_3')
    btn_equals = driver.find_element_by_id('com.android.calculator2:id/eq')
    result = driver.find_element_by_id('com.android.calculator2:id/result')
    
    btn_7.click()
    btn_plus.click()
    btn_3.click()
    btn_equals.click()
    
    assert result.text == '10' 

    btn_multiply = driver.find_element_by_id('com.android.calculator2:id/op_mul')
    btn_5 = driver.find_element_by_id('com.android.calculator2:id/digit_5')
    btn_multiply.click()
    btn_5.click()
    btn_equals.click()

    assert result.text == '50'  

    btn_divide = driver.find_element_by_id('com.android.calculator2:id/op_div')
    btn_2 = driver.find_element_by_id('com.android.calculator2:id/digit_2')
    btn_divide.click()
    btn_2.click()
    btn_equals.click()

    assert result.text == '25'  

    btn_subtract = driver.find_element_by_id('com.android.calculator2:id/op_sub')
    btn_8 = driver.find_element_by_id('com.android.calculator2:id/digit_8')
    btn_subtract.click()
    btn_8.click()
    btn_equals.click()

    assert result.text == '17'  
    
    btn_sqrt = driver.find_element_by_id('com.android.calculator2:id/op_sqrt')
    btn_sqrt.click()

    assert result.text == '4.123105625617661'  

perform_calculation()

driver.quit()