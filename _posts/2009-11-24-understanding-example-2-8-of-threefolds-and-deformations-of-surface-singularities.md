---
title: Understanding Example 2.8 of “Threefolds and deformations of surface singularities”
author: Stefano Maggiolo
layout: post
original_url: http://poisson.phc.unipi.it/~maggiolo/index.php/2009/11/understanding-example-2-8-of-threefolds-and-deformations-of-surface-singularities/
latex: true
categories:
  - Math
---
As it always happens, examples and more in general... everything, look much more easier when you work out all the details. But often, at first they does not seem so easy. Since I know my memory is very bad, usually when I want something to last I commit it to some TeX file. Why don't make it public? And here I am.

<!--more-->

Just two notes before starting: the technical one is that in order to have TeX formulas compiling, you need to do as instructed in [this page][1]; the mathematical one is that at the end there is a small appendix with some information on concepts and terms that are so renowned amongst expert that you can't find their meaning anywhere.

 [1]: http://math.etsu.edu/LaTeXMathML/

The paper from which the example is taken is "Threefolds and deformations of surface singularities" by Koll&aacute;r and Shepherd-Barron, published in vol. 91, n. 2 of Inventiones Mathematicae in 1988 (pag. 299-338); nonetheless, they write that it was already noted, e.g. by Pinkham in his PhD thesis.

A theorem of Laufer states that if \\( f\colon X \to Y \\) is a flat family of normal surfaces with at worst Gorenstein singularities, then \\( K\_{\\mathrm{rel}, y}^2 \\) is lower semi-continuous and moreover it is locally constant if and only if \\( f \\) admits a very weak resolution of singularities, possibly after finite and surjective base change.

The example shows that the assumption regarding Gorenstein singularities is necessary, at least for the second part of the statement. So they exhibit a family with \\( K\_{\\mathrm{rel}, y}^2 \\) constant but without a very weak resolution, even after base change (hence with a singularity worst than Gorenstein). For comparison, they also show a family with \\( K\_{\\mathrm{rel}, y}^2 \\) constant admitting a very weak resolution. But there is a simple way to distinguish the two situations: in the former case, the self-intersection of the canonical divisor on the resolution of the fibers varies along the family, while in the latter it is constant.

The construction outlined in the paper is the following. Consider two subvarieties of \\( \\mathbb{P}^5 \\):

* the Veronese surface \\( V \\);
* the scroll \\( F = \\mathbb{P}(O\_{\\mathbb{P}^1}(2)^{\\oplus 2}) \\) embedded via \\( O\_F(1) \\).

The former is easy. As for the latter, one notes immediately that, as said in Beauville's "Complex algebraic surfaces", \\( F \\) is isomorphic to \\( \\mathbb{P}^1 \times \\mathbb{P}^1 = \\mathbb{P}(O\_{\\mathbb{P}^1}^{\\oplus 2}) \\), since tensoring the sheaf by an invertible one does not change the resulting scroll. Then, why do they use \\( O\_{\\mathbb{P}^1}(2) \\)? Because so the natural embedding via \\( O\_F(1) \\) is the one they need. Indeed, as we will see, \\( O\_F(1) = O\_{\\mathbb{P}^1\times \\mathbb{P}^1}(1,2) \\) that has six global sections.

Recall that \\( O\_F(1) \\) is defined in this way:

* consider \\( E \to \\mathbb{P}^1 \\), the vector bundle associated to the sheaf \\( O\_{\\mathbb{P}^1}(2)^{\\oplus 2} \\);
* take the pullback \\( \pi^\star E \to F \\), where \\( \pi\colon F \to \\mathbb{P}^1 \\) is the projection;
* this bundle has a natural sub-bundle \\( N \\), since a point \\( L \in F \\) over \\( p \in \\mathbb{P}^1 \\) corresponds to a line \\( L \subseteq E\_p \\);
* \\( O\_F(1) \\) is the cokernel of the injection \\( N \to \pi^\star E \\).

To compute \\( O\_F(1) \\) we can use the adjunction formula for the canonical divisor of a projective bundle, and the fact that we know that \\( K\_F = O\_{\\mathbb{P}^1 \times \\mathbb{P}^1}(-2,-2) \\). The adjuntion formula states that for a projective bundle \\( p\colon F = \\mathbb{P}\_B(E) \to B \\), indeuced by a rank \\( r \\) vector bundle \\( E \\), then we have
\\[ K\_F = p^\star(K\_B + \det E) \\otimes O\_F(-r). \\]
In our case, \\( K\_B = O\_{\\mathbb{P}^1}(-2) \\), while \\( \det E = O\_{\\mathbb{P}^1}(4) \\); so \\( O\_F(2) = O\_{\\mathbb{P}^1 \times \\mathbb{P}^1}(2,4) \\), hence the result.

Consider coordinates \\( [x\_i] \\) and \\( [\bar{x}\_i] \\) on \\( \\mathbb{P}^1 \\), \\( [y\_i] \\) on \\( \\mathbb{P}^2 \\), \\( [a\_i] \\) on \\( \\mathbb{P}^5 \\), \\( [b\_i] \\) on \\( \\mathbb{P}^6 \\). The Veronese \\( V \\) is given by the map
\\[ [y\_i] \mapsto \left[y\_0^2, y\_1^2, y\_2^2, y\_1 y\_2, y\_0 y\_2, y\_0 y\_1\right] \\]
or equivalently (recall that the Veronese is not a complete intersection) by the homogeneous ideal
\\[I\_V = (a\_0 a\_1 - a\_5^2, a\_0 a\_2 - a\_4^2, a\_1 a\_2 - a\_3^2, a\_0 a\_3 - a\_4 a\_5, a\_1 a\_4 - a\_3 a\_5, a\_2 a\_5 - a\_3 a\_4). \\]
The scroll \\( F \\) is given by the map
\\[ ([x\_i], [\bar{x}\_i]) \mapsto \left[x\_0 \bar{x}\_0^2, x\_1\bar{x}\_0^2, x\_0\bar{x}\_1^2, x\_1\bar{x}\_1^2, x\_0 \bar{x}\_0\bar{x}\_1, x\_1\bar{x}\_0 \bar{x}\_1\right] \\]
or by the ideal
\\[ I\_F = (a\_0 a\_2 - a\_4^2, a\_1 a\_3 - a\_5^2, a\_0 a\_3 - a\_1 a\_2, a\_0 a\_5 - a\_1 a\_4, a\_2 a\_5 - a\_3 a\_4). \\]

Now we consider the cones \\( C\_V \\) and \\( C\_F \\) in \\( \\mathbb{P}^6 \\) over the two varieties \\( V \\) and \\( F \\) (which are described by the same ideals with \\( b\_i \\) instead of \\( a\_i \\)) and cut them with a pencil of hyperplanes \\( H\_t \\), exactly one of which passes through the same vertex \\( Q = [0, \ldots, 0, 1] \\) of the two cones. We assume that \\( H\_0 \\) is the hyperplane passing through \\( Q \\), and that its intersection with \\( V \\) and \\( F \\) is general, in the sense that the conic cut out on \\( \\mathbb{P}^2 \\) and the curve of bidegree \\( (1,2) \\) cut out on \\( \\mathbb{P}^1 \times\\mathbb{P}^1 \\) are both irreducible. Of course this is an open and non-empty condition, so that a random choice will do. But as often happens most of the "simple" choices are far from being random, and so one has to be careful. Indeed, we cannot take \\( b\_i = 0 \\) for some \\( 0 \leq i \leq 5 \\), since this would be a double line (if \\( i \leq 2 \\)) or a couple of lines (if \\( i \geq 3 \\)) on \\( \\mathbb{P}^2 \\), and also some other union of lines on \\( \\mathbb{P}^1 \times \\mathbb{P}^1 \\). A choice that will do is for example \\( b\_0 = b\_4 \\), as in \\( \\mathbb{P}^2 \\) this gives the irreducible conic \\( y\_0^2 = y\_1 y\_2 \\), while on \\( \\mathbb{P}^1 \times \\mathbb{P}^1 \\) gives the irreducible curve \\( x\_0 \bar{x}\_0^2 = x\_1 \bar{x}\_1^2 \\).

On the other hand, if \\( H\_t \\), for \\( t \neq 0 \\), is a hyperplane not passing through \\( Q \\) (as we want it to be), the varieties it cuts out on \\( C\_V \\) and \\( C\_F \\) are obviously isomorphic to \\( V \\) and \\( F \\), so there are no other restrictions to \\( H\_t \\) for \\( t \neq 0 \\).

A family of hyperplanes over the affine line satisfying these conditions is \\( \{H\_t = (t b\_6 = b\_0 - b\_4)\} \\). As we said, the general fibers of the two families of hyperplane sections are respectively \\( V \cong \\mathbb{P}^2 \\) and \\( F \cong \\mathbb{P}^1 \times \\mathbb{P}^1 \\). What are the central fibers, over \\( t = 0 \\)? We just need to put \\( b\_0 = b\_4 \\) on the ideals \\( I\_V \\) and \\( I\_F \\) (after changing \\( a\_i \\) with \\( b\_i \\)), or, in other words, take the cones over the images via the maps defining \\( V \\) and \\( F \\) of the curves defined by \\( y\_1 = \frac{y\_0^2}{y\_2} \\) on \\( V \\) and by \\( x\_0 = x\_1 \frac{\bar{x}\_1^2}{\bar{x}\_0^2} \\) on \\( F \\). It is easy to understand that the images of these curves are \\( \\mathbb{P}^1 \\) embedded in \\( \\mathbb{P}^4 \\) via \\( O\_{\\mathbb{P}^1}(4) \\):

* the restriction of \\( O\_{\\mathbb{P}^2}(2) \\) to a conic is \\( O\_{\\mathbb{P}^1}(4) \\);
* an irreducible smooth curve of bidegree \\( (m,n) \\) in \\( \\mathbb{P}^1\times \\mathbb{P}^1 \\) has genus \\( (m-1)(n-1) \\), so our curve of bidegree \\( (1,2) \\) is \\( \\mathbb{P}^1 \\) and the restriction of \\( O\_{\\mathbb{P}^1\times \\mathbb{P}^1}(1,2) \\) is just \\( O\_{\\mathbb{P}^1}(4) \\).

Another longer way is doing the computation. The maps become:
\\[ [y\_i] \mapsto \left[y\_0^2, \frac{y\_0^4}{y\_2^2}, y\_2^2, \frac{y\_0^2 y\_2}{y\_2}, y\_0 y\_2, \frac{y\_0^3}{y\_2}\right] = \left[y\_0^2 y\_2^2, y\_0^4, y\_2^4, y\_0^2 y\_2^2, y\_0 y\_2^3, y\_0^3 y\_2\right] \\]
and
\\[ ([x\_i], [\bar{x}\_i]) \mapsto \left[x\_1 \bar{x}\_1^2, x\_1\bar{x}\_0^2, x\_1 \frac{\bar{x}\_1^4}{\bar{x}\_0^2}, x\_1\bar{x}\_1^2, x\_1 \frac{\bar{x}\_0\bar{x}\_1^3}{\bar{x}\_0^2}, x\_1\bar{x}\_0 \bar{x}\_1\right] = \left[ \bar{x}\_0^2\bar{x}\_1^2, \bar{x}\_0^4, \bar{x}\_1^4, \bar{x}\_0^2 \bar{x}\_1^2, \bar{x}\_0\bar{x}\_1^3, \bar{x}\_0^3 \bar{x}\_1\right]. \\]
One sees immediately that these images are just rational normal curves of degree \\( 4 \\)

We have proved that the central fibers are the cones over these curves (in particular, they are isomorphic). Note that such a cone is isomorphic, as a scheme, to the weighted projective plane \\( \\mathbb{P}(1,1,4) \\). Indeed, such a space is defined as \\( \\mathrm{Proj} \\mathbb{C}[x\_0, x\_1, z] \\) with \\( \deg x\_i = 1 \\) and \\( \deg z = 4 \\) and the natural way to embed it in a projective space is to consider the lcm of \\( (1,1,4) \\), \\( 4 \\), and all the monomials of degree \\( 4 \\) as coordinates in a projective space. Of course one as to mod out by the inevitable relations that this process creates. Here, for example, we have
\\[ \\mathbb{P}(1,1,4) \cong \\mathrm{Proj} \\mathbb{C}[x\_0^4, x\_0^3 x\_1, x\_0^2 x\_1^2, x\_0 x\_1^3, x\_1^4, z] = \\]
\\[ = \\mathrm{Proj}\\mathbb{C}[a\_0, \ldots, a\_5] / (a\_0 a\_4 = a\_2^2 = a\_1 a\_3, a\_0 a\_2 = a\_1^2, a\_2 a\_4 = a\_3^2). \\]
This is exactly the cone over the rational normal curve in \\( \\mathbb{P}^4 \\).

Coming back to the example, we need to compute \\( K\_{\\mathrm{rel}, t}^2 \\) for the two families. This is trivially zero over \\( t \neq 0 \\), since the fibers are smooth. The minimal resolution of the central fibers is \\( \\mathbb{P}^1 \times \\mathbb{P}^1 \to \\mathbb{P}(1,1,4) \\), obtained blowing up the vertex \\( Q \\). There is one exceptional curve \\( E \\), but \\( E^2 = 0 \\) (it is a line in \\( \\mathbb{P}^1 \times \\mathbb{P}^1 \\)), so \\( K\_{\\mathrm{rel}, t}^2 = (aE)^2 = 0 \\), whatever the coefficient \\( a \\) in \\( E \cdot aE = E \cdot K \\) is.

Using the same construction, we observe that there exists a very weak simultaneous resolution of the family \\( \{H\_t \cap C\_F\} \\), obtained exactly blowing up \\( Q \\) in \\( \\mathbb{P}^6 \\); the strict transform of the central fiber will be exactly \\( \\mathbb{P}^1\times \\mathbb{P}^1 \\). Conversely, \\( \{H\_t \cap C\_V\} \\) don't admits a very weak simultaneous resolution. For, we will show that every birational modification of the family as a threefold would introduce an exceptional locus of dimension two, and therefore it would not be a very weak resolution.

To do so, we will show that the singularity of \\( C\_V \\) at the vertex is of the kind \\( \\mathbb{C}^3 / (x = -x) \\). Notice that two different hyperplanes \\( H\_t \\) and \\( H\_s \\) meet only in the hyperplane \\( b\_6 = 0 \\). So if we restrict to \\( b\_6 = 1 \\), the threefold of the family is embedded in \\( \\mathbb{P}^6 \setminus (b\_6 = 0) \\), that is, in the affine six-space, and we can study the singularity here. One sees immediately that this restriction is affine, and corresponds to the ring \\( \\mathbb{C}[y\_0^2, y\_1^2, y\_2^2, y\_1 y\_2, y\_0 y\_2, y\_0 y\_1] \\). But this is exactly the ring of invariant of \\( \\mathbb{C}[y\_0, y\_1, y\_2] \\) with respect to the action of \\( \\mathbb{Z}\_2 \\) that changes the sign.

Hence our claim on the type of the singularity is true. Now, we have to show that every resolution of this singularity introduce an exceptional locus of dimension \\( 2 \\). Indeed, if we blow up the origin in \\( \\mathbb{C}^3 \\), we obtain a lifting of the action of \\( \\mathbb{Z}\_2 \\), the exceptional locus being a copy of \\( \\mathbb{P}^2 \\), and the quotient is smooth. So every resolution of the family \\( \{H\_t \cap C\_V\} \\) introduce a new component in the central fiber and therefore cannot be a very weak resolution.

The last thing to check is that the self-intersections of the canonical divisors of the minimal resolution of the fibers detect the two different behaviors. Indeed, the general fiber are smooth with self-intersection of the canonical divisor equal to \\( K\_{\\mathbb{P}^2}^2 = 9 \\) and \\( K\_{\\mathbb{P}^1\times\\mathbb{P}^1}^2 = 8 \\), while the central fiber has \\( \\mathbb{P}^1\times\\mathbb{P}^1 \\) as minimal resolution and so in the first case the self-intersection varies, while in the second case it is constant.

### Appendix

Assume \\( f\colon Y \to X \\) to be a resolution of singularities, with \\( \bigcup E\_i \\) the exceptional locus. One can prove that there exist integers \\( a\_i \\) such that for all \\( j \\), one has \\( E\_j \cdot \\sum a\_i E\_i = E\_j \cdot K\_Y \\). The divisor \\( \\sum a\_i E\_i \\) is called the relative canonical divisor (please correct me if I'm wrong) and we have denoted it with \\( K\_{\\mathrm{rel}} \\).

A scheme has at worst Gorenstein singularities if all local rings are Gorenstein. In particular, this means that it is Cohen-Macauley and the dualizing sheaf is locally free. An isolated singularity \\( P \\) is Gorenstein if the dualizing sheaf is locally free near \\( P \\). By a criterion of Serre, a surface has at worst isolated Gorenstein singularities if and only if it is normal and Gorenstein.

Assume \\( X \\) is a normal and Gorenstein surface, with only one singular point \\( P \\); let \\( f Y \to X \\) a minimal resolution of singularities (so that \\( f^{-1}(P) \\) has no components with self-intersection \\( -1 \\)) and let \\( E \\) the exceptional curve. Then as we said \\( \\omega\_X \\) is locally free with associated divisor \\( K\_X \\) and the following formula holds:
\\[ K\_Y = f^\star K\_X - Z, \\]
where \\( Z \\) is an effective divisor supported on \\( E \\). Moreover, Miles Reid proved that there are two cases:

* \\( P \\) is a rational double point and \\( Z = 0 \\), or
* \\( P \\) is a singularity non-rational and the support of \\( Z \\) is the whole \\( E \\).

Note that in this case, \\( Z = K\_{\\mathrm{rel}} \\) and in particular \\( K\_Y^2 = K\_X^2 + K\_{\\mathrm{rel}}^2 \\).

Consider now a flat families of reduced surfaces \\( f\colon X → B \\) and \\( g\colon Y \to X \\) a projective morphism such that the composition is still flat and with \\( Y \\) reduced. Then \\( g \\) is called a very weak simultaneous resolution of the family if for every \\( b \in B \\), \\( g \\) restricted to the fiber, that is, \\( Y\_b \to X\_b \\), is a minimal resolution of \\( X\_b \\). It is important to note that even if the minimal resolution of a surface is unique, there may be several very weak resolution of a family.
