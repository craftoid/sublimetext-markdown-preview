Sample Markdown Cheat Sheet
=========================== 

This is a sample markdown file to help you write Markdown quickly :)

If you use the fabulous [Sublime Text 2 editor][ST2] along with the [Markdown Preview plugin][MarkdownPreview], open your ST2 Palette with `CMD+P` then choose `Markdown Preview in browser` to see the result in your browser.

## Text basics
this is *italic* and this is **bold** .  another _italic_ and another __bold__

this is `important` text. and percentage signs : % and `%`

This is a paragraph with a footnote (builtin parser only). [^note-id] 

Insert `[ toc ]` without spaces to generate a table of contents (builtin parser only).

## Indentation
> Here is some indented text
>> even more indented

## Titles
# Big title (h1)
## Middle title (h2)
### Smaller title (h3)
#### and so on (hX)
##### and so on (hX)
###### and so on (hX)

## Example lists (1)

 - bullets can be `-`, `+`, or `*`
 - bullet list 1
 - bullet list 2
    - sub item 1
    - sub item 2

        with indented text inside

 - bullet list 3
 + bullet list 4
 * bullet list 5

## Links

This is an [example inline link](http://lmgtfy.com/) and [another one with a title](http://lmgtfy.com/ "Hello, world").

Links can also be reference based : [reference 1][ref1] or [reference 2 with title][ref2].

References are usually placed at the bottom of the document

## Images

A sample image :

![revolunet logo](http://www.revolunet.com/static/parisjs8/img/logo-revolunet-carre.jpg "revolunet logo")

As links, images can also use references instead of inline links :

![revolunet logo][revolunet-logo]


## Code

It's quite easy to show code in markdown files.

Backticks can be used to `highlight` some words.

Also, any indented block is considered a code block.

    <script>
        document.location = 'http://lmgtfy.com/?q=markdown+cheat+sheet';
    </script>

## GitHub Flavored Markdown

If you use the Github parser, you can use some of [Github Flavored Markdown][gfm] syntax :

 * User/Project@SHA: revolunet/sublimetext-markdown-preview@7da61badeda468b5019869d11000307e07e07401
 * User/Project#Issue: revolunet/sublimetext-markdown-preview#1
 * User : @revolunet

Some Python code :

```python
import random

class CardGame(object):
    """ a sample python class """
    NB_CARDS = 32
    def __init__(self, cards=5):
        self.cards = random.sample(range(self.NB_CARDS), 5)
        print 'ready to play'
```

Some Javascript code :

```js
var config = {
    duration: 5,
    comment: 'WTF'
}
// callbacks beauty un action
async_call('/path/to/api', function(json) {
    another_call(json, function(result2) {
        another_another_call(result2, function(result3) {
            another_another_another_call(result3, function(result4) {
                alert('And if all went well, i got my result :)');
            });
        });
    });
})
```

The Github Markdown also brings some [nice Emoji support][emoji] : :+1: :heart: :beer:

[^note-id]: This is the text of the note. 


## **Python Markdown** Extensions

The **Python Markdown** parser provides support for several extensions.

### Extra Extensions

* [Abbreviations][]
* [Attribute Lists][]
* [Definition Lists][]
* [Fenced Code Blocks][]
* [Footnotes][]
* [Tables][]
* [Smart Strong][]

[Abbreviations]: http://pythonhosted.org/Markdown/extensions/abbreviations.html
[Attribute Lists]: http://pythonhosted.org/Markdown/extensions/attr_list.html
[Definition Lists]: http://pythonhosted.org/Markdown/extensions/definition_lists.html
[Fenced Code Blocks]: http://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html
[Footnotes]: http://pythonhosted.org/Markdown/extensions/footnotes.html
[Tables]: http://pythonhosted.org/Markdown/extensions/tables.html
[Smart Strong]: http://pythonhosted.org/Markdown/extensions/smart_strong.html


By default all extra extensions are enabled.
You can enable **all** extra extensions at once using the `extra` keyword.

    extensions: [ 'extra' ]


### Other Extensions

There are also some extensions that are not included in Markdown Extra
but come in the standard Python-Markdown library.

* [CodeHilite][]
* [HTML Tidy][]
* [HeaderId][]
* [Meta-Data][]
* [New Line to Break][]
* [RSS][]
* [Sane Lists][]
* [Table of Contents][]
* [WikiLinks][]

[CodeHilite]:  http://pythonhosted.org/Markdown/extensions/code_hilite.html
[HTML Tidy]:  http://pythonhosted.org/Markdown/extensions/html_tidy.html
[HeaderId]:  http://pythonhosted.org/Markdown/extensions/header_id.html
[Meta-Data]:  http://pythonhosted.org/Markdown/extensions/meta_data.html
[New Line to Break]:  http://pythonhosted.org/Markdown/extensions/nl2br.html
[RSS]:  http://pythonhosted.org/Markdown/extensions/rss.html
[Sane Lists]:  http://pythonhosted.org/Markdown/extensions/sane_lists.html
[Table of Contents]:  http://pythonhosted.org/Markdown/extensions/toc.html
[WikiLinks]:  http://pythonhosted.org/Markdown/extensions/wikilinks.html


## **Markdown2** Extensions

The **Markdown2** parser also provides support for extensions, known as [Extras][].   
You can configure the list of extras you want to use inside the package settings.


## Extra Extensions

The default extras are:

* [Footnotes][Footnotes Extra]
* Table of Contents
* [Fenced CodeBlocks][]
* [Cuddled Lists][]

[Footnotes Extra]:      https://github.com/trentm/python-markdown2/wiki/footnotes
[Fenced CodeBlocks]:    https://github.com/trentm/python-markdown2/wiki/fenced-code-blocks
[Cuddled Lists]:        https://github.com/trentm/python-markdown2/wiki/cuddled-lists


You can enable **all** default extras at once using the `extra` keyword.

    extensions: [ 'extra' ]

If you want all the default extras plus the 'wiki-table' extra,
your settings would look like this:

    {
        ...
        parser: 'markdown2',
        extensions: ['extra', 'wiki-table'],
        ...
    }


## Other Extras

For a complete list of extras please checkout the [Extras Wiki Page][Extras].

[Extras]:   https://github.com/trentm/python-markdown2/wiki/Extras


## Examples


### Tables

The `tables` extension of the *Python Markdown* parser is activated by default,
but is currently not available in *Markdown2*.

The syntax was adopted from the [php markdown project](http://michelf.ca/projects/php-markdown/extra/#table),
and is also used in github flavoured markdown.

| Year | Temperature (low) | Temperature (high) |
| ---- | ----------------- | -------------------|
| 1900 |               -10 |                 25 |
| 1910 |               -15 |                 30 |
| 1920 |               -10 |                 32 |


### Wiki Tables

If you are using *Markdown2* with the `wiki-tables` extra activated you should see a table below:

|| *Year* || *Temperature (low)* || *Temperature (high)* ||
||   1900 ||                 -10 ||                   25 ||
||   1910 ||                 -15 ||                   30 ||
||   1920 ||                 -10 ||                   32 ||


## About

This plugin and this sample file is proudly brought to you by the [revolunet team][revolunet]

 [ref1]: http://revolunet.com
 [ref2]: http://revolunet.com "rich web apps"
 [MarkdownREF]: http://daringfireball.net/projects/markdown/basics
 [MarkdownPreview]: https://github.com/revolunet/sublimetext-markdown-preview
 [ST2]: http://sublimetext.com
 [revolunet]: http://revolunet.com
 [revolunet-logo]: http://www.revolunet.com/static/parisjs8/img/logo-revolunet-carre.jpg "revolunet logo"
 [gfm]: http://github.github.com/github-flavored-markdown/
 [emoji]: http://www.emoji-cheat-sheet.com/


