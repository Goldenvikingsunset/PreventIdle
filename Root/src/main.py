import time
import pyautogui
import PySimpleGUI as sg
import multiprocessing

def prevent_idle():
    """
    Function that simulates activity by moving the mouse cursor
    """
    start_time = time.time()
    while True:
        pyautogui.moveRel(1, 1, duration=0.1)
        time.sleep(2)
        pyautogui.moveRel(-1, -1, duration=0.1)
        time.sleep(500)
        current_time = time.time()
        running_time = current_time - start_time
        window["time"].update(f"Running for {running_time} seconds")