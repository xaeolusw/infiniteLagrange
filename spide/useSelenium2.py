from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 用于反爬的破解
# 创建Chrome参数对象
options = webdriver.ChromeOptions()

# 无头浏览器，即不显示浏览器
options.add_argument('--headless')

# 添加试验性参数
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
# 创建Chrome浏览器对象并传入参数
browser = webdriver.Chrome(options=options)
# 执行Chrome开发者协议命令（在加载页面时执行指定的JavaScript代码）
browser.execute_cdp_cmd(
    'Page.addScriptToEvaluateOnNewDocument',
    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
)

# 设置浏览器窗口大小
browser.set_window_size(1200, 800)
browser.get('https://www.baidu.com/')
# 设置隐式等待时间为10秒
browser.implicitly_wait(10)
kw_input = browser.find_element(By.ID, 'kw')
kw_input.send_keys('sex girls pictures')
su_button = browser.find_element(By.CSS_SELECTOR, '#su')
su_button.click()
# 创建显示等待对象
wait_obj = WebDriverWait(browser, 10)
# 设置等待条件（等搜索结果的div出现）
wait_obj.until(
    expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, '#content_left')
    )
)
# 截屏
# 执行JavaScript代码
browser.execute_script('document.documentElement.scrollTop = 0')

browser.get_screenshot_as_file('python_result.png')