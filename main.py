from time import monotonic
import keyboard as keyb
import numpy as np
import time
from mss import mss

def get_color_rgb(x, y):
    # Проба цвета с координат
    m = mss()
    monitor = {
        "left": x,
        "top": y,
        "width": 1,
        "height": 1,
    }
    # Получаем пиксель с экрана монитора
    img = m.grab(monitor)

    # Преобразуем этот пиксель в матрицу
    img_arr = np.array(img)
    item = img_arr[0][0]
    r = item[2]
    g = item[1]
    b = item[0]

    return [r, g, b]

'''def tap(side):
    #keyb.press(side)
    #time.sleep(0.01) #even 0.015 worked
    #keyb.release(side)
    keyb.send(side)
'''
def is_equal(first, second):
    if abs(int(first[0]) - int(second[0])) <= 10 and abs(int(first[1]) - int(second[1])) <= 10 and abs(int(first[2]) - int(second[2])) <= 10:
        return True
    return False

def is_not_equal(first, second):
    if abs(int(first[0]) - int(second[0])) >= 20 or abs(int(first[1]) - int(second[1])) >= 20 or abs(int(first[2]) - int(second[2])) >= 20: #it was 30
        return True
    return False
    
def wait(i):
    if i < 75:
        time.sleep(0.2 + i/1000)
        return
    time.sleep(0.8)
    return

'''
position = 'left'
for i in range (50):
    time.sleep(0.19) #only 0.2 worked correctly
    left_pixel = get_color_rgb(905, 750)
    left_danger = get_color_rgb(920, 837)
    left_tree = get_color_rgb(960, 837)
    right_pixel = get_color_rgb(1095, 750)
    right_danger = get_color_rgb(1080, 837)
    right_tree = get_color_rgb(1030, 837)
    fir_pixel = get_color_rgb(815, 750)
    sec_pixel = get_color_rgb(800, 500)
    
   # print(left_pixel, left_danger, left_tree, right_pixel, right_danger, right_tree, fir_pixel, sec_pixel, position, i, '\n')

    if (is_equal(left_pixel, fir_pixel) or is_equal(left_pixel, sec_pixel)) and (is_not_equal(left_danger, left_tree) or position == 'left'):
        keyb.send('left')
        position = 'left'
    elif (is_equal(right_pixel, fir_pixel) or is_equal(right_pixel, sec_pixel)) and (is_not_equal(right_danger, right_tree) or position == 'right'):
        keyb.send('right')
        position = 'right'
    if left_danger[0] == 255:
        break
'''


keyb.wait('enter')

position = 'left'
i = 0

while True:
    i += 1
    wait(i) #only 0.2 worked correctly
    left_pixel = get_color_rgb(905, 750)
    left_danger = get_color_rgb(920, 837)
    left_tree = get_color_rgb(960, 835) #long stik on 837 is different
    right_pixel = get_color_rgb(1095, 750)
    right_danger = get_color_rgb(1080, 837)
    right_tree = get_color_rgb(1030, 837)
    fir_pixel = get_color_rgb(815, 750)
    sec_pixel = get_color_rgb(800, 500)
    #print(left_pixel, left_danger, left_tree, right_pixel, right_danger, right_tree, fir_pixel, sec_pixel, position, i, '\n')
    if (left_danger[0] == 255):
        time.sleep(1)
        keyb.send('space')
        i = 0
        #print('STOP', '\n')
        #break
        continue
    if  not is_not_equal(right_danger, right_tree):
        keyb.send('left')
        position = 'left'
        #print('1 left', '\n') '''position == 'left' and'''
        continue
    if  not is_not_equal(left_danger, left_tree): 
        #print('1 right', '\n') '''position == 'right' and'''
        keyb.send('right')
        position = 'right'
        continue
    if is_equal(left_pixel, right_pixel):
        keyb.send('left')
        #print('1 equal', '\n')
        position = 'left'
        continue

    if (is_equal(left_pixel, fir_pixel) or is_equal(left_pixel, sec_pixel)):
        keyb.send('left')
        time.sleep(0.04) #0.05 is ok
        keyb.send('left')
        position = 'left'
        #print('2 left', '\n')
    elif (is_equal(right_pixel, fir_pixel) or is_equal(right_pixel, sec_pixel)):
        keyb.send('right')
        time.sleep(0.04)
        keyb.send('right')
        position = 'right'
        #print('2 right', '\n')
    