from scannercommands import record_skid
import threading
import multiprocessing
import serial
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def create_skid(serial_port, user):
    skid_barcode_list = []

    CONTINUE_SCANING = True
    OBJECT_IDS = ''

    print('Please scann skid code... ')

    while CONTINUE_SCANING == True:
        if serial_port.in_waiting > 0:
            serialString = serial_port.read_all()
            string = str(serialString)
            string = string[2:len(string) - 3]
            if "\n" in string:
                string = string.rstrip("\n")
            print(string)
            if OBJECT_IDS == '':
                if user.find_skid_ids(string) == True:
                    OBJECT_IDS = string
                    command_excepted = bytes([0x1B, 0x5B, 0x31, 0x71, 0x0D])
                    serial_port.write(command_excepted)

                else:
                    command_wrong = bytes(
                        [0x1B, 0x5B, 0x38, 0x71, 0x1B, 0x5B, 0x35, 0x71, 0x1B, 0x5B, 0x30, 0x71, 0x1B, 0x5B, 0x31, 0x71,
                         0x1B, 0x5B, 0x30, 0x71, 0x1B, 0x5B, 0x31, 0x71, 0x0D])
                    serial_port.write(command_wrong)

            elif string != OBJECT_IDS:
                skid_barcode_list.append(string)
                command_excepted = bytes([0x1B, 0x5B, 0x31, 0x71, 0x0D])
                serial_port.write(command_excepted)

            elif string == OBJECT_IDS:
                command_excepted = bytes([0x1B, 0x5B, 0x30, 0x71, 0x0D])
                serial_port.write(command_excepted)
                CONTINUE_SCANING = False

            # print(serialString)

    recordskid(skid_barcode_list, OBJECT_IDS, user, serial_port)
    create_skid(serial_port, user)


def recordskid(barcode_list, deliveryunit_ids, user, serial_port):
    # start = time.time()
    delivery_record = user.find_delivery_data(deliveryunit_ids)
    # end = time.time()
    # print(end - start)
    print(delivery_record)
    if delivery_record != False:
        start = time.time()
        skid_name = str(delivery_record[0].get('unit_ids')[1]) + ' ' + str(delivery_record[0].get('project_ids')[1])
        end = time.time()
        print('SKID_NAME', end - start)
        print(skid_name)
        print('----------')
        start = time.time()
        skid_record_id = user.find_skid_record(skid_name, deliveryunit_ids)
        end = time.time()
        print('Create or find skid', end - start)
        print(skid_record_id)

        for barcode in barcode_list:
            user.record_barcode(barcode,skid_record_id)

        user.check_skid_for_completion(skid_record_id)

    # if delivery_record != False:
    #     skid_name = str(delivery_record[0].get('unit_ids')[1]) + ' ' + str(delivery_record[0].get('project_ids')[1])
    #     recordskid_barcodes(barcode_list, skid_name, deliveryunit_ids, user, serial_port)
    #
    # else:
    #     command_wrong = bytes(
    #         [0x1B, 0x5B, 0x38, 0x71, 0x1B, 0x5B, 0x35, 0x71, 0x1B, 0x5B, 0x30, 0x71, 0x1B, 0x5B, 0x31, 0x71,
    #          0x1B, 0x5B, 0x30, 0x71, 0x1B, 0x5B, 0x31, 0x71, 0x0D])
    #     serial_port.write(command_wrong)


def recordskid_barcodes(barcode_list, skid_name, deliveryunit_ids, user, serial_port):
    skid_ids = user.create_skid_record(skid_name, deliveryunit_ids)

    for barcode in barcode_list:
        user.create_barcode_boxes_records(barcode, skid_ids)

    user.assigne_skid_to_unit(deliveryunit_ids, skid_ids)
    user.check_skid_for_completion(skid_ids)

    command_excepted = bytes([0x1B, 0x5B, 0x31, 0x71, 0x0D])
    serial_port.write(command_excepted)

    # new_thread = threading.Thread(target=record_skid.start_threading,args=(skid_barcode_list,OBJECT_IDS,user,))
    # new_thread.start()

    # another_thread = threading.Thread(target=create_skid, args=(serial_port,user,))
    # another_thread.start()
    # another_thread.join()

    # proccess = multiprocessing.Process(target=create_skid,args=(serial_port,user))
    # proccess.start()
    #
    # record_skid.start_threading(skid_barcode_list,OBJECT_IDS,user)

    # record_skid.start_threading(skid_barcode_list,OBJECT_IDS,user)
    # record_skid.start_threading(skid_barcode_list,OBJECT_IDS,user)
    # create_skid(serial_port,user)

    # record_skid.start_threading(skid_barcode_list,OBJECT_IDS,user)
    # create_skid(serial_port,user)
    # another_thread = create_skid(serial_port,user)
    # another_thread = threading.Thread(target=create_skid, args=(serial_port,user,))
    # another_thread.start()

    # TODO: Create function to check what was included to skid and color finished module in odoo.
    # TODO: Navigate back to Read new Barcode to create new Barcode skid
    # TODO: Check if this already was scanned and EDIT on change.
