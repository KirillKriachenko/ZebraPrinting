
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

    print(skid_barcode_list)


