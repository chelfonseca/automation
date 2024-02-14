"""Module providing a function printing python version."""

import pyautogui
from time import sleep


# 1 - ClicK and type my user

pyautogui.click(731,384, duration=2)
pyautogui.write('jhonatan')
# 2 - Click and type my password
pyautogui.click(733,411, duration=2)
pyautogui.write('123456')
# 3 - Click in "Enter"
pyautogui.click(596,439, duration=2)
# 4 - Extract each product
with open('produtos.txt','r') as file:
    for line in file:
        product = line.split(',')[0]
        quantity = line.split(',')[1]
        price = line.split(',')[2]
        # 4.1 - Click and type product
        pyautogui.click(438,373, duration=0.5)
        pyautogui.write(product)
        # 4.1 - Click and type quantity
        pyautogui.click(435,399, duration=0.5)
        pyautogui.write(quantity)
        # 4.1 - Click and type price
        pyautogui.click(433,424, duration=0.5)
        pyautogui.write(price)
        # 4.1 - Click in "Register"
        pyautogui.click(311,579, duration=0.5)
        sleep(1)

