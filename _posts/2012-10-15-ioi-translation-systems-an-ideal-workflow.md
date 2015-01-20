---
title: 'IOI translation systems: an ideal workflow'
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2012/10/ioi-translation-systems-an-ideal-workflow/
categories:
  - Typography
---
In this second post of the series, I will present the idea we had in mind when we proposed the new software used to handle translations at IOI 2012.

<!--more-->

As said in the [first post][1] a **document-based** translation forces the translator to remember, for every paragraph, the version they started from; moreover, it asks them to identify the translated paragraph corresponding to one in the official statement that was changed.

 [1]: {% post_url 2012-10-09-ioi-translation-systems-a-survey-of-possible-approaches %}

The solution to both these problems is to use a **paragraph-based** translation system. Translators do not get a document to translate but a list of sentences, that a priori have no relations one with another. This approach is commonly used for localizing software, where the strings are really uncorrelated. But as we will see, it can be applied nicely to a situation as the IOI translations, as long as we add a final rendering step that glue together all the translations with the original parts that were left untranslated.

The **ideal workflow** is therefore similar to the following.

* Translators get the first version (let us call it `v`) of the statement to translate, as a list of translatable strings, internally marked as `(str_id, v)`.
* They start translating strings, each one saved as `(lang_id, str_id, v)`. This allows working at the same time on the same document: they just need to translate different strings.
* When the official statement get changed to version `v'`, there can be five situations arising: a string is left unchanged; a string is changed; a string is deleted; a new string is added; strings are reordered.
  * In the first case, the system create a copy of `(lang_id, str_id, v)` changing `v` to `v'`, thus the new version already has the translation for that string.
  * In the second case, the translation is again copied, but the new one is also marked as "incomplete", and the translator is prompted to update it; the changes are presented with a graphical diff tool and are much easily spotted since it is known that a change is in that string, and the string is quite short.
  * In the third case, no actions are required and the translation simply is not propagated to `v'`.
  * In the fourth case, the translator will be prompted to translate the new string.
  * The fifth case is exactly the same as the first one, as the translators are not required to do anything: the change involves only the final rendering.
* The contest administrators will change the statement without worrying about which situations their changes will create: an automated process compares the strings in the two versions and chooses the best behavior.
* In the end, the translators render a PDF file ready to be printed or handed to the contest admins.

This simple workflow surely hides a lot of technical details, even before thinking of an actual software implementing it. Remember that one of the requirements on the translation software is that combining its diffusion and its simplicity, it should be usable by anyone. A translation software as the one we are introducing is surely new, hence it must be as simple as possible, with respect to formatting and typesetting (especially, mathematics).

Being a string-based software, all **characters** (e.g., non-latin), **formatting** and **mathematics** must be encoded as a human-readable string. Characters can be safely treated using Unicode and pose no problems. To handle formatting, we need some simple markup language (such as TeX, HTML, Markdown, or Wiki markup), that can be edited both as raw text or with a simple WYSIWYG editor. Finally, very simple mathematics can be encoded with Unicode characters or with formatting tags (for superscript and subscript, for example), whereas more complex mathematics should follow a TeX-like approach.

So, it seems that we threw away TeX only to have it coming back here. This is not exactly the case, as there is an advantage of the string-based approach that we did not yet consider: **not everything must be translated**. For example, formatting that has to be applied to a whole paragraph or heading could be encoded in the non-translatable part, leaving to the translator only content without formatting. Complex mathematics is often displayed on its own, and thus can be left as non-translatable too.

The problem persists when we have mathematics or formatting to be applied inside a paragraph (for example, setting a word in bold or italic). In different languages the order of the words may change, so it is not possible to offer three strings for translation, one for before, one for after, and one for the word or the mathematics. I do not have a brilliant solution for this, but I believe that, at least for the kind of documents involved in an IOI, the amount of formatting or mathematics inside a paragraph is minimum, and boils down to learning how to do these:

  * emphasis (bold or italic);
  * code (monospace font);
  * subscript and superscript;
  * copy and paste from the original statement the characters not easy to input, like typographical quotes, dashes, math characters.

During the translations at IOI we received only one objection to this workflow: the delegation from China observed that to have a good translation they often need to exchange the order of the paragraph. Clearly this is not possible with the string-based approach (in a clean way --- it is of course possible to translate sentences "in the wrong place" to reorder them). I am not sure about how much the reordering is a necessity, as other Chinese people I spoke with agreed with them but did not consider it a must. I am currently not sure on how the workflow could be adapted to this without introducing a new layer of difficulties for all the other languages, so for the moment I will ignore the problem.

In the third part of the series I will present an actual software that tries to offer the workflow we saw here. There are many more technical problems, that will be explained in an unbiased way.

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
