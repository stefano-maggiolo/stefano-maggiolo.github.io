---
title: 'Suboptimal LaTeX #1: intro'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2014/02/suboptimal-latex-1-intro/
description: 'Some of the most common LaTeX mistakes and how to fix them. The introduction focuses on some generic mistakes especially in your writing workflow.'
categories:
  - Typography
---
In one of my previous careers, I have been a **typesetter** for a journal in high energy physics ([JHEP][1]), for which I typeset several hundreds of papers. In case you do not know, this means applying the journal's style and conventions to the LaTeX source provided by the author, and fixing many errors in the process (both coming from the author and from LaTeX). During this job, I could observe a rich bestiary of LaTeX mistakes, and in this series I will guide you through the most common.

 [1]: http://jhep.sissa.it

<!--more-->

In this first, introductory, post, let us see some top-level guidelines.

{% include figure.html width=150 float='right' url='LaTeX_logo.png' caption='LaTeX' %}

### Editing vs. typesetting

There is a time for **editing the content**, and there is a time for **typesetting**. The former should always come before the latter. Despite what we would like to think, LaTeX's typesetting sometimes needs some human guidance; but, the author should not provide that guidance before the content is final. On a similar topic, the choice of the style, despite being a fruitful source of procrastination, should be done only at the end, before the final typesetting tweaks. Avoid entirely these steps if you are submitting to a journal with its own typesetters.

### Excessive style customization

Even if LaTeX may need some guidance in the low-level typesetting (rephrasing some sentences to avoid ugly paragraph shapes, for example), it rarely needs changes in its high-level structure. You may think that the default paragraph's are too narrow, but there is a reason in that (hint: **legibility**). For editorial reason you may need to fill the page much more: then use two columns. In general, legibility should be the main goal; it is better to be ugly than to be hard to read.

### Excessive usage of macros

Of course, if you write some term many times, and you are not sure how you actually want to render it, you should use a macro. But if you have several **nested levels of macros**, include **whole .sty** files wrote by someone else just because you need one definition, use tons of known or less-known packages, then you are looking for trouble (and for some serious swearing by the typesetter). The first reason why these are bad practices is that your source files become a mess. This should already be enough, but consider also that the messier your source code is, the higher the chance that you overlook or forget something and that you get conflicts in your macros or packages. And when you entrust your source file to the journal's typesetters, they are even more likely to make mistakes. **Always keep your source files clean.**

### Not knowing your tools

Please, please, take some time to **learn the basics of LaTeX properly**. Take a course, or show your source to someone more expert. You will probably discover many mistakes that you were not even aware of making. If you think LaTeX is hard and you are having trouble, most likely you are doing by hand something that LaTeX already does automatically, or you are micro-managing too much.

### Not using LaTeX

LaTeX is a layer created in 1984 over TeX, a software designed in 1978. In computer terms, they are both **ancient**. In layman's terms, well, too. And you can totally feel it, especially if you are not only a simple user but try to work on it as a developer. Nonetheless, TeX and LaTeX are by far the most used typesetting softwares in academia, especially where the typesetting is harder (physics, or ancient language studies, to name two areas), and that is for a reason: there are **no viable alternatives**. Using anything but LaTeX (or another TeX derivative) for your journal article is just madness. On a side note: I am not a user of TeX, but judging from the few times I met it, I think using TeX is also madness (but of another, geekier, kind).

Tune in next week for the second part!

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
