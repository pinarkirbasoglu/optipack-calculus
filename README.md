# 📦 OptiPack: Packaging & Logistics Cost Optimization with Calculus
*Calculus ile Koli & Lojistik Maliyet Optimizasyonu*

[🇬🇧 English Version](#english) | [🇹🇷 Türkçe Versiyon](#turkce)

---

## English

OptiPack is an interactive analytical simulation tool designed to minimize packaging dimensions and logistics freight costs using **Multivariable Calculus** and **Constrained Optimization** techniques.

### 🚀 Key Features
- **Analytical Optimization:** Identifies the global minimum dimensions ($x^*, y^*, h^*$) under a constant target volume ($V$) constraint via 1st and 2nd derivative tests.
- **Flexible Geometries:** Supports both square base ($k = 1$) and custom aspect ratio rectangular bases ($y = kx$).
- **Financial Impact & ROI:** Quantifies unit and annual cost savings by comparing current box dimensions against the mathematically optimal configuration.
- **Interactive Visualizations:** Renders real-time 3D parametric boxes and convex cost curves powered by Plotly.
- **Rigorous Proof:** Features a comprehensive 6-step analytical derivation and convexity verification.
- **Bilingual Interface:** Instant language switching between English and Turkish.

### 📐 Mathematical Formulation
Given target volume $V$, aspect ratio $y = kx$, base cost $c_1$, and side wall cost $c_2$:

$$\text{Objective Cost Function: } C(x) = 2 c_1 k x^2 + \frac{2 c_2 (1 + k)V}{k x}$$

Setting the first derivative to zero ($\frac{dC}{dx} = 0$) yields the unique global minimum:

$$x^* = \sqrt[3]{\frac{(1 + k) c_2 V}{2 c_1 k^2}}, \quad y^* = k \cdot x^*, \quad h^* = \frac{V}{k (x^*)^2}$$

### 🛠️ Tech Stack
- **Python 3.x**
- **Streamlit** (Interactive Web UI)
- **Plotly** (Dynamic 3D Simulation & Convex Curves)
- **NumPy & SciPy & SymPy** (Numerical & Analytical Computation)

### 💻 Local Setup & Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/pinarkirbasoglu/optipack-calculus.git](https://github.com/pinarkirbasoglu/optipack-calculus.git)
   cd optipack-calculus