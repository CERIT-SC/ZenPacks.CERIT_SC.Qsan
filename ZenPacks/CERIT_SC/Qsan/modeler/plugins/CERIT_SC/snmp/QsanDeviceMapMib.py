from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.DataCollector.plugins.DataMaps import MultiArgs

class QsanDeviceMapMib(SnmpPlugin):
    maptype = "DeviceMap" 

    snmpGetMap = GetMap({ 
        '.1.3.6.1.2.1.1.1.0' : 'snmpDescr',
        '.1.3.6.1.2.1.1.2.0' : 'snmpOid',
        #'.1.3.6.1.2.1.1.3.0' : 'snmpUpTime',
        '.1.3.6.1.2.1.1.4.0' : 'snmpContact',
        '.1.3.6.1.2.1.1.5.0' : 'snmpSysName',
        '.1.3.6.1.2.1.1.6.0' : 'snmpLocation',
        '.1.3.6.1.4.1.22274.1.4.1.3' : 'setHWProductKey',
        '.1.3.6.1.4.1.22274.1.4.1.4' : 'setHWSerialNumber',
    })

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        om = self.objectMap(getdata)

        # e.g.: "S300Q-D316 2.1.2 (build 201109221700)" -> ["S300Q-D316","2.1.2 (build 201109221700)"]
        prod,ver=om.setHWProductKey.split(' ',1)
        if not prod is None:
            om.setHWProductKey = MultiArgs(prod,"Qsan")
        if not ver is None:
            om.setOSProductKey = MultiArgs(ver,"Qsan")

        return om
