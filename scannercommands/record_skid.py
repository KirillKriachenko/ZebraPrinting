import threading
import json

import concurrent.futures

def start_threading(barcode_list,deliveryunit_ids,user):
    print('Process started')
    print('USER',user)
    delivery_record = user.find_delivery_data(deliveryunit_ids)
    print('Delivery_record',delivery_record)
    skid_name = str(delivery_record[0].get('unit_ids')[1]) + ' ' + str(delivery_record[0].get('project_ids')[1])

    record_skid(barcode_list,skid_name,deliveryunit_ids,user)
    # record_skid(barcode_list,skid_name,deliveryunit_ids,user)

    # print('------------------------------')
    # print(delivery_record)

    # print(skid_name)
    # print(test["project_ids"])

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     executor.map(record_skid,)
    # new_thread = threading.Thread(target=record_skid, args=(barcode_list,skid_name,deliveryunit_ids,user,))
    # new_thread.start()
    #
    # new_thread.join()

def record_skid(barcode_list,skid_name,deliveryunit_ids,user):

    skid_ids = user.create_skid_record(skid_name,deliveryunit_ids)
    # print(skid_ids)

    for barcode in barcode_list:
        # print('BARCODE: ', barcode)
        user.create_barcode_boxes_records(barcode,skid_ids)

    user.assigne_skid_to_unit(deliveryunit_ids,skid_ids)

    user.check_skid_for_completion(skid_ids)