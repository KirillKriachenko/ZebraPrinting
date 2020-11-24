


























# from io import BytesIO
#
# import barcode
# import win32print
# import os,sys
#
# from barcode import Code128, EAN13
# from barcode.writer import ImageWriter
#
# import pyqrcode
# import png
# from pyqrcode import QRCode
# from zebra import Zebra
#
# def create_qrcode(text):
#
#     # url = pyqrcode.create(text)
#     # url.png('test',scale=2)
#     zebra_print()
#
#
# def zebra_print():
#     z = Zebra()
#     print('Printer queues found:', z.getqueues())
#     z.setqueue('ZDesigner GX420d')
#     # z.autosense()
#     z.setup(direct_thermal=True,label_height=(104,2),label_width=66)
#     z.print_config_label()

    # print(z.setup())
    # print(z.)
    # z.setup(direct_thermal=True, label_height=(406, 32), label_width=609)  # 3" x 2" direct thermal label
    # z.store_graphic('test', 'test.png')
    # label = """
    # N
    #
    # A50,150,0,4,1,1,N,"Example 4
    #
    # """
    # z.output("A50,150,0,4,1,1,N,'Example 4'")
    # print(z.output("A50,150,0,4,1,1,N,'Example 4'"))

# def print_proccess(text_to_print):
#     printer = win32print.OpenPrinter('ZDesigner GX420d')
#     job = win32print.StartDocPrinter(printer,1,('test of raw data',None,"TEXT"))
#
#     raw_data = bytes(text_to_print,'utf-8')
#
#
#     win32print.StartPagePrinter(printer)
#     win32print.WritePrinter(printer,'Test')
#     win32print.EndPagePrinter(printer)