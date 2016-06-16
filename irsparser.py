# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import PyQt4, PyQt4.QtGui, sys   
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
import xp_parser, eva_parser, prolaint_parser
import sys
reload(sys)

sys.setdefaultencoding('utf8')

from Ui_irsparser import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_ux_sbmtbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_ux_rstbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_eva_sbmtbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        eva_dict_parser = eva_parser.eva_log_parser(self.textEdit_eva.toPlainText())
        self.lineEdit_evaname.setText(eva_dict_parser["Name"])
        self.lineEdit_evacompany.setText(eva_dict_parser["Company"])
        self.lineEdit_evaaddress.setText(eva_dict_parser["Address"])
        self.lineEdit_evaemail.setText(eva_dict_parser["Email"])
        self.lineEdit_evacountry.setText(eva_dict_parser["Country"])
        self.lineEdit_evaphone.setText(eva_dict_parser["Phone"])
        self.lineEdit_evasdq.setText(eva_dict_parser["Support Delivery Queue"])
        self.lineEdit_evaavailablity.setText(eva_dict_parser["Hours of Availability"])
        self.lineEdit_evaEntitlementStatus.setText(eva_dict_parser["EntitlementStatus"])
        self.lineEdit_evaEntitlementType.setText(eva_dict_parser["Entitlement Type"])
        self.lineEdit_evaSLA.setText(eva_dict_parser["SLA"])
        self.lineEdit_evaSN.setText(eva_dict_parser["Serial Number"])
        self.lineEdit_evaProductNumner.setText(eva_dict_parser["Product Number"])
        self.lineEdit_evaWWN.setText(eva_dict_parser["WWN"])
        self.lineEdit_evaLocation.setText(eva_dict_parser["Location"])
        self.lineEdit_evaFailingHostName.setText(eva_dict_parser["FailingHostName"])

        self.lineEdit_evaType.setText(eva_dict_parser["Controller Type"])
        self.lineEdit_evaEventCode.setText(eva_dict_parser["Event Code"])
        self.lineEdit_evaPartNumber.setText(eva_dict_parser["Part Number"])
        self.lineEdit_evaPartDescription.setText(eva_dict_parser["Part Description"])
        self.lineEdit_evaEnvironment.setText(eva_dict_parser['Environment'])
        self.lineEdit_evaIssue.setText(eva_dict_parser['Issue'])

    @pyqtSignature("")
    def on_eva_rstbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.textEdit_eva.clear()
        self.lineEdit_evaname.clear()
        self.lineEdit_evacompany.clear()
        self.lineEdit_evaaddress.clear()
        self.lineEdit_evaemail.clear()
        self.lineEdit_evacountry.clear()
        self.lineEdit_evaphone.clear()
        self.lineEdit_evasdq.clear()
        self.lineEdit_evaavailablity.clear()
        self.lineEdit_evaEntitlementStatus.clear()
        self.lineEdit_evaEntitlementType.clear()
        self.lineEdit_evaSLA.clear()
        self.lineEdit_evaSN.clear()
        self.lineEdit_evaProductNumner.clear()
        self.lineEdit_evaWWN.clear()
        self.lineEdit_evaLocation.clear()
        self.lineEdit_evaFailingHostName.clear()
        self.lineEdit_evaPartNumber.clear()
        self.lineEdit_evaType.clear()
        self.lineEdit_evaPartDescription.clear()
        self.lineEdit_evaEnvironment.clear()
        self.lineEdit_evaIssue.clear()


    @pyqtSignature("")
    def on_xprstbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.xptextEdit.clear()
        self.lineEdit_xpname.clear()
        self.lineEdit_xpcompany.clear()
        self.lineEdit_xpaddress.clear()
        self.lineEdit_xpcountry.clear()
        self.lineEdit_xpphone.clear()
        self.lineEdit_xpemail.clear()
        self.lineEdit_xpavailability.clear()
        self.lineEdit_xptitle.clear()
        self.lineEdit_xpsdq.clear()
        self.lineEdit_xplocation.clear()
        self.lineEdit_xppart.clear()
        self.lineEdit_xpsn.clear()
        self.lineEdit_xptype.clear()
        self.lineEdit_xpcanister.clear()
        self.lineEdit_xpentmntstat.clear()
        self.lineEdit_xpentmnttyp.clear()
        self.lineEdit_xpsla.clear()
        self.lineEdit_xpEnvironment.clear()
        self.lineEdit_xpIssue.clear()
        #raise NotImplementedError
    
    @pyqtSignature("")
    def on_xpsbmtbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        xp_dict_parser = xp_parser.xp_log_parser(self.xptextEdit.toPlainText())
        self.lineEdit_xpname.setText(xp_dict_parser['Name'])
        self.lineEdit_xpcompany.setText(xp_dict_parser['Company'])
        self.lineEdit_xpaddress.setText(xp_dict_parser['Address'])
        self.lineEdit_xpcountry.setText(xp_dict_parser['Country'])
        self.lineEdit_xpphone.setText(xp_dict_parser['Phone'])
        self.lineEdit_xpemail.setText(xp_dict_parser['Email'])
        self.lineEdit_xpavailability.setText(xp_dict_parser['Hours of Availability'])
        self.lineEdit_xptitle.setText(xp_dict_parser['Workflow Case Title'])
        self.lineEdit_xpsdq.setText(xp_dict_parser['Support Delivery Queue'])
        self.lineEdit_xplocation.setText(xp_dict_parser['FailingFRULocation'])
        self.lineEdit_xppart.setText(xp_dict_parser['Part Number by BLI'])
        self.lineEdit_xpsn.setText(xp_dict_parser['Serial Number'])
        self.lineEdit_xptype.setText(xp_dict_parser['Model'])
        self.lineEdit_xpcanister.setText(xp_dict_parser['error_parts'])
        self.lineEdit_xpentmntstat.setText(xp_dict_parser['EntitlementStatus'])
        self.lineEdit_xpentmnttyp.setText(xp_dict_parser['Entitlement Type'])
        self.lineEdit_xpsla.setText(xp_dict_parser['SLA'])
        self.lineEdit_xpEnvironment.setText(xp_dict_parser['Environment'])
        self.lineEdit_xpIssue.setText(xp_dict_parser['Issue'])
    
    @pyqtSignature("")
    def on_pro_sbmtbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pro_dict_parser = prolaint_parser.proliant_log_parser(self.textEdit_pro.toPlainText())
        self.lineEdit_proName.setText(pro_dict_parser['Name'])
        self.lineEdit_proCompany.setText(pro_dict_parser['Company'])
        self.lineEdit_proAddress.setText(pro_dict_parser['Address'])
        self.lineEdit_proEmail.setText(pro_dict_parser['Email'])
        self.lineEdit_proCountry.setText(pro_dict_parser['Country'])
        self.lineEdit_proPhone.setText(pro_dict_parser['Phone'])
        self.lineEdit_proAvailablity.setText(pro_dict_parser['Hours of Availability'])
        self.lineEdit_proSDQ.setText(pro_dict_parser['Support Delivery Queue'])
        self.lineEdit_proEntitlementStatus.setText(pro_dict_parser['EntitlementStatus'])
        self.lineEdit_proSLA.setText(pro_dict_parser['SLA'])
        self.lineEdit_proEntitlementType.setText(pro_dict_parser['Entitlement Type'])
        self.lineEdit_proSerialNumber.setText(pro_dict_parser['Serial Number'])
        self.lineEdit_proProductNumber.setText(pro_dict_parser['Product Number'])
        self.lineEdit_proServerModel.setText(pro_dict_parser['Server Model'])
        self.lineEdit_proServerName.setText(pro_dict_parser['Server Name'])
        self.lineEdit_proLocation.setText(pro_dict_parser['Location'])
        self.lineEdit_proControllerModel.setText(pro_dict_parser['Controller'])
        self.lineEdit_proOSVersion.setText(pro_dict_parser['OS Version'])
        self.lineEdit_proPartNumber.setText(pro_dict_parser['Part Number'])
        self.lineEdit_proPartDesc.setText(pro_dict_parser['Part Description'])
        self.lineEdit_proEnvironment.setText(pro_dict_parser['Environment'])
        self.lineEdit_proIssue.setText(pro_dict_parser['Issue'])


    @pyqtSignature("")
    def on_pro_rstbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.textEdit_pro.clear()
        self.lineEdit_proName.clear()
        self.lineEdit_proCompany.clear()
        self.lineEdit_proAddress.clear()
        self.lineEdit_proEmail.clear()
        self.lineEdit_proCountry.clear()
        self.lineEdit_proPhone.clear()
        self.lineEdit_proAvailablity.clear()
        self.lineEdit_proSDQ.clear()
        self.lineEdit_proEntitlementStatus.clear()
        self.lineEdit_proSLA.clear()
        self.lineEdit_proEntitlementType.clear()
        self.lineEdit_proSerialNumber.clear()
        self.lineEdit_proProductNumber.clear()
        self.lineEdit_proServerModel.clear()
        self.lineEdit_proServerName.clear()
        self.lineEdit_proLocation.clear()
        self.lineEdit_proControllerModel.clear()
        self.lineEdit_proOSVersion.clear()
        self.lineEdit_proPartNumber.clear()
        self.lineEdit_proPartDesc.clear()
        self.lineEdit_proEnvironment.clear()
        self.lineEdit_proIssue.clear()
        
if __name__ == "__main__":    
    
    app = PyQt4.QtGui.QApplication(sys.argv)     
    dlg = Dialog()     
    dlg.show()
    sys.exit(app.exec_())  
