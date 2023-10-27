import random
from appium import webdriver

desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': 'Android API 34',
    'deviceName': 'Nexus S',
    'appPackage': 'com.android.calculator2',
    'appActivity': 'com.android.calculator2.Calculator',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

def perform_random_calculation():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    
    operation = random.choice(['add', 'subtract', 'multiply', 'divide'])
    
    btn_digit_num1 = driver.find_element_by_id(f'com.android.calculator2:id/digit_{num1}')
    btn_digit_num2 = driver.find_element_by_id(f'com.android.calculator2:id/digit_{num2}')
    result = driver.find_element_by_id('com.android.calculator2:id/result')
    
    if operation == 'add':
        btn_add = driver.find_element_by_id('com.android.calculator2:id/op_add')
        btn_equals = driver.find_element_by_id('com.android.calculator2:id/eq')
        btn_digit_num1.click()
        btn_add.click()
        btn_digit_num2.click()
        btn_equals.click()
    elif operation == 'subtract':
        btn_subtract = driver.find_element_by_id('com.android.calculator2:id/op_sub')
        btn_equals = driver.find_element_by_id('com.android.calculator2:id/eq')
        btn_digit_num1.click()
        btn_subtract.click()
        btn_digit_num2.click()
        btn_equals.click()
    elif operation == 'multiply':
        btn_multiply = driver.find_element_by_id('com.android.calculator2:id/op_mul')
        btn_equals = driver.find_element_by_id('com.android.calculator2:id/eq')
        btn_digit_num1.click()
        btn_multiply.click()
        btn_digit_num2.click()
        btn_equals.click()
    elif operation == 'divide':
        btn_divide = driver.find_element_by_id('com.android.calculator2:id/op_div')
        btn_equals = driver.find_element_by_id('com.android.calculator2:id/eq')
        btn_digit_num1.click()
        btn_divide.click()
        btn_digit_num2.click()
        btn_equals.click()

    result_text = result.text
    operation_name = ''
    if operation == 'add':
        operation_name = 'adição'
    elif operation == 'subtract':
        operation_name = 'subtração'
    elif operation == 'multiply':
        operation_name = 'multiplicação'
    elif operation == 'divide':
        operation_name = 'divisão'
    print(f'{num1} {operation_name} {num2} = {result_text}')

perform_random_calculation()

driver.quit()
