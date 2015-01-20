---
title: Typography holidays
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2009/01/typography-holidays/
categories:
  - Typography
---
In the last two months I had an almost precise timetable that said when I should study and when I can rest. This had the expected result: I didn't feel guilty when I rested. Anyway this couldn't help my guiltiness in these holidays. But maybe I deserve it.

<!--more-->

In these days of non-studying I did some programming: I've made a simple organizer for the **movie** I saw, with some "useful" statistics and graphs. For example, I've discovered that the only movies I've seen three times in the last four years are [*Edward scissorhands*][1], [*The consequences of love*][2], [*Howl's moving castle*][3], and [*The 400 blows*][4]; my most viewed directors are Stanley Kubrick and Tim Burton followed by Woody Allen and Nanni Moretti. Anyway the program needs some serious love before publishing.

 [1]: http://www.imdb.com/title/tt0099487/
 [2]: http://www.imdb.com/title/tt0398883/
 [3]: http://www.imdb.com/title/tt0347149/
 [4]: http://www.imdb.com/title/tt0053198/

Also I dedicated some time to **typography**, typography and LaTeX, typography without LaTeX. It all begins with [TUGboat][5], the journal of the TeX User Group. I didn't know about it, so I enjoyed almost twenty years of journal in a week. In particular I learned about [Fontforge][6] in [this introductory paper][7]. I knew the program, but I thought that the efforts needed to design even the sloppiest font were much higher. I also appreciated the paper's typeface, Founders Caslon.

 [5]: http://www.tug.org/TUGboat/contents.html
 [6]: http://fontforge.sourceforge.net/
 [7]: http://www.tug.org/TUGboat/Articles/tb24-3/williams.pdf

I learn about [**XeTeX**][8], a

 [8]: http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&#038;id=xetex

> typesetting system based on a merger of Donald Knuth's TeX system with Unicode and modern font technologies.

Sounds great! Indeed, last time I tried to use a TrueType or an OpenType font with LaTeX I've cried a lot. And not succeeded. Instead, with XeLaTeX it's as easy as naming a font installed in the operating system. For examples, see [this beautiful page][9]. Every rose has its thorns: many packages simply stop working in XeLaTeX, and Unicode support is great --- I can type a Unicode character and it displays the corresponding glyphs without translation tables, but if the font does not have the glyph you're lost since translation tables stop working too. This is too bad since mathematical fonts are handled in a complete different way and most occasions to use Unicode occur in math.

 [9]: http://nitens.org/taraborelli/latex

So I'm stuck with LaTeX. If you see my recent works, I've always used Palatino. This is done by adding the line

{% highlight latex %}
\usepackage{mathpazo}
{% endhighlight %}

This is not the best thing: the clone of Palatino shipped with most TeX distribution (I think it is derived by URW Palladio, but I'm not sure) lacks many useful glyphs --- mostly ligatures. But if we use it to render, for example, web pages, we will see that it has only a very narrow subset of Unicode. This problem is shared by Computer Modern itself, but it was overcomed by Latin Modern, an extension with support for a much larger subset of Unicode. The [TeX Gyre Project][10] is following the same strategy with the other standard fonts, a process called **gyrefication**;. I still have to convert my documents to use TeX Gyre Pagella, the gyrefication of Palatino. As for the desktop, I forgot to say in the last post that probably the most complete Unicode font is [STIX][11]. This project is late by several years, but in 2007 they finally managed to publich a beta of their font, which is available in the [Mozilla website][12], since the STIX consortium also retired the beta.

 [10]: http://www.gust.org.pl/projects/e-foundry/tex-gyre
 [11]: http://www.stixfonts.org/
 [12]: http://www.mozilla.org/projects/mathml/fonts/stix/STIXBeta.zip

At this time I almost decided to drop maths to become a font designer, so I flipped through some typography-oriented blog. Did you know that the German characters "ß", that I always called "sharfes es" (I did three years of German in junior high) is also called "es zet" since it is simply the ligature "sz"? It is explained in details [here][13].

 [13]: http://typefoundry.blogspot.com/2008/01/esszett-or.htmlshar

Another amazing thing I saw is this (probably illegal) [**book of Hermann Zapf**][14]. Once I was in South Korea, and I had the pleasure to see a man writing ideograms with the traditional big brush (I've no idea of its name). The question whether Asian people are fascinated by Latin alphabet as much as ideograms fascinate us popped in my mind, but I answered myself: "obviously Latin glyphs are not even comparable in beauty with ideograms." Well, now I think I was wrong. Not only they're comparable but finding beauty in such an everyday object of our lives add something that ideograms don't have (only because we're not used to them, so they're *only* art to our eyes).

 [14]: http://www.typogabor.com/manuale-hermann-zapf/index.html

At this time I took the Helvetica shipped with Mac Os X, put as my desktop font, and I began adoring it. I think the Web is ruining young people's life in a much more dangerous way then devouring their time. It devours their capacity to focus on **one** topic. A person cannot have many passions, if it wants to be successful in at least some of them. But the Web shows all these people, all with a different passion, and all these topics seem wonderful, and you really would like to become a good typographer, or a decent chef, make beautiful origami, and I can go on as I want. Last generation keyword was *search*; our has to be *select*.
