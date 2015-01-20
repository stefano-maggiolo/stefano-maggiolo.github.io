---
title: 'IOI 2012 &mdash; my experience'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2012/10/ioi-2012-my-experience/
categories:
  - Personal
---
[IOI 2012][1]'s closing ceremony was last Saturday, and I feel the need to summing up my experience, thank a lot of people, and try to understand how this "very Italian" edition of IOI did really went (at least looking at the aspect under the control of the team I was in: technical and scientific matters).

 [1]: http://www.ioi2012.org/

<!--more-->

As the HSC, we started working remotely a few months ago, but onsite only a week before the opening ceremony. Before we got there, we had an almost finalized version of the statements, but we were far from having defined limits, subtasks and so on. We had many solution, but not all we wanted. But I think this was to be expected, as work is much easier when done onsite, where you can actually cooperate.

The first few days we had some problems with the network, that delayed our program by almost a couple of days; other organizational problems caused the cancellation of a proper, human-made, test of the grading system, [CMS][2]. This probably caused the overlook of several small issues with the grading system and the OS of the contestant's machines that came out at the practice session on Monday.

 [2]: https://github.com/cms-dev/cms/

After the practice session, we split into two teams --- one stayed in the contest room fixing the issues, and they did a great job as the next day they were completely solved. The other team (including myself) went to the translation room, where they faced a much worse situation. In the first translation day, there were **lots** of problems. The first is that we arrived late: the contest and the translation were 40 minutes apart by car, and the above mentioned organizational problems, plus some delay on our part (I have to admit) caused us to be there 15 minutes after the start of the translation, instead of 30 minutes before as planned. After we arrived, the configuration of the translation server with the last version of the task's statements was interrupted by several power outages. But, after solving these problems, we realized that the new translation system was horribly slow. Sadly this was not solved until the second translation day.

I take responsibility of the fail of the first translation day, because I proposed the new system and I overlooked the performance problem. Even more, because we did not manage to explain how the new system worked and this caused confusion among the translators. I really think now that a change like that must be properly explained and planned much more carefully.

We managed to go back to the contest room one hour before the start of the first competition day, and we had just the time to load the translations and supervise the entrance of the contestants. Here we had the second (and last) big issues, where big means that I want to apologize for (even if this is 90% not the HSC's fault): sadly both contest's days started late, the first by 30 minutes, the second by 20.

At start, we had minimal problems to the webserver, solved by asking a few contestants to reload the page (I think nobody lost more than a minute, and only a few more than 20 seconds). This year the statements were presented to the contestants only as PDF in the contest interface, so all access were simultaneous instead of spread by the reading time; the initial load caused the few lost connections that some contest experienced.

During the contest, we appreciated the new system, as it allowed us to change a few things we did wrongly in the task preparation without making the contestants aware that anything was happening. In the end, we were very satisfied by the ranking of the first day.

The problem at that time was to improve the second day of translation. There were several improvements: on the software side, we disabled the very time-consuming routine that proposed suggestions for a new translation. Profiling the PHP code, it turned out that most of the time was spent in these functions. On the hardware side, we got a much more powerful server. I would like to thank Angelo, Bernard, Martin, Giuseppe and Roberto for help making the second translation day a success.

Indeed, solving the performance issues allowed us to be much more clear on how the system worked, to provide help, and many people recognized our work and the fact that the new translation system (that I am going to describe in a post soon) is a big improvement with respect to the old system, that is, using Word.

Even if the translation system worked in an almost perfect way, we arrived at the contest room less than a couple hours before the competition. We had to face a hard decision: during the night, the team finalizing the task graders decided to change one grader for technical reasons (mainly, trading off some security against cheating for a fairer time measurement and shorter evaluations). That change was completely sounding and I am glad they made it, but sadly the new time limit came out after the statement was finalized the night before. So, the choice was between changing the time limit providing a better evaluation of the submissions, and avoiding a change into the task statement **after** the translations were made. Luckily, the ISC got our back and confirmed that the right thing to do was to admit we got the time limit wrong and announce its changing. We announced the news in several ways and I think no contestant was penalized by this.

At the start of the second day we had a couple of network problems, that allowed us to test a new feature of CMS, the ability to assign additional time to contestants that were penalized. This feature run very smoothly and we had no complains about the network problems.

Also the ranking of the second day was quite good --- a bit more crowded in the top, and a bit harder for the guys in the middle, but summing up the results we goot a very smooth ranking, with nice cut points and not many ex aequo.

I have to thank all the HSC team: Giovanni^3, Luca, Matteo, Massimo, Roberto; the ISC, Monica and Fabio, all the guides and volunteers, for everything. Drivers and doorkeepers at Sirmione and Montichiari, for getting accustomed to our schedule. Technical people for the network and the laptops. And finally all the leaders and contestants, for understanding that we did our best, even if some time this was not really enough...

A lot of people asked us if we would like to do this again, in the future. We usually replied this is something you do once in a lifetime. Maybe the reason is that it had been a very tiresome and stressful week, yes; but, maybe, the real reason to do it only once is not to make it less special than it is today and will be in my memories. Thanks!

<!-- DO NOT EDIT BELOW THIS LINE -->
* * *

### See also

1. [IOI translation systems: a survey of possible approaches][2000]
1. [IOI translation systems: an ideal workflow][2001]
1. [IOI translation systems: an actual solution][2002]

 [2000]: {% post_url 2012-10-09-ioi-translation-systems-a-survey-of-possible-approaches %}
 [2001]: {% post_url 2012-10-15-ioi-translation-systems-an-ideal-workflow %}
 [2002]: {% post_url 2012-10-24-ioi-translation-systems-an-actual-solution %}
