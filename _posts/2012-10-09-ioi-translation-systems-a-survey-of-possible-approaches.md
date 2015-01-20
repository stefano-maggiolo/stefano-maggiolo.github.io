---
title: 'IOI translation systems: a survey of possible approaches'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2012/10/ioi-translation-systems-a-survey-of-possible-approaches/
categories:
  - Typography
---
As said in the previous post, during the IOI 2012 we introduced a novelty also in the way the delegation leaders handle the translations of the task statements. This is the first of a small series of posts dedicated to this issue, that "surprisingly" took away a lot of time from other parts of the contest preparation. In this first post I will present some of the approaches tried in the past and introduce the rationale for the one we introduced this year.

<!--more-->

At the IOI, the Host Scientific Committee presents its proposal for the three tasks the evening before the competition at the delegation leaders of more than 80 countries. The leaders decide whether to approve or not each task, and in the happy case the task get accepted (event that realizes almost all the time) they start translating the task in the native language(s) of their contestants. During the translation, they can make *minor objections*, requests for partial modifications of the statement.

Such modifications are mostly needed because contestants in the IOI come from many different cultures, and the same explanation can be very clear for one and not so clear for another person coming from the another part of the world. Sentences can be slightly rephrased in the translation process, but most leaders decide to ask to change the official statement because a not so slight rephrasing could be misunderstood for a cheating tentative.

Hence, a translation system for the IOI must handle modifications to the official statement *during* the translation process (usually grouped into *versions*), and must be able to cope with a large portion of scripts and languages of the world.

The usual way the IOI handled this task is using **MS Word**. Leaders were handed a `.doc` file, the official statement in English, and they would translate modifying the file. During the night, when new versions would come out, they would receive the difference in some format (plain text, or the one created by the *Compare documents* feature of MS Word. At the end, leaders would produce a PDF file from MS Word and print it for the students, or send it to the Host Scientific Committee for inclusion in the contest interface.

Using MS Word is not intrinsically a bad solution, since Word is one of the software most commonly found in OEM computers all around the world, is powerful enough to handle the formatting needs of the IOI, and is not so hard to use even for people not used to run Windows (this was especially true before MS Office 2007, as for example I find the new UI quite difficult).

There are **problems** though, both ethical and technical. From the **ethical** point of view, it would be much better to avoid using proprietary software, in particular for the distribution of the translations, but also for the composition. Moreover, for the IOI organization, paying for MS Office license for about one hundred computers is a serious expense. From the **technical** point of view, having a consistent formatting in MS Word does require some effort and definitely is outside the reach of occasional users. Support for mathematics could be much better, and the resulting translations may be very different looking from the original. Finally, the *Compare document* output is often not very evident in particular if the change is minimal (for example, punctuation).

A possible improvement would be to use **LaTeX**. The workflow would not change very much, but the output would be very predictable and of high quality, and the look would be the same for every translation. It is completely free software, produces PDF output natively and thus have no ethical problems. Nonetheless, the IOI 2005 in Poland tried using LaTeX and (as far as I was told) the change was not very welcomed by delegation leaders. Sadly, LaTeX is not very known even in the IOI community, and definitely needs more technical skills than MS Word. One can say that not knowing MS Word would make low quality documents, but not knowing LaTeX would make no document at all. Also, I am not really aware of problems related to non-latin scripts with LaTeX, even if I am quite confident that they could be resolved with new engines such as XeLaTeX.

Even though using LaTeX would be a major step to overcome both ethical and technical problems, there is a common issue with the two techniques we have seen. The problem is that using either MS Word or LaTeX, there is no direct connection between a paragraph in the translated document and a paragraph in a specific version of the official statement. This makes the job of updating the translations once new versions come out very difficult and error prone, because it relies on the translator to do two jobs that could be automatic:

* remembering the version of the official statement that they were using when translating a paragraph;
* identifying the changed sentence in the translated statement when looking at a change in the official statement.

Both these two jobs can be made **automatic** using a different approach to translations: not looking at the task statements as they were books to translate, but look at them as a composition of strings that needs to be translated separately, as if they were strings in a software to localize.

We will see in the next post the ideal workflow that this approach can make possible, and the compromises that one has to accept in order to have these advantages.

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
