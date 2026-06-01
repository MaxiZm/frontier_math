# Topic Card: Continuum Physics

## Scope
Continuous models from mathematical physics: PDEs (heat, wave, Navier–Stokes,
Schrödinger), variational problems and eigenvalue problems, asymptotic analysis,
and special-function solutions. Often the task is an exact eigenvalue, a critical
parameter, or a closed-form solution.

## Key methods & tools
Separation of variables and spectral methods; perturbation and asymptotic
expansions (WKB, matched asymptotics); variational bounds; dimensional analysis.
Typical tools: **SymPy** (symbolic ODE/PDE solving, series), **mpmath** (high-
precision eigenvalues, special functions, numerical ODE/integration at research
time), **Sage** for symbolic-numeric work. Final answers must reconstruct values
exactly where numerical methods are banned (`docs/07-final-answer-compliance.md`).
