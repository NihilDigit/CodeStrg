import time
import hzckUtil
import FileUtil as fu
import machine
import random
from CalcST7735 import BNST7735Driver, BNColor
from BN165DKBDriver import keyCode
from machine import Pin

# ST7735 Init
bnsd = BNST7735Driver(4, 48, 5, 2)

# KeyPad Init
CP = Pin(41, Pin.OUT)
CE = Pin(39, Pin.OUT)
PL = Pin(40, Pin.OUT)
Q7 = Pin(21, Pin.IN)
adcIn = (CP, CE, PL, Q7)

# Constants

white = BNColor(255, 255, 255)
black = BNColor(0, 0, 0)
dark_green = BNColor(0, 128, 0)
light_green = BNColor(0, 255, 0)


def draw_and_wait(stop=0.1):
    bnsd.show()
    time.sleep(stop)

def draw_triangle(up, x, y, is_active):
        color = light_green if is_active else dark_green
        if up:
            bnsd.drawUpTriangle(x, y, 50, 10, color, True)
        else:
            bnsd.drawDownTriangle(x, y, 50, 10, color, True)

def main_menu():
    
    def draw_options(options, show, kc):
        is_up_active = kc == 0
        is_down_active = kc == 2
        draw_triangle(True, 50, 55, is_up_active)
        draw_triangle(False, 50, 100, is_down_active)
        bnsd.drawText(f"{options[show]}", light_green, 22, 75)
    
    def draw_greeting(name, solved, delay):
        bnsd.drawText(f"Welcome, {name}!", light_green, 10, 5)
        if delay > 0:
            draw_and_wait(delay)
        bnsd.drawText("You've finished", light_green, 10, 20)
        if delay > 0:
            draw_and_wait(delay)
        bnsd.drawText(f"{solved} Questions!", light_green, 10, 35)
        if delay > 0:
            draw_and_wait(delay)
    
    bnsd.clear(black)
    global kc
    kc = -1
    name = 'Siga'
    solved = 100
    options = [' Start ', 'Configs', 'Ranking', 'UserMgr']
    show = 0
    draw_greeting(name, solved, 0.35)
    
    while kc != 6 and kc != 7:
        kc = keyCode(adcIn)
        if kc == 0:
            show = (show + 1) % len(options)
        elif kc == 2:
            show = (show - 1) % len(options)
            
        bnsd.clear(black)
        draw_greeting(name, solved, 0)
        draw_options(options, show, kc)
        bnsd.show()
        time.sleep(0.15)
    
    if kc == 7:
        bnsd.clear(black)
        bnsd.drawText("GoodBye!", light_green, 40, 50)
        bnsd.show()
        exit()
    
    if show == 0:
        result = difficulty_selection()
        start_exercising(result)
        main_menu()

def difficulty_selection():
    
    global result
    result = {
            'mode': 'Focus',
            'quantity': '50',
        }
    
    def draw_options_1(options, show):
        if show == 0:
            color = [light_green, dark_green]
        elif show == 1:
            color = [dark_green, light_green]
        bnsd.drawText("Mode Selection", light_green, 20, 10)
        bnsd.fillRoundRect(20, 35, 50, 70, 7, color[0])
        bnsd.fillRoundRect(80, 35, 50, 70, 7, color[1])
        bnsd.drawText(f"{options[0]}", black, 25, 60)
        bnsd.drawText(f"{options[1]}", black, 85, 60)
    
    def draw_options_2(options, show, kc):
        is_up_active = kc == 0
        is_down_active = kc == 2
        draw_triangle(True, 70, 40, is_up_active)
        draw_triangle(False, 70, 100, is_down_active)
        bnsd.drawText(f"{options[show]}", light_green, 60, 65)
    
    def operating_type():
        options = ['Focus', 'Mixed']
        show = 0
        global kc
        kc = -1
        while kc != 6:
            bnsd.clear(black)
            kc = keyCode(adcIn)
            if kc == 1:
                show = (show + 1) % len(options)
            elif kc == 3:
                show = (show - 1) % len(options)
            draw_options_1(options, show)
            bnsd.show()
            time.sleep(0.15)
        
        result['mode'] = options[show]
            
    def operating_quantity():
        global kc
        kc = -1
        show = 0
        options = ['30', '50', '80', '100']
        
        while kc != 6:
            kc = keyCode(adcIn)
            if kc == 0:
                show = (show + 1) % len(options)
            elif kc == 2:
                show = (show - 1) % len(options)
            
            bnsd.clear(black)
            bnsd.drawText("What Quantity", light_green, 20, 10)
            draw_options_2(options, show, kc)
            bnsd.show()
            time.sleep(0.15)

        result['quantity'] = options[show]
        
    def draw_options_3(quantity):
        bnsd.drawText("+ 10", dark_green, 30, 50)
        bnsd.drawText(f" {quantity}", light_green, 30, 70)
        bnsd.drawText("- 10", dark_green, 30, 90)
        
    def alt_operating_quantity():
        global kc
        kc = -1
        quantity = 50
        
        while kc != 6:
            kc = keyCode(adcIn)
            bnsd.clear(black)
            bnsd.drawText("What Quantity", light_green, 20, 10)
            draw_options_3(quantity)
            if kc == 0:
                bnsd.drawText("+ 10", light_green, 30, 50)
                quantity = (quantity + 10) % 100 
            elif kc == 2:
                bnsd.drawText("- 10", light_green, 30, 90)
                quantity = (quantity - 10) % 100
            bnsd.show()
            time.sleep(0.15)
        
        result['quantity'] = f'{quantity}'
        
    operating_type()
    alt_operating_quantity()
    print(result)
    return result

def start_exercising(result):
    count = 1
    time_left = 5
    
    def draw_info(mode, quantity, count, time_left):
        bnsd.drawLine(40, 0, 40, 128, light_green)
        bnsd.drawText(f"{count}", light_green, 0, 10)
        bnsd.drawLine(5, 30, 25, 10, light_green)
        bnsd.drawText(f"{quantity}", light_green, 15, 25)
        bnsd.drawText(f"{time_left/10}s", light_green, 5, 110)
        bnsd.drawText(f"{mode} Mode", light_green, 65, 10)
    
    def draw_options(options, show1, show2c, kc, current_sign):
        is_left_up_active = kc == 0
        is_left_down_active = kc == 2
        is_right_up_active = kc == 5
        is_right_down_active = kc == 6
        draw_triangle(True, 90, 60, is_left_up_active)
        draw_triangle(False, 90, 110, is_left_down_active)
        draw_triangle(True, 130, 60, is_right_up_active)
        draw_triangle(False, 130, 110, is_right_down_active)
        bnsd.drawText(f"{options[show1]}", light_green, 85, 80)
        bnsd.drawText(f"{options[show2]}", light_green, 125, 80)
        bnsd.drawText(current_sign, light_green, 60, 80)
    
    def draw_triangle(up, x, y, is_active):
        color = light_green if is_active else dark_green
        if up:
            bnsd.drawUpTriangle(x, y, 25, 10, color, True)
        else:
            bnsd.drawDownTriangle(x, y, 25, 10, color, True)
        
        
    def gen_question(mode):
        if mode == 'Mixed':
            operands = ['+', '-', 'x', '/']
        elif mode == 'Focus':
            operands = ['+', '-']
        operand = random.randint(0, len(operands) - 1)
        operator1 = random.randint(0, 40)
        operator2 = random.randint(0, 40)
        return f'{operator1}' + f' {operands[operand]} ' + f'{operator2}'
    
    options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    global kc
    kc = -1
    show1 = 0
    show2 = 0
    
    while kc != 7:
        bnsd.clear(black)
        count = 1
        current_sign = "+"
        
        while count <= int(result['quantity']):
            question = gen_question(result['mode'])
            time_left = 50
            show1 = show2 = 0
            
            while time_left >= 0 and kc != 7:
                kc = keyCode(adcIn)
                if kc == 0:
                    show1 = (show1 + 1) % len(options)
                elif kc == 2:
                    show1 = (show1 - 1) % len(options)
                elif kc == 5:
                    show2 = (show2 + 1) % len(options)
                elif kc == 6:
                    show2 = (show2 - 1) % len(options)
                elif kc == 1:
                    current_sign = "+" if current_sign == "-" else "-"
                    
                bnsd.clear(black)
                draw_info(result['mode'], result['quantity'], count, time_left)
                bnsd.drawText(question, light_green, 80, 30)
                draw_options(options, show1, show2, kc, current_sign)
                bnsd.show()
                time_left -= 1
                time.sleep(0.1)

            count += 1
            
main_menu()

