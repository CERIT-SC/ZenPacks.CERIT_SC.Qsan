from ZenPacks.community.deviceAdvDetail.LogicalDisk import *
from ZenPacks.community.deviceAdvDetail.HWStatus import *

class QsanVD(LogicalDisk,HWStatus):
    """Qsan Virtual Disk"""
    portal_type = meta_type = 'QsanVD'

    description     = ''    #e.g.: My disk
    size            = 0     #e.g.: 1234
    write           = ''    #e.g.: WB
    priority        = ''    #e.g.: MD
    bgRate          = 0     #e.g.: 0 
    state           = ''    #e.g.: Online
    health          = ''    #e.g.: Optimal
    progress        = ''    #e.g.: ??
    RAID            = ''    #e.g.: RAID 50
    LUNs            = 0     #e.g.: 1
    snapshotSpace   = ''    #e.g.: 0/0
    snapshots       = 0     #e.g.: 0
    RG              = ''    #e.g.: RAID50
    status          = 0

    health2id = {'': 0,'OPTIMAL':1,'DEGRADED':2,'FAILED':3,'PARTIALLY OPTIMAL':4}

    statusmap = { #healthmap!
        0: (DOT_GREY,  SEV_WARNING, 'Unknown'),
        1: (DOT_GREEN, SEV_CLEAN,   'Optimal'),
        2: (DOT_ORANGE,SEV_ERROR,   'Degraded'),
        3: (DOT_RED,   SEV_CRITICAL,'Failed'),
        4: (DOT_ORANGE,SEV_ERROR,   'Partially optimal'),
        9: (DOT_ORANGE,SEV_ERROR,   '*UNHANDLED*'),
    }

    _properties = LogicalDisk._properties + (
        {'id':'description',    'type':'string',    'mode':'w'},
        {'id':'size',           'type':'int',       'mode':'w'},
        {'id':'write',          'type':'string',    'mode':'w'},
        {'id':'priority',       'type':'string',    'mode':'w'},
        {'id':'bgRate',         'type':'int',       'mode':'w'},
        {'id':'status',         'type':'int',       'mode':'w'},
        {'id':'state',          'type':'string',    'mode':'w'},
        {'id':'health',         'type':'string',    'mode':'w'},
        {'id':'progress',       'type':'string',    'mode':'w'},
        {'id':'RAID',           'type':'string',    'mode':'w'},
        {'id':'LUNs',           'type':'int',       'mode':'w'},
        {'id':'snapshotSpace',  'type':'string',    'mode':'w'},
        {'id':'snapshots',      'type':'int',       'mode':'w'},
        {'id':'RG',             'type':'string',    'mode':'w'}
    )

    # Screen action bindings (and tab definitions)
    factory_type_information = ({   
        'id'             : 'HardDisk',
        'meta_type'      : 'HardDisk',
        'description'    : 'Qsan Virtual Disks',
        'icon'           : 'HardDisk_icon.gif',
        'actions'        : ({
            'id'            : 'status',
            'name'          : 'Status',
            'action'        : 'viewQsanVD',
            'permissions'   : (ZEN_VIEW, ),
        },{
            'id'            : 'perfConf',
            'name'          : 'Template',
            'action'        : 'objTemplates',
            'permissions'   : (ZEN_CHANGE_DEVICE, ),
        },),
    },)


InitializeClass(QsanVD)
