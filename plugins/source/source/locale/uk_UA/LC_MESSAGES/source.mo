��          L      |       �   l  �           3     E     `  �  p  D    A   U  =   �  *   �                                               Add command (:source:) in wiki parser. This command highlight your source code.

<B>Usage:</B>:
(:source params... :)
source code
(:sourceend:)

<B>Params:</B>
<I>lang</I> - programming language
<I>tabwidth</I> - tab size

<B>Example:</B>
<PRE>(:source lang="python" tabwidth=4:)
import os

if __name__ == "__main__":
    print "Hello World!"
(:sourceend:)
</PRE>
 Default Programming Language Default Tab Width Source Code (:source ...:) Source [Plugin] Project-Id-Version: source
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2011-11-13 20:56+0400
PO-Revision-Date: 2012-05-10 20:42+0300
Last-Translator: Jenyay <jenyay.ilin@gmail.com>
Language-Team: jenyay.net <jenyay.ilin@gmail.com>
Language: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Poedit-Language: Ukrainian
X-Poedit-Country: UKRAINE
X-Poedit-SourceCharset: utf-8
 Розширення додає вікі-команду (:source:) для розфарбовування тексту програми на різних мовах програмування.

<B>Використання:</B>:
(:source параметри... :)
початковий код
(:sourceend:)

<B>Параметри:</B>
<I>lang</I> - мова програмування
<I>tabwidth</I> - розмір табуляції

<B>Приклад:</B>
<PRE>(:source lang="python" tabwidth=4:)
import os

if __name__ == "__main__":
    print "Hello World!"
(:sourceend:)
</PRE>
 Мова програмування по замовчуванню Розмір табуляції по замовчуванню Текст програми (:source ...:) Source [Розширення] 