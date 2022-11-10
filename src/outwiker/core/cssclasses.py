# -*- coding=utf-8 -*-

CSS_ERROR = 'ow-error'
CSS_IMAGE = 'ow-image'
CSS_ATTACH = 'ow-attach'
CSS_ATTACH_FILE = 'ow-attach-file'
CSS_ATTACH_IMAGE = 'ow-attach-image'
CSS_ATTACH_DIR = 'ow-attach-dir'
CSS_ATTACH_LIST = 'ow-attach-list'
CSS_IMAGE = 'ow-image'
CSS_QUOTE = 'ow-quote'


def getDefaultStyles() -> str:
    return '''
		img{border:none}

		/* Attachment link */
		a.ow-attach {
		  border-bottom: 1px solid transparent;
		  text-decoration: none;
		  font-style: italic;
		}

		a.ow-attach:hover {
		  border-color: #eee;
		  color: #000;
		}

		a.ow-attach:before {
		  margin-right: 2px;
		  content: "";
		  height: 20px;
		  vertical-align: middle;
		  width: 20px;
		  background-repeat: no-repeat;
		  display: inline-block;
		  /* file icon by default */
		  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAxMDAgMTAwJz48cGF0aCBmaWxsPSdsaWdodGdyZXknIGQ9J004NS43MTQsNDIuODU3Vjg3LjVjMCwxLjQ4Ny0wLjUyMSwyLjc1Mi0xLjU2MiwzLjc5NGMtMS4wNDIsMS4wNDEtMi4zMDgsMS41NjItMy43OTUsMS41NjJIMTkuNjQzIGMtMS40ODgsMC0yLjc1My0wLjUyMS0zLjc5NC0xLjU2MmMtMS4wNDItMS4wNDItMS41NjItMi4zMDctMS41NjItMy43OTR2LTc1YzAtMS40ODcsMC41MjEtMi43NTIsMS41NjItMy43OTQgYzEuMDQxLTEuMDQxLDIuMzA2LTEuNTYyLDMuNzk0LTEuNTYySDUwVjM3LjVjMCwxLjQ4OCwwLjUyMSwyLjc1MywxLjU2MiwzLjc5NXMyLjMwNywxLjU2MiwzLjc5NSwxLjU2Mkg4NS43MTR6IE04NS41NDYsMzUuNzE0IEg1Ny4xNDNWNy4zMTFjMy4wNSwwLjU1OCw1LjUwNSwxLjc2Nyw3LjM2NiwzLjYyN2wxNy40MSwxNy40MTFDODMuNzgsMzAuMjA5LDg0Ljk4OSwzMi42NjUsODUuNTQ2LDM1LjcxNHonIC8+PC9zdmc+Cg==");
		  background-position: center 2px;
		  background-size: 70% auto;
		}

		a.ow-attach-dir:before {
		  margin-right: 5px;
		  content: "";
		  height: 20px;
		  vertical-align: middle;
		  width: 20px;
		  background-repeat: no-repeat;
		  display: inline-block;
		  /* folder icon if folder class is specified */
		  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAxMDAgMTAwJz48cGF0aCBmaWxsPSdsaWdodGJsdWUnIGQ9J005Ni40MjksMzcuNXYzOS4yODZjMCwzLjQyMy0xLjIyOCw2LjM2MS0zLjY4NCw4LjgxN2MtMi40NTUsMi40NTUtNS4zOTUsMy42ODMtOC44MTYsMy42ODNIMTYuMDcxIGMtMy40MjMsMC02LjM2Mi0xLjIyOC04LjgxNy0zLjY4M2MtMi40NTYtMi40NTYtMy42ODMtNS4zOTUtMy42ODMtOC44MTdWMjMuMjE0YzAtMy40MjIsMS4yMjgtNi4zNjIsMy42ODMtOC44MTcgYzIuNDU1LTIuNDU2LDUuMzk0LTMuNjgzLDguODE3LTMuNjgzaDE3Ljg1N2MzLjQyMiwwLDYuMzYyLDEuMjI4LDguODE3LDMuNjgzYzIuNDU1LDIuNDU1LDMuNjgzLDUuMzk1LDMuNjgzLDguODE3VjI1aDM3LjUgYzMuNDIyLDAsNi4zNjEsMS4yMjgsOC44MTYsMy42ODNDOTUuMjAxLDMxLjEzOCw5Ni40MjksMzQuMDc4LDk2LjQyOSwzNy41eicgLz48L3N2Zz4K");
		  background-position: center top;
		  background-size: 75% auto;
		}

		/* Attachments list - (:attachlist:) wiki command */
		.ow-attach-list ul {
		  margin-left: 15px;
		  padding-left: 10px;
		  border-left: 1px dashed #ddd;
		}

		.ow-attach-list li {
		  list-style: none;
		  font-weight: normal;
		}

		.ow-attach-list a.ow-attach-dir {
		  font-weight: bold;
		  font-style: normal;
		  transition: all 0.2s ease;
		}
    '''
