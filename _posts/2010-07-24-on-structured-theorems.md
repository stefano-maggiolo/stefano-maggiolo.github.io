---
title: On structured theorems
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2010/07/on-structured-theorems/
latex: true
categories:
  - Math
---
One of the main improvement that mathematics underwent is not a theory or a big theorem, but something that you probably don't even notice, being used to it. It is the [mathematical notation][1].

 [1]: http://en.wikipedia.org/wiki/History_of_mathematical_notation

<!--more-->

Apart from the simplest of the symbols, numerals, it is impressive how symbols like \\( + \\), \\( = \\), \\( = \\) were used only beginning from the 13th century. And even after then, a typical mathematician would have written in the following way.

> There do not exist four positive integers, the last being greater than two, such that the sum of the first two, each raised to the power of the fourth, equals the third raised to that same power.

Only between the 19th and the 20th centuries there has been a "symbolic revolution": in 1895, [Giuseppe Peano][2] wrote the *Formulario Mathematico*, where he expresses some of the most important theorems in the new language developed by himself. In 1900, Peano and Russell participate at the second International Congress of Mathematicians in Paris, and the latter was greatly impressed by the work of Peano; after receiving a copy of the *Formulario*, he used the same language to write (with Whitehead) the *Principia Mathematica*, a book that contributed immensely to the global widespread of the new symbolic language.

 [2]: http://en.wikipedia.org/wiki/Giuseppe_Peano

What's so great about using a language specifically devoted to the description of mathematics, instead of using a natural language? Certainly giving concise names to objects is a big advantage (the first to use symbols like \\( a \\), \\( b \\), ... for parameters and \\( x \\), \\( y \\), ... for unknowns was Euler). So we can write the following.

> There do not exist four positive integers \\( x \\), \\( y \\), \\( z \\), \\( n \\), with \\( n \\) greater than two, such that the sum of \\( x \\) and \\( y \\), each raised to the power of \\( n \\), equals \\( z \\), raised to \\( n \\).

It looked a lot better, but still, this is not the main improvement. The symbolic language gives us also a way to be very concise in the expression of concept.

> There do not exist four integers \\( x>0 \\), \\( y>0 \\), \\( z>0 \\), \\( n > 2 \\), such that the sum of \\( x \\) and \\( y \\), each raised to the power of \\( n \\), equals \\( z \\), raised to \\( n \\).

But still this lack of the main advantage. Indeed, when we write the following,

> There do not exist four integers \\( x>0 \\), \\( y>0 \\), \\( z>0 \\), \\( n > 2 \\), such that \\( x^n + y^n = z^n \\).

we are not only being concise, we are being **structured**. The formula splits naturally (to the trained eye) in two parts due to the "equals" sign; the other symbols have an immediate visual relation amongst each other that makes the understanding of the formula much easier. This way of writing adds to the descriptive power of English, the power of pattern recognition that we train every day looking at the world outside us.

Structure is a very important concept when the goal is to make people (including ourselves) understand something. The first thing we look in a math book or a paper is the index; while reading it, if it is not split into short enough, independent units we have trouble keeping the attention needed to follow the argument. What is strange, is that if we go into details, the writers' attention to the structure seems to fade away. This seems unnecessary looking at the statement of the Fermat's theorem above, that is simple enough to be displayed in a single line. But contemporary mathematics often has statements like this.

> Let \\( Y \\) be a smooth complex projective variety, \\( \sum d\_i D\_i \\) a \\( ℚ \\)-divisor (written as a sum of prime divisors) and let \\( L \\) be a line bundle (or Cartier divisor). Assume that \\( D ≔ L + \sum d\_i D\_i \\) is nef and big and that \\( \sum D\_i \\) has only simple normal crossing. Then \\( H^i(Y, O\_Y(K_Y + \lceil D \rceil)) = 0 \\) for \\( i > 0 \\).

There are also much worse examples.

> Let \\( N\_ℤ \\) be a free \\( ℤ \\)-module of finite rank ant \\( N\_ℝ = N\_ℤ ⊗ ℝ \\) the base change to \\( ℝ \\). Let \\( \overline{NE} ⊂ N\_ℝ \\) be a closed convex cone not containing a straight line. Let \\( K \\) be an element of the dual \\( ℚ \\)-vector space \\( N_ℚ^⋆ \\) such that \\( (K ⋅ C) < 0 \\) for some \\( C ∈ \overline{NE} \\). Assume that there exists \\( a(K) ∈ ℤ\_{>0} \\) such that, for all \\( H ∈ N\_ℤ^⋆ \\) with \\( H > 0 \\) on \\( \overline{NE} ∖ \{0\} \\), \\( r ≔ \max\{t ∈ ℝ: H + tK ≥ 0 \textrm{ on } \overline{NE}\} \\) is a rational number of the form \\( u/a(K) \\) (\\( u ∈ ℤ \\)). Then \\( \overline{NE} = \overline{NE}\_{K > 0} + \sum ℝ\_{≥0}[ξ\_i] \\), for a collection of \\( ξ\_i ∈ N\_ℤ \\) with \\( (ξ\_i ⋅ K) < 0 \\) such that the \\( ℝ\_{≥0}[ξ\_i] \\) do not accumulate in the halfspace \\( K < 0 \\).

These examples were taken from a 1998 book, but these kind of statements are pretty much usual. What is clear is that there is no structure in the statements as they are written. But if we read the theorems in our head we organize things:

* there are the objects we start from, each of which has its own properties,
* the relations amongst these objects,
* the conclusions.

Considering the first example, we have the following objects:

* \\( Y \\), that is a smooth complex projective variety;
* \\( \sum d\_i D\_i \\), which is a \\( ℚ \\)-divisor;
* \\( L \\), that is a line bundle.

There are also two conditions:

* \\( D \\) is nef and big;
* \\( \sum D_i \\) is simple normal crossing.

And finally, the result is that for \\( i > 0 \\), we have \\( H^i(Y, O\_Y(K\_Y + \lceil D \rceil)) = 0 \\).

This is the work we do in our head while we read the first statement. As for the second, probably one would have to write things down in an organized way to see clearly what are the objects, the relations, and the conclusions. The question is: why readers still have to do this work for themselves? They were alleviated from the translations between natural language and mathematical objects, but still the logical relations amongst the actors in a theorem are deeply buried into the natural language.

As a more detailed example, I rewrote some pages of the previously mentioned book in a way that emphasizes the structure of theorems' statements. It is a first try, and indeed it looks kind of ugly. But I'm sure that with some notion of design and LaTeX it can look a lot better.

* [The original pages][3].
* [Structured theorems, black and white][4].
* [Structured theorems, colors][5].

 [3]: http://books.google.com/books?id=Lrsvfxuaw7QC&#038;lpg=PP1&#038;pg=PA74#v=onepage&#038;q&#038;f=false
 [4]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2010/07/structured_th_bw.pdf
 [5]: http://poisson.phc.unipi.it/~maggiolo/wp-content/uploads/2010/07/structured_th_col.pdf

*Note*: this post is very influenced from the reading of [How to write a proof][6] by Leslie Lamport. The effort of the author of LaTeX was to emphasize how putting structure in proofs can help avoiding errors. I think that this is because it helps people to understand, so why can't we use the same approach everywhere?

 [6]: http://research.microsoft.com/en-us/um/people/lamport/pubs/lamport-how-to-write.pdf
