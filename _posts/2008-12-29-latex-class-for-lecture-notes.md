---
title: LaTeX class for lecture notes
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2008/12/latex-class-for-lecture-notes/
categories:
  - Math
  - Software
  - Typography
---
In the [last post][1] I wrote about how to take notes with LaTeX; that post focused on speed, and there were a `sty` file with the macros defined for that purpose. Here I won't speak about speed, but **style**.

 [1]: {% post_url 2008-12-27-how-to-take-lecture-notes-with-latex %}

<!--more-->

To begin, [LaTeX class file for lecture notes][2] you can find the class file I wrote for my notes. Just put it in you LaTeX tree (or in the directory of your document), with the `sty` [file][3], and write a document with the following structure.

 [2]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2008/12/notes.cls
 [3]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2008/12/commons.sty

{% highlight latex %}
\documentclass[OPTIONS]{Notes}

\title{TITLE}
\subject{SUBJECT}
\author{AUTHOR}
\email{EMAIL}
\speaker{SPEAKER}
\date{DD}{MM}{YYYY}
\dateend{DD}{MM}{YYYY}
\place{PLACE}

\begin{document}

\end{document}
{% endhighlight %}

Obviously you have to replace the values, or, when appropriate, delete some line. Note that "author" and "email" are name and e-mail of the notes taker. The options (see the first line) are these:

  * `english` or `italian`: the document's language;
  * `course`, `seminar` or `talk`: a course is a medium-length document structured in sections, subsections and paragraphs; a seminar is a short document without structure or with subsections; a talk is the sheets you take with you when you give a seminar.

The second option defines the style of the document; if you want to tweak some parameters, there are also these fine-tuning options:

  * `headertitle`, `headersection`, `headersubsection` or `headerno`: what to display on the top of the pages;
  * `theoremnosection`, `theoremsection` or `theoremsubsection`: numbering of theorems, definitions, etc.;
  * `cleardoublepage` or `nocleardoublepage`: whether we want empty double pages after a section ending;
  * `oneside` or `twoside`: margins and headers optimized for one-sided or two-sided printing;
  * `onecolumn` or `twocolumn`: how many columns per page.

The class defines also some commands:

  * for `course`, the command `\lecture{duration}{dd}{mm}{yyyy}` which writes on the margin information about the lesson's number, duration and date;
  * for `talk`, the commands `\separator`, which simply draws a horizontal line, and `\tosay{message}` which prints the message inside a box (useful to remember things you don't have to write on the blackboard);
  * `\mymarginpar{message}`, which behaves like a regular `\marginpar` but with a custom style.

Two words on what you get with this class file: the main **difference** is the font (Palatino instead of Computer Modern); the second main difference is the use of small-caps instead of boldface. I have to say I needed these modifications because I was very tired of the standard, omnipresent LaTeX style. Other small notable differences are the centered titles --- because I'm not writing a book --- and the theorem numbers placed before the word "theorem" --- to make easier searching for them. If you want to see an example, download a recent document from my [lecture notes page][4].

 [4]: http://poisson.phc.unipi.it/~maggiolo/index.php/lecture-notes/

Let's give a look on the **packages** this class requires, at least the ones you should use in your everyday documents.

  * [hyperref][5]: many PDF on the web doesn't have hyperlinks, from the table of contents to the sections, to an equation from where they refer to it, etc. With this package you can have automatically all these links and also tweak PDF metadatas.
  * [mathtools][6]: enhancements of the standard AMS-LaTeX packages; the documentation is an inspiring source of tips for beautiful typesetting.
  * [booktabs][7]: standard LaTeX tables look poorer than they should; learn why reading booktabs' documentation.
  * [multirow][8]: tables with cells spanning multiple rows.
  * [fancyhdr][9]: to customize the content of headers and footers.
  * [mparhack][10]: workaround for a bug on LaTeX `\marginpar`.
  * [tikz][11]: it's a high-level drawing language, designed by [Till Tantau][12] (you can remember him for software like latex-beamer); you can see a gallery with examples [here][13].
  * [mathdots][14]: redefines `\dots` and its friends so that they change size when appropriate.
  * [xfrac][15]: to typeset nice inline fractions, as in ½.
  * [faktor][16]: same as before, but without shrinking denominator's and numerator's size; useful for quotients.
  * [cancel][17]: to draw diagonal bars above terms in an equation.

 [5]: http://www.ctan.org/tex-archive/help/Catalogue/entries/hyperref.html
 [6]: http://www.ctan.org/tex-archive/help/Catalogue/entries/mathtools.html
 [7]: http://www.ctan.org/tex-archive/help/Catalogue/entries/booktabs.html
 [8]: http://www.ctan.org/tex-archive/help/Catalogue/entries/multirow.html
 [9]: http://www.ctan.org/tex-archive/help/Catalogue/entries/fancyhdr.html
 [10]: http://www.ctan.org/tex-archive/help/Catalogue/entries/mparhack.html
 [11]: http://pgf.sourceforge.net
 [12]: http://www.itheoi.mu-luebeck.de/en/mitarbeiter/tantau/
 [13]: http://www.texample.net/tikz/examples/
 [14]: http://www.ctan.org/tex-archive/help/Catalogue/entries/mathdots.html
 [15]: http://www.ctan.org/tex-archive/help/Catalogue/entries/xfrac.html
 [16]: http://www.ctan.org/tex-archive/help/Catalogue/entries/faktor.html
 [17]: http://www.ctan.org/tex-archive/help/Catalogue/entries/cancel.html

Please note that my class is not licensed in any way. If you want to use it, you're free to do anything you want with them. Anyway, I will be happy if you just drop [me][18] a line telling me you're using it.

 [18]: http://poisson.phc.unipi.it/~maggiolo/index.php/about-2/

