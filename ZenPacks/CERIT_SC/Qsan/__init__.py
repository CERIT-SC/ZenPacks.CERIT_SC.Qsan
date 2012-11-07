
import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Products.ZenModel.DeviceClass import manage_addDeviceClass
from Products.ZenModel.ZenPack import ZenPackBase

class ZenPack(ZenPackBase):
    def install(self, app):
        qsan = app.dmd.Devices.createOrganizer('/Storage/Qsan')
        qsan.setZenProperty(
            'zCollectorPlugins',[
                'CERIT_SC.snmp.QsanDeviceMapMib',
                'CERIT_SC.snmp.QsanPDMib',
                'CERIT_SC.snmp.QsanVDMib'])

        # SNMP requests/modelling can take veeeeery long time
        qsan.setZenProperty('zSnmpTimeout','60')
        qsan.setZenProperty('zCommandCommandTimeout','120') #TODO: snmptimeout*tries
        qsan.setZenProperty('zCollectorClientTimeout','3600')

        # MIB organizers /Storage
        if not hasattr(app.zport.dmd.Mibs, 'Storage'):
            manage_addDeviceClass(app.zport.dmd.Mibs, 'Storage')

        ZenPackBase.install(self, app)

#     def upgrade(self, app):
#         ZenPackBase.upgrade(self, app)

    def remove(self, app, leaveObjects=False):
        # Delete only suborganizer /Storage/Qsan
        if hasattr(app.zport.dmd.Devices, 'Storage') and \
            hasattr(app.zport.dmd.Devices.Storage, 'Qsan'):
                app.zport.dmd.Devices.manage_deleteOrganizer('/Storage/Qsan')

        ZenPackBase.remove(self, app, leaveObjects)
