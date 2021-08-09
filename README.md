# for-the-lulz

## pi_from_random
Python program that derives π using the function random().

## donut
C programs that let you have a donut(display donut in emulation).
```bash
gcc -o donut donut*.c -lm
```
### donut.c
Here's a donut.
Inner loop is plotting dots in a circle, which goes around another larger circle. In each loop, the sine/cosine terms are moving by a small, fixed angle.
### donut_ii.c
Fancier version of donut.c.
### donut_wo_mathlib.c
donut.c without the use of sin and cos (no linking the math library (-lm)) making it less CPU-intensive.
Rotate a point around the origin in two nested loops, and also rotate two angles just for the animation. Start at cos=1, sin=0 and rotate a circle around the origin to generate all the sines and cosines by applying a fixed rotation matrix.
### donut_wo_mathlib_float.c
donut.c without the use of float (no linking the math library (-lm)).
Uses integer fixed-point arithmetic at 10-bit precision.
### donut.js
Javascript source for both the ASCII and canvas rendering.

donut*.c needs ANSI- or VT100-like emulation.

All donuts' credits to [@a1k0n ][1]

[1]:
https://www.a1k0n.net/2011/07/20/donut-math.html
