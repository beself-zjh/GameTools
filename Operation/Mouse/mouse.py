import numpy as np
import win32api
import win32con

class IMouse():
    """Mouse interface"""

    def LeftClick(self, hwnd):
        raise NotImplementedError

class PointMouse:
    """Mouse operates on a point"""

    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def LeftClick(self, hwnd):
        pos = win32api.MAKELONG(self.x, self.y)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, pos)


class RangeMouse:
    """Mouse operates on range"""

    def __init__(self, left:int, top:int, right:int, bottom:int) -> None:
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
    
    def LeftClick(self, hwnd):
        x = np.random.randint(self.left, self.right + 1)
        y = np.random.randint(self.top, self.bottom)
        pos = win32api.MAKELONG(x, y)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, pos)
