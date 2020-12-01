import os, sys
from PIL import Image
import zpl
import win32print


def generate_lable(text,project_id,unit_number, project_abriviation):
    l = zpl.Label(100,60)
    height = 2
    l.origin(0,2)
    l.write_text(text,char_height=10, char_width=8, line_width=60, justification='C')
    l.endorigin()

    qr_code_text = 'QA,%s,%s,%s' % (text,unit_number,project_id)

    print(qr_code_text)

    l.origin(2,17)
    l.write_barcode(height=70,barcode_type='Q',mode='2',mask='1',magnification=10)
    l.write_text(qr_code_text)
    l.endorigin()

    l.origin(15,15)
    l.write_text('Unit: %s' % (unit_number),char_height=8, char_width=8, line_width=60, justification='C')
    l.endorigin()

    l.origin(13, 26)
    l.write_text(project_abriviation, char_height=6, char_width=6, line_width=60, justification='C')
    l.endorigin()

    print_job(l.dumpZPL())


def print_job(zpl):
    printer = win32print.OpenPrinter('ZDesigner GX420d')
    job = win32print.StartDocPrinter(printer, 1, ('test of raw data', None, "RAW"))

    print(zpl)

    # string= '''
    # ^XA
    # ^FO0,24^A0N,120,96^FB720,1,0,C,0^FDStart^FS
    # ^FO0,180^BQN,2,10,Q,7^FS
    # ^XZ
    # '''

    raw_data = bytes(zpl, 'utf-8')

    win32print.StartPagePrinter(printer)
    win32print.WritePrinter(printer, raw_data)
    win32print.EndPagePrinter(printer)
