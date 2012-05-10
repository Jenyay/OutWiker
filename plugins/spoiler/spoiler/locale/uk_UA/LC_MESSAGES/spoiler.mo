��          D      l       �   �  �      #     ,     F  �  M    �     	
  )   
     D
                          Add command (:spoiler:) in wiki parser.

<B>Usage:</B>
<PRE>(:spoiler:)
Text
(:spoilerend:)</PRE>

For nested spoilers use (:spoiler0:), (:spoiler1:)... (:spoiler9:) commands. 

<U>Example:</U>

<PRE>(:spoiler:)
Text
&nbsp;&nbsp;&nbsp;(:spoiler1:)
&nbsp;&nbsp;&nbsp;Nested spoiler
&nbsp;&nbsp;&nbsp;(:spoiler1end:)
(:spoilerend:)</PRE>

<B>Params:</B>
<U>inline</U> - Spoiler will be in inline mode.
<U>expandtext</U> - Link text for the collapsed spoiler. Default: "Expand".
<U>collapsetext</U> - Link text for the expanded spoiler. Default: "Collapse".

<U>Example:</U>

<PRE>(:spoiler expandtext="More..." collapsetext="Less" inline :)
Text
(:spoilerend:)</PRE>
 Collapse Collapse text (:spoiler:) Expand Project-Id-Version: spoiler
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2012-04-25 22:02+0400
PO-Revision-Date: 2012-05-10 20:45+0300
Last-Translator: Jenyay <jenyay.ilin@gmail.com>
Language-Team: jenyay.net <jenyay.ilin@gmail.com>
Language: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Poedit-Language: Ukrainian
X-Poedit-Country: UKRAINE
X-Poedit-SourceCharset: utf-8
 Додає вікі-команду (:spoiler:) для приховування частини тексту на сторінці (вставка спойлерів).

<B>Використання:</B>
<PRE>(:spoiler:)
Текст
(:spoilerend:)</PRE>

Для вкладений спойлерів використовуйте команди (:spoiler0:), (:spoiler1:)... (:spoiler9:). 

<U>Приклад:</U>

<PRE>(:spoiler:)
Текст
&nbsp;&nbsp;&nbsp;(:spoiler1:)
&nbsp;&nbsp;&nbsp;Вкладений спойлер
&nbsp;&nbsp;&nbsp;(:spoiler1end:)
(:spoilerend:)</PRE>

<B>Параметри:</B>
<U>inline</U> - Спойлер буде оформлений у вигляді тексту без виділення блоку.
<U>expandtext</U> - Текст для посилань, який буде показуватись, поки спойлер згорнутий. Значення по замовчуванню: "Розгорнути".
<U>collapsetext</U> - Текст для посилань, який буде показано, поки спойлер розгорнутий. Значення по замовчуванню: "Згорнути".

<U>Приклад:</U>

<PRE>(:spoiler expandtext="Розгорнути" collapsetext="Згорнути" inline:)
Текст
(:spoilerend:)</PRE>
 Згорнути Згорнутий текст (:spoiler:) Розгорнути 