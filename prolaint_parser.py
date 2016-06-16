__author__ = 'kli1'
import sys
import re
import get_value
reload(sys)

sys.setdefaultencoding('utf8')

search_Name='(?<=^Name:).*?$'
search_Company='(?<=^Company:).*?$'
search_Address = '(?<=^Address:).*?$'
search_Country='(?<=^Country:).*?$'
search_Phone='(?<=^Phone:).*?$'
search_Email='(?<=^Email:).*?$'
search_Availability='(?<=^Hours of Availability:).*?$'
search_SDQ='(?<=^Support Delivery Queue:).*?$'

search_EntitlementStatus='(?<=^EntitlementStatus:).*?$'
search_SLA='(?<=^SLA:).*?$'
search_EntitlementType='(?<=^Entitlement Type:).*?$'

search_SerialNumber='(?<=^Serial Number:).*?$'
search_ProductNumber='(?<=^Product Number:).*?$'
search_SystemSerialNumber='(?<=^System Serial Number:).*?$'
search_SystemProductNumber='(?<=^System Product Number:).*?$'
search_ServerModel='(?<=^Server Model:).*?$'
search_ServerModelinside='(?<=Server Model:).*(?=Server Product ID:)'
search_SystemName='(?<=^System Name:).*?$'

search_Location='(?<=^Failing FRU Location:).*?$'
search_Controller='(?<=^Smart Array Controller Model:).*?$'
search_OSVersion= '(?<=^OS Version:).*?$'

search_PartNumberbyBLI='(?<=^Part Number by BLI:) [0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]-[0-9]+[0-9]+[0-9]'
search_FailingFRUPartNumberr= '(?<=^Failing FRU Part Number:) [0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]-[0-9]+[0-9]+[0-9]'
search_PartDescription='(?<=Part Description:).*?$'


def proliant_log_parser(log):
    #inital dict
    dict_parser = dict().fromkeys(
        ['Name',
        'Company',
        'Address',
        'Email',
        'Country',
        'Phone',
        'Hours of Availability',
        'Support Delivery Queue',
        'EntitlementStatus',
        'SLA',
        'Entitlement Type',
        'Serial Number',
        'Product Number',
        'Server Model',
        'Server Name',
        'Location',
        'Controller',
        'OS Version',
        'Part Number',
        'Part Description',
        'Environment',
        'Issue'],''
    )
    name = ''
    value = ''

    dict_parser['Name'] = get_value.search_value(log,search_Name)
    dict_parser['Company']  = get_value.search_value(log,search_Company)
    dict_parser['Address']  = get_value.search_value(log,search_Address)
    dict_parser['Country'] = get_value.search_value(log,search_Country)
    dict_parser['Phone'] = get_value.search_value(log,search_Phone)
    dict_parser['Email'] = get_value.search_value(log,search_Email)
    dict_parser['Hours of Availability'] = get_value.search_value(log,search_Availability)
    dict_parser['Support Delivery Queue'] = get_value.search_value(log,search_SDQ)

    dict_parser['EntitlementStatus'] =get_value.search_value(log,search_EntitlementStatus)
    dict_parser['SLA'] = get_value.search_value(log,search_SLA)
    dict_parser['Entitlement Type'] = get_value.search_value(log,search_EntitlementType)

    dict_parser['Serial Number'] = get_value.search_value(log,search_SerialNumber) if get_value.search_value(log,search_SerialNumber) else get_value.search_value(log,search_SystemSerialNumber)
    dict_parser['Product Number'] = get_value.search_value(log,search_ProductNumber) if get_value.search_value(log,search_ProductNumber) else get_value.search_value(log,search_SystemProductNumber)

    dict_parser['Server Model'] = get_value.search_value(log,search_ServerModel) if get_value.search_value(log,search_ServerModel) else get_value.search_value(log,search_ServerModelinside)
    dict_parser['Server Name'] = get_value.search_value(log,search_SystemName)
    dict_parser['Location'] = get_value.search_value(log,search_Location)
    dict_parser['Controller'] = get_value.search_value(log,search_Controller)

    dict_parser['OS Version'] = get_value.search_value(log,search_OSVersion)
    dict_parser['Part Number'] = get_value.search_value(log,search_PartNumberbyBLI) if get_value.search_value(log,search_PartNumberbyBLI) else get_value.search_value(log,search_FailingFRUPartNumberr)
    dict_parser['Part Description'] = get_value.search_value(log,search_PartDescription)
    return dict_parser

if __name__ == '__main__':

   ss= ' yyu:uyn  '+'\n'' \
   ''ssdssds  :  ddd   '
   proliant_log_parser(ss)


