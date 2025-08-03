OV.RegisterHeaderPlugin ({
    registerButtons : (pluginInterface) => {
        pluginInterface.createHeaderButton ('info', OV.UI.Loc ('User manual'), 'info/index.html');
        pluginInterface.createHeaderButton ('donate', OV.UI.Loc ('Support the development'), 'https://github.com/sponsors/kovacsv');
        pluginInterface.createHeaderButton ('feedback', OV.UI.Loc ('Send feedback'), 'https://3dviewer.atlassian.net/servicedesk/customer/portal/1');
        pluginInterface.createHeaderButton ('twitter', OV.UI.Loc ('Follow on Twitter'), 'https://twitter.com/Online3DViewer');
        pluginInterface.createHeaderButton ('github', OV.UI.Loc ('View on GitHub'), 'https://github.com/kovacsv/Online3DViewer');
    }
});
