# This is a sample Python script.
from gui import main_form
import serial, sys
import getpass
from odoo_api import la_odoo_api
from scannercommands import createskid

# USER_UID = ''
USER = ''

SERIAL_PORT = serial.Serial('COM4',9600,timeout=0.5)

def authentification():
    email = input("Email: ")
    password = getpass.getpass()

    check_user = la_odoo_api.check_login_user(email,password)
    if check_user:
        global USER_LOGED_IN
        # global USER_UID
        global USER

        USER_LOGED_IN = True

        # USER_UID = check_user
        USER = check_user

    else:
        print('USER %s NOT FOUND' % email)
        print('Please try again')
        authentification()

# def get_from_scanner(command):
#     if command == 'CreateSkid':
#         global LISTEN_FOR_COMMAND
#         LISTEN_FOR_COMMAND = False

# def get_from_scanner(barcode,command):
#     if command == 'add':
#         BOX_BARCODE_LIST.append(barcode)

if __name__ == '__main__':
    global GET_COMMAND
    GET_COMMAND = True
    print('Please enter your login infomation: ')
    authentification()
    while GET_COMMAND == True:
        if SERIAL_PORT.in_waiting > 0:
            serialString = SERIAL_PORT.readline()

            command = str(serialString)
            command = command[2:len(command) - 3]
            print(command)

            message = 'ESC[8qESC[3qESC[9q'.encode('ASCII')
            SERIAL_PORT.write(message)

            if command == 'CreateSkid':

                GET_COMMAND = False
                createskid.create_skid(SERIAL_PORT,USER)



    # while USER_LOGED_IN == True:
    #     if (serialPort.in_waiting > 0):
    #         serialString = serialPort.readline()
    #
    #         command = str(serialString)
    #
    #         print(command)




#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

    # main_form.create_gui()



    # filebuffer = dev[0].interfaces()[0].endpoints()[0]
    # interface_number = dev[0].interfaces()[0].bInterfaceNumber
    # dev.reset()
    #
    # if dev.is_kernel_driver_active(interface_number):
    #     dev.detach_kernel_driver(interface_number)
    #
    # dev.set_configuration()
    # endpoint_address = filebuffer.bEndpointAddress
    #
    # reader = dev.read(endpoint_address, 1024)
    #
    # print(len(reader))
    # print(reader)
    #
    # dev.attach_kernel_driver(interface_number)
    # main_form.create_gui()






























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
