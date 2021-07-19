# -*- coding=utf-8 -*-

from outwiker.core.commands import showError
from outwiker.gui.baseaction import BaseAction


class AttachPasteLinkActionForAttachPanel(BaseAction):
    """
    Insert link to selected files to editor.

    Hidden action.
    """
    stringId = "AttachPasteLink"

    def __init__(self, application):
        self._application = application

    @property
    def title(self):
        return _("Paste attach link")

    @property
    def description(self):
        return _("Paste link to attached file")

    def run(self, params):
        attachPanel = self._application.mainWindow.attachPanel.panel
        files = attachPanel.getSelectedFiles()
        if len(files) == 0:
            showError(self._application.mainWindow,
                      _("You did not select a file to paste"))
            return

        self._application.onAttachmentPaste(files)
