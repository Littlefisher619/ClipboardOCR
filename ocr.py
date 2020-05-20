from aip import AipOcr
from PIL import ImageGrab
from time import sleep
import win32clipboard as wincld
import io

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_image_from_file(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def print_ocr_results(img,multiplelines=True):
    ocrresult=client.basicGeneral(img)
    resulttext=''
    for i in ocrresult['words_result']:
        print(i['words'],end= '\n' if multiplelines else '')

def get_image_from_clipboard():
    im = ImageGrab.grabclipboard()
    if im is None:
        return None
    print('[+]image size: %sx%s\nOCR Result >>>' % (im.size[0], im.size[1]))
    mf = io.BytesIO()
    im.save(mf, 'JPEG')
    mf.seek(0)
    return mf.read()

def clear_clipboard():
    wincld.OpenClipboard()
    wincld.EmptyClipboard()
    wincld.CloseClipboard()

if __name__ == '__main__':

    print('[*]Monitoring on Clipboard...')
    while True:
        sleep(0.2)
        img = get_image_from_clipboard()
        if img is None:
            continue

        print_ocr_results(img)
        clear_clipboard()
        print('[-]Clipboard cleared.')
        print('[*]Monitoring on Clipboard...')


'''
import win32con
import win32clipboard as wincld


def get_text():
    wincld.OpenClipboard()
    text_result = wincld.GetClipboardData(win32con.CF_DSPBITMAP)
    wincld.CloseClipboard()
    return text_result


def set_text(info):
    wincld.OpenClipboard()
    wincld.EmptyClipboard()
    wincld.SetClipboardData(win32con.CF_UNICODETEXT, info)
    wincld.CloseClipboard()
'''