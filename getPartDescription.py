__author__ = 'kli1'


def getPartDesc(line):


      idx = line.find('Part Description:')
      #ss = line[idx+len('Part Description:'):]
      print idx
      if -1>0 :
          print 1
      else:
          print 2

if __name__ == '__main__':

    getPartDesc("671148-001, Part Description: 1000GB (1-TB) 7.2K FATA 1\" add on hard drive, CSR: A, RoHS: Yes")