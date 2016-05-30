__author__ = 'kli1'
import sys
reload(sys)

sys.setdefaultencoding('utf8')


def prolaint_log_parser(log):
    #inital dict
    dict_parser = dict().fromkeys(
        ['Name',
        'Company',
        'Address',
        'Country',
        'Phone',
        'Email',
        'Support Delivery Queue',
        'Workflow Case Title',
        'Hours of Availability',
        'OS Version',
        'Failing FRU Location',
        'Failing FRU Part Number',
        'Part Number by BLI',
        'System Name',
        'error_location',
        'EntitlementStatus',
        'SLA',
        'Entitlement Type',
        'Serial Number',
        'Product Number',
        'Model',
        'Reporting Device Serial Number',
        'Reporting Device Product Number'],' '
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
    return dict_parser

if __name__ == '__main__':

   ss= ' yyu:uyn  '+'\n'' \
   ''ssdssds  :  ddd   '
   prolaint_log_parser(ss)


