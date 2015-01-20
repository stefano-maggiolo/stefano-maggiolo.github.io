---
title: Why a mathematician can be an excellent software engineer
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2012/03/why-a-mathematician-can-be-an-excellent-software-engineer/
categories:
  - Math
  - Software
---
I have been lucky enough to have tried these two occupations, in different ways, often mixed but also on their own. Nonetheless, the discover the title is referring to is quite recent, and coincides with the broadening of a software project I am very proud to have started and contributed to: [CMS][1], the contest system that is going to be used at the 2012 edition of the International Olympiads in Informatics (which, and it is not by chance, are going to be in Italy).

 [1]: http://github.com/cms-dev/cms

<!--more-->

But first, a step behind: in order to say that a mathematician can be a great software engineer, one first has to establish which are the **skills** that mathematics contributes to grow in a person. Far from me is the idea that I can have a comprehensive view of these skills. For a much more significant reading, you can take a look at [this post][2] on Terry Tao's blog.

 [2]: https://terrytao.wordpress.com/career-advice/does-one-have-to-be-a-genius-to-do-maths/

But I have experienced one of the points that post makes: more (much more!) than genius and inspiration, mathematics progresses with hard work, and most of this work heads toward reading the literature. This has two aims: the first, more practical, is to be able to use particular results in one's own mathematics; the second is to work by analogies, and find connections at a deeper level that can be translated in different settings. Note the difference between "**applying**" and "**translating**".

Both of these aims are important, but if one would have to choose which one to have magically improved overnight, I think that almost everyone would choose the second: it is much easier to follow one's thoughts reading the proof of a theorem, than to understand what an author is trying to convey with his/her whole paper. Often because the author is not so willing to explain it, or because it is also harder to write than a theorem's proof!

So, let us focus on this second aim. In order to be good at this, one has to be able to look at the linear sequence of propositions, theorems, definitions and so on, and transform these in a more meaningful structure. The obvious thing that comes to mind is **dependence**: Theorem 3.4 needs the statements of Lemma 3.3 and Lemma 2.3, and it uses the concept defined in Definition 1.1.

This creates a complex enough **structure**, and the ability to keep in one's head this structure is very important. As it is the one of simplify this structure, highlighting the most important connections and the most important nodes: a technical lemma can be often ignored in such a structure, but a definition is often motivated by some specific result, even if it is used everywhere.

What is impressive is that, on the software side, these **two ways of reading** appear too! Following a proof is like looking at a function body: you do not need to know much of the rest, you need the recipe for that specific issue, you can assume that complex calls, or complex results, just do what they are asked to do. You can look at a whole list of these pieces, and understand them one by one, and have no idea whatsoever of what they do altogether.

And, if one had ever worked on small projects, or even on big projects but caring only for his/her small piece on the big picture, this is often enough. And this is what I thought before starting CMS. But as this last project grew larger as the number of collaborators, I started recognizing that the **right way to organize** in my mind mine and other people's contributions was not to look at them line by line, but to try to understand what was their aim: asking first why they did something in that way, and only after caring about how they did it.

There is a concrete **difference** in this analogy between mathematics and software engineering though: there is a field of computer science (to which students are exposed) that tries to study and highlight these connections; to make reusable not only functions but also ideas. This field studies [design patterns][3] and, up to my knowledge, the only part of mathematics that could be thought as an analogy to it is category theory. The problem, though, is that category theory, being a part of mathematics, can make reusable only fully formalized concepts. This is a strength, but also a limitation, because many analogies among different theories cannot be effectively studied because of the impossibility to fully formalize them.

 [3]: http://en.wikipedia.org/wiki/Software_design_pattern

