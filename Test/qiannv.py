
# import moudles 导入pywin32的 Dispatch 函数
from win32com.client import Dispatch
import Constant.coordinate_const as CONST
import win32api
import win32con
import win32gui
import time

# create op instance 创建op对象
def test():
    # op = Dispatch("op.opsoft")
    # hwnd = op.FindWindowEx("LDPlayerMainFrame", "雷电模拟器")
    # # hwnds = hwndstr.split(',')
    # op.BindWindow(hwnd, "normal", "windows", "normal", 1)
    # # ret = op.GetWindowRect(hwnd)
    # # op.SetClientSize(hwnd, 871, 580) 
    # # op.MoveWindow(hwnds[0], 0, 0)
    # # op.SetWindowTransparent(hwnd, 255)
    # # ret = op.Capture(330, 313, 397, 341, "screen.bmp")
    # # text = op.Ocr(330, 313, 397, 341, "" ,0.8)
    # # ret,x,y = op.FindPic(0,0,2000,2000,"screen.bmp","0f0f0f",0.5,0)
    # # print(op.isBind())
    # # op.MoveWindow(op.GetBindWindow(), 0, 0)

    # # op.sleep(1000)
    # print(op.MoveTo(CONST.AVATAR_X, CONST.AVATAR_Y))
    # op.sleep(1000)
    # print(op.LeftClick())



    hwnd = win32gui.FindWindow(None, "雷电模拟器")
    print(hwnd)
    h = win32gui.FindWindowEx(hwnd, 0, None, "TheRender")
    print(win32gui.GetClassName(h))
    print(win32gui.GetWindowText(h))
    print(win32gui.GetWindowRect(h))
    # hwndChildList = []     
    # win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    # for h in hwndChildList:
    #     print(win32gui.GetWindowText(h))
    win32gui.MoveWindow(hwnd, 0, 0, 871, 580, True)
    pos = win32api.MAKELONG(CONST.AVATAR_X, CONST.AVATAR_Y)
    win32api.SendMessage(h, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, pos)
    # time.sleep(0.1)
    win32api.SendMessage(h, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, pos)
