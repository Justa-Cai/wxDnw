# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcmyFrame(wx.Frame):
#!XRCED:begin-block:xrcmyFrame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcmyFrame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "myFrame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.progress = xrc.XRCCTRL(self, "progress")
        self.txtDownloadPath = xrc.XRCCTRL(self, "txtDownloadPath")
        self.btnDownloadBrowser = xrc.XRCCTRL(self, "btnDownloadBrowser")
        self.txtUploadPath = xrc.XRCCTRL(self, "txtUploadPath")
        self.btnUploadBrowser = xrc.XRCCTRL(self, "btnUploadBrowser")
        self.txtLog = xrc.XRCCTRL(self, "txtLog")
        self.item_open = self.GetMenuBar().FindItemById(xrc.XRCID("item_open"))
        idx = self.GetMenuBar().FindMenu("OpenRecent")
        if idx != wx.NOT_FOUND:
            self.menu_openRecent = self.GetMenuBar().GetMenu(idx)
        else:
            self.menu_openRecent = self.GetMenuBar().FindItemById(xrc.XRCID("menu_openRecent")).GetSubMenu()
        self.item_download = self.GetMenuBar().FindItemById(xrc.XRCID("item_download"))
        self.item_upload = self.GetMenuBar().FindItemById(xrc.XRCID("item_upload"))
        self.item_about = self.GetMenuBar().FindItemById(xrc.XRCID("item_about"))
        self.statusbar = xrc.XRCCTRL(self, "statusbar")

        self.Bind(wx.EVT_BUTTON, self.OnButton_btnDownloadBrowser, self.btnDownloadBrowser)
        self.Bind(wx.EVT_BUTTON, self.OnButton_btnUploadBrowser, self.btnUploadBrowser)
        self.Bind(wx.EVT_MENU, self.OnMenu_item_open, self.item_open)
        self.Bind(wx.EVT_MENU, self.OnMenu_item_download, self.item_download)
        self.Bind(wx.EVT_MENU, self.OnMenu_item_upload, self.item_upload)
        self.Bind(wx.EVT_MENU, self.OnMenu_item_about, self.item_about)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

#!XRCED:begin-block:xrcmyFrame.OnButton_btnDownloadBrowser
    def OnButton_btnDownloadBrowser(self, evt):
        # Replace with event handler code
        print "OnButton_btnDownloadBrowser()"
#!XRCED:end-block:xrcmyFrame.OnButton_btnDownloadBrowser        

#!XRCED:begin-block:xrcmyFrame.OnButton_btnUploadBrowser
    def OnButton_btnUploadBrowser(self, evt):
        # Replace with event handler code
        print "OnButton_btnUploadBrowser()"
#!XRCED:end-block:xrcmyFrame.OnButton_btnUploadBrowser        

#!XRCED:begin-block:xrcmyFrame.OnMenu_item_open
    def OnMenu_item_open(self, evt):
        # Replace with event handler code
        print "OnMenu_item_open()"
#!XRCED:end-block:xrcmyFrame.OnMenu_item_open        

#!XRCED:begin-block:xrcmyFrame.OnMenu_item_download
    def OnMenu_item_download(self, evt):
        # Replace with event handler code
        print "OnMenu_item_download()"
#!XRCED:end-block:xrcmyFrame.OnMenu_item_download        

#!XRCED:begin-block:xrcmyFrame.OnMenu_item_upload
    def OnMenu_item_upload(self, evt):
        # Replace with event handler code
        print "OnMenu_item_upload()"
#!XRCED:end-block:xrcmyFrame.OnMenu_item_upload        

#!XRCED:begin-block:xrcmyFrame.OnMenu_item_about
    def OnMenu_item_about(self, evt):
        # Replace with event handler code
        print "OnMenu_item_about()"
#!XRCED:end-block:xrcmyFrame.OnMenu_item_about        

#!XRCED:begin-block:xrcmyFrame.OnClose
    def OnClose(self, evt):
        # Replace with event handler code
        print "OnClose()"
#!XRCED:end-block:xrcmyFrame.OnClose        




# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    wxDnw_xrc = '''\
<?xml version="1.0" ?><resource>
  <object class="wxFrame" name="myFrame">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxStaticText">
              <size>100,-1</size>
              <label>Progress:</label>
            </object>
          </object>
          <object class="sizeritem">
            <object class="wxGauge" name="progress">
              <XRCED>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <option>1</option>
            <flag>wxALL|wxEXPAND|wxALIGN_RIGHT</flag>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <option>0</option>
        <flag>wxALL|wxEXPAND</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxStaticText">
              <size>100,-1</size>
              <label>Download:</label>
              <wrap>1</wrap>
            </object>
            <option>0</option>
            <flag>wxALL|wxEXPAND</flag>
          </object>
          <object class="sizeritem">
            <object class="wxTextCtrl" name="txtDownloadPath">
              <XRCED>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <option>1</option>
            <flag>wxALL|wxEXPAND</flag>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="btnDownloadBrowser">
              <label>...</label>
              <XRCED>
                <events>EVT_BUTTON</events>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <option>0</option>
            <flag>wxRIGHT|wxEXPAND</flag>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <option>0</option>
        <flag>wxALL|wxEXPAND</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="sizeritem">
            <object class="wxStaticText">
              <size>100,-1</size>
              <label>Upload:</label>
              <wrap>1</wrap>
            </object>
            <option>0</option>
            <flag>wxALL|wxEXPAND</flag>
          </object>
          <object class="sizeritem">
            <object class="wxTextCtrl" name="txtUploadPath">
              <XRCED>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <option>1</option>
            <flag>wxALL|wxEXPAND</flag>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="btnUploadBrowser">
              <label>...</label>
              <XRCED>
                <events>EVT_BUTTON</events>
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <option>0</option>
            <flag>wxRIGHT|wxEXPAND</flag>
          </object>
          <orient>wxHORIZONTAL</orient>
        </object>
        <option>0</option>
        <flag>wxALL|wxEXPAND</flag>
        <border>5</border>
      </object>
      <object class="sizeritem">
        <object class="wxTextCtrl" name="txtLog">
          <size>600,400</size>
          <style>wxTE_AUTO_SCROLL|wxTE_MULTILINE</style>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <option>1</option>
        <flag>wxALL|wxEXPAND</flag>
        <border>5</border>
      </object>
    </object>
    <object class="wxMenuBar">
      <XRCED>
        <events>EVT_MENU</events>
      </XRCED>
      <object class="wxMenu">
        <label>File</label>
        <object class="wxMenuItem" name="item_open">
          <label>Open</label>
          <bitmap stock_id="wxART_FILE_OPEN"/>
          <accel>Ctrl+O</accel>
          <XRCED>
            <events>EVT_MENU</events>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <object class="wxMenu" name="menu_openRecent">
          <label>OpenRecent</label>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <object class="separator"/>
        <object class="wxMenuItem" name="item_download">
          <label>Download</label>
          <bitmap stock_id="wxART_FILE_OPEN"/>
          <accel>Ctrl+D</accel>
          <help>Download To Device</help>
          <XRCED>
            <events>EVT_MENU</events>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <object class="wxMenuItem" name="item_upload">
          <label>Upload</label>
          <bitmap stock_id="wxART_FILE_OPEN"/>
          <accel>Ctrl+U</accel>
          <help>Upload To Device</help>
          <XRCED>
            <events>EVT_MENU</events>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
      </object>
      <object class="wxMenu">
        <label>Help</label>
        <XRCED>
          <events>EVT_MENU</events>
          <assign_var>1</assign_var>
        </XRCED>
        <object class="wxMenuItem" name="item_about">
          <label>About</label>
          <XRCED>
            <events>EVT_MENU</events>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
      </object>
    </object>
    <object class="wxToolBar">
      <object class="tool" name="toolbar_download"/>
      <object class="tool" name="toolbar_upload"/>
    </object>
    <object class="wxStatusBar" name="statusbar">
      <fields>1</fields>
      <widths>100</widths>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <size>1024,768</size>
    <title>wxDnw</title>
    <centered>1</centered>
    <focused>1</focused>
    <XRCED>
      <events>EVT_CLOSE</events>
    </XRCED>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/wxDnw/wxDnw_xrc', wxDnw_xrc)
    __res.Load('memory:XRC/wxDnw/wxDnw_xrc')


# ----------------------- Gettext strings ---------------------

def __gettext_strings():
    # This is a dummy function that lists all the strings that are used in
    # the XRC file in the _("a string") format to be recognized by GNU
    # gettext utilities (specificaly the xgettext utility) and the
    # mki18n.py script.  For more information see:
    # http://wiki.wxpython.org/index.cgi/Internationalization 
    
    def _(str): pass
    
    _("Progress:")
    _("Download:")
    _("...")
    _("Upload:")
    _("...")
    _("File")
    _("Open")
    _("OpenRecent")
    _("Download")
    _("Download To Device")
    _("Upload")
    _("Upload To Device")
    _("Help")
    _("About")
    _("wxDnw")

