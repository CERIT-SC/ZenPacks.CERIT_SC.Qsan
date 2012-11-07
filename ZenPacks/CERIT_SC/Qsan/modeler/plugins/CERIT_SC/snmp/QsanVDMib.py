from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class QsanVDMib(SnmpPlugin):
    relname  = "QsanVDMap"
    modname  = "ZenPacks.CERIT_SC.Qsan.QsanVD"
    relname  = "logicaldisks"
    compname = "hw"
    
    snmpGetTableMaps = (
        GetTableMap(
            'QsanVDs',
            '.1.3.6.1.4.1.22274.1.2.3.1',
            {
                '.1':  'description',
                '.2':  'size',
                '.3':  'write',
                '.4':  'priority',
                '.5':  'bgRate',
                '.6':  'state',
                '.7':  'health',
                '.8':  'progress',
                '.9':  'RAID',
                '.10': 'LUNs',
                '.11': 'snapshotSpace',
                '.12': 'snapshots',
                '.13': 'RG',
            }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        qsan_vds = tabledata.get('QsanVDs')
        if not qsan_vds:
            return

        rm = self.relMap()
        for oid,data in qsan_vds.items():
            try:
                om = self.objectMap(data)
                om.id = self.prepId('QsanVD_%s' % (om.description))
                om.snmpindex = oid.strip('.')
                om.size = int(getattr(om,'size',0)) * 1073741824

                # convert disk "health" into status ID
                status_id = om.health2id.get(getattr(om,'health','').upper())
                om.status = status_id if not status_id is None else 9
            except:
                pass
            rm.append(om)

        return rm
