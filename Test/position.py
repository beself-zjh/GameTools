from win32com.client import Dispatch
import pynput.mouse as pm

op = Dispatch("op.opsoft.1")
hwnd = op.FindWindow("", "雷电模拟器")
op.BindWindow(hwnd, "gdi", "normal", "normal", 1)
# op.SetClientSize(hwnd, 871, 580)
# print(op.GetWindowProcessId(hwnd))
# op.MoveWindow(hwnd, 0, 0)
op.ScreenToClient(hwnd)


def on_move(x, y):
    # 监听鼠标点击
    pos = op.GetCursorPos()
    mxy="({},{})".format(x, y)
    print(pos, mxy)

with pm.Listener(on_move=on_move) as pmlistener:
    pmlistener.join()
