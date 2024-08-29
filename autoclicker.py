import pyautogui
import cv2
import numpy as np
import datetime

def identify_click(fp, threshold = 0.8):
    # 截取当前屏幕
    screenshot = pyautogui.screenshot()
    temp = np.array(screenshot)
    # 将截图转换为 OpenCV 格式
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 读取目标图像（例如按钮图像）
    button_image = cv2.imread(fp)

    # 使用模板匹配在屏幕截图中查找目标图像的位置
    result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果中最匹配的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 设置一个匹配阈值
    threshold = threshold
    if max_val >= threshold:
        # 计算中心点位置
        button_x = max_loc[0] + button_image.shape[1] // 2
        button_y = max_loc[1] + button_image.shape[0] // 2

        # 移动鼠标并点击
        pyautogui.moveTo(button_x, button_y, duration=0)
        pyautogui.click()
        clicked_flag = True
    else:
        print("目标图像未找到")
        clicked_flag = False
    
    return clicked_flag

def click(button_x, button_y):
    pyautogui.moveTo(button_x, button_y, duration=0)
    pyautogui.click()
    return

def detect(fp):
    # 截取当前屏幕
    screenshot = pyautogui.screenshot()
    temp = np.array(screenshot)
    # 将截图转换为 OpenCV 格式
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 读取目标图像（例如按钮图像）
    button_image = cv2.imread(fp)

    # 使用模板匹配在屏幕截图中查找目标图像的位置
    result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果中最匹配的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 设置一个匹配阈值
    threshold = 0.7
    if max_val >= threshold:
        # 计算中心点位置
        button_x = max_loc[0] + button_image.shape[1] // 2
        button_y = max_loc[1] + button_image.shape[0] // 2
        detected_flag = True
    else:
        print("目标图像未找到")
        detected_flag = False
    
    return detected_flag, button_x, button_y

if __name__ == "__main__":
    # 设置识别和点击的间隔时间
    interval = 0.001
    # 设置识别和点击的间隔时间
    pyautogui.PAUSE = interval
    detect_flag = False
    # identify the page switching button
    while not detect_flag:
        detect_flag, duihuan_x, duihuan_y = detect("./img/duihuan.png")
    print("已识别到兑换按钮，请勿移动窗口位置")
    detect_flag = False
    while not detect_flag:
        detect_flag, paimaidian_x, paimaidian_y = detect("./img/paimaidian.png")
    print("已识别到拍卖殿按钮，请勿移动窗口位置")

    # 识别并点击按钮
    target_time = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    while True:
        current_time = datetime.datetime.now()
        if current_time >= target_time:
            break

    for i in range(3):
        # 反复切换两次界面
        for i in range(5):
            click(duihuan_x, duihuan_y)
            click(paimaidian_x, paimaidian_y)

        ## 选定商品
        while not identify_click("./img/testinggood.png"):
            pass

        ## 点击购买：一锤定音
        while not identify_click("./img/yichuidingyin.png"):
            pass

        ## 点击购买：二次确认
        while not identify_click("./img/queren.png"):
            pass

        ## 测试程序，确认没有一锤定音券
        while not identify_click("./img/nocoupon.png", threshold=0.1):
            pass
        
        ## 测试程序，确认没有一锤定音券
        while not identify_click("./img/nocoupon.png", threshold=0.1):
            pass



    