# -*- coding: utf-8 -*-

import re

from pyparsing import QuotedString, Regex, Literal

from .tokenblock import TextBlockToken


class FontsFactory:
    """
    Фабрика для создания шрифтовых / блочных токенов
    """
    @staticmethod
    def makeItalic(parser):
        """
        Создать токен для курсивного шрифта
        """
        return ItalicToken(parser).getToken()

    @staticmethod
    def makeBold(parser):
        """
        Создать токен для полужирного шрифта
        """
        return BoldToken(parser).getToken()

    @staticmethod
    def makeBoldItalic(parser):
        """
        Создать токен для полужирного курсивного шрифта
        """
        return BoldItalicToken(parser).getToken()

    @staticmethod
    def makeUnderline(parser):
        """
        Создать токен для подчеркнутого шрифта
        """
        return UnderlineToken(parser).getToken()

    @staticmethod
    def makeStrike(parser):
        """
        Создать токен для зачеркнутого шрифта
        """
        return StrikeToken(parser).getToken()

    @staticmethod
    def makeSubscript(parser):
        """
        Создать токен для нижнего индекса
        """
        return SubscriptToken(parser).getToken()

    @staticmethod
    def makeSuperscript(parser):
        """
        Создать токен для верхнего индекса
        """
        return SuperscriptToken(parser).getToken()

    @staticmethod
    def makeCode(parser):
        """
        Создать токен для кода
        """
        return CodeToken(parser).getToken()

    @staticmethod
    def makeSmall(parser):
        """
        Создать парсер для мелкого шрифта
        """
        return SmallFontToken(parser).getToken()

    @staticmethod
    def makeBig(parser):
        """
        Создать парсер для крупного шрифта
        """
        return BigFontToken(parser).getToken()

    @staticmethod
    def makeMark(parser):
        """
        Create the mark token
        """
        return MarkToken(parser).getToken()


class CodeToken(TextBlockToken):
    """
    Токен для кода
    """
    start = "@@"
    end = "@@"

    def getToken(self):
        return QuotedString(CodeToken.start,
                            endQuoteChar=CodeToken.end,
                            multiline=True,
                            convertWhitespaceEscapes=False).setParseAction(self.convertToHTML("<code>", "</code>"))("code")


class SuperscriptToken(TextBlockToken):
    """
    Токен для верхнего индекса
    """
    start = "'^"
    end = "^'"

    def getToken(self):
        return QuotedString(SuperscriptToken.start,
                            endQuoteChar=SuperscriptToken.end,
                            multiline=True,
                            convertWhitespaceEscapes=False).setParseAction(self.convertToHTML("<sup>", "</sup>"))("superscript")


class SubscriptToken(TextBlockToken):
    """
    Токен для нижнего индекса
    """
    start = "'_"
    end = "_'"

    def getToken(self):
        return QuotedString(SubscriptToken.start,
                            endQuoteChar=SubscriptToken.end,
                            multiline=True,
                            convertWhitespaceEscapes=False).setParseAction(self.convertToHTML("<sub>", "</sub>"))("subscript")


class UnderlineToken(TextBlockToken):
    """
    Токен для подчеркнутого текста
    """
    start = "{+"
    end = "+}"

    def getToken(self):
        return QuotedString(UnderlineToken.start,
                            endQuoteChar=UnderlineToken.end,
                            multiline=True,
                            convertWhitespaceEscapes=False).setParseAction(self.convertToHTML("<u>", "</u>"))("underline")


class StrikeToken(TextBlockToken):
    """
    Токен для зачеркнутого текста
    """
    start = "{-"
    end = "-}"

    def getToken(self):
        return QuotedString(StrikeToken.start,
                            endQuoteChar=StrikeToken.end,
                            multiline=True,
                            convertWhitespaceEscapes=False).setParseAction(self.convertToHTML("<strike>", "</strike>"))("strike")


class ItalicToken:
    """
    Токен для курсива
    """
    start = "''"
    end = "''"

    def __init__(self, parser):
        self.parser = parser

    def getToken(self):
        return Regex(self.start + "(.+?)" + self.end, re.S).setParseAction(self._parseAction)("italic")

    def _parseAction(self, s, l, t):
        return '<i>{}</i>'.format(self.parser.parseTextLevelMarkup(t[0][len(self.start):-len(self.end)]))


class BoldToken:
    """
    Токен для полужирного шрифта
    """
    start = "'''"
    end = "'''"

    def __init__(self, parser):
        self.parser = parser

    def getToken(self):
        return Regex(self.start + "(.+?)" + self.end, re.S).setParseAction(self._parseAction)("bold")

    def _parseAction(self, s, l, t):
        return '<b>{}</b>'.format(self.parser.parseTextLevelMarkup(t[0][len(self.start):-len(self.end)]))


class BoldItalicToken:
    """
    Токен для полужирного курсивного шрифта
    """
    start = "''''"
    end = "''''"

    def __init__(self, parser):
        self.parser = parser

    def getToken(self):
        return Regex(self.start + "(.+?)" + self.end, re.S).setParseAction(self._parseAction)("bold_italic")

    def _parseAction(self, s, l, t):
        return '<b><i>{}</i></b>'.format(self.parser.parseTextLevelMarkup(t[0][len(self.start):-len(self.end)]))


class SmallFontToken(TextBlockToken):
    """
    Токен для мелкого шрифта
    """
    def getToken(self):
        return Regex(r"\[(?P<count>-{1,4})(?P<text>.*?)\1\]",
                     re.MULTILINE | re.DOTALL).setParseAction(self.__parse)("small")

    def __parse(self, s, l, t):
        # Расчет масштаба в зависимости от количества минусов
        size = 100 - len(t["count"]) * 20

        return u'<span style="font-size:{size}%">{text}</span>'.format(size=size, text=self.parser.parseTextLevelMarkup(t["text"]))


class BigFontToken(TextBlockToken):
    """
    Токен для крупного шрифта
    """
    def getToken(self):
        return Regex(r"\[(?P<count>\+{1,5})(?P<text>.*?)\1\]",
                     re.MULTILINE | re.DOTALL).setParseAction(self.__parse)("big")

    def __parse(self, s, l, t):
        # Расчет масштаба в зависимости от количества минусов
        size = 100 + len(t["count"]) * 20

        return u'<span style="font-size:{size}%">{text}</span>'.format(
            size=size,
            text=self.parser.parseTextLevelMarkup(t["text"])
        )


class MarkToken(TextBlockToken):
    """
    Mark text token
    """
    start = "[!"
    end = "!]"

    def getToken(self):
        return QuotedString(MarkToken.start,
                            endQuoteChar=MarkToken.end,
                            multiline=True,
                            convertWhitespaceEscapes=False).setParseAction(self.convertToHTML("<mark>", "</mark>"))("mark")
