import pyautogui
import keyboard
import time
from PIL import Image, ImageDraw
import pygetwindow as gw


def check_pixel_color(x, y):
    pixel_color = pyautogui.pixel(x, y)
    if pixel_color == (255, 255, 255):
        return True
    else:
        return False


def press_key_if_pixel_white(x, y):
    if check_pixel_color(x, y):
        time.sleep(0.08)
        keyboard.press('e')
        print("press")
        time.sleep(1)
        keyboard.release('e')


def screenSnap():
    exit()
    chrome_screenshot = pyautogui.screenshot(
         region=(chrome_window.left, chrome_window.top, chrome_window.width, chrome_window.height))
    draw = ImageDraw.Draw(chrome_screenshot)
    draw.point((pixel_x - chrome_window.left, pixel_y - chrome_window.top), fill="red")
    draw.point((pixel_x_c - chrome_window.left, pixel_y_c - chrome_window.top), fill="red")
    chrome_screenshot.show()


chrome_window = gw.getWindowsWithTitle("Destiny 2")[0]

#pixel_x = 1560
#pixel_y = 993
#pixel_x_c = 1680
#pixel_y_c = 993
#1560 993
#1680 994
pixel_x = chrome_window.left + 775 #nornal coords of "E"
pixel_y = chrome_window.top + 782
pixel_x_c = chrome_window.left + 895 # coords of "Perfect catch"
pixel_y_c = chrome_window.top + 782

keyboard.on_press_key("enter", lambda _: screenSnap())

# Continuously check the pixel color and press the "e" key if it's white
while True:
    press_key_if_pixel_white(pixel_x, pixel_y)
    press_key_if_pixel_white(pixel_x_c, pixel_y_c)