import threading
import json

def start_threading(barcode_list,deliveryunit_ids,user):
    delivery_record = user.find_delivery_data(deliveryunit_ids)
    print('------------------------------')
    skid_name = str(delivery_record[0].get('unit_ids')[1]) + ' ' + str(delivery_record[0].get('project_ids')[1])
    print(skid_name)
    # print(test["project_ids"])

    new_thread = threading.Thread(target=record_skid, args=(barcode_list,skid_name,deliveryunit_ids,user))
    new_thread.start()


def record_skid(barcode_list,skid_name,deliveryunit_ids,user):

    skid_ids = user.create_skid_record(skid_name,deliveryunit_ids)


    for barcode in barcode_list:
        print('BARCODE: ', barcode)
        user.create_barcode_boxes_records(barcode,skid_ids)