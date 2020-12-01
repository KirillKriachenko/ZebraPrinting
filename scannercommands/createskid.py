from scannercommands import record_skid

def create_skid(serial_port,user):
    skid_barcode_list = []

    CONTINUE_SCANING = True
    OBJECT_IDS = ''

    while CONTINUE_SCANING == True:
        if serial_port.in_waiting > 0:
            serialString = serial_port.readline()
            string = str(serialString)
            string = string[2:len(string) - 3]
            if OBJECT_IDS == '':
                if user.find_skid_ids(string) == True:
                    OBJECT_IDS = string

            elif string != OBJECT_IDS:
                skid_barcode_list.append(string)
            elif string == OBJECT_IDS:
                CONTINUE_SCANING = False
            print(serialString)

    record_skid.start_threading(skid_barcode_list,OBJECT_IDS,user)
    create_skid(serial_port,user)
    #TODO: Create function to check what was included to skid and color finished module in odoo.
    #TODO: Navigate back to Read new Barcode to create new Barcode skid
    #TODO: Check if this already was scanned and EDIT on change.

