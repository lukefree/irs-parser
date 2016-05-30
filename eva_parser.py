__author__ = 'kli1'

import sys
reload(sys)

sys.setdefaultencoding('utf8')


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
        'Workflow Case Title',
        'EntitlementStatus',
        'SLA',
        'Entitlement Type',
        'Serial Number',
        'Product Number',
        'WWN',
        'FailingFRULocation',
        'Drive Location',
        'FailingHostName',
        'Controller Type',
        'Part Number',
        'Spare part number',
        'Part Number by BLI',
        'Part Description',
        'Recommended action'], ''
    )
    name = ''
    value = ''

    if log:
        logbuff = log.split('\n')
        for line in logbuff:
            new_line = line.replace('=', ':')
            if new_line.count(':') > 0:
                value = ''
                s = new_line.split(':')
                name = str(s[0]).strip()
                for i in range(1,len(s)):
                   value = value + str(s[i]).strip()
            dict_parser[name] = value
    #check disk location
    print 'Drive Location', len(dict_parser['Drive Location'])
    if len(dict_parser['Drive Location'])>0:
        dict_parser['FailingFRULocation']=dict_parser['Drive Location']
    #check Serial number and Product Number
    if len(dict_parser['Serial Number']):
        pass
    else:
        dict_parser['Serial Number']=dict_parser['System Serial Number']

    if len(dict_parser['Product Number']):
        pass
    else:
        dict_parser['Product Number'] = dict_parser['System Product Number']


    if dict_parser['Part Number by BLI'].find('Spare part not recognized by BLI') < 0 and len(dict_parser['Part Number by BLI']) >0 :
        ss='Part Description'

        # Get part number
        PartNumber=dict_parser['Part Number by BLI'].split(',')
        dict_parser['Part Number'] = PartNumber[0]
        # Get part Description
        PartDescription = PartNumber[1].replace(ss,'')
        dict_parser['Part Description'] = PartDescription

    elif len(dict_parser['Spare part number']):
        dict_parser['Part Number'] = dict_parser['Spare part number']
    else:
        dict_parser['Part Number'] = 'Not Found'




    return dict_parser

if __name__ == '__main__':

   ss= ' yyu:uyn  '+'\n'' \
   ''ssdssds  :  ddd   '
   eva_log_parser(ss)


