import pyautogui as input_device
import time
from typing import NamedTuple

class MousePoint(NamedTuple):
    x:int
    y:int

def get_mouse_point()-> MousePoint:
    print("[ Program ] Please move mouse to target point in 3 seconds...")
    time.sleep(3)
    x,y = input_device.position()
    print(x,y)
    return MousePoint(x,y)
    
