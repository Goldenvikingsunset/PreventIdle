import time
import pyautogui
import PySimpleGUI as sg
import multiprocessing


def KeepUI():

    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Make-Em-Think-You-Are-Working is now running.\nYou can keep it minimised, and it will continue running.\nClose it to disable it.', font=("Helvetica", 15), text_color='#FFD700')],
        [sg.Button('Start', key='Start'), sg.Button('Stop', key='Stop', disabled=True)]
    ]

    window = sg.Window('Make-Em-Think-You-Are-Working', layout, alpha_channel=1,
                       element_justification='c', background_color='#2F4F4F')

    while True:
        event, values = window.read()
        if event == 'Start':
            p2 = multiprocessing.Process(target=dontsleep)
            p2.start()
            window['Start'].update(disabled=True)
            window['Stop'].update(disabled=False)
        elif event == 'Stop':
            p2.terminate()
            window['Start'].update(disabled=False)
            window['Stop'].update(disabled=True)
        elif event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            if p2.is_alive():
                p2.terminate()
            break


def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(2)
        pyautogui.press('volumeup')
        time.sleep(500)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=KeepUI)
    p1.start()