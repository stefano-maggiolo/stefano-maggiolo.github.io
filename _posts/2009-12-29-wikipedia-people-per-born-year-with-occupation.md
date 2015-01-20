---
title: Wikipedia people per born year with occupation
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2009/12/wikipedia-people-per-born-year-with-occupation/
categories:
  - Typography
---
There are times in which you just want to graph something. So I picked up this mildly interesting idea of inspecting what kind of people are mostly portrayed in the Wikipedia and tried a CSS graphing solution.

<!--more-->

<style>
td {
  vertical-align: middle;
  padding: 2px;
}

#page {
  width: 686px;
  border: 1px solid black;
  margin: 5px auto;
  position: relative;
}

#graph {
  margin: 10px;
  background: Lavender;
  border: 1px solid black;
  position: relative;
  height: 510px;
}

#graph li {
  position: absolute;
  bottom: 0px;
  width: 18px;
  margin: 0px 4px 0px 0px;
  padding: 0px 0px 0px;
  font-size: xx-small;
  list-style: none;
  text-align: center;
  box-shadow: 2px -0px 2px #666;
  border-top-right-radius: 4px;
  border-top-left-radius: 4px;
}

#graph li p {
  margin-top: 5px;
  transform: rotate(-90deg);
}

#line {
  margin: 10px;
  padding: 0px;
  height: 2em;
  font-size: small;
  position: relative;
}

#line li {
  position: absolute;
  bottom: 0px;
  height: 26px;
  margin: 5px 2px;
  padding: 0px;
  font-size: small;
  list-style: none;
  text-align: center;
  transform: rotate(-90deg);
}

#legend {
  margin: 15px;
  padding: 2px 5px;
  font-size: x-small;
  position: absolute;
  right: 0px;
  top: 0px;
  border: 1px solid black;
  background: White;
}

#legend div {
  height: 20px;
  width: 20px;
  margin: 2px;
  border: 1px solid black
  line-height: 22px;
  text-overflow: visible;
  box-shadow: 2px -0px 2px #666;
}

.noble { background: LightSkyBlue; }
.art { background: LightCoral; }
.sport { background: GreenYellow; }
</style>

<div id="page">
 <h3 style="text-align: center">Wikipedia people per born year with occupation</h3>
 <div id="graph">
  <ul>
   <li class="bar sport" style="height: 495.1018244844px; left: 0px;"><p>8232</p></li>
   <li class="bar sport" style="height: 497.00953837046px; left: 22px;"><p>8523</p></li>
   <li class="bar sport" style="height: 497.07393214358px; left: 44px;"><p>8533</p></li>
   <li class="bar sport" style="height: 496.47213559271px; left: 66px;"><p>8440</p></li>
   <li class="bar sport" style="height: 494.78068319828px; left: 88px;"><p>8184</p></li>
   <li class="bar sport" style="height: 493.20836710718px; left: 110px;"><p>7953</p></li>
   <li class="bar sport" style="height: 488.08064154231px; left: 132px;"><p>7244</p></li>
   <li class="bar sport" style="height: 479.27707233007px; left: 154px;"><p>6171</p></li>
   <li class="bar sport" style="height: 471.03538699594px; left: 176px;"><p>5311</p></li>
   <li class="bar sport" style="height: 457.01095452934px; left: 198px;"><p>4114</p></li>
   <li class="bar sport" style="height: 439.04377872675px; left: 220px;"><p>2966</p></li>
   <li class="bar sport" style="height: 407.20436654605px; left: 242px;"><p>1661</p></li>
   <li class="bar sport" style="height: 368.97463038991px; left: 264px;"><p>828</p></li>
   <li class="bar art" style="height: 332.73677104168px; left: 286px;"><p>428</p></li>
   <li class="bar art" style="height: 296.44012324595px; left: 308px;"><p>221</p></li>
   <li class="bar art" style="height: 272.149259845px; left: 330px;"><p>142</p></li>
   <li class="bar art" style="height: 265.58443748755px; left: 352px;"><p>126</p></li>
   <li class="bar art" style="height: 248.31403519862px; left: 374px;"><p>92</p></li>
   <li class="bar art" style="height: 242.66064711446px; left: 396px;"><p>83</p></li>
   <li class="bar art" style="height: 221.05220188608px; left: 418px;"><p>56</p></li>
   <li class="bar art" style="height: 201.18450034721px; left: 440px;"><p>39</p></li>
   <li class="bar art" style="height: 180.99089278694px; left: 462px;"><p>27</p></li>
   <li class="bar art" style="height: 161.69387662748px; left: 484px;"><p>19</p></li>
   <li class="bar art" style="height: 155.58592049438px; left: 506px;"><p>17</p></li>
   <li class="bar noble" style="height: 120.66059519129px; left: 528px;"><p>9</p></li>
   <li class="bar noble" style="height: 148.7125860703px; left: 550px;"><p>15</p></li>
   <li class="bar noble" style="height: 114.19253938474px; left: 572px;"><p>8</p></li>
   <li class="bar noble" style="height: 140.85420275156px; left: 594px;"><p>13</p></li>
   <li class="bar noble" style="height: 76.128359589828px; left: 616px;"><p>4</p></li>
   <li class="bar noble" style="height: 76.128359589828px; left: 638px;"><p>4</p></li>
  </ul>
  <table id="legend">
   <tr><td><div class="sport"></div></td><td>Athletes (mainly footballers)</td></tr>
   <tr><td><div class="art"></div></td><td>Artists (mainly actors)</td></tr>
   <tr><td><div class="noble"></div></td><td>Nobles (mainly royal infants)</td></tr>
  </table>
 </div>
 <ul id="line">
  <li style="left: 0px;">1980</li>
  <li style="left: 22px;">1981</li>
  <li style="left: 44px;">1982</li>
  <li style="left: 66px;">1983</li>
  <li style="left: 88px;">1984</li>
  <li style="left: 110px;">1985</li>
  <li style="left: 132px;">1986</li>
  <li style="left: 154px;">1987</li>
  <li style="left: 176px;">1988</li>
  <li style="left: 198px;">1989</li>
  <li style="left: 220px;">1990</li>
  <li style="left: 242px;">1991</li>
  <li style="left: 264px;">1992</li>
  <li style="left: 286px;">1993</li>
  <li style="left: 308px;">1994</li>
  <li style="left: 330px;">1995</li>
  <li style="left: 352px;">1996</li>
  <li style="left: 374px;">1997</li>
  <li style="left: 396px;">1998</li>
  <li style="left: 418px;">1999</li>
  <li style="left: 440px;">2000</li>
  <li style="left: 462px;">2001</li>
  <li style="left: 484px;">2002</li>
  <li style="left: 506px;">2003</li>
  <li style="left: 528px;">2004</li>
  <li style="left: 550px;">2005</li>
  <li style="left: 572px;">2006</li>
  <li style="left: 594px;">2007</li>
  <li style="left: 616px;">2008</li>
  <li style="left: 638px;">2009</li>
 </ul>
</div>

### About the data

I crawled the Wikipedia with [mwclient][1], a library that does exactly this: allows to connect (e.g., from Python) to a Wikimedia-powered site and easily access the properties of the pages. Not related to my goal, it is able to modify pages too.

 [1]: http://sourceforge.net/projects/mwclient/

I looked up at most at 100 people per born year, looking at the categories they were into, and assigning them one or more (usually) broader categories, as "nobles" or "art" or "sport". There were many more, but these accounted for almost all people born after 1980, the period I'm focusing on now.

Looking at the data, Wikipedia-aware people with six years or less are mostly aristocrats, in particular they were mostly sons/daughters of kings somewhere in Europe. Of course there weren't many of them, about fifty in this six years span.

From six years to seventeen, there is an exponential grow of people in the Wikipedia, arriving to almost half a thousand born in 1993. Most of them are child actors from all over the world (USA, but also UK, Europe, and the far east, China and Japan).

Athletes, that began appearing earlier (figure skaters, weightlifters, gymnasts), become predominant from eighteen years old to the end of the period I considered, thirty years old. This happens thanks to the explosion of footballers. Seems that even obscure, second-league soccer players have their fans and so their Wikipedia pages.

### About CSS bar graphs

Simple bar graphs are quite easy to do with pure HTML+CSS solutions, if you are not too demanding about particular features. Using ad-hoc images allows more freedom, but is obviously annoying.

My solution draws bars as list items, absolutely positioned. Hence there is a small annoyance: you have to manually put the left coordinate of the bars. But this is not too bad in 99% of the situations, that is when you use PHP to generate in some way the data. On the bar there is the height value, while the label (i.e., the year) is in another list in the bottom. Sadly this cause the graph to degrade poorly in textual browsers.

Finally there are some cosmetic CSS3 issues: rotated labels, rounded bars, blurred drop shadow, that you should be enjoying if you have a modern browser (Safari 4, Firefox 3.5).
