# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

import wx

from outwiker.gui.baseaction import BaseAction
from outwiker.gui.dateformatdialog import DateFormatDialog


class WikiDateBaseAction (BaseAction):
    __metaclass__ = ABCMeta

    def __init__ (self, application):
        self._application = application


    @abstractmethod
    def getCommandName (self):
        pass


    def run (self, params):
        assert self._application.mainWindow is not None
        assert self._application.mainWindow.pagePanel is not None

        with DateFormatDialog (self._application.mainWindow,
                               _(u"Enter format of the date\n(empty string - format from program setting)"),
                               _(u"Date format"),
                               u"") as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                params = u' format="{}"'.format (dlg.Value) if len (dlg.Value) != 0 else u""
                text = u"(:{}{}:)".format (self.getCommandName(), params)

                self._application.mainWindow.pagePanel.pageView.codeEditor.replaceText (text)



class WikiDateCreationAction (WikiDateBaseAction):
    """
    Вставка команды для вывода даты создания страницы
    """
    stringId = u"WikiDateCreation"

    @property
    def title (self):
        return _(u"Creation date (:crdate:)")


    @property
    def description (self):
        return _(u"Insert the creation date command (:crdate:)")


    def getCommandName (self):
        return u"crdate"


class WikiDateEditionAction (WikiDateBaseAction):
    """
    Вставка команды для вывода даты последнего редактирования страницы
    """
    stringId = u"WikiDateEdit"

    def __init__ (self, application):
        self._application = application


    @property
    def title (self):
        return _(u"Edition date (:eddate:)")


    @property
    def description (self):
        return _(u"Insert the edition date command (:eddate:)")


    def getCommandName (self):
        return u"eddate"
