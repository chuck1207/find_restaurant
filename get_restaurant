def get_urls():
    loca = input("장소를 입력해주세요")
    urls = []
    driver = webdriver.Chrome(executable_path= "chromedriver.exe")

    for i in range(1,11):
        try:
            url = "https://www.mangoplate.com/search/{0}?keyword={0}&page={1}".format(loca,str(i))
            driver.get(url)
            driver.implicitly_wait(3)
        except:
            break

        boxes = driver.find_elements_by_css_selector("body > main > article > div.column-wrapper > div > div.inner > section > div.search-list-restaurants-inner-wrap > ul.list-restaurants > li.server_render_search_result_item > div.list-restaurant-item > figure")


        for box in boxes:
            urls.append(box.find_element_by_css_selector("a").get_attribute("href"))    
            
    return urls

def get_meta(driver,url):
    address= []
    call = []
    category = []
    cost= []
    times =[]
    title = []
    urls = []
    title.append(driver.find_element_by_css_selector("body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > header > div.restaurant_title_wrap > span > h1").text)
    address.append(driver.find_element_by_css_selector("body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(1) > td").text.split("\n")[0])
    call.append(driver.find_element_by_css_selector("body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(2) > td").text)
    category.append(driver.find_element_by_css_selector("body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(3) > td").text)
    cost.append(driver.find_element_by_css_selector("body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(4) > td").text)
    times.append(driver.find_element_by_css_selector("body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(6) > td").text)
    urls.append(url)
    return pd.DataFrame({'title':title,'address':address,'call':call,"category":category,'cost':cost,'time':times,'url':urls})

def get_review(driver):
    boxes = driver.find_elements_by_css_selector("body > main > article > div.column-wrapper > div.column-contents > div > section.RestaurantReviewList > ul > li")
    boxes

    title = []
    name = []
    date = []
    review = []
    for box in boxes:
        title.append(driver.find_element_by_css_selector("body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > header > div.restaurant_title_wrap > span > h1").text)
        name.append(box.find_element_by_css_selector("a > div.RestaurantReviewItem__User > span").text)
        date.append(box.find_element_by_css_selector("a > div.RestaurantReviewItem__ReviewContent > div > span").text)
        review.append(box.find_element_by_css_selector("a > div.RestaurantReviewItem__ReviewContent > div > p").text)   
    
    return pd.DataFrame({'title':title,'name':name,'date':date,"review":review})
