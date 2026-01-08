This repository provides mathematical validation and test coverage.
It does NOT constitute a production-ready cryptographic library.

# Shamir Validation Suite
A mathematical validation and audit package for Shamir Secret Sharing.

See the formal validation report in [reports/validation.md](reports/validation.md).


## Mathematical Proof of Reconstruction
Shamir Secret Sharing is based on Lagrange interpolation at x=0.

Given secret \(S \in \mathbb{F}\), threshold \(t\), and polynomial:

\[
f(x) = S + a_1 x + a_2 x^2 + \dots + a_{t-1} x^{t-1}
\]

Shares: \((x_i, y_i)\) with \(y_i = f(x_i)\).  
Reconstruction at \(x=0\) uses Lagrange interpolation:

\[
S = \sum_{i=1}^{t} y_i \cdot \prod_{\substack{j=1 \\ j \neq i}}^{t} \frac{-x_j}{x_i - x_j}
\]

## Implementation
Implemented in Python 3.x and JavaScript with deterministic RNG.
Deterministic RNG is used exclusively for reproducible validation
and MUST NOT be used in production environments.


## CI/CD and Reports
Automated validation runs across multiple seeds: [1337, 42, 2025, 9001, 314159].  
Reports are generated in Markdown (`summary.md`) and HTML (`summary.html`).

## 💰 Research Bounty (Optional)
Please use the following Bitcoin address for bounty distribution:
**bc1q4fv9w2pwpgqyp0gzt20c6n6m4mxs9yga2qgm9f**
This address is provided for voluntary research support only.


## Security Recommendations
- Define finite field explicitly (GF(p) or GF(2^n))
- Enforce uniqueness and validity of x-coordinates
- Use cryptographically secure RNG for coefficients
- Add metadata (field, threshold, index, checksum/MAC) to shares
- Implement constant-time field operations

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.


