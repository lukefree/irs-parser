__author__ = 'kli1'
import re
import sys
reload(sys)

sys.setdefaultencoding('utf8')

def search_value(buff,search_term):

    for line in buff.split('\n'):
        m = re.search(search_term,line)
        if m:
            #print line

            values= m.group().split('\n')
            #print values
            for value in values:
                if str(value).strip():
                  print value, len(str(value).strip())
                  return str(value).strip()
    return ''

if __name__ == '__main__':

    ss= ' yyu:uyn  '+'\n'' \
   ''ssdssds  :  ddd   '


    search_value(ss,'ssss')
