---
title: How much is time wrong around the world?
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2014/01/how-much-is-time-wrong-around-the-world/
description: 'Why Spaniards have dinner so late? A map of the difference between solar time and clock time around the world.'
categories:
  - Statistics
---
A few years ago I went to Spain for the first time, and like many I was surprised by **how late is dinner**. The first night I dined almost alone in a restaurant at 8pm, going away just as people were starting to come in. Of course this can be mostly explained by cultural reasons, but the clearly later-than-usual summer sunsets must also have played a role in shaping the Spanish days.

<!--more-->

> **Note.** Click [here][5] for a new, updated, version of the map, with some more discussion.

 [5]: {% post_url 2015-02-17-the-time-it-takes-to-change-the-time %}

{% include figure.html width=300 float='left' url='/images/SolarTimeVsStandardTime.png' caption='Solar time vs standard time' %}

At the time I'm writing, near the winter solstice, Madrid's sunset is around 17:55, **more than an hour later** than the sunset in, for example, Naples, which is at a similar latitude. The same difference holds at the summer solstice and around the year. Just because it applies to most places I've been, a time like that in Naples feels more natural to me, and probably to most non-Spanish people. But is it?

Looking for other regions of the world having the same peculiarity of Spain, I edited a [world map from Wikipedia][1] to show the difference between solar and standard time. It turns out, there are many places where **the sun rises and sets late in the day**, like in Spain, but not a lot where it is very early (highlighted in red and green in the map, respectively). Most of Russia is heavily red, but mostly in zones with very scarce population; the exception is St. Petersburg, with a discrepancy of two hours, but the effect on time is mitigated by the high latitude. The **most extreme** example of Spain-like time is western China: the difference reaches three hours against solar time. For example, today the sun rises there at 10:15 and sets at 19:45, and solar noon is at 15:01.

 [1]: http://commons.wikimedia.org/wiki/File:Standard_time_zones_of_the_world_(2012)_-_Pacific_Centered.svg

So, why do some countries are forced to have such discrepancies? The only way to assign to a place a **canonical time** which follows our main assumptions is to observe the instant in the day when the Sun is higher in the sky, and call that 12:00. This is **not practical** for at least two important reasons.

{% include figure.html width=150 float='right' url='/images/analemma-sun.jpg' caption='Analemma of the sun' %}

One is that (solar) **days do not all have the same length**: the modern calendar compensates by letting midday oscillate a bit around the year: for example, midday in Naples goes from 11:47 in early November to 12:17 in early February. The difference between solar noon and clock noon is beautifully explained by an analemma, a picture with an exposure taken every few days at clock noon, showing how the sun moves in the sky not only in height (the north-south) direction due to the different seasons, but also in the east-west direction due precisely to the different lengths of the solar days.

More importantly, **each city at a slightly different longitude would have a slightly different time**. It seems strange that time systems with such a huge problem had ever been practical, but in the pre-industrial-revolution world, travels were so uncommon and slow that this problem was no more than a minor annoyance. But in today's hyper connected (physically and virtually) world, it is obviously not an option.

The transition from apparent solar time, where all days have different lengths, to solar mean time, where midday wanders around 12:00, was caused by the proliferation of **mechanical clocks** in the early 19th century. The change to a time zone system, to solve the second problem, was caused instead by the telegraph and even more by the spreading of **railway networks** in the second half of that century; it's not a coincidence that the first country moving to a common time was Great Britain.

Indeed, if we acknowledge that the two problems must be solved, the natural result is the current **time zone system**. The immediate consequence is that in the western part of the time zone the sun rises and sets later than in the eastern part. Normally, these differences amount to at most half an hour in either direction, but **human geography** sometime forces greater differences. In Spain's case, to allow Spain to have the same time as central Europe, the difference can exceed ninety minutes. China instead decided in 1949 to adopt a single time zone, and to place its center in the richer east, forcing the less populated west to have an uncomfortable time. Indeed, though not officially recognized by the government, people in Xinjiang (China's west-most region) follow a time zone closer to their apparent solar time, shifted by two hours from Beijing time.

**Note:** luckily, the map was uploaded on Wikipedia as SVG, so it was simply edited with a text editor to add the gradients (using Inkscape to match the objects with their ids). I do not usually like cylindrical projections (my favourite is [Robinson][2]'s, and yes, [I like coffee][3]), but this time it made drawing gradients so much easier. And the [Miller][4] is a fair enough compromise.

 [2]: http://en.wikipedia.org/wiki/Robinson_projection
 [3]: http://xkcd.com/977/
 [4]: http://en.wikipedia.org/wiki/Miller_cylindrical_projection

<!-- DO NOT EDIT BELOW THIS LINE -->
* * *

### See also

1. [My two cents on the daylight saving time][2000]
1. [Global time, emotional time, and the annoyance of DST][2001]
1. [The time it takes to change the time][2002]

 [2000]: {% post_url 2009-03-22-my-two-cents-on-the-daylight-saving-time %}
 [2001]: {% post_url 2014-06-02-emotional-time %}
 [2002]: {% post_url 2015-02-17-the-time-it-takes-to-change-the-time %}
