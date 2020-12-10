from xmlrpc import client as xmlrpclib
import json


LA_ODOO_URL = 'http://localhost:8070'
# LA_ODOO_URL = 'https://odoo.livingart.ca:8443'
LA_ODOO_DB = 'LivingartDB'
# LA_ODOO_DB = 'odoo.livingart.ca'
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(LA_ODOO_URL))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(LA_ODOO_URL))


def check_login_user(username, password):
    uid = common.login(LA_ODOO_DB, username, password)
    if uid != False:
        print('Loggin SUCCESS.')
        print('Please scann command...')
        return User(username, password, uid)
    else:
        return False


# def find_skid_ids(uid,password,skid_id):
#     print(skid_id)
#     find_skid = models.execute(LA_ODOO_DB,uid,password,'la.deliveryunits','search_count',
#                    [[['id','=',skid_id]]])
#     print(find_skid)
#     if find_skid > 0:
#         print('TRUE')

class User:
    def __init__(self, email, password, uid):
        self.common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(LA_ODOO_URL))
        self.models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(LA_ODOO_URL))

        self.email = email
        self.password = password
        self.uid = common.authenticate(LA_ODOO_DB, self.email, self.password, {})

    def find_skid_ids(self, skid_id):
        try:
            find_skid = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password, 'la.deliveryunits', 'search_count',
                                               [[['id', '=', skid_id]]])
            return True
        except:
            print('Skid code not found')
            return False


    def find_delivery_data(self, skid_id):
        # print('SKID ID', skid_id)
        try:
            find_delivery_record = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password,
                                                          'la.deliveryunits', 'search_read',
                                                          [[['id', '=', skid_id]]],
                                                          {'fields': ['id', 'project_ids', 'unit_ids'], 'limit': 1})
            print()
            return find_delivery_record
        except:
            print('Delivery data not found.')
            return False
            # print(find_delivery_record)

    def find_skid_record(self,skid_name,deliveryunit_ids):
        try:
            find_skid = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password, 'la.skiddata', 'search_read',
                                               [[['delivery_unit_ids.id', '=', deliveryunit_ids]]],
                                               {'fields': ['id'], 'limit': 1})
            if not find_skid:
                find_skid = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password, 'la.skiddata', 'create',
                                                   [{
                                                       'scid_name': skid_name,
                                                       'delivery_unit_ids': deliveryunit_ids
                                                   }])
                print(find_skid)
                return find_skid
            else:
                print(find_skid[0].get('id'))
                return find_skid[0].get('id')
        except:
            print('Create skid faild')


    def record_barcode(self,barcode, skid_ids):
    # print('SKID_IDS ', skid_ids)
        try:
            find_product_ids = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password,
                                                      'barcode.product', 'search_read',
                                                      [[['barcode', '=', barcode]]],
                                                      {'fields': ['product_ids']})
            #
            # find_product_ids = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password,
            #                                           'barcode.product', 'search_read',
            #                                           [[['barcode', '=', barcode]]])

            print(find_product_ids)
            # for found_product in find_product_ids:
            #     print(found_product[0].get('product_ids')[0])
            #     check_if_active = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password,
            #                                               'product.product','search_read',
            #                                               [[['active','=',True],['id','=',found_product[0].get('product_ids')[0]]]])
            #     print(check_if_active)
            last_id = len(find_product_ids)-1
            print(find_product_ids[last_id].get('product_ids')[0])
            if find_product_ids != []:
                record = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password, 'la.boxdata', 'create',
                                                [{
                                                    'barcode': barcode,
                                                    'product_ids': find_product_ids[0].get('product_ids')[0],
                                                    'skid_ids': skid_ids
                                                }])
            else:
                print('Product with barcode ---{0}--- NOT FOUND'.format(barcode))
        except:
            print('Find product Error')

    # def create_skid_record(self, skid_name, deliveryunit_ids):
    #     try:
    #         # print('SKID_ID ', deliveryunit_ids)
    #         find_skid = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password, 'la.skiddata', 'search_read',
    #                                            [[['delivery_unit_ids.id', '=', deliveryunit_ids]]],
    #                                            {'fields': ['id'], 'limit': 1})
    #         # print('FIND_SKID', find_skid)
    #
    #         if not find_skid:
    #             find_skid = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password, 'la.skiddata', 'create',
    #                                                [{
    #                                                    'scid_name': skid_name,
    #                                                    'delivery_unit_ids': deliveryunit_ids
    #                                                }])
    #             # print('CREATED SKID ', find_skid)
    #
    #             return find_skid
    #         else:
    #             # print(find_skid[0].get('id'))
    #             return find_skid[0].get('id')
    #         # create_skid =
    #     except:
    #         print('Something went wrong - create_skid_record')
    #
    # def create_barcode_boxes_records(self, barcode, skid_ids):
    #     # print('SKID_IDS ', skid_ids)
    #     try:
    #         find_product_ids = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password,
    #                                                   'barcode.product', 'search_read',
    #                                                   [[['barcode', '=', barcode]]],
    #                                                   {'fields': ['product_ids'], 'limit': 1})
    #         # print(find_product_ids)
    #         # print('----------------------')
    #         # print(find_product_ids[0].get('product_ids')[0])
    #         if find_product_ids != []:
    #             record = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password, 'la.boxdata', 'create',
    #                                             [{
    #                                                 'barcode': barcode,
    #                                                 'product_ids': find_product_ids[0].get('product_ids')[0],
    #                                                 'skid_ids': skid_ids
    #                                             }])
    #     except:
    #         print('Something get wrong - create_barcode_boxes_records')
    #
    # def assigne_skid_to_unit(self,deliveryunit_id,skid_id):
    #     # print('DELIVERY Unit ', deliveryunit_id)
    #     # print('Skid id ', skid_id)
    #     try:
    #         update_deliveryunit = self.models.execute_kw(LA_ODOO_DB, self.uid, self.password, 'la.deliveryunits', 'write', [[deliveryunit_id], {
    #             'skid_ids': skid_id
    #         }])
    #     except:
    #         print('Skid not assigned - assigne_skid_to_unit')
    #

    def check_skid_for_completion(self,skid_id):
        try:
            if_test = self.models.execute_kw(LA_ODOO_DB,self.uid,self.password,'la.skiddata','test_function',[skid_id])
        except:
            print('Something get wrong - check_skid_for_completion')



        # try:
        #
        #     print(check)
        # except:
        #     print('problems')
# common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
# models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
#
# uid = common.login(db, username, password)
#
# select_list = models.execute_kw(db, uid, password, 'la.recuts', 'search',
#                                 [[['part_barcode', '!=', ''], ['cabinet_part', '!=', ''], ['recut_color', '=', False],
#                                   ['notes', '=', False], ['po', '=', False], ['state', '=', 'waiting']]])
#
# for rec in select_list:
#     find_recut = models.execute_kw(db, uid, password, 'la.recuts', 'read', [rec], {'fields': ['part_barcode']})
#     connection = psycopg2.connect(
#         host="localhost",
#         database="production_database",
#         user="lauser",
#         password="lauser@123")
#
#     for record in find_recut:
#         barcode = record['part_barcode']
#         print(barcode)
#
#         cursor = connection.cursor()
#         postgreSQL_select_query = "SELECT * FROM production_records where barcode = %s"
#         cursor.execute(postgreSQL_select_query, (barcode,))
#         row = cursor.fetchone()
#         if row:
#             print(row)
#             cutting_string = row[3]
#             cabinet_name = row[5]
#             cabinet_part = row[6]
#             part_color = row[7]
#
#             new_row = cutting_string.replace('{', '')
#             new_row = new_row.replace('}', '')
#             new_row = new_row.replace('""', '')
#             new_row = new_row.encode().decode('unicode_escape')
#
#             models.execute_kw(db, uid, password, 'la.recuts', 'write', [[rec], {
#                 'cut_string': new_row,
#                 'cabinet': cabinet_name,
#                 'cabinet_part': cabinet_part,
#                 'recut_color': part_color,
#                 'recut_reason': 'Production recut'
#             }])
#
#         else:
#             print('NOT found', barcode)
#
#         cursor.close()
#
#     connection.close()

# print(barcode)

# print(select_list)

# # connection = psycopg2.connect(
# #         host="localhost",
# #         database="production_database",
# #         user="openpg",
# #         password="openpgpwd"
# #     )

# # barcode_dic = {}
# for record in select_list:
#     recut_id = record['id']
#     barcode = record['part_barcode']

#     cursor = connection.cursor()
#     postgreSQL_select_query = "SELECT * FROM production_records where barcode = %s"
#     cursor.execute(postgreSQL_select_query, (barcode,))
#     row = cursor.fetchone()

#     cutting_string = row[3]
#     cabinet_name = row[5]
#     cabinet_part = row[6]
#     part_color = row[7]

#     new_row = cutting_string.replace('{','')
#     new_row = new_row.replace('}','')
#     new_row = new_row.replace('""','')
#     new_row = new_row.encode().decode('unicode_escape')

#     models.execute_kw(db, uid, password, 'la.recuts', 'write', [[recut_id], {
#         'cut_string': new_row,
#         'cabinet':cabinet_name,
#         'cabinet_part':cabinet_part,
#         'recut_color':part_color,
#         'recut_reason':'Production recut'
#     }])


#     cursor.close()

# connection.close()


#    #//////////////////////////////////////////////////////////////


# dict1 = {recut_id:barcode}
# barcode_dic.update(dict1)

# print(barcode_dic)

# for data in barcode_dic:
#     barcode = barcode_dic.get(data)
#     print(barcode)

#     connection = psycopg2.connect(
#         host="localhost",
#         database="production_database",
#         user="openpg",
#         password="openpgpwd"
#     )


# connection = psycopg2.connect(
#     host="127.0.0.1",
#     database="production_database",
#     user="lauser",
#     password="lauser@123"
# )

# dat = json.dumps(record)
# data = json.loads(dat)
# print(data["id"])
# data = json.loads(record)
# json_data = json.load(record)
# print(json_data)


# def obj_dict(obj):
#     return obj.__dict__

# for rec in select_list:
#     json_string = json.dumps(rec,default=obj_dict)

#     print(json_string.id)
