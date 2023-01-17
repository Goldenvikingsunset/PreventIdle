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

def stop_script():
    """
    Function that stops the script
    """
    window["start"].update(visible=True)
    window["stop"].update(visible=False)
    global running
    running = False

def start_script():
    """
    Function that starts the script
    """
    global running
    running = True
    window["start"].update(visible=False)
    window["stop"].update(visible=True)