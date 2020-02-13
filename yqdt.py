# pyecharts是用于生成echarts图表的类库,echarts是百度开源的一个数据可视化库
# OPTIONS方法是用于请求获得由Request-URI标识的资源在请求/响应的通信过程中可以使用的功能选项。通过这个方法，客户端可以在采取具体资源请求之前，决定对该资源采取何种必要措施，或者了解服务器的性能。
from pyecharts import options as opts
from pyecharts.charts import Map
# selenium主要是用来做自动化测试，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。
# 模拟浏览器进行网页加载，当requests,urllib无法正常获取网页内容的时候
from selenium import webdriver
# By是selenium中内置的一个class，在这个class中有各种方法来定位元素
from selenium.webdriver.common.by import By
# Expected_Conditions的使用场景有2种
# 1.直接在断言中使用
# 2.与WebDriverWait配合使用，动态等待页面上元素出现或者消失
from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait等设置等待时间和超时时间
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
wait = WebDriverWait(browser, 10)

browser.get('https://news.sina.cn/zt_d/yiqing0121')

provinces = []
values = []
for i in range(2, 69, 2):
    province = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#mylist > div.mapCont.mapMoreCont > div.m_list > div:nth-child({}) > span.c1'.format(i))))
    provinces.append(province.text)
    value = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#mylist > div.mapCont.mapMoreCont > div.m_list > div:nth-child({}) > span.c2'.format(i))))
    values.append(value.text)


def map_visualmap() -> Map:
    c = (
        Map()
            .add("", [list(z) for z in zip(provinces, values)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="疫情地图"),
            visualmap_opts=opts.VisualMapOpts(max_=600),
        )
    )
    return c.render()


map_visualmap()
