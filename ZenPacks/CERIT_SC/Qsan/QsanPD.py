from Products.ZenModel.HardDisk import *
from ZenPacks.community.deviceAdvDetail.HWStatus import *

class QsanPD(HardDisk,HWStatus):
    """Qsan Physical Disk"""
    portal_type = meta_type = 'QsanPD'

    location     = ''    #e.g.: e0d0
    size         = 0     #e.g.: 1234
    RG           = ''    #e.g.: RAID50
    state        = ''    #e.g.: Online
    health       = ''    #e.g.: Good
    usage        = ''    #e.g.: RD
    manufacturer = ''    #e.g.: SEAGATE
    serialNumber = ''    #e.g.: 6SK0VYF1000000000001
    diskType     = ''    #e.g.: SAS
    writeCache   = 0     #e.g.: Disabled
    standby      = 0     #e.g.: Disabled
    readAhead    = 0     #e.g.: Enabled
    CQ           = 0     #e.g.: Enabled
    status       = 0

    health2id = {'': 0,'GOOD':1,'FAILED':2,'ERROR ALERT':3,'READ ERRORS':4}
 
    statusmap = { # healthmap!
        0: (DOT_GREY,  SEV_WARNING, 'Unknown'),
        1: (DOT_GREEN, SEV_CLEAN,   'Good'),
        2: (DOT_RED,   SEV_CRITICAL,'Failed'),
        3: (DOT_ORANGE,SEV_ERROR,   'Error Alert'),
        4: (DOT_ORANGE,SEV_ERROR,   'Read Errors'),
        9: (DOT_ORANGE,SEV_ERROR,   '*UNHANDLED*'),
    }

    _properties = HardDisk._properties + (
        {'id':'location',     'type':'string',    'mode':'w'},
        {'id':'size',         'type':'int',       'mode':'w'},
        {'id':'RG',           'type':'string',    'mode':'w'},
        {'id':'status',       'type':'int',       'mode':'w'},
        {'id':'state',        'type':'string',    'mode':'w'},
        {'id':'health',       'type':'string',    'mode':'w'},
        {'id':'usage',        'type':'string',    'mode':'w'},
        {'id':'manufacturer', 'type':'string',    'mode':'w'},
        {'id':'serialNumber', 'type':'string',    'mode':'w'},
        {'id':'diskType',     'type':'string',    'mode':'w'},
        {'id':'writeCache',   'type':'int',       'mode':'w'},
        {'id':'standby',      'type':'int',       'mode':'w'},
        {'id':'readAhead',    'type':'int',       'mode':'w'},
        {'id':'CQ',           'type':'int',       'mode':'w'}
    )

    # Screen action bindings (and tab definitions)
    factory_type_information = ({   
        'id'             : 'HardDisk',
        'meta_type'      : 'HardDisk',
        'description'    : 'Qsan Physical Disks',
        'icon'           : 'HardDisk_icon.gif',
        'actions'        : ({
            'id'            : 'status',
            'name'          : 'Status',
            'action'        : 'viewQsanPD',
            'permissions'   : (ZEN_VIEW, ),
        },{
            'id'            : 'perfConf',
            'name'          : 'Template',
            'action'        : 'objTemplates',
            'permissions'   : (ZEN_CHANGE_DEVICE, ),
        },),
    },)


InitializeClass(QsanPD)
