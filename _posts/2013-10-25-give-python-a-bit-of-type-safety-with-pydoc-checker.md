---
title: Give Python a bit of type safety with Pydoc Checker
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2013/10/give-python-a-bit-of-type-safety-with-pydoc-checker/
categories:
  - Software
---
We all love **Python**: it is easy to learn, expressive, powerful and with impressive libraries to perform complicate operations with only a few keystrokes. We love it so much that it ends up being used in projects big enough for its limitations and drawbacks to appear. Not that I am not guilty of this. And for this exact reason, I wrote **[Pydoc Checker][1]**, a small module that addresses one of these issues: the (too) dynamic type system.

 [1]: https://github.com/stefano-maggiolo/pydocchecker

<!--more-->

I am not an expert in **typing systems**, and this is not an essay against or pro one of them. I am just presenting some experience in being a co-author of [CMS][2], a suite of Python programs handling programming contests.

 [2]: http://github.com/cms-dev/cms

Within CMS, dynamic (and in particular duck) typing has been quite nice, especially in the **beginning**. The advantage being able to refactor parts of the code without the need to touch the rest: the same code could handle files and file-like objects in the exact same way, without having an intricate hierarchy of File(Buffered)?(Input\|Output)(Stream)? classes in the library.

Though, when the project became **larger**, and the code more **stable**, I often found hard to isolate code while reading it: to understand a method, often I went back to the caller to look at what kind of data it was passing. Often functions are overloaded, in the sense that they accept their inputs in different format; this is also very hard to track in Python since the contract of a function is hidden in its implementation. This limits the isolation even in the other direction: to understand how a function works, you also need to understand the contract of the functions it calls, by *looking at their implementation*.

For this reason, we started writing **type annotations** in the Pydoc comment of functions and methods, for each argument and for the return type. It did not start with a formal decision of the team; instead, I like to think that having these annotations was easily recognized so helpful that their usage spread contagiously through the team. You can see examples throughout the [code][3].

 [3]: https://github.com/cms-dev/cms/blob/master/cms/service/EvaluationService.py

Still, there is an issue: do you **trust your callers** to fulfill your (now explicit) contract? Especially after some refactoring, it is nice that the same code that handles a file also handles your new file-like object, but it is even nicer if you are informed whether somebody *checked that it actually works* with that particular file-like object. Assumptions on the specific types happen more often than one would desire, and most of the time they are hard to spot. If some code appears to work with another type it was not designed to work with, and it does without any warning, these assumptions become completely invisible.

[Pydoc Checker][1] modifies the functions and methods in your code adding a run-time validation of the type of the arguments, of the return value, and of the exceptions raised, based on the types declared in the Pydoc of the function or method. Running the testsuite with Pydoc Checker, and also leaving it enabled during the manual testing, **greatly increases the confidence** that the code follows the requests of the annotations, and by transitivity, of you, the programmer.

A **similar approach** is followed by the JS compilers included in Closure, that tries to infer as much type information as possible from the code and from the type annotations in the JSDoc, and to confirm that there is a match between the guarantees of the callee and the request of the caller. The Closure approach is much more sophisticated (type inference is hard), and has the big advantage of happening at compile time, but has also some drawbacks: if the compiler is not able to infer some types, it is possible that further annotations silently become useless. Happening at run-time, instead, Pydoc Checker's checks are always performed for each annotated functions.
