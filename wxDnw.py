#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
wxDnw

dnw tools implement use wxPython

author: 
    caicry@gmail.com
date: 
    2012-03-24
blog:
    hi.baidu.com/caicry/
github:
    github.com/caicry

3q for these webs:
    safe thread operator in wxPython:
        http://www.blog.pythonlibrary.org/2010/05/22/wxpython-and-threads/
last modified:
"""
import wx
import sys
import os
import dnw
import threading
import ConfigParser
from wxDnw_xrc import xrcmyFrame
from dnw import DNW

#!dnw:begin-block: Dowload Thread
EVT_DNW_DOWLOAD_THREAD_ID = wx.NewId() #@UndefinedVariable
def EVT_DNW_DOWNLOAD_THREAD(win, func):
    win.Connect(-1, -1, EVT_DNW_DOWLOAD_THREAD_ID, func)

class DnwDownloadThreadEvt(wx.PyEvent): #@UndefinedVariable
    def __init__(self, data):
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_DNW_DOWLOAD_THREAD_ID)
        self.data = data

class DnwDownloadThread(threading.Thread):
    def __init__(self, dialog):
        threading.Thread.__init__(self)
        self.dialog = dialog

    def OnProgress(self, progress):
        wx.PostEvent(self.dialog, DnwDownloadThreadEvt(progress))

    def run(self):
        try:
            dnw_handle = dnw.DNW(progress_func=self.OnProgress)
            if dnw_handle:
                self.dialog.DBG("Start Download...")
                dnw_handle.DownloadFile(self.dialog.GetDownloadFilePath())
                self.dialog.DBG("Download Finish")
            else:
                self.dialog.DBG("Can't Download ...")
        except dnw.DNWError, e:
            self.dialog.DBG(e.value)
        finally:
            self.dialog.optThread = None
            
class DnwUploadThread(threading.Thread):
    def __init__(self, dialog):
        threading.Thread.__init__(self)
        self.dialog = dialog

    def OnProgress(self, progress):
        wx.PostEvent(self.dialog, DnwDownloadThreadEvt(progress))

    def run(self):
        try:
            dnw_handle = dnw.DNW(progress_func=self.OnProgress)
            if dnw_handle:
                self.dialog.DBG("Start Upload...")
                dnw_handle.UploadFile(self.dialog.GetUploadFilePath())
                self.dialog.DBG("Upload Finish")
            else:
                self.dialog.DBG("Can't Upload ...")
        except dnw.DNWError, e:
            self.dialog.DBG(e.value)
        finally:
            self.dialog.optThread = None
#!dnw:end-block: Dowload Thread


class MainFrame(xrcmyFrame):
    """
    Main Frame
    """
    def __init__(self):
        xrcmyFrame.__init__(self, None) 
        self.progress.SetRange(100)
        self.Show()
        self.optThread = None
        self.openRecentFileList = []
        EVT_DNW_DOWNLOAD_THREAD(self, self.OnProgress)
        self.InitOpenRecentFiles()
        
    def DBG(self, txt):
        self.txtLog.AppendText(txt + '\n')
        #wx.MessageBox(txt)
        
    def DBG_CLEAR(self):
        self.txtLog.Clear()
    
    def GetConfigFilePath(self):
        return os.path.expanduser('~/.wxDnw.conf')
        
    def InitOpenRecentFiles(self):
        path = self.GetConfigFilePath()
        if os.path.isfile(path):
            cf = ConfigParser.ConfigParser()
            cf.read(path)
            num = cf.getint('CONFIG', 'NUM')
            if (num>0):
                for i in range(0, num):
                    self.openRecentFileList.append(cf.get('CONFIG', 'PATH_%d' % i))
        self.UpdateOpenRecentMenu()
                    
       
    def SaveOpenRecentFiles(self): 
        path = self.GetConfigFilePath()
        if os.path.isfile(path):
            os.remove(path)
        
        cf = ConfigParser.ConfigParser()
        cf.add_section('CONFIG')
        cf.set('CONFIG', 'NUM', len(self.openRecentFileList))
        j=0
        
        self.openRecentFileList = list(set(self.openRecentFileList))
        for i in self.openRecentFileList:
            cf.set('CONFIG', 'PATH_%d' % j, i)
            j+=1
        cf.write(open(path, 'w'))
        self.UpdateOpenRecentMenu()
        pass

    def UpdateOpenRecentMenu(self):
        for i in self.menu_openRecent.GetMenuItems():
            self.menu_openRecent.RemoveItem(i)
            
        self.openRecentFileList = list(set(self.openRecentFileList))
        for i in self.openRecentFileList:
            item = self.menu_openRecent.Append(wx.NewId(), i)
            self.Bind(wx.EVT_MENU, self.OnOpenRecentMenuItem, item)
   
    def OnOpenRecentMenuItem(self, event): 
        menu = self.GetMenuBar()
        self.txtDownloadPath.SetValue(menu.FindItemById(event.GetId()).GetLabel())
        
        
    def OnProgress(self, event):
        totalen, l, speed, progress = event.data
        self.progress.SetValue(progress)
        self.StatusBar.SetStatusText("totalen:%d len:%d progress:%%%d speed:%.2fKB/S" % (totalen, l, progress, speed))
    
    def GetDownloadFilePath(self):
        return self.txtDownloadPath.GetValue()
    
    def GetUploadFilePath(self):
        return self.txtUploadPath.GetValue()
    
    def OnButton_btnDownloadBrowser(self, evt):
        path = wx.FileSelector("Choose File To Download")
        if path:
            self.txtDownloadPath.SetValue(path)
    
    def OnButton_btnUploadBrowser(self, evt):
        path = wx.FileSelector("Choose File To Store Upload", flags = wx.FD_SAVE)
        if path:
            self.txtUploadPath.SetValue(path)
    
    def OnMenu_item_download(self, evt):
        if self.optThread == None:
            self.openRecentFileList.insert(0, self.GetDownloadFilePath())
            self.SaveOpenRecentFiles()
            self.DBG_CLEAR()
            self.optThread = DnwDownloadThread(self)
            self.optThread.start()
        else:
            wx.MessageBox("Threading is running..")
        
    def OnMenu_item_open(self, evt):
        path = wx.FileSelector("Choose File To Download")
        if path:
            self.txtDownloadPath.SetValue(path)
    
    def OnMenu_item_upload(self, evt):
        if self.optThread == None:
            self.DBG_CLEAR()
            self.optThread = DnwUploadThread(self)
            self.optThread.start()
        else:
            wx.MessageBox("Threading is running..")
            
    def OnClose(self, evt):
        if self.optThread:
            wx.MessageBox("Waiting for thread end..")
        else:
            self.Destroy()
            
            
    def OnMenu_item_about(self, evt):
        
        description = """dnw tools for mini2440"""

        licence = """GPLV3"""

        info = wx.AboutDialogInfo()

        info.SetName('wxDnw')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2012 - 2013 CaiRuyi')
        info.SetWebSite('http://hi.baidu.com/caicry/')
        info.SetLicence(licence)
        info.AddDeveloper('caicry@mail.com')
        info.AddDocWriter('caicry@mail.com')
        info.AddArtist('caicry@mail.com')
        info.AddTranslator('caicry@mail.com')

        wx.AboutBox(info)
    
if __name__ == '__main__':
    app = wx.App()
    mainFrame = MainFrame()
    app.MainLoop()
