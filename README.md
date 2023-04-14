# Les courbes de Bézier

## Introduction

Les courbes de Bézier sont des courbes paramétriques définies par une suite de points de contrôle. Elles sont utilisées dans de nombreux domaines, notamment dans le domaine de l'animation. Elles sont utilisées pour décrire des trajectoires de mouvement, des formes, des textures, etc.

## Sources:

* [Courbes de Bézier Wikipédia](https://fr.wikipedia.org/wiki/Courbe_de_B%C3%A9zier)

## Lexique

- **Courbe polynomial** : Une courbe polynomiale est une courbe définie par une suite de polynômes de la forme $P(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n$.
- **Courbe polynomial paramétrique** : Une courbe polynomiale paramétrique est une courbe polynomiale définie par une suite de polynômes paramétriques.

    Par exemple, une courbe polynomiale paramétrique en deux dimensions pourrait être décrite par les équations:

    $x = a_0 + a_1t + a_2t^2 + a_3t^3$ <br />
    $y = b_0 + b_1t + b_2t^2 + b_3t^3$

    où les coefficients $a_0$, $a_1$, $a_2$, $a_3$, $b_0$, $b_1$, $b_2$ et $b_3$ sont des constantes déterminées en fonction de la forme de la courbe.

    En utilisant ces équations, il est possible de tracer la courbe en faisant varier le paramètre t sur une plage de valeurs appropriée. La forme de la courbe dépend de la forme des équations polynomiales, ainsi que des valeurs des coefficients.
- **Polynome de Bernstein**: Les polynomes de Bernstein sont des polynomes utilisés pour décrire les courbes de Bézier. Elles permettent de donner une représentation probabiliste des courbes de Bézier.

    Pour $n$ points de contrôle $(P_0, ..., P_n)$, le polynome de Bernstein de degré $n$ et d'indice $i$ est:

    $B_i^n(t) = \binom{n}{i} t^i (1 - t)^{n - i}$

    où $\binom{n}{i}$ est le coefficient binomial de $n$ et $i$.

    Pour $n = 2$, le polynome de Bernstein est:

    $B_0^2(t) = (1 - t)^2$ <br />
    $B_1^2(t) = 2t(1 - t)$ <br />
    $B_2^2(t) = t^2$ <br />
    $\binom{2}{0} = 1$ et $\binom{2}{1} = 2$ et $\binom{2}{2} = 1$


    Pour $n = 3$, le polynome de Bernstein est:

    $B_0^3(t) = (1 - t)^3$ <br />
    $B_1^3(t) = 3t(1 - t)^2$ <br />
    $B_2^3(t) = 3t^2(1 - t)$ <br />
    $B_3^3(t) = t^3$

    - Propriété:
        - $\forall t \in [0; 1]$, $\sum_{i=0}^n B_i^n(t) = 1$

---

## Théorie

Les courbes de Bézier sont des courbes polynomiales paramétriques.

La courbe de Bézier pour les $n + 1$ points $(P_0, ..., P_n)$ est l'ensemble de points défini par la représentation paramétrique:

$P(t) = \sum_{i=0}^n B_i^n(t) P_i$

où

$B_i^n(t)$ est la fonction de Bézier de degré $n$ et d'indice $i$.

et $t \in [0; 1]$.

$B_i^n(t)$ est un nombre réel qui dépend de $t$ et de $n$. <br />
$P_i$ est un vecteur. <br />
$B_i^n(t) * P_i$ reviens à multiplier chaque valeurs de $P_i$ par $B_i^n(t)$. De même pour l'addition <br />

---

## Exemples

## Pour $n = 2$, la somme des polynomes de Bernstein est:

$B_0^2(t) + B_1^2(t) + B_2^2(t) = 1$
Donc 
$1 = (1 - t)^2 + 2t(1 - t) + t^2$

à cela on ajoute les points de contrôle $(P_0, ..., P_n)$:

$P(t) = (1 - t)^2 P_0 + 2t(1 - t) P_1 + t^2 P_2$

On a donc $\forall t \in [0; 1]$: la courbe de Bézier de degré 2.

## Pour $n = 3$, la somme des polynomes de Bernstein est:

$B_0^3(t) + B_1^3(t) + B_2^3(t) + B_3^3(t) = 1$

$B_0^3 = \binom{3}{0} t^0 (1 - t)^{3 - 0}$ Donc $B_0^3 = (1 - t)^3$ <br />
$B_1^3 = \binom{3}{1} t^1 (1 - t)^{3 - 1}$ Donc $B_1^3 = 3t(1 - t)^2$ <br />
$B_2^3 = \binom{3}{2} t^2 (1 - t)^{3 - 2}$ Donc $B_2^3 = 3t^2(1 - t)$ <br />
$B_3^3 = \binom{3}{2} t^3 (1 - t)^{3 - 3}$ Donc $B_3^3 = t^3$<br />
Donc $\forall t \in [0; 1]$ $1 = (1 - t)^3 + 3t(1 - t)^2 + 3t^2(1 - t) + t^3$ <br />
On ajoute les points de contrôle $(P_0, ..., P_n)$: <br />
$P(t) = (1 - t)^3 P_0 + 3t(1 - t)^2 P_1 + 3t^2(1 - t) P_2 + t^3 P_3$ <br />
On a donc $\forall t \in [0; 1]$: la courbe de Bézier de degré 3.
