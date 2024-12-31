from outwiker.core.event import (Event, pagetype, EVENT_PRIORITY_DEFAULT,
                                 EVENT_PRIORITY_MAX_CORE,
                                 EVENT_PRIORITY_MIN_CORE)
from outwiker.core.events import (PAGE_UPDATE_CONTENT, PAGE_UPDATE_ICON,
                                  PAGE_UPDATE_STYLE, PAGE_UPDATE_TAGS,
                                  PAGE_UPDATE_TITLE,
                                  LinkClickParams, HoverLinkParams,
                                  PreprocessingParams, PostprocessingParams,
                                  PreHtmlImprovingParams,
                                  EditorPopupMenuParams, PageDialogInitParams,
                                  PageDialogDestroyParams,
                                  PageDialogPageTypeChangedParams,
                                  PageDialogPageTitleChangedParams,
                                  PageDialogNewPageOrderChangedParams,
                                  PageDialogPageStyleChangedParams,
                                  PageDialogPageIconChangedParams,
                                  PageDialogPageTagsChangedParams,
                                  PageDialogPageFactoriesNeededParams,
                                  EditorStyleNeededParams,
                                  PageUpdateNeededParams,
                                  PreWikiOpenParams,
                                  PostWikiOpenParams,
                                  PostWikiCloseParams,
                                  IconsGroupsListInitParams,
                                  PageModeChangeParams,
                                  AttachListChangedParams,
                                  AttachSubdirChangedParams,
                                  TextEditorKeyDownParams,
                                  PreWikiCloseParams,
                                  PostContentReadingParams,
                                  PreContentWritingParams,
                                  TextEditorCaretMoveParams,
                                  BeginAttachRenamingParams,
                                  AttachSelectionChangedParams,
                                  NotesTreeItemsPreparingParams,
                                  ForceNotesTreeItemsUpdate,
                                  )
