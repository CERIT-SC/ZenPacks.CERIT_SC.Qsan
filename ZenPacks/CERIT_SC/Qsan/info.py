from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.ZenUtils.Utils import convToUnits

from ZenPacks.CERIT_SC.Qsan.interfaces import *

class QsanVDInfo(ComponentInfo):
    implements(IQsanVDInfo)

    description   = ProxyProperty("description")
    state         = ProxyProperty("state")
    health        = ProxyProperty("health")
    progress      = ProxyProperty("progress")
    write         = ProxyProperty("write")
    priority      = ProxyProperty("priority")
    bgRate        = ProxyProperty("bgRate")
    RG            = ProxyProperty("RG")
    RAID          = ProxyProperty("RAID")
    LUNs          = ProxyProperty("LUNs")
    snapshotSpace = ProxyProperty("snapshotSpace")
    snapshots     = ProxyProperty("snapshots")

    @property
    def stripesize(self):
        return convToUnits(self._object.stripesize)

    @property
    def size(self):
        return convToUnits(self._object.size)

    @property
    def status(self):
        if not hasattr(self._object, 'statusString'): return 'Unknown'
        else: return self._object.statusString()


class QsanPDInfo(ComponentInfo):
    implements(IQsanPDInfo)

    state         = ProxyProperty("state")
    health        = ProxyProperty("health")
    location      = ProxyProperty("location")
    RG            = ProxyProperty("RG")
    usage         = ProxyProperty("usage")
    manufacturer  = ProxyProperty("manufacturer")
    serialNumber  = ProxyProperty("serialNumber")
    diskType      = ProxyProperty("diskType")
    writeCache    = ProxyProperty("writeCache")
    standby       = ProxyProperty("standby")
    readAhead     = ProxyProperty("readAhead")
    CQ            = ProxyProperty("CQ")

    @property
    def size(self):
        return convToUnits(self._object.size)

    @property
    def status(self):
        if not hasattr(self._object, 'statusString'): return 'Unknown'
        else: return self._object.statusString()

