import pyautogui
import time

n = 43

time.sleep(3);
pyautogui.write('@');
for i in range(n):
    pyautogui.hotkey('up');
time.sleep(1);
pyautogui.hotkey('enter');

for i in range(n-2):
    pyautogui.write('@');
    pyautogui.hotkey('down');
    pyautogui.hotkey('enter');
    print(i+1);
