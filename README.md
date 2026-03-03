# smarter-tech-package-sort
Solution to Smarter Technologies package-sorting challenge. Implements sort(width, height, length, mass) to route packages to STANDARD, SPECIAL, or REJECTED based on bulky (volume/dimension) and heavy (mass) rules, with simple tests and clear run instructions.

# Smarter Technologies: Package Sorting Challenge

## Overview

This repository contains my solution to the Smarter Technologies core engineering technical assessment. The objective was to implement a function that determines how packages should be dispatched within an automated robotic system based on their dimensions and mass.

The solution is designed to be simple, readable, and correct, with clear test coverage for core and boundary scenarios.

## Problem Summary

Each package must be classified according to the following rules:

A package is considered **Bulky** if:
. Its volume (width × height × length) is greater than or equal to 1,000,000 cm³, or
. Any single dimension is greater than or equal to 150 cm

A package is considered **Heavy** if:
. Its mass is greater than or equal to 20 kg

Dispatch rules:

. STANDARD → Not bulky and not heavy
. SPECIAL → Either bulky or heavy
. REJECTED → Both bulky and heavy


## Implementation

The core function is implemented in `sort.py`:

    sort(width, height, length, mass)

It returns one of the following strings:
. "STANDARD"
. "SPECIAL"
. "REJECTED"

The implementation strictly follows the problem specification and correctly handles boundary conditions using >= comparisons.


## How to Run

Clone the repository:

    git clone https://github.com/anudeep0701/smarter-tech-package-sort.git
    cd smarter-tech-package-sort

Run the tests:

    python test_sort.py

If everything is correct, you should see:

    All tests passed!

## Test Coverage

The included tests validate:

. STANDARD packages
. SPECIAL packages (heavy only)
. SPECIAL packages (bulky via volume)
. SPECIAL packages (bulky via dimension)
. REJECTED packages (both heavy and bulky)
. Threshold and boundary cases

## Notes

. The solution assumes valid numeric inputs.
. The focus is on clarity, correctness, and maintainability.
. The logic is intentionally concise to reflect clean production-style code.
