/*
###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
*/

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.QsanVDPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'QsanVD',
            autoExpandColumn: 'description',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'name'},
                {name: 'RG'},
                {name: 'RAID'},
                {name: 'description'},
                {name: 'diskType'},
                {name: 'stripesize'},
                {name: 'size'},
                {name: 'progress'},
                {name: 'state'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
            },{
                id: 'size',
                dataIndex: 'size',
                header: _t('Size'),
                width: 70
            },{
                id: 'RG',
                dataIndex: 'RG',
                header: _t('RAID group')
            },{
                id: 'RAID',
                dataIndex: 'RAID',
                header: _t('RAID type')
            },{
                id: 'state',
                dataIndex: 'state',
                header: _t('State'),
            },{
                id: 'progress',
                dataIndex: 'progress',
                header: _t('Progress'),
                width: 70
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 60
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                width: 120
            }]
        });
        ZC.QsanVDPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('QsanVDPanel', ZC.QsanVDPanel);
ZC.registerName('QsanVD', _t('Virtual Disk'), _t('Virtual Disks'));


/* QsanPD */
ZC.QsanPDPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'QsanPD',
            autoExpandColumn: 'serialNumber',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'name'},
                {name: 'location'},
                {name: 'diskType'},
                {name: 'size'},
                {name: 'manufacturer'},
                {name: 'serialNumber'},
                {name: 'state'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'location',
                dataIndex: 'location',
                header: _t('Location'),
                width: 60
            },{
                id: 'manufacturer',
                dataIndex: 'manufacturer',
                header: _t('Manufacturer'),
                width: 160
            },{
                id: 'serialNumber',
                dataIndex: 'serialNumber',
                header: _t('Serial #'),
                width: 160
            },{
                id: 'diskType',
                dataIndex: 'diskType',
                header: _t('Type'),
                width: 70
            },{
                id: 'size',
                dataIndex: 'size',
                header: _t('Size'),
                width: 70
            },{
                id: 'state',
                dataIndex: 'state',
                header: _t('State'),
                width: 60
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 60
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                width: 120
            }]
        });
        ZC.QsanPDPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('QsanPDPanel', ZC.QsanPDPanel);
ZC.registerName('QsanPD', _t('Physical Disk'), _t('Physical Disks'));

})();
