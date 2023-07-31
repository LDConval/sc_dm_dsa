import pyautogui
import pydirectinput as pdi
import time, win32api, win32con, win32gui

from flask import Flask, render_template, Response, escape, request
import io
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(r'template.html')

build_keys = {
    'a': ['\xFF', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    'b': ['\xFF', 'T', 'Y', 'U', 'I', 'G', 'H', 'J', 'B', 'N', 'M']
}
gas_keys = {
    'a' : 'O',
    'b' : 'P'
}

def press_key(key):
    if key in '1234567890':
        # for some reason, SC uses different method for the numbet keys
        pdi.press(key)
        return
    sc_window_hwnd = win32gui.FindWindow(None, "Brood War")
    if not sc_window_hwnd:
        sc_window_hwnd = win32gui.FindWindow(None, "星际争霸：重制版")
    if not sc_window_hwnd:
        print("Cannot find SC window!!! Please launch StarCraft first")
        return
    win32api.SendMessage(sc_window_hwnd, win32con.WM_KEYDOWN, ord(key), 0)
    time.sleep(0.05)
    win32api.SendMessage(sc_window_hwnd, win32con.WM_KEYUP, ord(key), 0)

@app.route('/send_comment')
def commentary():
    try:
        comment = request.args.get("comment").strip()
        side = comment[0].lower()
        assert side == 'a' or side == 'b'
        if len(comment) == 2 and comment[1].lower() == 'g': # GAS
            press_key(gas_keys[side])
        else:
            type = int(comment[1:])
            assert type > 0 and type < 11
            press_key(build_keys[side][type])
    except Exception as e:
        pass
    try:
        username = request.args.get("username").strip()
        comment = request.args.get("comment").strip()
        with open("comments.txt", "a", encoding = "utf-8") as fp:
            fp.write(f"""<div><b class='user'>{ escape(username) }: </b><span>{ escape(comment) }</span></div>\n""")
    except Exception as e:
        pass
    return "OK"

if __name__ == '__main__':
    import socket
    local_ip = socket.gethostbyname(socket.gethostname())
    app.run(host=local_ip, port=1700, debug=True, threaded=True)