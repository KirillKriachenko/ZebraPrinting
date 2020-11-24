# This is a sample Python script.
from zebra import Zebra
import os, sys
import win32print
import printer_barcode

import os
from PIL import Image
import zpl


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l = zpl.Label(100, 60)
    height = 0
    l.origin(0, 0)
    l.write_text("Problem?", char_height=10, char_width=8, line_width=60, justification='C')
    l.endorigin()

    height += 13
    image_width = 5
    l.origin((l.width - image_width) / 2, height)
    image_height = l.write_graphic(
        Image.open('test-barcode.png'),
        # Image.open(os.path.join(os.path.dirname(zpl.__file__), 'test-barcode.png')),
        image_width)
    l.endorigin()

    height += image_height + 5
    l.origin(22, height)
    l.write_barcode(height=70, barcode_type='U', check_digit='Y')
    l.write_text('07000002198')
    l.endorigin()

    height += 20
    l.origin(0, height)
    l.write_text('Happy Troloween!', char_height=5, char_width=4, line_width=60,
                 justification='C')
    l.endorigin()

    print(l.dumpZPL())
    l.preview()

    print(type(l.dumpZPL()))

    zpl = """
    ^XA
    ^FO150,40^BY3
    ^BCN,110,Y,N,N
    ^FD123456^FS
    ^FO0,0^A0N,120,96^FB720,1,0,C,0^FDProblem?
    ^XZ 
    """

    print(type(zpl))

    printer = win32print.OpenPrinter('ZDesigner GX420d')
    job = win32print.StartDocPrinter(printer,1,('test of raw data',None,"RAW"))
    #
    #
    raw_data = bytes(l.dumpZPL(), 'utf-8')
    # print(raw_data)
    #
    win32print.StartPagePrinter(printer)
    win32print.WritePrinter(printer,raw_data)
    win32print.EndPagePrinter(printer)




























    # printer_barcode.create_qrcode('Test')
    # printer_barcode.zebra_print('Start 114 Combine')
    # p = win32print.OpenPrinter('ZDesigner GX420d')
    # job = win32print.StartDocPrinter(p,1,('test of raw data',None,"TEXT"))
    #
    # raw_data = bytes ('Hi from Python','utf-8')
    #
    # win32print.StartPagePrinter(p)
    # win32print.WritePrinter(p,raw_data)
    # win32print.EndPagePrinter(p)


    # # print('-------------')
    # # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
