---
title: 'Suboptimal LaTeX #3: mathematical environments'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2014/03/suboptimal-latex-3-mathematical-environments/
description: 'Some of the most common LaTeX mistakes and how to fix them. This part is about the math environments: choose the correct one and use it effectively.'
categories:
  - Typography
---
We have seen some [generic mistakes and suggestions][1], and how to correctly use [spacing][2] in your papers. Today we will try to shine some light on how to choose the proper mathematical environment, which is in itself a complicate issue.

 [1]: {% post_url 2014-02-17-suboptimal-latex-1-intro %}
 [2]: {% post_url 2014-02-24-suboptimal-latex-2-spacing %}

<!--more-->

The source for all figures in this post is in [this writeLaTeX][3].

 [3]: https://www.writelatex.com/read/rxkrvdntnhqf

First of all, some suggestion about typesetting mathematics: `amsmath` is a must, and you should read its [documentation][4]. Another package whose documentation is really useful to read is [`mathtools`][5]. You will learn for example of the useful family of commands around `\mathclap` (but do not abuse them).

 [4]: ftp://ftp.ams.org/ams/doc/amsmath/amsldoc.pdf
 [5]: http://mirrors.ctan.org/macros/latex/contrib/mh/mathtools.pdf

### What environments not to use

This is a pet peeve of mine, after having to deal most of the time with authors using almost exclusively `eqnarray`. This results in a lot of pain for the typesetter, other than a suboptimal output. Since this is intended to be a short guide, I will send the interested to [this article][6] for the explanation of why you should not use it. The summary is that `eqnarray` is really just a slightly modified `array` environment, and the simplicity of its implementation causes a lot of inconsistencies.

 [6]: http://tug.org/TUGboat/tb33-1/tb103madsen.pdf

### What environments to use

So, what should you use? The short answer is: any of the `amsmath` environments, that you can read in the previously linked [documentation][4]. But maybe you want some more **direct help** in choosing.

{% include figure.html width=150 float='right' url='math_aligned.png' caption='Example of inner and outer environments' %}

The first thing to know is that `amsmath` environment can be categorized in two sets: **outer and inner environments**. Outer environments, like `equation`, `align` and `multline` are indeed the external building block of your display, whereas inner environments can be used to give the proper alignment to specific parts of the display. A way of think of this is that each line of an outer environments is an "equation", hence needs an equation number, whereas lines in an inner environment do not define new "equations". You can see an example in the figure, even if the best way to do something like that is using the `cases` environment.

Outer environment usually have a starred version (for example, `align*` for `align`) that behaves exactly the same but does not write equation numbers. Instead of `equation*`, you can use `\[ ... \]`.

### An algorithm

To understand what environment I need, I usually start counting how many equations I want (by thinking: "if I wanted to have equation numbers in this block, how many of them would I want?"):

  * if the answer is one, then I look at how many lines the equation is composed of;
  * for one equation, one line, I use `equation`;
  * for one equation, multiple lines, I either use `multline` (when there is a long member that needs wrapping) or `equation` wrapping the inner environment `split` (when there is a chain of equality signs).

  * if there are more equations, I usually use `align`, and rarely `gather` when the equations have no easy alignment.

{% include figure.html width=150 float='right' url='math_environments.png' caption='Showcase of math environments' %}

There are some subtleties in this procedure: for example, I prefer `equation` and `split` over `align` because of the vertically centered equation number. Note also that if you have a lot of short equations, you can use `align` to put more of them in a single line, keeping the alignment, just using more ampersands.

The most important problem to me is that there isn't an easy way to provide alignment of the equations defined in the outer environment if you used an inner environment to write them. For example, the best way to write two equations with two lines each, would be to use an `align` containing two `split` or `multline`; but then there is no way of aligning the two equality signs of the two main equations (except for [some hack][7]). Therefore, in these cases I heavily hearted use a single `align`.

 [7]: http://tex.stackexchange.com/a/44451

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
