from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class QsanPDMib(SnmpPlugin):
    relname  = "QsanPDMap"
    modname  = "ZenPacks.CERIT_SC.Qsan.QsanPD"
    relname  = "harddisks"
    compname = "hw"
    
    snmpGetTableMaps = (
        GetTableMap(
            'QsanPDs',
            '.1.3.6.1.4.1.22274.1.2.1.1',
            {
                '.1':  'location',
                '.2':  'size',
                '.3':  'RG',
                '.4':  'state',
                '.5':  'health',
                '.6':  'usage',
                '.7':  'manufacturer',
                '.8':  'serialNumber',
                '.9':  'diskType',
                '.10': 'writeCache',
                '.11': 'standby',
                '.12': 'readAhead',
                '.13': 'CQ',
            }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        qsan_pds = tabledata.get('QsanPDs')
        if not qsan_pds:
            return

        rm = self.relMap()
        for oid,data in qsan_pds.items():
            try:
                om = self.objectMap(data)
                om.id = self.prepId('QsanPD_%s' % (om.location))
                om.snmpindex = oid.strip('.')

                om.writeCache = getattr(om,'writeCache','Disabled') == 'Enabled'
                om.standby    = getattr(om,'standby','Disabled') == 'Enabled'
                om.readAhead  = getattr(om,'readAhead','Disabled') == 'Enabled'
                om.CQ         = getattr(om,'CQ','Disabled') == 'Enabled'

                om.size       = int(getattr(om,'size',0)) * 1073741824

                # convert disk "health" into status ID
                status_id = om.health2id.get(getattr(om,'health','').upper())
                om.status = status_id if not status_id is None else 9
            except:
                pass
            rm.append(om)

        return rm
