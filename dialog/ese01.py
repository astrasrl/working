#!/bin/env python
# -*- coding: utf-8 -*-

import wx
import awc.controls.windows as aw
import esempio_wdr as wdr

class MainApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        dlg = ese01Dialog( None, -1, title='TITOLO DELLE FINESTRA',
                           pos=wx.Point(300,400))
        dlg.Show(True)
        return True

class ese01Dialog(aw.Dialog):
    def __init__(self, *args, **kwargs):
        if not kwargs.has_key('title') and len(args) < 3:
            kwargs['title'] = 'titolo finestra'
        aw.Dialog.__init__(self, *args, **kwargs)
        self.AddSizedPanel(ese01Panel(self, -1))  
        #self.CenterOnScreen()  
    
    
class ese01Panel(aw.Panel):
    def __init__(self, *args, **kwargs):
        aw.Panel.__init__(self, *args, **kwargs)
        wdr.ese01Func(self)
        
    
            

if __name__ == '__main__':
    app = MainApp(False)
    app.MainLoop()