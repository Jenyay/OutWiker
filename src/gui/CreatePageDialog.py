# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Apr 07 20:05:46 2010

import os

import wx

from core.search import TagsList
import core.system
from core.tree import RootWikiPage

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

#from core.factory import FactorySelector
import core.factory

class CreatePageDialog(wx.Dialog):
	def __init__(self, parentPage = None, currentPage = None, *args, **kwds):
		"""
		parentPage -- родительская страница (используется, если страницу нужно создавать, а не изменять)
		currentPage -- страница, которую надо изменить (используется, если страницу нужно изменять, а не создавать)
		"""
		# begin wxGlade: CreatePageDialog.__init__
		kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
		wx.Dialog.__init__(self, *args, **kwds)
		self.label_1 = wx.StaticText(self, -1, _("Title"))
		self.titleTextCtrl = wx.TextCtrl(self, -1, "")
		self.label_2 = wx.StaticText(self, -1, _("Tags (comma separated)"))
		self.tagsTextCtrl = wx.TextCtrl(self, -1, "")
		self.label_3 = wx.StaticText(self, -1, _("Page type"))
		self.comboType = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
		self.iconsList = wx.ListCtrl(self, -1, style=wx.LC_ICON|wx.LC_AUTOARRANGE|wx.LC_SINGLE_SEL|wx.FULL_REPAINT_ON_RESIZE)

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

		self.currentPage = currentPage
		self.parentPage = parentPage

		self.imagesDir = core.system.getImagesDir()
		self.iconspath = os.path.join (self.imagesDir, "iconset")
		self.defaultIcon = os.path.join (self.imagesDir, "page.png")

		self._fillComboType()

		self.icons = wx.ImageList (16, 16)
		self.iconsList.AssignImageList (self.icons, wx.IMAGE_LIST_NORMAL)

		# Словарь, с помощью которого можно найти путь к файлу по элементу списка
		# Ключ - элемент списка, значение - путь к файлу
		self.iconsDict = {}
		self.makeIconsList()

		if parentPage.parent != None:
			tags = TagsList.getTagsString (parentPage.tags)
			self.tagsTextCtrl.SetValue (tags)

		# Для изменения страницы
		if currentPage != None:
			self.SetTitle(_(u"Edit page properties"))
			self._prepareForChange (currentPage)

		self.Bind (wx.EVT_BUTTON, self.onOk, self.btnOk)


	def onOk (self, event):
		if not self.testPageTitle (self.pageTitle):
			wx.MessageBox (_(u"Invalid page title"), _(u"Error"), wx.ICON_ERROR | wx.OK)
			return

		if self.currentPage != None \
				and not self.currentPage.canRename (self.pageTitle):
			wx.MessageBox (_(u"Can't rename page when page with that title already exists"), _(u"Error"), wx.ICON_ERROR | wx.OK)
			return

		if self.currentPage == None and \
				self.parentPage != None and \
				not RootWikiPage.testDublicate(self.parentPage, self.pageTitle):
			wx.MessageBox (_(u"A page with this title already exists"), _(u"Error"), wx.ICON_ERROR | wx.OK)
			return

		event.Skip()
	

	def testPageTitle (self, title):
		"""
		Возвращает True, если возможно создать страницу с таким заголовком
		"""
		if ("/" in title or 
			"\\" in title or
			title.startswith ("__") or
			len (title.strip()) == 0):
			return False

		return True
	

	def _prepareForChange (self, currentPage):
		"""
		Подготовить диалог к редактированию свойств страницы
		"""
		tags = TagsList.getTagsString (currentPage.tags)
		self.tagsTextCtrl.SetValue (tags)
		
		# Запретить изменять заголовок
		self.titleTextCtrl.SetValue (currentPage.title)

		# Установить тип страницы
		self._setPageType(currentPage)

		# Добавить текущую иконку
		icon = currentPage.icon
		if icon != None:
			index = self.icons.Add (wx.Bitmap (icon) )
			selItem = self.iconsList.InsertImageStringItem (len (self.iconsDict) - 1, _(u"Current icon"), index)
			self.iconsList.SetItemState (selItem, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
			self.iconsDict[selItem] = icon
	

	def _setPageType (self, currentPage):
		"""
		Установить тип страницы в диалоге
		"""
		n = 0
		items = self.comboType.GetItems()
		for factory in core.factory.FactorySelector.factories:
			if factory.type == core.factory.FactorySelector.getFactory(currentPage).type:
				self.comboType.SetSelection (n)
				self.comboType.Disable ()
				break
			n += 1


	@staticmethod
	def CreateForCreate (parentpage, parentWnd):
		"""
		Создать диалог для создания страницы.
		Вызывать вместо конструктора
		"""
		return CreatePageDialog (parentpage, None, parent = parentWnd)


	@staticmethod
	def CreateForEdit (currentpage, parentWnd):
		"""
		Создать диалог для создания страницы.
		Вызывать вместо конструктора
		"""
		return CreatePageDialog (currentpage.parent, currentpage, parent = parentWnd)
	
	
	def makeIconsList (self):
		self.iconsList.ClearAll()
		self.icons.RemoveAll()
		self.iconsDict = {}

		# Иконка по умолчанию
		self.icons.Add (wx.Bitmap (self.defaultIcon) )
		firstItem = self.iconsList.InsertImageStringItem (0, u"page.png", 0)
		self.iconsDict[firstItem] = self.defaultIcon
		self.iconsDict[-1] = self.defaultIcon

		files = [fname for fname in os.listdir (self.iconspath)]
		files.sort()

		index = 1
		for fname in files:
			fullpath = os.path.join (self.iconspath, fname)
			bitmap = wx.Bitmap (fullpath)
			self.icons.Add (bitmap)
			item = self.iconsList.InsertImageStringItem (index, fname, index)
			self.iconsDict[item] = fullpath
			#print item

			index += 1
		
		self.iconsList.SetItemState (firstItem, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


	def __set_properties(self):
		# begin wxGlade: CreatePageDialog.__set_properties
		self.SetTitle(_("Create Page"))
		self.SetSize((500, 350))
		self.titleTextCtrl.SetMinSize((350,-1))
		self.tagsTextCtrl.SetMinSize((250, -1))
		self.iconsList.SetMinSize((500, 200))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: CreatePageDialog.__do_layout
		grid_sizer_1 = wx.FlexGridSizer(5, 1, 0, 0)
		grid_sizer_4 = wx.FlexGridSizer(1, 2, 0, 0)
		grid_sizer_3 = wx.FlexGridSizer(1, 2, 0, 0)
		grid_sizer_2 = wx.FlexGridSizer(1, 2, 0, 0)
		grid_sizer_2.Add(self.label_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
		grid_sizer_2.Add(self.titleTextCtrl, 0, wx.ALL|wx.EXPAND, 4)
		grid_sizer_2.AddGrowableCol(1)
		grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
		grid_sizer_3.Add(self.label_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
		grid_sizer_3.Add(self.tagsTextCtrl, 0, wx.ALL|wx.EXPAND, 4)
		grid_sizer_3.AddGrowableCol(1)
		grid_sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)
		grid_sizer_4.Add(self.label_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
		grid_sizer_4.Add(self.comboType, 0, wx.ALL|wx.EXPAND, 4)
		grid_sizer_4.AddGrowableCol(1)
		grid_sizer_1.Add(grid_sizer_4, 1, wx.EXPAND, 0)
		grid_sizer_1.Add(self.iconsList, 1, wx.ALL|wx.EXPAND, 2)
		self.SetSizer(grid_sizer_1)
		grid_sizer_1.AddGrowableRow(3)
		grid_sizer_1.AddGrowableCol(0)
		self.Layout()
		# end wxGlade
	
		self._createOkCancelButtons (grid_sizer_1)
	

	def _createOkCancelButtons (self, sizer):
		# Создание кнопок Ok/Cancel
		buttonsSizer = wx.StdDialogButtonSizer ()
		sizer.AddSpacer(0)
		sizer.Add (buttonsSizer, 1, wx.ALIGN_RIGHT | wx.ALL, border = 2)

		self.btnOk = wx.Button (self, wx.ID_OK)
		self.btnCancel = wx.Button (self, wx.ID_CANCEL)

		buttonsSizer.Add (self.btnOk)
		buttonsSizer.Add (self.btnCancel)

		#self.Bind (wx.EVT_BUTTON, self.onOk, self.btnOk)
		
		sizer.Fit(self)
		self.Layout()

	
	def _fillComboType (self):
		self.comboType.Clear()
		for factory in core.factory.FactorySelector.factories:
			self.comboType.Append (factory.type, factory)

		if not self.comboType.IsEmpty():
			self.comboType.SetSelection (0)


	@property
	def selectedFactory (self):
		index = self.comboType.GetSelection()
		return self.comboType.GetClientData (index)

	@property
	def pageTitle (self):
		return self.titleTextCtrl.GetValue()

	@property
	def tags (self):
		tagsString = self.tagsTextCtrl.GetValue()
		tags = TagsList.parseTagsList (tagsString)
		return tags

	@property
	def icon (self):
		item = self.iconsList.GetNextItem (-1, state = wx.LIST_STATE_SELECTED)
		#print item
		return self.iconsDict[item]



# end of class CreatePageDialog


