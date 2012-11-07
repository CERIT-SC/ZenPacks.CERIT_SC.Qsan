from Products.Zuul.form import schema
from Products.Zuul.infos.component import IComponentInfo

class IQsanVDInfo(IComponentInfo):
    health        = schema.Text(title=u"Modeled health",  readonly=True, group='Overview')
    state         = schema.Text(title=u"Modeled state",   readonly=True, group='Overview')
    progress      = schema.Text(title=u"Progress",        readonly=True, group='Overview')

    size          = schema.Text(title=u"Size",            readonly=True, group='Details')
    write         = schema.Text(title=u"Write",           readonly=True, group='Details')
    priority      = schema.Text(title=u"Priority",        readonly=True, group='Details')
    bgRate        = schema.Text(title=u"Background rate", readonly=True, group='Details')
    RG            = schema.Text(title=u"RAID group",      readonly=True, group='Details')
    RAID          = schema.Text(title=u"RAID type",       readonly=True, group='Details')
    LUNs          = schema.Text(title=u"# LUNs",          readonly=True, group='Details')
    snapshotSpace = schema.Text(title=u"Snapshot space",  readonly=True, group='Details')
    snapshots     = schema.Text(title=u"# snapshots",     readonly=True, group='Details')

class IQsanPDInfo(IComponentInfo):
    health        = schema.Text(title=u"Modeled health",  readonly=True, group='Overview')
    state         = schema.Text(title=u"Modeled state",   readonly=True, group='Overview')

    size          = schema.Text(title=u"Size",            readonly=True, group='Details')
    RG            = schema.Text(title=u"RAID group",      readonly=True, group='Details')
    usage         = schema.Text(title=u"Usage",           readonly=True, group='Details')
    manufacturer  = schema.Text(title=u"Manufacturer",    readonly=True, group='Details')
    serialNumber  = schema.Text(title=u"Serial #",        readonly=True, group='Details')
    diskType      = schema.Text(title=u"Disk type",       readonly=True, group='Details')
    writeCache    = schema.Bool(title=u"Write cache",     readonly=True, group='Details')
    standby       = schema.Bool(title=u"Standby",         readonly=True, group='Details')
    readAhead     = schema.Bool(title=u"Read ahead",      readonly=True, group='Details')
    CQ            = schema.Bool(title=u"Command queuing", readonly=True, group='Details')
