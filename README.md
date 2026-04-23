# Structural Equation Modeling (SEM) of AI-Driven Trust in Fintech

## Project Summary
This repository contains a comprehensive implementation of **Structural Equation Modeling (SEM)** focused on the Fintech sector. The study investigates how AI-driven personalization impacts perceived user trust and subsequent financial decision-making quality.

## Methodology
The analysis follows the standard two-step SEM approach:
1. **Measurement Model (CFA):** Validating the relationship between observed indicators (survey items) and latent constructs.
2. **Structural Model:** Testing hypothesized causal pathways ($AIP \rightarrow TRST \rightarrow FDQ$) using Maximum Likelihood estimation.

## Theoretical Constructs
- **AI-Personalization (AIP):** Perceived customization of financial services.
- **Perceived Trust (TRST):** The psychological state of vulnerability acceptance towards the AI.
- **Financial Decision Quality (FDQ):** Behavioral outcome measured by the perceived accuracy of financial choices.

## Technical Details
- **Environment:** Python 3.x
- **Core Library:** `semopy`
- **Dataset:** Synthetic survey data (N=600) designed with controlled covariance to demonstrate ideal model fit.

## Results & Fit Indices
The model is optimized to demonstrate professional-grade fit statistics:
- **CFI / TLI:** > 0.95
- **RMSEA:** < 0.06
- **SRMR:** < 0.08

## Author
**Hamit Büyükgüzel**
*Master's Candidate in Digital Economy & Marketing*
*GitHub:* [hamitbuyukguzel-bit](https://github.com/hamitbuyukguzel-bit)

## License
Licensed under the **MIT License**.
