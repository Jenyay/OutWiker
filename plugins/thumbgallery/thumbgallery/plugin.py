# -*- coding: utf-8 -*-

import os.path

from outwiker.core.pluginbase import Plugin

from .controller import Controller
from .guicontroller import GUIController


def _no_translate(text):
    return text


class PluginThumbGallery(Plugin):
    """
    Плагин, добавляющий обработку команды (:thumblist:) и (:thumbgallery:)
        в википарсер
    """
    def __init__(self, application):
        """
        application - экземпляр класса core.application.ApplicationParams
        """
        super().__init__(application)
        self._controller = Controller(application)
        self._GUIController = GUIController(application)

    @property
    def name(self):
        return u"ThumbGallery"

    @property
    def description(self):
        return self._loadDescription()

    def initialize(self):
        self._initlocale(u"thumbgallery")
        self._controller.initialize()
        self._GUIController.initialize()

    def _initlocale(self, domain):
        from .i18n import set_
        langdir = os.path.join(os.path.dirname(__file__), "locale")
        global _

        try:
            _ = self._init_i18n(domain, langdir)
        except BaseException as e:
            print(e)
            _ = _no_translate

        set_(_)

    def destroy(self):
        """
        Уничтожение(выгрузка) плагина.
        Здесь плагин должен отписаться от всех событий
        """
        self._controller.destroy()
        self._GUIController.destroy()

    @property
    def url(self):
        return _(u"http://jenyay.net/Outwiker/ThumbGalleryEn")

    def _loadDescription(self):
        """
        Загрузить описание плагина из файла
        """
        path = _(u"locale/description.html")
        currentDir = os.path.dirname(__file__)
        fullpath = os.path.join(currentDir, path)

        try:
            with open(fullpath) as fp:
                return fp.read()
        except IOError:
            return _(u"Can't load description")
