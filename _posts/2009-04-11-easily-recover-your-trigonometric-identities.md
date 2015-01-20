---
title: Easily recover your trigonometric identities
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2009/04/easily-recover-your-trigonometric-identities/
latex: true
categories:
  - Math
---
I will present here my experience in Italian high schools; namely, the main goal of studying math in high school (at least, in the first half, not in the specialization part) should be learning how to recover facts and concept (and formulas), not memorizing pages of formulas. However, in most cases some concept are more prone to be filled with long formula to remember. One example is trigonometry.

<!--more-->

At high school you learn some basic definitions and facts about trigonometry; after that, you'd like to solve some equations, but shortly after you have to learn the infamous...

  * ... duplication formulas:
    \\[ \sin(2\alpha) = 2 \sin \alpha \cos \alpha \textrm{,} \\]
    \\[ \cos(2\alpha) = \cos^2 \alpha - \sin^2 \alpha \textrm{;} \\]

  * ... bisection formulas:
    \\[ \sin\left(\frac{\alpha}{2}\right) = \sqrt{\frac{1-\cos \alpha}{2}}\textrm{,} \\]
    \\[ \cos\left(\frac{\alpha}{2}\right) = \sqrt{\frac{1+\cos \alpha}{2}}\textrm{;} \\]

  * ... addition formulas:
    \\[ \sin(\alpha+\beta) = \sin \alpha \cos \beta + \sin \beta \cos \alpha\textrm{,} \\]
    \\[ \cos(\alpha+\beta) = \cos \alpha \cos \beta + \sin \alpha \sin \beta\textrm{;} \\]

  * ... "prostaferesi" (don't know the English name) formulas:
    \\[ \sin \alpha + \sin \beta = 2 \sin \left(\frac{\alpha+\beta}{2}\right) \cos \left(\frac{\alpha-\beta}{2}\right)\textrm{,} \\]
    \\[ \cos \alpha + \cos \beta = 2 \cos \left(\frac{\alpha+\beta}{2}\right) \cos \left(\frac{\alpha-\beta}{2}\right)\textrm{;} \\]

  * ... Werner formulas:
    \\[ \sin \alpha \cos \beta = \frac{1}{2} \left( \sin(\alpha+\beta) + \cos(\alpha-\beta)\right)\textrm{,} \\]
    \\[ \sin \alpha \sin \beta = \frac{1}{2} \left( \cos(\alpha-\beta) - \cos(\alpha+\beta)\right)\textrm{,} \\]
    \\[ \cos \alpha \cos \beta = \frac{1}{2} \left( \cos(\alpha+\beta) + \cos(\alpha-\beta)\right)\textrm{.} \\]

Obviously there are many relations amongst these formulas, but depending on the sadisticness of the teacher, he could not highlight the relations, or even warn you to remember also the versions with different signs, or the corresponding formulas for the tangent...

This won't come as a surprise, but there is a much simpler way to recover all these identities without learning them by heart, or remembering obscure geometric proofs. The key point is the **Euler identity** [[^1]], that is \\( e^{i\alpha} = \cos \alpha + i \sin \alpha \\). Too bad that most high school students don't know what a complex number is before learning trigonometry; however, understanding Euler identity require just a little faith even from the most skeptical student: just let them know that we can call \\( e^{i\alpha} \\) the point in the \\( (1,i) \\)-plane corresponding to \\( \cos \alpha \\) times \\( 1 \\) and \\( \sin \alpha \\) times the symbol \\( i \\). Oh, and that it happens that \\( i^2 = -1 \\) (ok, this may require a little more faith). Or the teacher could also present it as a formal statement.

 [^1]: Maybe you heard about the most beautiful formula of mathematics, \\( e^{i \pi} + 1 = 0 \\); it follows from Euler identity putting \( \alpha = \pi \).

What is important is that we are much more able to manipulate exponentials than trigonometric functions; basically, to recover all the previous formulas, we translate trigonometric functions to exponentials, manipulate them, and translate them back to trigonometry, where all \\( i \\) will cancel (if not, we did an error somewhere). Euler identity tells us how to go from exponentials to trigonometry, we need to know how to translate in the other way. But this is simple: from
\\[ e^{i\alpha} = \cos \alpha + i \sin \alpha\textrm{,} \\]
\\[ e^{-i\alpha} = e^{i(-\alpha)} = cos(-\alpha) + i \sin(-\alpha) = \cos \alpha - i \sin \alpha\textrm{,} \\]
taking sum or difference, we get
\\[ \cos \alpha = \frac{e^{i\alpha} + e^{-i\alpha}}{2}\textrm{,} \\]
\\[ \sin \alpha = \frac{e^{i\alpha} - e^{-i\alpha}}{2i}\textrm{.} \\]

Now we are ready for an example:
\\[ \sin(\alpha+\beta) = \frac{e^{i(\alpha+\beta)}- e^{-i(\alpha+\beta)}}{2i} = \\]
\\[ = \frac{1}{2i} \bigg( e^{i \alpha + i \beta} - e^{-i\alpha - i\beta} \bigg) = \\]
\\[ = \frac{1}{2i} \bigg( e^{i\alpha} e^{i\beta} - e^{-i\alpha}e^{-i\beta} \bigg) = \\]
\\[ = \frac{1}{2i} \Bigg( \big(\cos \alpha + i \sin \alpha\big)\big(\cos\beta +i\sin\beta\big) - \\]
\\[ \qquad - \big(\cos(-\alpha) + i \sin(-\beta)\big)\big(\cos(-\beta) + i\sin(-\beta)\big) \Bigg) = \\]
\\[ = \frac{1}{2i} \Bigg( \big(\cos \alpha + i \sin \alpha\big)\big(\cos\beta +i\sin\beta\big) - \\]
\\[ \qquad - \big(\cos\alpha - i \sin\beta\big)\big(\cos\beta - i\sin\beta\big) \Bigg) = \\]
\\[ = \frac{1}{2i} \Bigg( \cos \alpha \cos\beta + i \cos\alpha\sin\beta + i \sin \alpha \cos\beta + i^2\sin\alpha\sin\beta - \\]
\\[ \qquad - \big(\cos\alpha\cos\beta - i\cos\alpha\sin\beta -i\sin\beta\cos\alpha + i^2 \sin\alpha\sin\beta\big) \Bigg) = \\]
\\[ = \frac{1}{2i} \Bigg( \cos \alpha \cos\beta + i \cos\alpha\sin\beta + i \sin \alpha \cos\beta - \sin\alpha\sin\beta - \cos\alpha\cos\beta + \\]
\\[ \qquad + i\cos\alpha\sin\beta + i\sin\beta\cos\alpha + \sin\alpha\sin\beta) \Bigg) = \\]
\\[ = \frac{1}{2i} \Bigg( 2 i \cos\alpha\sin\beta + 2i \sin\alpha\cos\beta \Bigg) = \\]
\\[ = \cos\alpha\sin\beta + \sin\alpha\cos\beta\textrm{.} \\]

This computation seems long, but it is elementary and fast, since most terms cancel with each other. The other formulas follows with the same principle: translate to exponentials, manipulate the exponentials, do the simplifications, translate back to trigonometry.
