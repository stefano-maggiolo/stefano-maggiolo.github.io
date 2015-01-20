---
title: If it looks like a word, it is a word one third of the time
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2014/08/if-it-looks-like-a-word-it-is-a-word-one-third-of-the-time/
categories:
  - Statistics
---
With the [last post][1], we looked at words of three letters in the Google corpora for six languages, to understand which language has the most three-letter words. But our original question was which one has the most ratio of words among trigrams that "look like" real words, and today we are going to answer that question.

 [1]: {% post_url 2014-07-07-if-it-looks-like-a-words-then-it-is-a-word %}

<!--more-->

Defining what looks like a real word might be difficult, because the answer is ultimately subjective, but we can again perform a simple statistical computation to get a good enough approximation.

I decided to define that a trigram *abc* looks like a word if:

  * the trigram *abc* occurs in any part of any word;
  * the bigram *ab* occurs as the starting part of any word;
  * the bigram *bc* occurs as the ending part of any word;

We could use again the Google corpora, limiting ourself to "common" words, but since the definition uses occurrences in *any* words, it should be enough to look in a dictionary. Also, to make everything a little more robust, I require that there are at least three occurrences of the trigram or bigram within the dictionary, not only one.

Using the script extract.py in [this GitHub gist][2], we construct for each language a list of trigrams that look like words, starting from the standard dictionaries provided with Ubuntu. These are the number of such trigrams by language.

 [2]: https://gist.github.com/stefano-maggiolo/f8ddab487ab7ba4bd204

| Language         | Trigrams that look like words |
| ---------------- | ----------------------------- |
| American English | 3364                          |
| British English  | 3366                          |
| German           | 2492                          |
| Spanish          | 2065                          |
| Italian          | 911                           |
| French           | 1911                          |

English has the most of these trigrams, followed by German, Spanish, French, and Italian. The variance is very high; judging from my knowledge of the two extremes (English and Italian), I can argue that Italian is more strict in the order that letters can follow each other (usually alternating consonants and vowels). [[^1]]

 [^1]: I wonder if this has any consequence on how easy is to define a crossword in the two languages. Sadly I could not find any good source on this fundamental issue, I think also due to the lack of multilingual crossword authors. The Wikipedia entry shows examples of a Japanese-style grid, which seems very influenced by the stricter alternation of consonants and vowels. By experience, that is also the style of many Italian crosswords, but not necessarily the unique.

To obtain the ratios, we just need to use merge.py in the same gist to intersect the list of trigrams with the list obtain via Google nGrams. Here are the results by language.

| Language         | Trigrams looking like words | Three-letter words | Ratio |
| ---------------- | --------------------------- | ------------------ | ----- |
| American English | 3364                        | 1026               | 30%   |
| British English  | 3366                        | 1034               | 31%   |
| German           | 2492                        | 679                | 27%   |
| Spanish          | 2065                        | 529                | 26%   |
| Italian          | 911                         | 398                | 44%   |
| French           | 1911                        | 615                | 32%   |

Apparently, I was wrong! It's not English that shows a high ratio of three-letter words but... Italian. This of course is mainly due to the much lower number of trigrams in Italian. It is also interesting to see that German is close to be the language with the lowest ratio despite being the one with the most frequent usage of three-letter words; but we already saw that that is because its most frequent three-letter words are really frequent.
