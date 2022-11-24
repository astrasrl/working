#!/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Name:         exportsetup.py
# Author:       Marcello Montaldo ( marcello.montaldo@gmail.com)
# Created:      2013/07/03
# Copyright:    Astra S.r.l.
# ------------------------------------------------------------------------------

import wx               # https://docs.wxpython.org/index.html
import menu_wdr as wdr
import myanag

VERS='1.10.0'
import Env
import MySQLdb
import stormdb as adb


def Login():
    Env.Azienda.DB.servername = 'localhost'
    Env.Azienda.DB.username   = 'x4user'
    Env.Azienda.DB.password   = 'x4user'
    Env.Azienda.DB._dbType    = 'mysql'
    nomedb = 'x4_impero'
    conn = MySQLdb.connect(host=Env.Azienda.DB.servername,
                           user=Env.Azienda.DB.username,
                           passwd=Env.Azienda.DB.password,
                           db=nomedb,
                           use_unicode=True)
    conn.autocommit(True)
    Env.Azienda.DB.connection = conn
    db = adb.DB()
    db._dbCon = conn
    db.connected = True
    Env.Azienda.read_dati_azienda(db)




    
class MainApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame = MainFrame( None, -1, "Main App", [150,20], [500,340] )
        frame.Show(True)

        Login()
        
        dbAliquote = adb.DbTable(Env.Azienda.BaseTab.TABNAME_ALIQIVA, 'aliqiva')
        dbAliquote.Retrieve()
        for r in dbAliquote:
            print r.id, r.codice, r.descriz
        
        return True 
    
class MainFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE):
        def ci(x):
            return self.FindWindowById(x)                 
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.CreateMyMenuBar()
        self.CreateMyToolBar()
        self.CreateStatusBar(1)
        self.SetStatusText("vers.%s" % VERS)
        
        wx.EVT_MENU(self, wdr.ID_EXIT, self.OnCloseWindow)
        wx.EVT_MENU(self, wdr.ID_OPEN, self.OnOpen)
        wx.EVT_MENU(self, wdr.ID_TBOPEN, self.OnOpenTb)
        
    def CreateMyMenuBar(self):
        self.SetMenuBar( wdr.MyMenuBarFunc() )  
        
    def CreateMyToolBar(self):
        tb = self.CreateToolBar(wx.TB_HORIZONTAL|wx.NO_BORDER)
        wdr.MyToolBarFunc( tb )

    def LaunchFrame(self, frameclass, size=None, show=True, centered=False, dialog=False,  **kwargs):
        wx.BeginBusyCursor()
        frame = None
        err = None
        try:
            if True:#try:
                frame = frameclass(self, **kwargs)
                if size:
                    frame.SetSize(size)
                if centered:
                    frame.CenterOnScreen()
        finally:
            wx.EndBusyCursor()
        if err:
            awu.MsgDialog(self, message=err, style=wx.ICON_ERROR)
        else:
            if show and frame is not None:
                s = frame.GetSize()
                frame.SetSize((s[0]+1, s[1]+1))
                frame.SetSize(s)
                if dialog:
                    frame.ShowModal()
                else:
                    frame.Show()
                frame.SetFocus()
        return frame

        
    def OnCloseWindow(self, event):
        self.Destroy()
                
    def OnOpen(self, evt):
        from anag.agenti import AgentiFrame
        self.LaunchFrame(AgentiFrame)        
        
    def OnOpenTb(self, evt):
        print 'open da toolbar'
        
    
        
if __name__ == '__main__':
    app = MainApp(False)
    app.MainLoop()
        