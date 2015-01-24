---
title: Global time, emotional time, and the annoyance of DST
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2014/06/emotional-time/
categories:
  - Statistics
---
My post on the [difference between local time and solar time][1] obtained some mild popularity, and this gave me some time to think more about the subject of local vs. global time, and about emotional time. What is emotional time? Read on to know!

 [1]: {% post_url 2014-01-06-how-much-is-time-wrong-around-the-world %}

<!--more-->

{% include figure.html width=250 float='right' url='/images/SolarTimeVsStandardTime.png' caption='Solar time vs standard time' %}

One of the main reaction to my map was surprise about the **predominance of red areas** (where the sun peaks after twelve o'clock) versus green areas (where the peak is before 12:00). This is easy to understand, if you think about it: would you prefer to live in a place where the sun shines from 05:00 to 17:00, or where it shines from 07:00 to 19:00? I doubt that many people would prefer the first (green) alternative to the second (red). [[^1]]

 [^1]: Places like this exists: for the green one, an example is October in Recife, a city of almost four million people in eastern Brazil; for the red, May in Singapore.

{% include figure.html width=250 float='left' url='/images/daylight-saving-world-subdivisions.png' caption='Areas observing DST' %}

This explains why the majority of people is in a "red" part of the world, even **without considering daylight saving time** [[^2]], that during the summer shifts most of Europe and Northern America one hour towards the red. [[^3]]

 [^2]: Several people asked for a version of the map considering DST. Sadly it would require a lot of time because of situations like this.
 [^3]: Russia is a notable exception because even though it technically does not observe DST, it recently switched time as to observe a permanent DST (and thus appears very red, inspiring a lot of communism jokes). Argentina looks similar, but their history is much more complicated.

Ok, so **people prefer red places**, and even more in the summer. But the way people name a certain instant is really a convention, so why, instead of shifting everybody's clocks, don't we just let everyone chose the hour they wake up, open their shops, go to school and to sleep? Changing the hours of operation only for the businesses for which it makes sense would probably cause less problems than shifting hours for everybody, after all.

The real problem with all of this is that people have a certain **emotional "attachment"** to a specific time in the day: for most people, 06:00 is quite early, and they'd feel grumpy if they had to wake up at that hour. Dinner time is also deeply felt by most people, deriving from family habits: for most Italians, it is from 20:00 to 21:00, increasingly progressively going south. In England, it's around 19:00. It is probably easier to change the underlying time than to convince people to modify their dinner habits to follow the sun.

This is what I call **emotional time**: the feeling, learned with experience and culture, that a specific hour is the best for a certain activity. What is the perfect time for dinner? Of course is 20:00, dinner time at my parents' house when I grew up. What if one morning I wake up at 11? Well, certainly I was lazy. Emotional time has almost no connection with solar time: we eat at 20:00 all year round, even if that means we eat in the dark in December and before sunset in June.

### A global time?

As distances around the globe become shorter thanks to the internet, the need for fixing **appointment from different timezones** is increasing. If you correspond with just one or two other timezones, it is usually simple to remember one or two differences. [[^4]]

 [^4]: Especially if the differences are of whole hours, and not of half-hours (like with India, Iran, and some parts of Australia), or of quarter-hours (like with Nepal).

Since emotional time varies only slightly around the world, it is then easy to understand which hours are reasonable for the other party. Just add the difference and compare with your emotional time, which hopefully is not very different from that in the other country.

{% include figure.html width=150 float='left' url='/images/swatch-beat-logo.png' caption='Swatch Internet Time' %}

Still, as the number of timezones to consider increases, this becomes more and more awkward, and there have been several attempts to create a **global time**: a time system in which an instant is called in the same way anywhere in the world. In 1998, Swatch introduced the [Swatch Internet Time][6], where a day is divided in 1000 *beats*, each of them slightly shorted than 1.5 minutes. Swatch built upon the valid attempts of converting people to [decimal times][7] during the French Revolution, but added the "global time" part. [[^5]] [New Earth Time][9] is a similar concepts of a global time, but based on angles instead of decimal systems, and hence every day is subdivided in 360 parts. [Globetime][10] is a more recent project that has been brought to my attention, and uses the same subdivision.

 [^5]: And, on the minus side, had the terrible idea of declaring its headquarters as the center of the new time system.
 [6]: http://www.swatch.com/gb_en/internettime/
 [7]: http://en.wikipedia.org/wiki/Decimal_time
 [9]: http://en.wikipedia.org/wiki/New_Earth_Time
 [10]: http://www.globetime.org/

Of course, using **UTC time** would be a similar way of using a unique time around the globe, but changing the unit (to decimal or sessagesimal) makes it easier to avoid confusion when switching between local and global time. But does a global time helps in arranging meetings? Yes and no: if you are arranging in person it might help to refer to a common global time that everyone has learned to tie to their local time; if instead you are proposing a meeting, than you need to learn the usual working hours of the other party, which is, if any, more difficult than remembering just the timezone difference and relying on the canonicity of emotional time. [[^6]]

 [^6]: A global time would really help during two weeks in the year, at least if you are organizing meetings between the UK and the US: their DST switch dates are not aligned, so for one week in March the time difference is just 7 hours instead than 8, and for one week in October it is 9 hours. If you have a recurring meeting, for those two weeks the time of the meeting would shift, but only for one side of the pond.

Even more so, using a global time would mean that people had to lose their emotional connection with specific times, and the evidences show that this is hard for people, more than changing currency [[^7]], and probably harder than changing measurement system.

 [^7]: Currencies, after all, change all the time thanks to inflation, so people are not locked in assigning an emotional value to specific quantities (or, they do, but then it is obvious that they are meaningless).

<!-- DO NOT EDIT BELOW THIS LINE -->
* * *

### See also

1. [My two cents on the daylight saving time][2000]
1. [How much is time wrong around the world?][2001]

 [2000]: {% post_url 2009-03-22-my-two-cents-on-the-daylight-saving-time %}
 [2001]: {% post_url 2014-01-06-how-much-is-time-wrong-around-the-world %}
