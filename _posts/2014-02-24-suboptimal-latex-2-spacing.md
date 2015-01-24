---
title: 'Suboptimal LaTeX #2: spacing'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2014/02/suboptimal-latex-2-spacing/
categories:
  - Typography
---
In the [first post of the series][1] I gave some high level suggestions on writing a paper with LaTeX. Instead, from now on I will focus on specific typographical areas. The first I want to explore is **spacing**, which often goes unnoticed (because, well, you cannot see spaces) but is nonetheless one of the most important aspects in ensuring that a paper flows correctly.

 [1]: {% post_url 2014-02-17-suboptimal-latex-1-intro %}

<!--more-->

All LaTeX fragments I used to produce the figures are collected in [this writeLaTeX page][2]

 [2]: https://www.writelatex.com/read/kxrzggsvbxkv

### Vertical spacing between paragraphs

{% include figure.html width=200 float='right' url='/images/spacing_double_backslashes.png' caption='Space between paragraph' %}

In LaTeX, leaving a blank line is the way of ending a paragraph, which means starting a new line and applying the necessary indent. But not all paragraph breaks are equal: if a paragraph also ends a logic part of the section, leave more space by ending it with two backslashes (to go to a new line) and a blank line (to start a new paragraph). I think I never had the need to go to a new line without creating a new paragraph, writing `\\` without the blank line right after.

The figure above showcases the correct and wrong patterns: the first two breaks are proper ways of ending a paragraph, whereas the last one is wrong: it is visually equivalent to ending a paragraph and using `\noindent`, another instruction you should avoid.

At typesetting time, you may need to tweak the vertical spacing between paragraphs, even though it is usually avoidable. If you cannot avoid it, do not use `\vfill`, `\vspace`, or multiple `\\`, but something like `\\[2mm]`; if you need to add a lot of space, use a multiple of `\baselineskip` as the argument, for example `\\[3\baselineskip]`.

### Vertical space before an equation

{% include figure.html width=200 float='right' url='/images/spacing_before_math.png' caption='Spacing before an equation' %}

A similar error occurs when you leave a blank line before a mathematical environment: long story short, do not do it. You can see in the figure the difference between the two cases.

The problem is that if you do so, you are starting a new paragraph with the equation. This is never what you want, especially if before you have a colon! Nonetheless, if you use the default style you will not see any difference. To produce the figure above, I had to increase `\parskip` (the additional vertical space between paragraphs) from the default, zero, to a positive value.

If you are thinking "then if I use the default style, I can ignore this suggestion", remember that when you write the content you should not care about the style of the paper, since you should make that choice after the content is finalized.

### Vertical spacing sneaking in

{% include figure.html width=250 float='right' url='/images/spacing_centering.png' caption='Space within environments' %}

Some environments have the not obvious side effect of inserting vertical spacing. The main example here is `center`. The alternative is `\centering`, which unlike the environment does not add any vertical spacing. Another alternative is `\centerline`, which can be used only for very small pieces of text or for figures, because it does not wrap over new lines. See the figure for the differences.

The same problem occurs with the environments `flushright` and `flushleft`: to avoid additional vertical spacing, you should use `\raggedleft` and `\raggedright`, respectively.

### Horizontal spacing in `align`

{% include figure.html width=200 float='right' url='/images/spacing_align.png' caption='Spacing in alignment' %}

Horizontal spacing is more difficult to get wrong, but there is a common mistake when using the `align` in mathematical mode. It happens when you put the alignment ampersand <emph>after</emph> the equality sign instead than before, as in the figure.

Why anybody would want to put the ampersand after the equality sign? Because if the line breaks, they want the second part to be aligned after the equality sign too. But there are better ways:

  * one is to use `&\phantom\{ {}={} }` at the begin of the second line: without the empty groups, LaTeX would think that the equal sign has nothing around, and it would collapse the horizontal spacing;
  * another is to use `={}&` on all other lines, again to force the binary relation spacing around the equality sign.

Next week, in the third part, we will see how to choose the perfect mathematical environments. Stay tuned!

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
