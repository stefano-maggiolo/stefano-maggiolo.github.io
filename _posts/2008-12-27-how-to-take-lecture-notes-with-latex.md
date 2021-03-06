---
title: How to take lecture notes with LaTeX
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2008/12/how-to-take-lecture-notes-with-latex/
categories:
  - Math
  - Software
  - Typography
---
Since it is a frequently asked question, I will explain here how I manage to take lecture notes with LaTeX. It's not that hard, once you have the right tools.

<!--more-->

**Ingredients:**

  * a working laptop, possibly with 2+ hours of battery life (mine haven't got anymore, sigh);
  * a clever and rich Unicode-based keyboard layout;
  * a font with extended Unicode support;
  * an editor with snippets;
  * some LaTeX macros (less important than you think);
  * optionally some utilities.

If someone doesn't know it, **[Unicode][1]** is a powerful character encoding standard, designed to be universal: it codifies virtually all glyphs ever created by humans ([except][2] Klingon, maybe). In particular there are equivalents for many LaTeX macros --- for example, `\forall` is Unicode character `U2200`. To find math glyphs, there's a list [here][3]; alternatively there is the useful Gnome program [Gucharmap][4] [[^1]].

Selected your favorite characters, you have to find a way to type them with some combination of keys, that is, a custom **keyboard layout**. Under Linux, the right way to do this is to create a `symbol` file for `XKB`. This procedure is neither easy nor well documented, so probably my solution is far from being correct. Anyway you should be able to download [the layout][6], putting it at `/usr/share/X11/xkb/symbols/` and enabling it with `setxkbmap us_math`. If you're lucky, you could enable it also via Gnome keyboard properties [[^2]]. This layout works for a Macbook and uses eight levels for every key, depending on Shift and the two Apple keys. In particular there are these letters.

| ⇧ | Left ⌘ | Right ⌘ | Alphabet | Typeface      | Case       |
| - | ------ | ------- | -------- | ------------- | ---------- |
|   |        |         | Latin    | Roman         | Lower-case |
| X |        |         | Latin    | Roman         | Upper-case |
|   | X      |         | Greek    | Roman         | Lower-case |
| X | X      |         | Greek    | Roman         | Upper-case |
|   |        | X       | Latin    | Double-struck | Upper-case |
| X |        | X       | Latin    | Calligraphic  | Upper-case |
|   | X      | X       | Latin    | Fraktur       | Lower-case |
| X | X      | X       | Latin    | Fraktur       | Upper-case |

Up to now you can type strange mathematical Unicode characters, but maybe you can't see them because the **font** you use does not have the corresponding glyphs. On a recent Gnome box, Pango (Gnome's text rendering library) should let you see a glyph if at least one of the fonts installed defines it. Usually the most comprehensive font is [DejaVu][8], the extension of the omnipresent Bitstream Vera.

The next step is to tell LaTeX that we want to write our document with Unicode characters and we want them translated to macros. To do this we had to use these lines.

{% highlight latex %}
\usepackage[utf8x]{inputenc}
\SetUnicodeOption{mathletters}
\SetUnicodeOption{autogenerated}
{% endhighlight %}

LaTeX manages Unicode in a very simple way: it has a big table which defines how to translate Unicode characters to LaTeX macros. These table is stored in a bunch of files in the `/usr/share/texmf-texlive/tex/latex/ucs/data/` directory (or an equivalent one), once you have installed the package `latex-ucs`. The bad thing is that, as far as I know, this package is unmaintained since 2004. I've inserted at least the characters used in the layout, and you can download the updated files [here][9] and put it in your local LaTeX tree.

Okay. We can write most LaTeX macros with a single characters. You only have to get used to the new keys, I hope they're arranged in a rational way. In any case, there are some constructions not corresponding to characters. Fractions, matrices and environments are the most tedious; let's get rid of them.

One way to do this is by **snippets**. Usually snippets work in this way: you type some key combinations and the editor converts the keys you typed to the construct you want, and adds some facilities to speed up the whole thing. For example, [gedit][10] with [LaTeXPlugin][11] allows you to press `Alt+o` to start an environment, and you have to type only once the environment title. Moreover, gedit let you write your own snippets. Another LaTeX-friendly editor is Emacs with AUCTeX.

As for fractions and matrices, I prefer using **LaTeX macros** instead of snippets. The most useful macros I use are the `\[p][s][frac|mat]`: fraction or matrices, with parenthesis if there is the "p", small if there is the "s" (small means suitable for in-line math). Analysts may want to have macros for (partial) derivatives; and remember that to write differentials you have to write `\mathrm{d}t`, not simply `dt`! The macros file I use is [here][12] (use it with `\usepackage{Commons}`).

This is more or less what you need to write notes with LaTeX. In addition, I want to suggest some **utilities**. To write commutative diagrams, I use [Commu][13]. To manage the bibliographies, [Referencer][14] --- but I don't use it during lectures. Instead, I often want to see what I wrote, so I need an automated compilation utility. I used for a long time `make` with a custom makefile, but now there is [Rubber][15], which does everything (and more) without the need for a makefile. For example, if you want to compile all documents in a directory, just type `rubber --pdf *.tex`.

To conclude, two words on the actual act of write notes, if you want to begin. Consider that writing on a keyboard is much more distracting than writing with a pen, in particular at the beginning. The latter is a natural act, the former is not, since you have to take care of additional structure, and you cannot "just copy the blackboard". At the end of the hour, I have almost every time a compiling document, but there are many spelling errors and during the lessons I often leave equations in-lined, so after them I have to put on `displaymath` the long ones and split them up, if necessary. In the resulting document, the potential lack of structure (chapters, sections, definitions, and so on) is much more evident than for handwritten notes; anyway this usually depends on the style of the speaker and the tone of the lecture (an informal review tends to have less structure than a formal one).

To sum up, I list in a single place (here) the downloads linked throughout the article:

  * the keyboard [layout][6] for a Macbook;
  * the updated translation [table][9] for `latex-ucs`;
  * the [file][12] with the LaTeX macros.

[^1]: At the bottom of the page you can find links to similar programs for Windows and Mac Os X.
[^2]: To change Mac Os X layout there is <a href="http://scripts.sil.org/ukelele">Ukulele</a>. I know there are similar softwares also for Windows.

 [1]: http://www.unicode.org
 [2]: http://en.wikipedia.org/wiki/Klingon_writing_systems#KLI_pIqaD
 [3]: http://www.unicode.org/charts/symbols.html
 [4]: http://live.gnome.org/Gucharmap
 [6]: /files/us_math.gz
 [8]: http://dejavu.sourceforge.net/
 [9]: /files/data.zip
 [10]: http://projects.gnome.org/gedit/
 [11]: http://live.gnome.org/Gedit/LaTeXPlugin
 [12]: /files/commons.sty
 [13]: {% post_url 2008-12-14-commu %}
 [14]: http://icculus.org/referencer/
 [15]: http://www.pps.jussieu.fr/~beffara/soft/rubber/

<!-- DO NOT EDIT BELOW THIS LINE -->
* * *

### See also

1. [LaTeX class for lecture notes][2000]
1. [Suboptimal LaTeX #1: intro][2001]
1. [Suboptimal LaTeX #2: spacing][2002]
1. [Suboptimal LaTeX #3: mathematical environments][2003]
1. [Suboptimal LaTeX #4: mathematics][2004]
1. [Suboptimal LaTeX #5: miscellanea][2005]

 [2000]: {% post_url 2008-12-29-latex-class-for-lecture-notes %}
 [2001]: {% post_url 2014-02-17-suboptimal-latex-1-intro %}
 [2002]: {% post_url 2014-02-24-suboptimal-latex-2-spacing %}
 [2003]: {% post_url 2014-03-03-suboptimal-latex-3-mathematical-environments %}
 [2004]: {% post_url 2014-03-10-suboptimal-latex-4-mathematics %}
 [2005]: {% post_url 2014-05-25-suboptimal-latex-5-miscellanea %}
