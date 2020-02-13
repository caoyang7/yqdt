from pyecharts import options as opts
from pyecharts.charts import Map
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
wait = WebDriverWait(browser, 10)

browser.get('https://news.sina.cn/project/fy2020/yq_province.shtml?province=liaoning')

provinces = []
values = []

for i in range(2, 15):
    province = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mylist"]/div[2]/div[{}]/span[1]'.format(i))))
    provinces.append(province.text + '市')
    value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mylist"]/div[2]/div[{}]/span[2]'.format(i))))
    values.append(value.text)


def map_visualmap():
    c = (
        Map(init_opts=opts.InitOpts(width="1500px", height="700px"))
            .add("", [list(z) for z in zip(provinces, values)], "辽宁")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="辽宁省疫情地图"),
            visualmap_opts=opts.VisualMapOpts(max_=10),
        )
    )
    return c.render()


map_visualmap()
