---
title: 'Suboptimal LaTeX #4: mathematics'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2014/03/suboptimal-latex-4-mathematics/
categories:
  - Typography
---
In the previous episodes: [generic mistakes and suggestions][1], and how to fix the [spacing][2] and [math environments][3] in your papers. Continuing along these lines, in this post we will see some common mistakes done when writing mathematics.

 [1]: {% post_url 2014-02-17-suboptimal-latex-1-intro %}
 [2]: {% post_url 2014-02-24-suboptimal-latex-2-spacing %}
 [3]: {% post_url 2014-03-03-suboptimal-latex-3-mathematical-environments %}

<!--more-->

As for the previous episodes, the source for all figures in this post is in a [writeLaTeX][4].

 [4]: https://www.writelatex.com/read/tpdkbvjtkgdr

### If you learn one thing from all of this, let it be this

Every time I see a paper containing this mistake I cry a little bit: it is probably one of the most unprofessional errors that writers of scientific content with LaTeX can do. What is it? It is writing multi-letter symbols and even --- please world forgive them --- entire words in math mode without any escaping. It is simply horrible.

{% include figure.html width=150 float='right' url='/images/mathematics_text.png' caption='Text in math mode' %}

What happens is that whenever you write letters as they are, LaTeX thinks that each letter is a symbol on its own. "`This is bad`" in the figure is rendered as if each letter was a symbol and you were multiplying all of them together (of course, spaces disappear). I have seen this error in many situations, such as (from the less ugly to the ugliest):

  * multi-letters symbols like the matrix spaces `SL`, `SO`;
  * functions whose name is an abbreviation of a word, like `det` or `perm`;
  * entire words;
  * or even sentences, like in `\{x \mid x is odd\}`.

In the case of multi-letters operators and functions (and, if you want, single-letter operators), you need to treat the letters as a single mathematical unit, with the spacing around them determined by their role. So for operators, you must use `\DeclareMathOperator`; functions are a bit blurred: I use `\DeclareMathOperator` too, but also `\mathrm` is acceptable.

In the other cases, you are inserting some text in mathematical mode; the correct way of doing that is using `\text` (available in the `amsmath` package), which instruct LaTeX to move temporarily back to text mode. Using `\mathrm` is wrong because it just changes the shape of the letter, not their semantic (for example, spaces are ignored). Also, `\text` draws the letters with the shape of the surrounding environment: if you are in a theorem, written in italic, then `\text` will write in italic too. And finally, it respect font sizes if you use it, say, within an exponent.

### When to use `\mathrm`, and the myth of LaTeX taking care of everything

Apart from the situation presented above (multi-letter function names), there is at least another important case where you should use `\mathrm`: in the infamous "dx" at the end of an integral, the "d" should be upright... ok, maybe this is just my opinion, but it should!

{% include figure.html width=150 float='right' url='/images/mathematics_dx.png' caption='Integrals and dx' %}

Less debatable is the fact that LaTeX does not know that your "dx" has a different meaning in the integral than the function to integrate, and thus should be properly highlighted by leaving some space before it. I use the smallest standard space available, `\,`.

More in general, a lot of people support the myth that LaTeX knows better and typesets formulas in the best possible way. This is often true, with one big exception: when you, as a human, have more information about the formula than LaTeX. In that case, you should feel free to slightly tweak the formula. The most important thing to remember is to be consistent; in particular, it helps to use only the standard spacing macros (`\!`, `\,`, `\;`, `\quad`, `\qquad`).

The same applies to bracket sizing: leaving the decision to LaTeX, by using only `\left(` and `\right)`, is certainly better than using only `(` and `)`; but sometimes it is even better to decide for yourself. To do so, use `\<size>l(` and `\<size>r)`, where size can be `big`, `Big`, `bigg`, and `Bigg` --- and do not forget the `l` and `r` to specify if you are opening or closing the bracket! The same is possible for all other parenthesis types, including `\langle` and `\rangle`, that are almost always what you want instead of `<` and `>`.

### Do you know about `\allowdisplaybreaks`?

Having a single equation going on for pages and pages is probably not the most compelling way of writing a paper... but sometimes it is necessary. By default, LaTeX does not break a page within a mathematical environment, so how do you avoid going over the page? Simple, you just break the environment in two!

Simple and wrong, because then you have to change your equation if the text before it gets longer or shorter (but that would be fine if you do it in the [typesetting phase][1]), but also because the alignment gets lost. If all the lines in the first part are very long and all those in the second part are short, the second part will be more or less center aligned, instead of left aligned. And so the reader loses the visual cue hinting that all lines were part of a single group.

The correct way is instead using `\allowdisplaybreaks`, which does what it says: allows LaTeX to break pages within a mathematical environment. You can use it just after the `\begin{environment}` to apply it only to that display. Moreover, if you end a line with `\\*` instead of `\\`, LaTeX won't break after that line, which is very useful when you have a collection of equations with multiple lines.

### Use what LaTeX gives you

A lot of people just use `...` when `\dots` is visually and semantically better. Most don't know about `\cdots` which is even better than `\dots` within a chain of additions, for example. I have very rarely seen `\overbrace` and `\underbrace` in the wild, and the same goes for `\xrightarrow`, to draw arrows with text on top. Nobody uses the [`cancel`][5] package to show that two terms were the opposite of each other. [`sfrac`][6] is almost unheard of, so instead of having beautiful diagonal fractions inside the text, we have either horrible `1/2` or, even worse, huge gaps between lines.

 [5]: http://www.ctan.org/pkg/cancel
 [6]: http://www.ctan.org/pkg/xfrac

Even without resorting to obscure packages, that often causes problems when sending out your sources, LaTeX mathematics need not to be dull! You just need to know what [symbols, accents, decorations][7], [packages][8] you can use.

 [7]: http://www.tex.ac.uk/tex-archive/info/symbols/comprehensive/symbols-a4.pdf
 [8]: {% post_url 2008-12-29-latex-class-for-lecture-notes %}

<!-- DO NOT EDIT BELOW THIS LINE -->
* * *

### Part of this series

1. [Suboptimal LaTeX #1: intro][1000]
1. [Suboptimal LaTeX #2: spacing][1001]
1. [Suboptimal LaTeX #3: mathematical environments][1002]
1. [Suboptimal LaTeX #4: mathematics][1003]
1. [Suboptimal LaTeX #5: miscellanea][1004]

 [1000]: {% post_url 2014-02-17-suboptimal-latex-1-intro %}
 [1001]: {% post_url 2014-02-24-suboptimal-latex-2-spacing %}
 [1002]: {% post_url 2014-03-03-suboptimal-latex-3-mathematical-environments %}
 [1003]: {% post_url 2014-03-10-suboptimal-latex-4-mathematics %}
 [1004]: {% post_url 2014-05-25-suboptimal-latex-5-miscellanea %}


### See also

1. [How to take lecture notes with LaTeX][2000]
1. [LaTeX class for lecture notes][2001]

 [2000]: {% post_url 2008-12-27-how-to-take-lecture-notes-with-latex %}
 [2001]: {% post_url 2008-12-29-latex-class-for-lecture-notes %}
