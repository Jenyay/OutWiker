# -*- coding=utf-8 -*-

import rcssmin

CSS_WIKI = 'ow-wiki'
CSS_ERROR = 'ow-error'
CSS_IMAGE = 'ow-image'
CSS_LINK_PAGE = 'ow-link-page'
CSS_LINK_ATTACH = 'ow-link-attach'
CSS_ATTACH_FILE = 'ow-attach-file'
CSS_ATTACH_IMAGE = 'ow-attach-image'
CSS_ATTACH_DIR = 'ow-attach-dir'
CSS_ATTACH_LIST = 'ow-attach-list'
CSS_ATTACH_LIST_ITEM = 'ow-attach-list-item'
CSS_ATTACH_ERROR = 'ow-attach-error'
CSS_CHILD_LIST = 'ow-child-list'
CSS_CHILD_LIST_TITLE = 'ow-child-list-title'
CSS_WIKI_INCLUDE = 'ow-wiki-include'
CSS_LIST_ITEM_EMPTY = 'ow-li-empty'
CSS_LIST_ITEM_TODO = 'ow-li-todo'
CSS_LIST_ITEM_INCOMPLETE = 'ow-li-incomplete'
CSS_LIST_ITEM_COMPLETE = 'ow-li-complete'
CSS_LIST_ITEM_STAR = 'ow-li-star'
CSS_LIST_ITEM_PLUS = 'ow-li-plus'
CSS_LIST_ITEM_MINUS = 'ow-li-minus'
CSS_LIST_ITEM_CIRCLE = 'ow-li-circle'
CSS_LIST_ITEM_CHECK = 'ow-li-check'
CSS_LIST_ITEM_LT = 'ow-li-lt'
CSS_LIST_ITEM_GT = 'ow-li-gt'


def getDefaultStyles() -> str:
    css = '''
		img {
            border:none;
            vertical-align:middle;
        }

        /* Error message */
        div.ow-error {
          color: #cc0033;
          background-color: #FFBABA;
          border: 1px solid;
		  margin: 1em 0px;
		  padding: 1em;
        }

        span.ow-error {
          color: #cc0033;
          background-color: #FFBABA;
          border: 1px solid;
		  margin: 1em 0px;
		  padding: 1em;
        }

        a.ow-link-page {
            text-decoration: none;
            border-bottom: 0.1em dashed;
        }

        /* Unorder list items */
        ul.ow-wiki {
            padding-left: 1rem;
            list-style-type: none;
        }

        ul.ow-wiki > li.ow-wiki {
          padding-left: 1.5rem;
          background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMm1tIiBoZWlnaHQ9IjJtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMiAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCguMjQ4MjIgMCAwIC4yNDgwOCAtMi4zNzEzIC0yLjU0NzYpIj4KPGNpcmNsZSBjeD0iMTMuNTgxIiBjeT0iMTQuMjk5IiByPSIxIiBzdHJva2U9IiMwMDAiIHN0cm9rZS13aWR0aD0iLjgxOSIvPgo8L2c+Cjwvc3ZnPgoK");
          background-position: 0.0rem 0.0rem;
          background-size: 1.0rem 1.0rem;
          background-repeat: no-repeat;
        }

        ul.ow-wiki li.ow-li-empty {
            background-image: none;
        }

        ul.ow-wiki li.ow-li-circle {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMm1tIiBoZWlnaHQ9IjJtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMiAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCguMzMzNDUgMCAwIC4zMjQ0OSAtMy41Mjg1IC0zLjY1MDUpIiBmaWxsPSJub25lIj4KPGNpcmNsZSBjeD0iMTMuNTgxIiBjeT0iMTQuMjk5IiByPSIxIiBmaWxsPSJub25lIiBzdHJva2U9IiMwMDAiIHN0cm9rZS13aWR0aD0iLjQiLz4KPC9nPgo8L3N2Zz4K");
        }

        ul.ow-wiki li.ow-li-complete {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMS45ODU3bW0iIGhlaWdodD0iMS45ODU3bW0iIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDEuOTg1NyAxLjk4NTciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMi4xMDMgLTEyLjgzNykiPgo8cmVjdCB4PSIxMi4zNDUiIHk9IjEzLjA3OSIgd2lkdGg9IjEuNTE2NCIgaGVpZ2h0PSIxLjUxNjQiIGZpbGw9Im5vbmUiIGltYWdlLXJlbmRlcmluZz0iYXV0byIgc3Ryb2tlPSIjMDAwIiBzdHJva2Utd2lkdGg9Ii4xODM2MiIvPgo8L2c+CjxwYXRoIGQ9Im0wLjI2OTI1IDAuMjY5MjUgMS40NzI0IDEuNDcyNCIgc3Ryb2tlPSIjMDAwIiBzdHJva2Utd2lkdGg9Ii4xOCIvPgo8cGF0aCBkPSJtMS43NTg1IDAuMjQ0MDEtMS40ODA5IDEuNDg5MyIgc3Ryb2tlPSIjMDAwIiBzdHJva2Utd2lkdGg9Ii4xOCIvPgo8L3N2Zz4K");
        }

        ul.ow-wiki li.ow-li-incomplete {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMS45ODU3bW0iIGhlaWdodD0iMS45ODU3bW0iIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDEuOTg1NyAxLjk4NTciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMi4xMDMgLTEyLjgzNykiPgo8cmVjdCB4PSIxMi4zNDUiIHk9IjEzLjA3OSIgd2lkdGg9IjEuNTE2NCIgaGVpZ2h0PSIxLjUxNjQiIGZpbGw9Im5vbmUiIGltYWdlLXJlbmRlcmluZz0iYXV0byIgc3Ryb2tlPSIjMDAwIiBzdHJva2Utd2lkdGg9Ii4xODM2MiIvPgo8L2c+CjxwYXRoIGQ9Im0xLjc1ODUgMC4yNDQwMS0xLjQ4MDkgMS40ODkzIiBzdHJva2U9IiMwMDAiIHN0cm9rZS13aWR0aD0iLjE4Ii8+Cjwvc3ZnPgo=");
        }

        ul.ow-wiki li.ow-li-todo {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMS45ODU3bW0iIGhlaWdodD0iMS45ODU3bW0iIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDEuOTg1NyAxLjk4NTciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMi4xMDMgLTEyLjgzNykiPgo8cmVjdCB4PSIxMi4zNDUiIHk9IjEzLjA3OSIgd2lkdGg9IjEuNTE2NCIgaGVpZ2h0PSIxLjUxNjQiIGZpbGw9Im5vbmUiIGltYWdlLXJlbmRlcmluZz0iYXV0byIgc3Ryb2tlPSIjMDAwIiBzdHJva2Utd2lkdGg9Ii4xODM2MiIvPgo8L2c+Cjwvc3ZnPgoK");
        }

        ul.ow-wiki li.ow-li-star {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMm1tIiBoZWlnaHQ9IjJtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMiAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCgxLjAwNTMgMCAwIC45NDEwMSAtMTIuMTg5IC0xMi4wMzcpIiBmaWxsPSJub25lIiBzdHJva2U9IiMwMDAiIHN0cm9rZS13aWR0aD0iLjIiPgo8cGF0aCBkPSJtMTMuMTIxIDEzLjE2NHYxLjM4MTUiLz4KPHBhdGggZD0ibTEzLjcxOSAxMy41MDktMS4xOTY0IDAuNjkwNzYiLz4KPHBhdGggZD0ibTEzLjcxOSAxNC4yLTEuMTk2NC0wLjY5MDc2Ii8+CjwvZz4KPC9zdmc+Cgo=");
        }

        ul.ow-wiki li.ow-li-plus {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMm1tIiBoZWlnaHQ9IjJtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMiAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCguNiAwIDAgMSAtNy4wNTMyIC0xMi42NjMpIiBzdHJva2Utd2lkdGg9Ii4xOTM2NSI+CjxwYXRoIGQ9Im0xMi40MjIgMTMuNjYzaDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIuMTkzNjUiLz4KPC9nPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCgwIC42IC0xIDAgMTQuNjYzIC03LjA1MzIpIiBzdHJva2Utd2lkdGg9Ii4xOTM2NSI+CjxwYXRoIGQ9Im0xMi40MjIgMTMuNjYzaDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIuMTkzNjUiLz4KPC9nPgo8L3N2Zz4K");
        }

        ul.ow-wiki li.ow-li-minus {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMm1tIiBoZWlnaHQ9IjJtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMiAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCguNiAwIDAgMSAtNy4wNTMyIC0xMi42NjMpIiBzdHJva2Utd2lkdGg9Ii4xOTM2NSI+CjxwYXRoIGQ9Im0xMi40MjIgMTMuNjYzaDIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIuMTkzNjUiLz4KPC9nPgo8L3N2Zz4K");
            background-position: 0rem 0rem;
            background-size: 1.0rem 1.0rem;
        }

        ul.ow-wiki li.ow-li-check {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMm1tIiBoZWlnaHQ9IjJtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMiAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCguNzUwMSAwIDAgLjc5ODkgLTkuMTA2NSAtOS45MTc4KSI+CjxwYXRoIGQ9Im0xMi42MTcgMTMuNDA1IDAuNTk4NzcgMS4wMjM0IDEuMTIyNi0xLjY5MzIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIuMjU1cHgiLz4KPC9nPgo8L3N2Zz4K");
            background-position: 0rem 0rem;
            background-size: 1.0rem 1.0rem;
        }

        ul.ow-wiki li.ow-li-lt {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMm1tIiBoZWlnaHQ9IjJtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMiAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCguNzMyMTcgMCAwIC42NTA2MyAtOC41ODM5IC04LjAzODkpIj4KPHBhdGggZD0ibTEzLjg2OSAxMy4yODQtMS4zNzU0IDAuNTU2NzIgMS4zNzY5IDAuNjUxMjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIuMTc5NDdweCIvPgo8L2c+Cjwvc3ZnPgo=");
        }

        ul.ow-wiki li.ow-li-gt {
            background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMm1tIiBoZWlnaHQ9IjJtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMiAyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09Im1hdHJpeCgtLjczMjE3IDAgMCAtLjY1MDYzIDEwLjU4NCAxMC4wMzIpIj4KPHBhdGggZD0ibTEzLjg2OSAxMy4yODQtMS4zNzU0IDAuNTU2NzIgMS4zNzY5IDAuNjUxMjkiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIuMTc5NDdweCIvPgo8L2c+Cjwvc3ZnPgo=");
        }


        /* Child list */
		ul.ow-child-list {
		  padding-left: 1rem;
          list-style-type: none;
		}

		ul.ow-child-list ul {
		  margin-left: 15px;
		  padding-left: 10px;
		  border-left: 1px dashed #ddd;
		}

		ul.ow-child-list li {
		  padding-left: 1.5rem;
          background-position: 0.0rem 0.0rem;
          background-size: 1.0rem 1.0rem;
          background-repeat: no-repeat;
          height: 1.8em;
          background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjxzdmcgaWQ9IklDT04iIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojYjBjYmUwO30uY2xzLTEsLmNscy0ye3N0cm9rZTojNjY2NjdlO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6MTVweDt9LmNscy0ye2ZpbGw6IzVmOWNjYjt9PC9zdHlsZT48L2RlZnM+PHRpdGxlLz48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0zOTEsMTU4LjV2MjY1YTI1LDI1LDAsMCwxLTI1LDI1SDE0NmEyNSwyNSwwLDAsMS0yNS0yNVY4OC41YTI1LDI1LDAsMCwxLDI1LTI1SDI5NloiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zOTEsMTU4LjVIMzIxYTI1LDI1LDAsMCwxLTI1LTI1di03MFoiLz48L3N2Zz4=");
		}

        span.ow-child-list-title {
		  font-weight: bold;
        }

        span.ow-child-list-title:before {
		  margin-right: 0px;
		  content: "";
		  height: 1.8em;
		  vertical-align: middle;
		  width: 1.5em;
		  background-repeat: no-repeat;
		  display: inline-block;
		  background-image: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjxzdmcgaWQ9IklDT04iIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxkZWZzPjxzdHlsZT4uY2xzLTF7ZmlsbDojYjBjYmUwO30uY2xzLTEsLmNscy0ye3N0cm9rZTojNjY2NjdlO3N0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1saW5lam9pbjpyb3VuZDtzdHJva2Utd2lkdGg6MTVweDt9LmNscy0ye2ZpbGw6IzVmOWNjYjt9PC9zdHlsZT48L2RlZnM+PHRpdGxlLz48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik0zOTEsMTU4LjV2MjY1YTI1LDI1LDAsMCwxLTI1LDI1SDE0NmEyNSwyNSwwLDAsMS0yNS0yNVY4OC41YTI1LDI1LDAsMCwxLDI1LTI1SDI5NloiLz48cGF0aCBjbGFzcz0iY2xzLTIiIGQ9Ik0zOTEsMTU4LjVIMzIxYTI1LDI1LDAsMCwxLTI1LTI1di03MFoiLz48L3N2Zz4=");
		  background-position: center 0px;
		  background-size: 75% auto;
		}

		/* Attachment link */
		a.ow-link-attach {
		  border-bottom: 1px solid transparent;
		  text-decoration: none;
		  font-style: italic;
          white-space: nowrap;
		}

		a.ow-link-attach:hover {
		  border-color: #eee;
		  color: #000;
		}

		a.ow-link-attach:before {
		  margin-right: 0px;
		  content: "";
		  height: 1.8em;
		  vertical-align: middle;
		  width: 1.5em;
		  background-repeat: no-repeat;
		  display: inline-block;
		  /* file icon by default */
		  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDAiIGhlaWdodD0iNDAwIj48cGF0aCBmaWxsPSIjMkE5NEY0IiBkPSJNMTM1LjYyNiAzNDYuMWMtMjAuMjAxIDAtMzkuMTQ2LTcuODItNTMuMzQ3LTIyLjAyLTE0LjE5OS0xNC4yLTIyLjAyLTMzLjE0Ni0yMi4wMi01My4zNDYgMC0yMC4yMDEgNy44Mi0zOS4xNDYgMjIuMDItNTMuMzQ3TDIyOS40MTQgNzAuMjUzYzExLjI2My0xMS4yNTkgMjYuMDc2LTE3LjAyNyA0MS42ODEtMTYuMjkxIDE0Ljg4My43MTggMjkuMjYyIDcuMjk2IDQwLjQ4OSAxOC41MjNzMTcuODA3IDI1LjYwNSAxOC41MjQgNDAuNDg3Yy43NTQgMTUuNjE5LTUuMDMxIDMwLjQyMi0xNi4yOTMgNDEuNjgybC0xMzguMjE4IDEzOC4yMmMtMTQuNjY2IDE0LjY2My0zOC41MjUgMTQuNjYzLTUzLjE4OSAwLTcuMDg1LTcuMDg2LTEwLjk4Ni0xNi41My0xMC45ODYtMjYuNTk1IDAtMTAuMDY2IDMuOTAxLTE5LjUxMSAxMC45ODctMjYuNTk2bDkzLjYzMS05My42MzdjNC44MzctNC44MzYgMTIuNjgtNC44MzYgMTcuNTE4IDAgNC44MzggNC44MzggNC44MzggMTIuNjgyLjAwMiAxNy41MmwtOTMuNjMzIDkzLjYzN2MtMi40MDUgMi40MDQtMy43MyA1LjYyOC0zLjczIDkuMDc2IDAgMy40NDcgMS4zMjUgNi42NzEgMy43MyA5LjA3NiA1LjAwNSA1LjAwMyAxMy4xNDYgNS4wMDYgMTguMTUyIDBsMTM4LjIxOC0xMzguMjJjNi4zNS02LjM0OSA5LjQ4My0xNC4yOTIgOS4wNjUtMjIuOTY5LS40Mi04LjcxOC00LjQzMy0xNy4yOTktMTEuMjk2LTI0LjE2My0xNC4zMDEtMTQuMzAxLTM0LjEyMi0xNS4yMzgtNDcuMTM1LTIuMjMxTDk5Ljc5OCAyMzQuOTA3Yy05LjUyIDkuNTIxLTE0Ljc2NCAyMi4yNDUtMTQuNzY0IDM1LjgyOCAwIDEzLjU4MiA1LjI0NCAyNi4zMDcgMTQuNzY0IDM1LjgyNiA5LjUyMSA5LjUyMSAyMi4yNDUgMTQuNzY1IDM1LjgyOCAxNC43NjVzMjYuMzA3LTUuMjQ0IDM1LjgyNy0xNC43NjVsMTQ3LjE0MS0xNDcuMTRjNC44MzgtNC44MzggMTIuNjgtNC44MzkgMTcuNTE5IDAgNC44MzggNC44MzggNC44MzggMTIuNjgxIDAgMTcuNTE5TDE4OC45NzIgMzI0LjA4MWMtMTQuMiAxNC4xOTktMzMuMTQ2IDIyLjAxOS01My4zNDYgMjIuMDE5eiIvPjwvc3ZnPg==");
		  background-position: center 0px;
		  background-size: 75% auto;
		}

		a.ow-attach-dir:before {
		  margin-right: 2px;
		  content: "";
		  height: 1.8em;
		  vertical-align: middle;
		  width: 1.5em;
		  background-repeat: no-repeat;
		  display: inline-block;
		  /* folder icon if folder class is specified */
		  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAxMDAgMTAwJz48cGF0aCBmaWxsPSdsaWdodGJsdWUnIGQ9J005Ni40MjksMzcuNXYzOS4yODZjMCwzLjQyMy0xLjIyOCw2LjM2MS0zLjY4NCw4LjgxN2MtMi40NTUsMi40NTUtNS4zOTUsMy42ODMtOC44MTYsMy42ODNIMTYuMDcxIGMtMy40MjMsMC02LjM2Mi0xLjIyOC04LjgxNy0zLjY4M2MtMi40NTYtMi40NTYtMy42ODMtNS4zOTUtMy42ODMtOC44MTdWMjMuMjE0YzAtMy40MjIsMS4yMjgtNi4zNjIsMy42ODMtOC44MTcgYzIuNDU1LTIuNDU2LDUuMzk0LTMuNjgzLDguODE3LTMuNjgzaDE3Ljg1N2MzLjQyMiwwLDYuMzYyLDEuMjI4LDguODE3LDMuNjgzYzIuNDU1LDIuNDU1LDMuNjgzLDUuMzk1LDMuNjgzLDguODE3VjI1aDM3LjUgYzMuNDIyLDAsNi4zNjEsMS4yMjgsOC44MTYsMy42ODNDOTUuMjAxLDMxLjEzOCw5Ni40MjksMzQuMDc4LDk2LjQyOSwzNy41eicgLz48L3N2Zz4K");
		  background-position: center top;
		  background-size: 75% auto;
		}

		/* Attachments list - (:attachlist:) wiki command */
		ul.ow-attach-list {
		  margin-left: 0px;
		  padding-left: 0px;
		}

		.ow-attach-list ul {
		  margin-left: 15px;
		  padding-left: 10px;
		  border-left: 1px dashed #ddd;
		}

		ul.ow-attach-list li {
		  list-style: none;
		  font-weight: normal;
          background-image: none;
          padding-left: 1.0rem;
		}

		.ow-attach-list a.ow-attach-dir {
		  font-weight: bold;
		  font-style: normal;
		  transition: all 0.2s ease;
		}

        span.ow-attach-error {
		  font-style: italic;
          white-space: nowrap;
          color: #cc0033;
        }

        span.ow-attach-error:before {
		  margin-right: 0px;
		  content: "";
		  height: 1.8em;
		  vertical-align: middle;
		  width: 1.5em;
		  background-repeat: no-repeat;
		  display: inline-block;
		  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MDAiIGhlaWdodD0iNDAwIj48cGF0aCBmaWxsPSIjMkE5NEY0IiBkPSJNMTM1LjYyNiAzNDYuMWMtMjAuMjAxIDAtMzkuMTQ2LTcuODItNTMuMzQ3LTIyLjAyLTE0LjE5OS0xNC4yLTIyLjAyLTMzLjE0Ni0yMi4wMi01My4zNDYgMC0yMC4yMDEgNy44Mi0zOS4xNDYgMjIuMDItNTMuMzQ3TDIyOS40MTQgNzAuMjUzYzExLjI2My0xMS4yNTkgMjYuMDc2LTE3LjAyNyA0MS42ODEtMTYuMjkxIDE0Ljg4My43MTggMjkuMjYyIDcuMjk2IDQwLjQ4OSAxOC41MjNzMTcuODA3IDI1LjYwNSAxOC41MjQgNDAuNDg3Yy43NTQgMTUuNjE5LTUuMDMxIDMwLjQyMi0xNi4yOTMgNDEuNjgybC0xMzguMjE4IDEzOC4yMmMtMTQuNjY2IDE0LjY2My0zOC41MjUgMTQuNjYzLTUzLjE4OSAwLTcuMDg1LTcuMDg2LTEwLjk4Ni0xNi41My0xMC45ODYtMjYuNTk1IDAtMTAuMDY2IDMuOTAxLTE5LjUxMSAxMC45ODctMjYuNTk2bDkzLjYzMS05My42MzdjNC44MzctNC44MzYgMTIuNjgtNC44MzYgMTcuNTE4IDAgNC44MzggNC44MzggNC44MzggMTIuNjgyLjAwMiAxNy41MmwtOTMuNjMzIDkzLjYzN2MtMi40MDUgMi40MDQtMy43MyA1LjYyOC0zLjczIDkuMDc2IDAgMy40NDcgMS4zMjUgNi42NzEgMy43MyA5LjA3NiA1LjAwNSA1LjAwMyAxMy4xNDYgNS4wMDYgMTguMTUyIDBsMTM4LjIxOC0xMzguMjJjNi4zNS02LjM0OSA5LjQ4My0xNC4yOTIgOS4wNjUtMjIuOTY5LS40Mi04LjcxOC00LjQzMy0xNy4yOTktMTEuMjk2LTI0LjE2My0xNC4zMDEtMTQuMzAxLTM0LjEyMi0xNS4yMzgtNDcuMTM1LTIuMjMxTDk5Ljc5OCAyMzQuOTA3Yy05LjUyIDkuNTIxLTE0Ljc2NCAyMi4yNDUtMTQuNzY0IDM1LjgyOCAwIDEzLjU4MiA1LjI0NCAyNi4zMDcgMTQuNzY0IDM1LjgyNiA5LjUyMSA5LjUyMSAyMi4yNDUgMTQuNzY1IDM1LjgyOCAxNC43NjVzMjYuMzA3LTUuMjQ0IDM1LjgyNy0xNC43NjVsMTQ3LjE0MS0xNDcuMTRjNC44MzgtNC44MzggMTIuNjgtNC44MzkgMTcuNTE5IDAgNC44MzggNC44MzggNC44MzggMTIuNjgxIDAgMTcuNTE5TDE4OC45NzIgMzI0LjA4MWMtMTQuMiAxNC4xOTktMzMuMTQ2IDIyLjAxOS01My4zNDYgMjIuMDE5eiIvPjwvc3ZnPg==");
		  background-position: center 0px;
		  background-size: 75% auto;
		}
    '''

    return rcssmin.cssmin(css)
