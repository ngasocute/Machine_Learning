from selenium import webdriver
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager

listSearchURLs = [
    'https://www.youtube.com/results?search_query=nh%E1%BA%A1c+tr%E1%BA%BB', # nhạc trẻ
    'https://www.youtube.com/results?search_query=%C3%A2m+nh%E1%BA%A1c&sp=EgIIBQ%253D%253D', # âm nhạc
    'https://www.youtube.com/results?search_query=ca+nh%E1%BA%A1c&sp=EgIIBQ%253D%253D', # ca nhạc
    'https://www.youtube.com/results?search_query=nh%E1%BA%A1c&sp=EgIIBQ%253D%253D', # nhạc
    'https://www.youtube.com/results?search_query=ca+kh%C3%BAc&sp=EgIIBQ%253D%253D', #ca khúc
    'https://www.youtube.com/results?search_query=mv+official&sp=EgIIBQ%253D%253D', # mv official
    'https://www.youtube.com/results?search_query=music+video&sp=EgIIBQ%253D%253D', # music video
    'https://www.youtube.com/results?search_query=official+video&sp=EgIIBQ%253D%253D', # official video
    'https://www.youtube.com/results?search_query=nh%E1%BA%A1c+ti%E1%BA%BFng+anh+chill', # nhạc tiếng anh chill
    'https://www.youtube.com/results?search_query=nh%E1%BA%A1c+lofi+chill+', #nhạc lofi chill
    'https://www.youtube.com/results?search_query=nh%E1%BA%A1c+tiktok+hay', # nhạc tiktok hay 
    'https://www.youtube.com/results?search_query=best+love+songs+2022', #best love songs 2022
    'https://www.youtube.com/results?search_query=trending+tiktok+songs', # trending tiktok songs
    'https://www.youtube.com/results?search_query=nh%E1%BA%A1c+lofi+chill+ti%E1%BA%BFng+anh', # nhạc lofi chill tiếng anh
]
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
f = open('scraping_data.txt', 'a', encoding='utf-8')

for url in listSearchURLs:
    browser.get(url)
    sleep(5)

    previous_count = 0
    page_sections = browser.find_elements_by_css_selector('.style-scope.ytd-item-section-renderer')
    current_count = len(page_sections)
    print("Scrolling to enable all the pages")
    while previous_count != current_count:
        try:
            previous_count = current_count
            browser.execute_script("arguments[0].scrollIntoView();", page_sections[-1])
            print("Number of total Elements found: {}".format(len(page_sections)))
        finally:
            # As the page load the newer elements, you need to implement logic here to wait until the loading spinner at the
            # button becomes invisible (not attached to the DOM)
            sleep(2)  # WorkAround as you need to implement the above logic here
            page_sections = browser.find_elements_by_css_selector('.style-scope.ytd-item-section-renderer')
            current_count = len(page_sections)


    listVideo = browser.find_elements_by_tag_name("ytd-video-renderer")
    listURLs = []


    for video in listVideo:
        listURLs.append(video.find_element_by_xpath(".//a").get_attribute('href'))
        f.write(listURLs[-1] + '\n')
    
f.close()
