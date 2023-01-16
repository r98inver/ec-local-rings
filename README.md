# Elliptic Curves over local rings $F_q[x]/x^k$

In this repository you can find scripts and computations for our paper [LINK HERE].   
Should you have any question or suggestion, do not hesitate to contact the authors:
- Daniele Taufer: name.surname@gmail.com
- Riccardo Invernizzi: name.surname@student.kuleuven.be

**Sections:**
- [Paper Computations](https://github.com/r98inver/ec-local-rings#paper-computations): the scripts used in the paper, along with their results, are briefly presented;
- [Useful Scripts](): code to easily work with elliptic curve over these rings.

### Paper Computations
- [short_sum_verification.magma](https://github.com/r98inver/ec-local-rings/blob/main/short_sum_verification.magma): verification of the equality between the second addition law in [Bosma - Lenstra, 1995](https://www.math.ru.nl/~bosma/pubs/JNT1995.pdf) (except for a minor typo) and our short form;
- [zfx_fast.py](zfx_fast.py) and [zfxred_fast.py](zfxred_fast.py): python script to compute the symbolic expression of $z$ coordinates of points as a polynomial in their $x$ coordinate over $\mathcal{O}$ (in extended and reduced Weierstrass form respectively). The parameter $k$ can be set before running the script. The output is saved as a loadable `magma` script called `zfx_stored_{k}.magma` (extended form) or `zfxred_stored_{k}.magma`. Two examples can be found in [zfx_stored_30.magma](zfx_stored_30.magma) and [zfxred_stored_300.magma](zfx_stored_30.magma);
- [ind.magma](ind.magma) / [indred.magma](indred.magma): computation of the $\psi_i$ polynomials as described in the paper; the output is stored as loadable magma script in `psi_stored.magma` (resp. `psired_stored.magma`). An example on how to load these polynomials can be found in [psi_loaded_30.magma](psi_loaded_30.magma) and [psired_loaded_222.magma](psired_loaded_222.magma);
- [ex1.magma](ex1.magma) / [ex2.magma](ex2.magma): examples of behaviour of the minimum degree of points when $\psi_p(p)$ is not a unit;
- [proof_23.magma](proof_23.magma): verification of important facts that leads to the solution of all corner cases for $p=2,3$;

### Useful sripts

- [utils.magma](utils.magma): the file containing most of the useful function to work with elliptic curves over $F_q[x]/x^k$, including point addition and multiplication, lifting and others;
- [quickstart.magma](quickstart.magma): a showcase of usage of the most important functions of `utils.magma`;
- [grp.magma](grp.magma): samples random points from random curves with fixed parameters, and computes their order and $p$-multiples; useful to infer the group structure, or at least the highest order of points in the group (since point with highest order appears more often); parameter choices are explained in the script;
- [zfx_stored_30.magma](zfx_stored_30.magma) / [zfxred_stored_300.magma](zfx_stored_30.magma): stored values of the $z$ coordinate of a point over $\mathcal{O}$ as a polynomial function of its $x$ in the extended (resp. reduced) form, for $k=30$ (resp. $k=300$). Notice that a symbolic polynomial ring must be defined before loading; specific loading instructions are provided in each file;
- [psi_stored_30.magma](psi_stored_30.magma): stored values of $\psi_i$ for $i \leq 30$ in the extended form; the loader script [psi_loaded_30.magma](psi_loaded_30.magma) can be used to import them, otherwise a symbolic polynomial ring must be defined before loading; smaller sets are provided for faster loading, at [psi_stored_27.magma](psi_stored_27.magma) and [psi_stored_17.magma](psi_stored_17.magma) (each one with its own loader);
- [psired_stored_222.magma](psired_stored_222.magma): same script for short form; loader at [psired_loaded_222.magma](psired_loaded_222.magma), smaller version at [psired_stored_129.magma](psired_stored_129.magma);
