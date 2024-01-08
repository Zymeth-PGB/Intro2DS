import selenium as sn
import numpy as np
import random as rd
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

BASE_URL = "https://chothuenha.com.vn/"

cost = []
area = []
bed_room = []
toilet = []
direction_house = []
address = []
start_date = []
due_date = []
post_id = []
district = []
street = []
view = []

def getLinks():
    """Hàm lấy danh sách link qua các trang

    Args:

    Returns:
        List: Danh sách link.
    """
    
    driver = sn.webdriver.Chrome()
    page = '&page='
    links = []

    for i in range(1, 1001, 1):
        if i == 1:
            driver.get(BASE_URL)
        else:
            driver.get(BASE_URL + page + f'{i}')
            
        sleep(rd.randint(5, 10))
        
        elems = driver.find_elements(By.CSS_SELECTOR, '.home-title [href]')
        temp = [elem.get_attribute('href') for elem in elems]
        links.append(temp)
        
    links = np.array(links)
    links_unique = np.unique(links)
    
    driver.quit()
    
    return links_unique

def loadData(links_unique: list):
    """Hàm lấy dữ liệu từ danh sách các link

    Args:
        links_unique (list): link các trang web đã lưu vào danh sách.

    Returns:
        pd.DataFrame: Pandas dataframe kết quả chứa dữ liệu mong muốn.
    """
    
    driver = sn.webdriver.Chrome()
    
    for i, link in enumerate(links_unique):
        driver.get(link)
        sleep(5)
        
        text = driver.page_source
        
        # Kiểm tra xem trang có tồn tại hay không và lấy dữ liệu dựa trên full XPath của trang web
        if text.find('Trang bạn yêu cầu không tồn tại!') == -1:
            cost.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[3]/div/div[1]/div').text)
            area.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[3]/div/div[2]/div[2]').text)
            bed_room.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[3]/div/div[3]/div[2]').text)
            direction_house.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[4]/div[2]/div[2]/div/div[5]/span[3]').text)
            address.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[4]/div[3]/ul/div/span').text)
            start_date.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[4]/div[4]/div/div[1]/span[2]').text)
            due_date.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[4]/div[4]/div/div[2]/span[2]').text)
            post_id.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[4]/div[4]/div/div[4]/span[2]').text)
            district.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/header/ul/li[3]/a').text)
            street.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/header/ul/li[4]/a').text)
            view.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[2]/div[3]').text)
            toilet.append(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/main/section[3]/div[2]/div/div/div[4]/div[2]/div[2]/div/div[4]/span[3]').text)

    driver.quit()

    df = pd.DataFrame({
        'Giá': cost,
        'Diện tích': area,
        'Số phòng ngủ': bed_room,
        'Số toilet': toilet,
        'Hướng nhà': direction_house,
        'Địa chỉ nhà': address,
        'Ngày đăng tin': start_date,
        'Ngày hết hạn': due_date,
        'Mã tin': post_id,
        'Quận': district,
        'Đường': street,
        'Lượt xem': view
    })
    
    return df

def saveDataFrame2CSV(df: pd.DataFrame, savePath: str, sep: str = ',', encoding: str = 'utf-8'):
    """Hàm lưu DataFrame thành dạng file CSV

    Args:
        df (DataFrame): DataFrame cần lưu lại CSV
        savePath (str): Đường dẫn chứa tên tập tin cần lưu, ví dụ: "data/save.csv"
        sep (str, optional): Ký tự phân chia các đặc trưng trong file csv. Defaults to ','.
        encoding (str, optional): . Defaults to 'utf-8'.

    Returns:
        bool: True
    """
    
    try:
        df.to_csv(savePath, sep = sep, encoding = encoding, index = False)
    except:
        raise ModuleNotFoundError
    
    return True
