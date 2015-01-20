---
title: 'Using eso-pic to draw SISSA&#039;s letterhead'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2009/12/using-eso-pic-to-draw-sissas-letterhead/
categories:
  - Typography
---
I happily use LaTeX package [letteracdp][1] to write all my letters. There's just one problem: it lacks a way to put a letterhead different from the one encoded in the source file.

 [1]: http://www.math.unipd.it/~mezzetti/Gustavo/Ludic/CDP/

<!--more-->

A simple solution is to use eso-pic to draw the letterhead as a watermark in every page. The code to do this is the following.

{% highlight latex %}
\makeatletter
\AddToShipoutPicture{{ '{%' }}
  \setlength{\@tempdimb}{\oddsidemargin}%
  \addtolength{\@tempdimb}{1in}%
  \setlength{\@tempdimc}{1\paperheight}%
  \addtolength{\@tempdimc}{-1in}%
  \setlength{\unitlength}{1pt}%
  \put(\strip@pt\@tempdimb,\strip@pt\@tempdimc){\parbox{\textwidth}{\centering%
    \raisebox{-18pt}[0pt][20pt]{\includegraphics[scale=.09]{sissa.pdf}}\\%
    \textbf{SCUOLA INTERNAZIONALE SUPERIORE DI STUDI AVANZATI}\\%
    Via Beirut 2--4, 34151 Trieste (Italy) tel: (+39)04037871 - fax: (+39)0403787249%
    }}%
}
\makeatother</pre></blockquote</p>
{% endhighlight %}

Of course this snippet can be used in any situation, not only with letteracdp. You only have to download [Sissa's logo][2] (converted from the SVG obtained [here][3]).

 [2]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2009/12/sissa.pdf
 [3]: http://www.sissa.it/download/index.php?path=logo%2Fnew%2Fvector/

For future reference, here are two example of simple letters in Italian and in English.

* Example of usage of letteracdp in Italian ([sources][4], [PDF][5]).
* Example of usage of letteracdp in English ([sources][6], [PDF][7]).

 [4]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2009/12/lettera_italiano.tex
 [5]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2009/12/lettera_italiano.pdf
 [6]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2009/12/letter_english.tex
 [7]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2009/12/letter_english.pdf
