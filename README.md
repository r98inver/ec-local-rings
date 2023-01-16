# Elliptic Curves over local rings $F_q[x]/x^k$

In this repository you can find scripts and computations for our paper [LINK HERE].   
Should you have any question or suggestion, do not hesitate to contact the authors:
- Daniele Taufer: name.surname@gmail.com
- Riccardo Invernizzi: name.surname@student.kuleuven.be

**Sections:**
- [Paper Computation](https://github.com/r98inver/ec-local-rings#paper-computation): the scripts used in the paper, along with their results, are briefly presented;
- [Useful Scripts](): code to easily work with elliptic curve over these rings.

### Paper Computation
- [short_sum_verification.magma](https://github.com/r98inver/ec-local-rings/blob/main/short_sum_verification.magma): verification of the equality between the second addition law in [Bosma - Lenstra, 1995](https://www.math.ru.nl/~bosma/pubs/JNT1995.pdf) (except for a minor typo) and our short form;
- [zfx_fast.py](zfx_fast.py) and [zfxred_fast.py](zfxred_fast.py): python script to compute the symbolic expression of $z$ coordinates of points as a polynomial in their $x$ coordinate over $\mathcal{O}$ (in extended and reduced Weierstrass form respectively). The parameter $k$ can be set before running the script. The output is saved as a loadable `magma` script called `zfx_stored_{k}.magma` (extended form) or `zfxred_stored_{k}.magma`. Two examples can be found in [zfx_stored_30.magma](zfx_stored_30.magma) and [zfxred_stored_300.magma](zfx_stored_30.magma);

### Useful sripts

- [utils.magma](utils.magma): the file containing most of the useful function to work with elliptic curves over $F_q[x]/x^k$, including point addition and multiplication, lifting and others;
- [quickstart.magma](quickstart.magma): a showcase of usage of the most important functions of `utils.magma`;
- [zfx_stored_30.magma](zfx_stored_30.magma) / [zfxred_stored_300.magma](zfx_stored_30.magma): stored values of the $z$ coordinate of a point over $\mathcal{O}$ as a polynomial function of its $x$ in the extended (reduced) form, for $k=30$ ($k=300$). Notice that a symbolic polynomial ring must be defined before loading; specific loading instructions are provided in each file;
