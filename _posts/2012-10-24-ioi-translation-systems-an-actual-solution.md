---
title: 'IOI translation systems: an actual solution'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2012/10/ioi-translation-systems-an-actual-solution/
categories:
  - Typography
---
In the [second post][1] we saw the workflow we had in mind. Here I will show you the solution we had found in order to implement the workflow, and discuss why other possible solutions could not be implemented.

 [1]: {% post_url 2012-10-15-ioi-translation-systems-an-ideal-workflow %}

<!--more-->

A real world software implementing the workflow is composed of **three parts**.

1. A way to allow admins to insert the statements, with the appropriate tagging of translatable and not translatable sections, and to update them to new versions, checking the correspondence between old and new translatable strings.
1. The actual translation interface, offering strings to translate and showing diffs in a string if there was an update.
1. The rendering of the final document as a PDF.

The first two parts are relatively easy with respect to the third, in the sense that they are not hard to solve just throwing code at them. The third is complicated by the lack of a single Unicode font that covers all languages (apart maybe [GNU Unifont][2], which is a nice font to have as a fallback, but not for the whole text). Moreover, we have the following.

 [2]: http://unifoundry.com/unifont.html

**Problem #1**: languages that share the same Unicode range can use slightly different shapes for the same Unicode glyph. Example: a font which is suitable for Arabic looks funny if used to write in Farsi.

## Third part

From the point of view of the quality of the output, using some **TeX engine** as a backend would be the best option. In particular, XeTeX, which easily supports system fonts and Unicode input files seems to be a nice option. But, a single translated statement often uses several Unicode ranges: the range of the main language, Latin alphabet for code parts, mathematics, and possibly other glyphs.

**Problem #2**: very few pieces of software do automatic font substitution, and XeTeX is not among them. Basically, the only software doing that is a browser.

Indeed, we cannot hope to encode for every character a font that we would like to use, it would be <emph>very</emph> unpractical and even more tedious, but it would be the only way to use XeTeX. So we need a way to use a **browser** to render the translated statements. The only software doing this programmatically is [wkhtmltopdf][3], which uses WebKit as backend. This is not bad, as we will use HTML tags for simple formatting (which are mostly common knowledge), and we can add a custom, language-dependant, CSS to hint to use the correct font (as in the Farsi vs. Arabic problem). But there are some problems with printing HTML pages.

 [3]: http://code.google.com/p/wkhtmltopdf/

**Problem #3**: WebKit [does not implement][4] all page-break-* CSS properties that would allow, for example, to avoid a page-break after a header.

 [4]: https://bugs.webkit.org/buglist.cgi?quicksearch=page-break

The partial solution we implemented is to use the only functional way to avoid page breaks, namely the page-break-inside, to wrap together in a non-breakable div a header and a (short) following paragraph. This cannot be done for long paragraphs, as pages could be almost empty, but fixes the problem most of the time. When it does not, a careful translator can add newlines in order to have nice page breaks.

## First and second part

Probably, the best solution would be to implement a custom software to handle (even separately) these two parts. Time restrictions, and the will not to reinvent the wheel, made us look for existing software instead. The one more similar to what we had in mind is [MediaWiki][5], with the [Translate extension][6].

 [5]: http://www.mediawiki.org/wiki/MediaWiki
 [6]: http://www.mediawiki.org/wiki/Extension:Translate

It has **several advantages**: firstly, it is a close friend of HTML, so it interoperates well with the rendering interface (we can use HTML tags directly in the strings and they will render correctly both in the MediaWiki interface and in the final PDF); it has a very good changelog / revision history mechanism, both for the admin interface and for the translators; the translators interface is visually exactly what we wanted in the first place. But, there are also things we do not like.

**Problem #4**: MediaWiki have a very basic permission system, especially for translating pages; it insists on rendering even vector images at a low resolution (but we need the vector one in the PDF); it offers limited interface to programmatically add users and pages; it does not handle automatically left-to-right text inside a right-to-left paragraph. Finally, the translate extension is **slow**.

These problems can be solved in a not-so-nice way by hacking into MediaWiki code, which to me is a reasonable solution, since the features of MediaWiki that we need to use are very limited and therefore it is difficult to break something. The slowness of the extension in particular is mainly due to the fact that every time a translator open a string, it loads a list of "suggestions", which means that it compute the Levenshtein distance between that string and all the other strings already translated. This becomes very soon impossible to handle and it was the cause of the problems we had in the first translation day, before we realized what was happening.

Probably, with more time and more resources, writing an ad hoc solution to be used instead of MediaWiki would be worth the trouble. Nonetheless, if I had to choose what to improve magically, it would be the rendering part (both in quality of the output and in bug-proofness), but it is definitely very hard. I intend to **release** a polished version of the code soon, but up to now this post concludes the series on translation systems. Stay tuned!

<!-- DO NOT EDIT BELOW THIS LINE -->
* * *

### Part of this series

1. [IOI translation systems: a survey of possible approaches][1000]
1. [IOI translation systems: an ideal workflow][1001]
1. [IOI translation systems: an actual solution][1002]

 [1000]: {% post_url 2012-10-09-ioi-translation-systems-a-survey-of-possible-approaches %}
 [1001]: {% post_url 2012-10-15-ioi-translation-systems-an-ideal-workflow %}
 [1002]: {% post_url 2012-10-24-ioi-translation-systems-an-actual-solution %}


### See also

1. [IOI 2012 &mdash; my experience][2000]

 [2000]: {% post_url 2012-10-01-ioi-2012-my-experience %}
