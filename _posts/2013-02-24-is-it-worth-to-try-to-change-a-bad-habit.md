---
title: Is it worth to try to change a bad habit?
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2013/02/is-it-worth-to-try-to-change-a-bad-habit/
latex: true
categories:
  - Math
  - Statistics
---
Suppose that you have a very nice shared **coffee machine** (the espresso one of course!), but the normal behavior is to leave the [portafilter][1] on after making a coffee. This implies that *before* making the coffee one has to remove the portafilter, clean it with water, drop water everywhere while going from the tap to the grinder. It could be better.

 [1]: https://www.google.com/search?q=portafilter&tbm=isch

Thus, you start cleaning the portafilter after making your coffee, hoping that people starting with a clean portafilter would feel inspired to clean it afterwards. But is it worth it?

<!--more-->

Let us **model the problem**. For simplicity, we think of a machine with a single group. I hope you are not alone in your crusade for post-coffee cleaning, so let's say \\( p \\) is the probability that a coffee is made by a generous person, one that cleans the portafilter after making coffee, regardless of how it was before. Also, there must be some people that clean the portafilter after using it only if they did not have to clean it before, and we fix the probability of a coffee be made by them as \\( (1-p)q \\) (that is, among the non-generous, the probability is \\( q \\)). The remaining \\( (1-p)(1-q) \\) cups of coffee are made by careless people, that do not clean the portafilter after making coffee.

The question is: **does it matter to be generous**? For some values of \\( p \\) and \\( q \\), what is the probability \\( r \\) of having a clean portafilter? It is quite simple to compute: we just need to combine the different possibilities for the previous coffee, with their probabilities and outcomes. The choices are on the kind of person making the last coffee, and whether that person had to clean the portafilter before making coffee or not.

* If the last person was generous, we will have a clean portafilter. This event has probability \\( p \\).
* If the last person was careless, we will have a dirty portafilter.
* If the last person was neither generous nor careless, the portafilter will be in the same position as it was before. But we know the probability of the portafilter being clean: it is again \\( r \\)! Combining it with the probability of the kind of person, we have a probability of \\( (1-p)qr \\) for the portafilter being clean in this scenario.

So, we have that \\( r \\) is the sum of all favorable cases: \\( r = p + (1-p)qr \\), and solving for \\( r \\) we get \\( r = \frac{p}{1 - q + qp} \\).

{% include figure.html width=200 float='right' url='coffee-chart-005.png' caption='r as q changes for p = 0.05' %}

Mmm. Is this good or bad? Let us try plotting for some values of \\( p \\). I'd say that a sane guessing for \\( p \\) is 5 percent. The following is what happens when \\( q \\) changes.

**Not very good**: to have a clean portafilter more than one half of the times, only 5 percent (\\( q = 0.95 \\)) of the remaining people are allowed to be careless! Even worse, if the remaining people are half careless and half not (\\( q = 0.50 \\)), we will have a clean portafilter a mere one tenth of the times. Maybe if there were more generous, like, 10 percent…

{% include figure.html width=200 float='left' url='coffee-chart-010.png' caption='r as q changes for p = 0.10' %}

**Not a big improvement**: for a half possibility of a clean portafilter we need less than 10 percent of careless (\\( q = 0.90 \\)), and if half of the remaining people were not careless, we would had a clean portafilter less than one out of five times (\\( r = 0.18 \\)).

Moreover, if we perform the same computation for a machine with **three groups** (as it is the one we have at work), the situation gets worse, as people may feel justified not to clean after them if they see a dirty portafilter on <em>another</em> group.

Sometimes math help people see a brighter future and encourage them to do their best. Today it just **made you a coffee-careless** person.
