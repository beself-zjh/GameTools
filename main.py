import Test.qiannv as tq

tq.test()

# import win32gui

# hwnd_title = dict()


# def get_all_hwnd(hwnd, mouse):
#     hwnd_title.update({win32gui.GetClassName(hwnd): win32gui.GetWindowText(hwnd)})


# win32gui.EnumWindows(get_all_hwnd, 0)
# for handle, title in hwnd_title.items():
#     if title:
#         print("h:{},t:{}".format(handle, title))