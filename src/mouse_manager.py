import pyautogui as input_device
import time
from typing import NamedTuple

class MousePoint(NamedTuple):
    x:int
    y:int

def capture_mouse_position()-> MousePoint:
    print("[ Mouse Manager ] Please move mouse to target point in 3 seconds...")
    time.sleep(3)
    x,y = input_device.position()
    return MousePoint(x,y)
    
def move_mouse_to(target:MousePoint, time:float)->None:
    input_device.moveTo(target.x, target.y, time)

def drag_mouse_to(target:MousePoint, time:float)-> None:
    input_device.dragTo(target.x, target.y, time)

def click_left_button():
    input_device.click()

def press_key(key:str):
    input_device.press(key)

def press_hotkey(first_key:str, secod_key: str):
    input_device.hotkey(first_key, secod_key)