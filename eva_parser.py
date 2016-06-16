__author__ = 'kli1'
import re
import sys
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
search_WWN='(?<=^WWN:).*[0-9A-Za-z]+[[0-9A-Za-z]+[[0-9A-Za-z]+[[0-9A-Za-z]-[0-9A-Za-z]+[[0-9A-Za-z]+[[0-9A-Za-z]+[[0-9A-Za-z]-[0-9A-Za-z]+[[0-9A-Za-z]+[[0-9A-Za-z]+[[0-9A-Za-z]-[0-9A-Za-z]+[[0-9A-Za-z]+[[0-9A-Za-z]+[[0-9A-Za-z]'

search_Location='(?<=Location:).*?$|^Enclosure:.*?$'
search_FailingHostName='(?<=FailingHostName:).*?$'
search_EventCode= '(?<=Event Code:).*\([0-9A-Z]+[0-9A-Z] [0-9A-Z]+[0-9A-Z] [0-9A-Z]+[0-9A-Z] [0-9A-Z]+[0-9A-Z]\)$'
search_ControllerType='(?<=Controller Type:).*HSV+[0-9]+[0-9]+[0-9]'
search_PartNumberbyBLI='(?<=Part Number by BLI:) [0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]-[0-9]+[0-9]+[0-9]'
search_SparePartNumber= '(?<=Spare part number:) [0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]-[0-9]+[0-9]+[0-9]'
search_PartDescription='(?<=Part Description:).*?$'

def eva_log_parser(log):
    #inital dict
    dict_parser = dict().fromkeys(
        ['Name',
        'Company',
        'Address',
        'Country',
        'Phone',
        'Email',
        'Hours of Availability',
        'Support Delivery Queue',
        'EntitlementStatus',
        'SLA',
        'Entitlement Type',
        'Serial Number',
        'Product Number',
        'WWN',
        'Location',
        'FailingHostName',
        'EventCode',
        'Controller Type',
        'Part Number',
        'Part Description',
        'Recommended action',
        'Environment',
        'Issue'], ''
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
    dict_parser['WWN'] = get_value.search_value(log,search_WWN)
    dict_parser['Location'] = get_value.search_value(log,search_Location)
    dict_parser['FailingHostName'] = get_value.search_value(log,search_FailingHostName)
    dict_parser['Controller Type'] = get_value.search_value(log,search_ControllerType)

    dict_parser['Event Code'] = get_value.search_value(log,search_EventCode)
    dict_parser['Part Number'] = get_value.search_value(log,search_PartNumberbyBLI) if get_value.search_value(log,search_PartNumberbyBLI) else get_value.search_value(log,search_SparePartNumber)
    dict_parser['Part Description'] = get_value.search_value(log,search_PartDescription)
    return dict_parser

if __name__ == '__main__':

   ss= ' yyu:uyn  '+'\n'' \
   ''ssdssds  :  ddd   '
   eva_log_parser(ss)


