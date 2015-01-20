---
title: All possible actions of a cyclic group on an algebraic curve
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2012/05/all-possible-action-of-a-cyclic-group-on-an-algebraic-curve/
latex: true
categories:
  - Math
---
I will present here a small program to compute (a superset of) all possible faithful actions of a cyclic group on a smooth algebraic curve (Riemann surface) of genus g, given the information on a part of the ramification. In other words, the program computes all possible cyclic subgroups of Aut(F) for some curve F of genus g. The actual possibilities may be fewer than the ones computed, because in this first version of the program the only ingredient is Riemann-Hurwitz formula, that is a necessary condition, but not sufficient.

The code is hosted [on github][1].

 [1]: https://github.com/stefano-maggiolo/cyclic_actions

<!--more-->

Let \\( F \\) be a smooth algebraic curve of genus \\( g \\), and \\( C\_r \\) a cyclic group of order \\( r \geq 2 \\) acting faithfully on \\( F \\). Let \\( C = F/G \\) be the quotient curve, of genus \\( h \\), and \\( \pi\colon F \to C \\) the quotient morphism. Riemann-Hurwitz formula tells us that
\\[ 2 g - 2 = r(2h - 2) + \sum\_{p \in F} (|{\rm Stab}\_{C\_r}(p)| - 1). \\]


In other words, the "nice" formula \\( 2g-2 = r(2h-2) \\) must be amended with a term coming from the points in which the morphism \\( \pi \\) is not &eacute;tale. We can simplify the discrepancy using the fact that \\( |{\rm Stab}\_{C\_r}(p)| \\) is the same for all points \\( p \\) in the same orbit (that is, for all points \\( p \\) over the same point \\( q \in C \\)), and we have a total contribution of
\\[ (|{\rm Stab}\_{C\_r}(p)| - 1) \cdot |C\_r \cdot p| = \left( \frac{r}{|C\_r \cdot p|} - 1\right) \cdot |C\_r \cdot p| = r - |C\_r \cdot p| = r - |\pi^{-1}(q)| \\]
from the points over \\( q \\). Writing \\( n\_q = |\pi^{-1}(q)| \\), we can rewrite Riemann-Hurwitz as
\\[ 2 g - 2 = r(2h - 2) + \sum\_{q \in C} (r - n\_q). \\]

The input data for the program are the genus \\( g \\) of \\( F \\) and the information on the counterimage on some branch points of \\( C \\), that is, some points in which the counterimage fails to have \\( r \\) points. For example, we may ask for all cyclic actions on a curve of genus \\( 4 \\) such that there are two points with \\( n\_q = 1 \\) and one point with \\( n\_q = 2 \\).

The first observation is that \\( r \\) is forced to be a multiple of the lcm of all prescribed \\( n\_q \\): if there are \\( n\_q \\) points in a orbit, an element of \\( C\_r \\) must have order exactly \\( n\_q \\), and so \\( n\_q \\vert r \\).

The second observation is that we need to have at least \\( g = 2 \\) or \\( g = 1 \\) and one prescribed point of ramification to have a limit on \\( r \\).

Let \\( Q' \\) be the discrepancy in Riemann-Hurwitz formula. The third observation is that we can factor out the prescribed ramification as in
\\[ Q' = Q + \sum\_{q}(r - n\_q) = Q + Nr - c,\\]
where \\( q \\) varies among the points with prescribed ramification, \\( N \geq 0 \\) is the number of points of \\( C \\) with prescribed ramification, \\( c > 0 \\) is a constant, and \\( Q \geq 0 \\) is the (potential) additional contribution from the ramification.

The program is now straightforward. We try every \\( r \\) that is a multiple of the lcm, starting from \\( 2 \\) upwards. For every such \\( r \\) we can express the genus of \\( C \\) as
\\[ h = \frac{(2-N)r + (2g - 2 + c) - Q}{2r} = \frac{(2-N)r + c' - Q}{2r}. \\]
Since \\( h \\) is a non-negative integer and the only parameter that can vary is the non-negative \\( Q \\), there are only a finite number of values for \\( h \\). For every such values, we need to find out if there is a configuration of branch points that can realize that contribution. To do so, we compute the possible contributions to the discrepancy for a branch point in \\( C \\), that are of the form \\( (i - 1) \cdot r / i \\) for a divisor \\( i \\) of \\( r \\), and we can recursively find out all linear combinations of those discrepancies that sum to \\( Q \\).

The only thing still open is to find an upper limit for \\( r \\). As before, solving for \\( h \\) gives us
\\[ h = \frac{(2-N)r + c' - Q}{2r}. \\]
Since \\( h \geq 0 \\) and \\( r \geq 2 \\), the numerator is non-negative. On the other hand, if we solve for \\( Q \\) we obtain
\\[ Q = (2-N)r + c' - 2 r h \\]
that is again non-negative.

We obtain three cases depending on the sign of the coefficient of \\( r \\), that is, depending on the sign of \\( 2-N \\).

Case \\( 2-N < 0 \\). In this case, we obtain
\\[ r \leq \mathrm{min} \left\\{ \frac{c' - 2 r h}{N-2}, \frac{c' - Q}{N-2} \right\\} \Longrightarrow r \leq \frac{c'}{N-2}, \\]
since both \\( h \\) and \\( Q \\) are non-negative.

Case \\( 2-N = 0 \\). Since \\( Q \geq 0 \\), we obtain that either \\( h = 0 \\) or \\( r \leq c'/2h \\), so we need to care only for a bound when \\( h = 0 \\) (where, \\( Q = c' \\) is constant). Note that for any \\( r \\), the smallest non-zero contribution to \\( Q \\) is \\( (i-1)\cdot r/i \\) for the smallest non-trivial divisor \\( i \\) of \\( r \\). In particular, the smallest contribution is at least \\( r/2 \\). Therefore, we can use as a limit \\( r \leq 2c' \\).

Case \\( 2-N > 0 \\). Of course \\( 2-N \leq 2 \\); we have \\( Q = (2-N-2h)r + c' \\). If \\( 2-N-2h \leq 0 \\) there are no problems since \\( Q \\) is bounded and we can limit \\( r \\) to twice the maximum \\( Q \\) as in the previous case. If \\( 2-N-2h > 0 \\), then \\( Q = r + c' \\) or \\( Q = 2r + c' \\), and it seems that \\( r \\) cannot be bounded. What happens is that \\( c' \\), the difference between \\( Q \\) and the nearest multiple of \\( r \\), become relatively smaller and smaller as \\( r \\) increases, and then \\( Q \\) cannot be realized with the possible contributions. It is hard enough to estimate a bound on \\( r \\) based on this, but it is much easier to limit \\( r \\) using a result of Wiman in 1895 that states that the maximum order of an automorphism of a Riemann surface is \\( 2(2g + 1) \\).
