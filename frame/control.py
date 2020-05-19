import wx
import classification.classification as cf


class mainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title=u"金融聚类分析器")
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetSize((200, 200))
        self.Center()

        # 容器
        mainBox = wx.BoxSizer(wx.VERTICAL)
        fgSizer1 = wx.FlexGridSizer(3, 1, 15, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # 文本
        font = wx.Font(15, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.m_staticText1 = wx.StaticText(self, -1, u'请选择需要的操作：', wx.DefaultPosition, wx.DefaultSize, style=wx.ALIGN_RIGHT)
        # self.my_staticText1.SetFont(font)

        # 按钮
        m_button1 = wx.Button(self, wx.ID_ANY, u"已存在数据库中", wx.DefaultPosition, wx.DefaultSize, 0)
        m_button2 = wx.Button(self, wx.ID_ANY, u"未存在数据库中", wx.DefaultPosition, wx.DefaultSize, 0)

        # 按钮事件
        m_button1.Bind(wx.EVT_BUTTON, self.OnButtonClick1)
        m_button2.Bind(wx.EVT_BUTTON, self.OnButtonClick2)

        # 将控件添加到容器中
        fgSizer1.Add(self.m_staticText1, 0, wx.TOP, 20)
        fgSizer1.Add(m_button1, 0, wx.ALIGN_CENTER)
        fgSizer1.Add(m_button2, 0, wx.ALIGN_CENTER)
        mainBox.Add(fgSizer1, 0, wx.ALIGN_CENTER)

        self.SetSizer(mainBox)
        self.Layout()

    def OnButtonClick1(self, evt):
        frame1 = chooseFrame1()
        frame1.Show(True)
        self.Show(False)

    def OnButtonClick2(self, evt):
        frame2 = chooseFrame2()
        frame2.Show(True)
        self.Show(False)


class chooseFrame1(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title=u"金融聚类分析器")
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetSize((650, 500))
        self.Center()

        # 容器
        mainBox = wx.BoxSizer(wx.VERTICAL)
        fgSizer1 = wx.FlexGridSizer(0, 2, 10, 20)
        fgSizer2 = wx.FlexGridSizer(10, 5, 10, 20)

        # 文本
        self.m_staticText1 = wx.StaticText(self, -1, u'请输入公司名称：')
        self.m_staticText2 = wx.StaticText(self, -1, u'变更次数：')
        self.m_staticText3 = wx.StaticText(self, -1, u'建立时间：')
        self.m_staticText4 = wx.StaticText(self, -1, u'注册资本：')
        self.m_staticText5 = wx.StaticText(self, -1, u'网店个数：')
        self.m_staticText6 = wx.StaticText(self, -1, u'分支机构数：')
        self.m_staticText7 = wx.StaticText(self, -1, u'股东信息：')
        self.m_staticText8 = wx.StaticText(self, -1, u'年报出资信息：')
        self.m_staticText9 = wx.StaticText(self, -1, u'对外担保：')
        self.m_staticText10 = wx.StaticText(self, -1, u'对外投资：')
        self.m_staticText11 = wx.StaticText(self, -1, u'中标次数：')
        self.m_staticText12 = wx.StaticText(self, -1, u'招聘记录：')
        self.m_staticText13 = wx.StaticText(self, -1, u'参保日期：')
        self.m_staticText14 = wx.StaticText(self, -1, u'社保信息：')
        self.m_staticText15 = wx.StaticText(self, -1, u'产品合格率：')
        self.m_staticText16 = wx.StaticText(self, -1, u'执行标的：')
        self.m_staticText17 = wx.StaticText(self, -1, u'经营异常次数：')
        self.m_staticText18 = wx.StaticText(self, -1, u'处罚次数：')
        self.m_staticText19 = wx.StaticText(self, -1, u'出质股权次数：')
        self.m_staticText20 = wx.StaticText(self, -1, u'欠税额：')
        self.m_staticText21 = wx.StaticText(self, -1, u'信用等级：')
        self.m_staticText22 = wx.StaticText(self, -1, u'失信黑名单次数：')
        self.m_staticText23 = wx.StaticText(self, -1, u'商标申请次数：')
        self.m_staticText24 = wx.StaticText(self, -1, u'软件著作权登记次数：')
        self.m_staticText25 = wx.StaticText(self, -1, u'专利申请次数：')
        self.m_staticText26 = wx.StaticText(self, -1, u'域名知识产权数：')

        # 输入框
        self.tc1 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC01')
        self.tc2 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC02', style=wx.TE_READONLY)
        self.tc3 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC03', style=wx.TE_READONLY)
        self.tc4 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC04', style=wx.TE_READONLY)
        self.tc5 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC05', style=wx.TE_READONLY)
        self.tc6 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC06', style=wx.TE_READONLY)
        self.tc7 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC07', style=wx.TE_READONLY)
        self.tc8 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC08', style=wx.TE_READONLY)
        self.tc9 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC09', style=wx.TE_READONLY)
        self.tc10 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC10', style=wx.TE_READONLY)
        self.tc11 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC11', style=wx.TE_READONLY)
        self.tc12 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC12', style=wx.TE_READONLY)
        self.tc13 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC13', style=wx.TE_READONLY)
        self.tc14 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC14', style=wx.TE_READONLY)
        self.tc15 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC15', style=wx.TE_READONLY)
        self.tc16 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC16', style=wx.TE_READONLY)
        self.tc17 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC17', style=wx.TE_READONLY)
        self.tc18 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC18', style=wx.TE_READONLY)
        self.tc19 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC19', style=wx.TE_READONLY)
        self.tc20 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC20', style=wx.TE_READONLY)
        self.tc21 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC21', style=wx.TE_READONLY)
        self.tc22 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC22', style=wx.TE_READONLY)
        self.tc23 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC23', style=wx.TE_READONLY)
        self.tc24 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC24', style=wx.TE_READONLY)
        self.tc25 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC25', style=wx.TE_READONLY)
        self.tc26 = wx.TextCtrl(self, -1, '', size=(100, -1), name='TC26', style=wx.TE_READONLY)

        # 按钮
        btn_search = wx.Button(self, -1, u'查询', pos=(255, 410), size=(100, 25))
        btn_search.Bind(wx.EVT_BUTTON, self.search)

        # 将控件添加到容器中
        fgSizer1.Add(self.m_staticText1, 0, wx.TOP, 5)
        fgSizer1.Add(self.tc1, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText2, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText3, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText4, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText5, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText6, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc2, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc3, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc4, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc5, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc6, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText7, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText8, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText9, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText10, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText11, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc7, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc8, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc9, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc10, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc11, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText12, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText13, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText14, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText15, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText16, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc12, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc13, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc14, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc15, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc16, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText17, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText18, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText19, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText20, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText21, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc17, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc18, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc19, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc20, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc21, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText22, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText23, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText24, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText25, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText26, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc22, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc23, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc24, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc25, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc26, 0, wx.ALL, 0)

        mainBox.Add(fgSizer1, 0, wx.ALL, 10)
        mainBox.Add(fgSizer2, 0, wx.ALL, 10)

        self.SetSizer(mainBox)
        self.Layout()

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def search(self, evt):
        text = self.tc1.GetValue()
        self.tc2.SetValue(text)

    def OnClose(self, evt):
        '''关闭窗口事件函数'''
        dlg = wx.MessageDialog(None, u'确定要关闭本窗口？', u'操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if (dlg.ShowModal() == wx.ID_YES):
            frame.Show(True)
            self.Destroy()


class chooseFrame2(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title=u"金融聚类分析器")
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetSize((820, 500))
        self.Center()

        # 容器
        mainBox = wx.BoxSizer(wx.VERTICAL)
        fgSizer1 = wx.FlexGridSizer(0, 2, 10, 20)
        fgSizer2 = wx.FlexGridSizer(10, 5, 10, 20)

        # 文本
        self.m_staticText1 = wx.StaticText(self, -1, u'请输入公司名称：')
        self.m_staticText2 = wx.StaticText(self, -1, u'变更次数：')
        self.m_staticText3 = wx.StaticText(self, -1, u'建立时间：')
        self.m_staticText4 = wx.StaticText(self, -1, u'注册资本：')
        self.m_staticText5 = wx.StaticText(self, -1, u'网店个数：')
        self.m_staticText6 = wx.StaticText(self, -1, u'分支机构数：')
        self.m_staticText7 = wx.StaticText(self, -1, u'股东信息：')
        self.m_staticText8 = wx.StaticText(self, -1, u'年报出资信息：')
        self.m_staticText9 = wx.StaticText(self, -1, u'对外担保：')
        self.m_staticText10 = wx.StaticText(self, -1, u'对外投资：')
        self.m_staticText11 = wx.StaticText(self, -1, u'中标次数：')
        self.m_staticText12 = wx.StaticText(self, -1, u'招聘记录：')
        self.m_staticText13 = wx.StaticText(self, -1, u'参保日期：')
        self.m_staticText14 = wx.StaticText(self, -1, u'社保信息：')
        self.m_staticText15 = wx.StaticText(self, -1, u'产品合格率：')
        self.m_staticText16 = wx.StaticText(self, -1, u'执行标的：')
        self.m_staticText17 = wx.StaticText(self, -1, u'经营异常次数：')
        self.m_staticText18 = wx.StaticText(self, -1, u'处罚次数：')
        self.m_staticText19 = wx.StaticText(self, -1, u'出质股权次数：')
        self.m_staticText20 = wx.StaticText(self, -1, u'欠税额：')
        self.m_staticText21 = wx.StaticText(self, -1, u'信用等级：')
        self.m_staticText22 = wx.StaticText(self, -1, u'失信黑名单次数：')
        self.m_staticText23 = wx.StaticText(self, -1, u'商标申请次数：')
        self.m_staticText24 = wx.StaticText(self, -1, u'软件著作权登记次数：')
        self.m_staticText25 = wx.StaticText(self, -1, u'专利申请次数：')
        self.m_staticText26 = wx.StaticText(self, -1, u'域名知识产权数：')

        # 输入框
        self.tc1 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC01')
        self.tc2 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC02')
        self.tc3 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC03')
        self.tc4 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC04')
        self.tc5 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC05')
        self.tc6 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC06')
        self.tc7 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC07')
        self.tc8 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC08')
        self.tc9 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC09')
        self.tc10 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC10')
        self.tc11 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC11')
        self.tc12 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC12')
        self.tc13 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC13')
        self.tc14 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC14')
        self.tc15 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC15')
        self.tc16 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC16')
        self.tc17 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC17')
        self.tc18 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC18')
        self.tc19 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC19')
        self.tc20 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC20')
        self.tc21 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC21')
        self.tc22 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC22')
        self.tc23 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC23')
        self.tc24 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC24')
        self.tc25 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC25')
        self.tc26 = wx.TextCtrl(self, -1, '', size=(140, -1), name='TC26')

        # 按钮
        btn_search = wx.Button(self, -1, u'查询', pos=(255, 410), size=(100, 25))
        btn_clear = wx.Button(self, -1, u'清空', pos=(400, 410), size=(100, 25))
        btn_search.Bind(wx.EVT_BUTTON, self.search)
        btn_clear.Bind(wx.EVT_BUTTON, self.clear)

        # 将控件添加到容器中
        fgSizer1.Add(self.m_staticText1, 0, wx.TOP, 5)
        fgSizer1.Add(self.tc1, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText2, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText3, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText4, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText5, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText6, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc2, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc3, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc4, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc5, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc6, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText7, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText8, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText9, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText10, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText11, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc7, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc8, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc9, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc10, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc11, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText12, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText13, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText14, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText15, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText16, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc12, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc13, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc14, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc15, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc16, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText17, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText18, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText19, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText20, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText21, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc17, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc18, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc19, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc20, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc21, 0, wx.ALL, 0)
        fgSizer2.Add(self.m_staticText22, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText23, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText24, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText25, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.m_staticText26, 0, wx.TOP | wx.LEFT, 3)
        fgSizer2.Add(self.tc22, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc23, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc24, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc25, 0, wx.ALL, 0)
        fgSizer2.Add(self.tc26, 0, wx.ALL, 0)

        mainBox.Add(fgSizer1, 0, wx.ALL, 10)
        mainBox.Add(fgSizer2, 0, wx.ALL, 10)

        self.SetSizer(mainBox)
        self.Layout()

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def search(self, evt):
        if self.tc1.GetValue() != '':
            self.tc1.SetValue(cf.newcreditgrade(int(self.tc1.GetValue()))[0])
        if self.tc2.GetValue() != '':
            self.tc2.SetValue(cf.newalttime(int(self.tc2.GetValue()))[0])
        if self.tc3.GetValue() != '':
            self.tc3.SetValue(cf.newestdate(int(self.tc3.GetValue()))[0])
        if self.tc4.GetValue() != '':
            self.tc4.SetValue(cf.newregcap(int(self.tc4.GetValue()))[0])
        if self.tc5.GetValue() != '':
            self.tc5.SetValue(cf.newshopnum(int(self.tc5.GetValue()))[0])
        if self.tc6.GetValue() != '':
            self.tc6.SetValue(cf.newbranchnum(int(self.tc6.GetValue()))[0])
        if self.tc7.GetValue() != '':
            splitlist = self.tc7.GetValue().split("，")
            self.tc7.SetValue(cf.newcontribution(float(splitlist[0]), float(splitlist[1]))[0])
        if self.tc8.GetValue() != '':
            splitlist = self.tc8.GetValue().split("，")
            self.tc8.SetValue(cf.newyear(float(splitlist[0]), float(splitlist[1]))[0])
        if self.tc9.GetValue() != '':
            self.tc9.SetValue(cf.newguarantee(float(self.tc9.GetValue()))[0])
        if self.tc10.GetValue() != '':
            self.tc10.SetValue(cf.newinvestment(int(self.tc10.GetValue()))[0])
        if self.tc11.GetValue() != '':
            self.tc11.SetValue(cf.newbid(int(self.tc11.GetValue()))[0])
        if self.tc12.GetValue() != '':
            self.tc12.SetValue(cf.newrecruit(int(self.tc12.GetValue()))[0])
        if self.tc13.GetValue() != '':
            self.tc13.SetValue(cf.newinsurance(int(self.tc13.GetValue()))[0])
        if self.tc14.GetValue() != '':
            splitlist = self.tc14.GetValue().split("，")
            self.tc14.SetValue(
                cf.newsecurity(int(splitlist[0]), int(splitlist[1]), int(splitlist[2]), int(splitlist[3]),
                               int(splitlist[4]))[0])
        if self.tc15.GetValue() != '':
            self.tc15.SetValue(cf.newquality(float(self.tc15.GetValue()))[0])
        if self.tc16.GetValue() != '':
            self.tc16.SetValue(cf.newamount(float(self.tc16.GetValue()))[0])
        if self.tc17.GetValue() != '':
            self.tc17.SetValue(cf.newabnormal(int(self.tc17.GetValue()))[0])
        if self.tc18.GetValue() != '':
            self.tc18.SetValue(cf.newpunish(int(self.tc18.GetValue()))[0])
        if self.tc19.GetValue() != '':
            self.tc19.SetValue(cf.newrightpledge(int(self.tc19.GetValue()))[0])
        if self.tc20.GetValue() != '':
            self.tc20.SetValue(cf.newtaxunpaid(float(self.tc20.GetValue()))[0])
        if self.tc21.GetValue() != '':
            self.tc21.SetValue(cf.newcreditgrade(int(self.tc21.GetValue()))[0])
        if self.tc22.GetValue() != '':
            self.tc22.SetValue(cf.newcredit(int(self.tc22.GetValue()))[0])
        if self.tc23.GetValue() != '':
            self.tc23.SetValue(cf.newbrandnum(int(self.tc23.GetValue()))[0])
        if self.tc24.GetValue() != '':
            self.tc24.SetValue(cf.newcopynum(int(self.tc24.GetValue()))[0])
        if self.tc25.GetValue() != '':
            self.tc25.SetValue(cf.newpatentnum(int(self.tc25.GetValue()))[0])
        if self.tc26.GetValue() != '':
            self.tc26.SetValue(cf.newdomnum(int(self.tc26.GetValue()))[0])

    def clear(self, evt):
        self.tc1.SetValue('')
        self.tc2.SetValue('')
        self.tc3.SetValue('')
        self.tc4.SetValue('')
        self.tc5.SetValue('')
        self.tc6.SetValue('')
        self.tc7.SetValue('')
        self.tc8.SetValue('')
        self.tc9.SetValue('')
        self.tc10.SetValue('')
        self.tc11.SetValue('')
        self.tc12.SetValue('')
        self.tc13.SetValue('')
        self.tc14.SetValue('')
        self.tc15.SetValue('')
        self.tc16.SetValue('')
        self.tc17.SetValue('')
        self.tc18.SetValue('')
        self.tc19.SetValue('')
        self.tc20.SetValue('')
        self.tc21.SetValue('')
        self.tc22.SetValue('')
        self.tc23.SetValue('')
        self.tc24.SetValue('')
        self.tc25.SetValue('')
        self.tc26.SetValue('')

    def OnClose(self, evt):
        '''关闭窗口事件函数'''
        dlg = wx.MessageDialog(None, u'确定要关闭本窗口？', u'操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if (dlg.ShowModal() == wx.ID_YES):
            frame.Show(True)
            self.Destroy()


class MyApp(wx.App):
  def OnInit(self):
    self.mainframe = mainFrame()
    self.myframe1 = chooseFrame1()
    self.myframe2 = chooseFrame2()
    self.SetTopWindow(self.mainframe)
    self.myframe1.Show(True)
    self.myframe2.Show(True)
    return True


if __name__ == '__main__':
    app = wx.App()
    frame = mainFrame()
    frame.Show(True)
    app.MainLoop()
