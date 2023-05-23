import pyautogui
import time

def keep_active(interval):
    while True:
        pyautogui.move(1, 1)  # 移动鼠标1像素
        pyautogui.move(-1, -1)  # 移回原位置
        time.sleep(interval)

# 设置保持活跃的间隔时间为5分钟
keep_active(5 * 60)
