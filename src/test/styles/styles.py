#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os.path
import shutil

from outwiker.core.style import Style
from outwiker.core.tree import RootWikiPage, WikiDocument
from outwiker.core.application import Application
from outwiker.pages.wiki.wikipage import WikiPageFactory, WikiWikiPage
from outwiker.pages.html.htmlpage import HtmlPageFactory, HtmlWikiPage
from test.utils import removeWiki


class StylesTest (unittest.TestCase):
    def setUp (self):
        # Количество срабатываний особытий при обновлении страницы
        self._pageUpdateCount = 0
        self._pageUpdateSender = None

        # Здесь будет создаваться вики
        self.path = u"../test/testwiki"
        removeWiki (self.path)
        self.eventcount = 0

        self.rootwiki = WikiDocument.create (self.path)
        WikiPageFactory.create (self.rootwiki, u"Викистраница 1", [])
        HtmlPageFactory.create (self.rootwiki, u"Html-страница 2", [])

        self._styleFname = u"__style.html"
        self._styleDir = u"__style"
        self._exampleStyleDir = u"../styles/example_jblog"
        self._exampleStyleDir2 = u"../styles/example_jnet"
        self._testStylePath = os.path.join (self._exampleStyleDir, self._styleFname)

        Application.wikiroot = self.rootwiki
        Application.onPageUpdate += self.onPageUpdate


    def onPageUpdate (self, sender):
        self._pageUpdateCount += 1
        self._pageUpdateSender = sender


    def tearDown (self):
        Application.onPageUpdate -= self.onPageUpdate
        removeWiki (self.path)


    def testDefault (self):
        """
        Проверка того, что возвращается правильный путь до шаблона по умолчанию
        """
        style = Style()
        defaultStyle = style.getDefaultStyle()
        self.assertEqual (os.path.abspath (defaultStyle), 
                os.path.abspath ("styles/__default/__style.html") )


    def testStylePageDefault (self):
        """
        Проверка на то, что если у страницы нет файла стиля, то возвращается стиль по умолчанию
        """
        style = Style()
        defaultStyle = style.getDefaultStyle()
        style_page1 = style.getPageStyle (self.rootwiki[u"Викистраница 1"])
        style_page2 = style.getPageStyle (self.rootwiki[u"Html-страница 2"])

        self.assertEqual (style_page1, defaultStyle)
        self.assertEqual (style_page2, defaultStyle)


    def testStylePage1 (self):
        style = Style()
        page = self.rootwiki[u"Викистраница 1"]
        shutil.copy (self._testStylePath, page.path)

        validStyle = os.path.abspath (os.path.join (page.path, self._styleFname))
        pageStyle = os.path.abspath (style.getPageStyle (page))

        self.assertEqual (pageStyle, validStyle)


    def testStylePage2 (self):
        style = Style()
        page = self.rootwiki[u"Html-страница 2"]
        shutil.copy (self._testStylePath, page.path)

        validStyle = os.path.abspath (os.path.join (page.path, self._styleFname))
        pageStyle = os.path.abspath (style.getPageStyle (page))

        self.assertEqual (pageStyle, validStyle)


    def testFakeStyle (self):
        style = Style()
        page = self.rootwiki[u"Викистраница 1"]
        os.mkdir (os.path.join (page.path, self._styleFname) )

        validStyle = os.path.abspath (style.getDefaultStyle())
        pageStyle = os.path.abspath (style.getPageStyle (page))

        self.assertEqual (pageStyle, validStyle)


    def testSetStyleAsDir (self):
        style = Style()
        page = self.rootwiki[u"Викистраница 1"]

        pageStyleFname = os.path.join (page.path, self._styleFname)
        pageStyleDir = os.path.join (page.path, self._styleDir)

        self.assertFalse (os.path.exists (pageStyleDir))
        self.assertFalse (os.path.exists (pageStyleFname))

        style.setPageStyle (page, self._exampleStyleDir)

        self.assertTrue (os.path.exists (pageStyleDir))
        self.assertTrue (os.path.exists (pageStyleFname))

        style.setPageStyleDefault (page)

        self.assertFalse (os.path.exists (pageStyleDir))
        self.assertFalse (os.path.exists (pageStyleFname))


    def testSetStyleAsFile (self):
        style = Style()
        page = self.rootwiki[u"Викистраница 1"]

        pageStyleFname = os.path.join (page.path, self._styleFname)
        pageStyleDir = os.path.join (page.path, self._styleDir)

        self.assertFalse (os.path.exists (pageStyleDir))
        self.assertFalse (os.path.exists (pageStyleFname))

        style.setPageStyle (page, os.path.join (self._exampleStyleDir, self._styleFname) )

        self.assertTrue (os.path.exists (pageStyleDir))
        self.assertTrue (os.path.exists (pageStyleFname))

        style.setPageStyleDefault (page)

        self.assertFalse (os.path.exists (pageStyleDir))
        self.assertFalse (os.path.exists (pageStyleFname))


    def testSetStyle2 (self):
        style = Style()
        page = self.rootwiki[u"Викистраница 1"]

        pageStyleFname = os.path.join (page.path, self._styleFname)
        pageStyleDir = os.path.join (page.path, self._styleDir)

        self.assertFalse (os.path.exists (pageStyleDir))
        self.assertFalse (os.path.exists (pageStyleFname))

        style.setPageStyle (page, self._exampleStyleDir)

        self.assertTrue (os.path.exists (pageStyleDir))
        self.assertTrue (os.path.exists (pageStyleFname))

        style.setPageStyle (page, style.getDefaultStyle())

        self.assertFalse (os.path.exists (pageStyleDir))
        self.assertTrue (os.path.exists (pageStyleFname))


    def testEvent (self):
        """
        Вызов событий при изменении стиля страницы
        """
        style = Style()
        page = self.rootwiki[u"Викистраница 1"]

        self.assertEqual (self._pageUpdateCount, 0)

        style.setPageStyle (page, self._exampleStyleDir)
        self.assertEqual (self._pageUpdateCount, 1)

        style.setPageStyleDefault (page)
        self.assertEqual (self._pageUpdateCount, 2)

        style.setPageStyle (page, self._exampleStyleDir2)
        self.assertEqual (self._pageUpdateCount, 3)


    def testInvalidPage (self):
        style = Style()
        style.setPageStyle (None, self._exampleStyleDir)
        style.setPageStyleDefault (None)

        style.setPageStyle (self.rootwiki, self._exampleStyleDir)
        style.setPageStyleDefault (self.rootwiki)
