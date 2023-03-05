"""以下信息为系统地址"""
from selenium.webdriver.common.by import By

url = "https://litemall.hogwarts.ceshiren.com/"

"""以下信息为登录元素"""
li_username = By.CSS_SELECTOR, "[name='username']"
li_password = By.CSS_SELECTOR, "[name='password']"
li_login_btn = By.XPATH, "//*[text()='登录']/.."

"""以下信息为商品上架元素"""
li_goods_manage = By.XPATH, "//*[text()='商品管理']"
li_goods_groud = By.XPATH, "//*[text()='商品上架']"
li_goods_num = By.XPATH, "//*[contains(text(),'商品编号')]/..//input"
li_goods_name = By.XPATH, "//*[contains(text(),'商品名称')]/..//input"
li_groud_btn = By.XPATH, "//*[text()='上架']/.."

"""以下信息为搜索商品元素"""
li_goods_list = By.XPATH, "//*[text()='商品列表']"
li_input_goods_num = By.CSS_SELECTOR, "[placeholder='请输入商品编号']"
li_input_goods_name = By.CSS_SELECTOR, "[placeholder='请输入商品名称']"
li_search_btn = By.CSS_SELECTOR, ".el-icon-search"

"""以下信息为手机登录元素"""
appPackage = "com.jnzc.shipudaquan"
appActivity = "amodule.activity.main.Main"
app_myself = By.XPATH, "//*[@resource-id='com.jnzc.shipudaquan:id/nav_item5']"
app_login = By.XPATH, "//*[@text='立即登录']"
app_username = By.XPATH, "//*[@class='android.widget.EditText']"
app_next = By.XPATH, "//*[@text='下一步']"
app_passwd = By.XPATH, "//*[@text='输入密码' and @index='2']"
app_login_btn = By.XPATH, "//*[@text='登录']"

"""以下信息为查找app指定元素"""
app_VIP = By.XPATH, "//*[@resource-id='com.jnzc.shipudaquan:id/nav_item2']"
app_channel_area = By.XPATH, "//*[@class='android.support.v7.widget.RecyclerView']"
app_food_area = By.XPATH, "//*[@resource-id='com.jnzc.shipudaquan:id/rvListView']"
