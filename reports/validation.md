# Shamir Secret Sharing — Validation Report

This repository provides a deterministic, language-agnostic
validation of Shamir Secret Sharing reconstruction using
Lagrange interpolation over a finite field.

The purpose of this report is to document the mathematical
correctness and reproducibility of the validation suite.

---

## Mathematical Model

Let a secret be encoded as the constant term of a polynomial:

f(x) = a₀ + a₁x + a₂x² + ... + aₜ₋₁xᵗ⁻¹  (mod p)

where:
- a₀ is the secret,
- p is a large prime modulus,
- t is the reconstruction threshold.

Given any t distinct points (xᵢ, yᵢ), the secret is reconstructed
by evaluating the Lagrange interpolation polynomial at x = 0:

f(0) = Σᵢ yᵢ · lᵢ(0)

with:

lᵢ(0) = Πⱼ≠ᵢ (−xⱼ) / (xᵢ − xⱼ)  (mod p)

---

## Validation Scope

The validation suite implements this reconstruction in two
independent languages:

- Python
- JavaScript (Node.js, BigInt arithmetic)

Both implementations:
- use the same prime field,
- use deterministic coefficient generation,
- reconstruct the secret from the same subset of shares,
- perform no cryptographic randomness,
- expose no production API.

The code is intended solely for mathematical validation.

---

## Determinism

All validation runs are deterministic:

- fixed polynomial coefficients
- fixed share indices
- fixed reconstruction subset

This ensures reproducibility across environments and CI runs.

---

## Continuous Integration

A minimal GitHub Actions workflow executes:

- python/validate.py
- javascript/validate.js

on every push to the main branch.

Successful execution confirms that both implementations
reconstruct the original secret exactly.

---

## Result

For all validation runs:

- Original secret == Recovered secret
- Reconstruction succeeds with threshold shares
- Reconstruction is consistent across languages

This confirms the mathematical correctness of the
Lagrange interpolation reconstruction used in Shamir
Secret Sharing.

---

## Non-Goals

This repository intentionally does NOT provide:

- a production-ready library
- cryptographic randomness
- side-channel protections
- performance optimizations

Its sole purpose is transparent mathematical validation.
