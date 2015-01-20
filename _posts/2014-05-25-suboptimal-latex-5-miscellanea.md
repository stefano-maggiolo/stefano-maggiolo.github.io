---
title: 'Suboptimal LaTeX #5: miscellanea'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2014/05/suboptimal-latex-5-miscellanea/
categories:
  - Typography
---
This post concludes the short series on LaTeX; we will see some other suggestion that did not fit in the other posts on [generic mistakes and suggestions][1], [spacing][2], [math environments][3] and [mathematics][4].

 [1]: {% post_url 2014-02-17-suboptimal-latex-1-intro %}
 [2]: {% post_url 2014-02-24-suboptimal-latex-2-spacing %}
 [3]: {% post_url 2014-03-03-suboptimal-latex-3-mathematical-environments %}
 [4]: {% post_url 2014-03-10-suboptimal-latex-4-mathematics %}

<!--more-->

The source with example from this post is in a [writeLaTeX][5].

 [5]: https://www.writelatex.com/read/nxycyqqcbyrd

### Use what LaTeX gives you (part 2)

Even though the LaTeX-savyness of a person reading a post like this must be higher than normal, I'm still pretty sure that there is at least someone that does not know that there is no need to design a **title page** by yourself: all decent classes handle the command `\maketitle`, which takes the information from `\title`, `\author` and `\date`. Oh, and for the last one, you can use `\today`. Most classes also have an `\abstract` macro.

Another surprising hole in the LaTeX knowledge of some author is **defining new macros** with `\newcommand`: they are probably old TeX users, and therefore use `\def`. The main advantage of `\newcommand` is that it gives an error when the new macro's name already exists, instead of silently overwriting it. Even if you do not use the existing macro, some other package might be relying on it, and weird errors may arise. If instead you are sure that there are no bad interactions, you can force the overwrite using `\renewcommand`.

### Labels and refs

{% include figure.html width=150 float='right' url='/images/miscellanea_eqref.png' caption='(ref) and eqref' %}

It might comes as a surprise, but I've also witnessed (fortunately, just two) authors not knowing about **automatic references** with `\label` and `\ref`. Fixing their articles has been... interesting. Much more common is not knowing about `\eqref` for **citing equations**: writing the parentheses by yourself achieve a similar looking result, but using a semantic command can be quite useful in the typesetting phase. Speaking of `\ref` and `\eqref`, it is essential to use a **non-breaking space** before them, to avoid having the number as the first character of a new line. To do so, just change the space with a tilde like in this example:

{% highlight latex %}
... as said in figure~\ref{fig:x}.
{% endhighlight %}

Another frequent problem is to use the **same label twice**: keep an eye for ``LaTeX Warning: Label `x' multiply defined`` errors in the LaTeX logs. To mitigate the possibility of defining multiple labels, it is common to prepend the type to all labels names, for example `sec:cats` and `fig:cats` for a section and a figure about cats, instead of just `cats`... for both.

Many authors also do not know that LaTeX is particularly tolerant with respect to a **wrong position of the label** command! For example, a snippet like the following most probably does not do what the author wanted.

{% highlight latex %}
\begin{figure}\label{cat_picture}
\includegraphics[width=\textwidth]{cat_picture.jpg}
\caption{This is a picture of a cat.}
\end{figure}
{% endhighlight %}

Did you spot the problem? The numbering of the picture is given by the caption, not by the figure environment. Hence the label will not refer to the number of the figure, because it wasn't defined yet! Instead, it will refer to the number of a previous element (like a section). You would assume that LaTeX gives you at least a warning for this suspect arrangement, but you'd be wrong. It is a good habit to write the label at the last possible time, even when not strictly necessary, in order to avoid these errors.

### Theorem environments

If you need to use **theorems or similar environments**, the short story is to use the [amsthm][6] package. It allows you to define in one simple line the environment you need in your paper, for example:

 [6]: ftp://ftp.ams.org/ams/doc/amscls/amsthdoc.pdf

{% highlight latex %}
\newtheorem{thm}{Theorem}
{% endhighlight %}

for a Theorem environment that you can use with `\begin{thm}`. Remember that there are **three predefined styles** of such environments, one well suited for statements to be proved (theorem, lemmas, etc.), one for definitions, examples, etc., and the last for additional notes and remarks. For example, this is a good preamble:

{% highlight latex %}
\theoremstyle{plain}
\newtheorem{thm}{Theorem}
\newtheorem{lem}{Lemma}

\theoremstyle{definition}
\newtheorem{defn}{Definition}
\newtheorem{exmp}{Example}

\theoremstyle{remark}
\newtheorem{rem}{Remark}
\newtheorem{note}{Note}
{% endhighlight %}

{% include figure.html width=150 float='right' url='/images/miscellanea_theorems.png' caption='Theorems with amsthm' %}

It also provides many other configurations, like whether to show the numbering and when to reset it.

Finally, it has an embedded **proof environment**, and a command `\qedhere` to help LaTeX drawing the q.e.d. symbol at the correct place: indeed, if you finish your proof with a displayed equation, LaTeX by default places the symbol on the next line.
