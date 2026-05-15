# Optoelectronic Material Analysis and Bandgap Prediction

A beginner-friendly research project for analyzing semiconductor and optoelectronic material data using Python. The project includes UV-Vis absorbance analysis, Tauc plot based bandgap extraction, photoluminescence peak analysis, I-V characteristics of optoelectronic devices, EQE response visualization, and a simple machine learning model for bandgap prediction.

This repository is suitable for research internship applications related to materials science, optoelectronics, semiconductor devices, energy devices, and experimental data analysis.

---

## Project Motivation

Optoelectronic and energy devices such as solar cells, LEDs, photodetectors, and semiconductor thin films require careful analysis of experimental data. Common characterization methods include UV-Vis spectroscopy, photoluminescence, current-voltage measurement, and external quantum efficiency analysis. This project builds a clean Python workflow to process such data and extract useful material/device parameters.

---

## Key Features

- UV-Vis absorbance data analysis
- Tauc plot generation for optical bandgap estimation
- Photoluminescence spectrum visualization and peak detection
- Current-voltage curve analysis of a solar-cell-like device
- External quantum efficiency response visualization
- Synthetic dataset generation for reproducible experimentation
- Machine learning based bandgap prediction using material features
- Publication-style plots saved automatically in `outputs/figures/`

---

## Repository Structure

```text
optoelectronic-material-analysis/
│
├── data/
│   ├── raw/                 # Synthetic raw characterization datasets
│   └── processed/           # Processed material-property dataset
│
├── outputs/
│   └── figures/             # Generated plots
│
├── src/
│   ├── generate_sample_data.py
│   ├── bandgap_tauc_analysis.py
│   ├── pl_peak_analysis.py
│   ├── iv_device_analysis.py
│   ├── eqe_analysis.py
│   └── ml_bandgap_prediction.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/optoelectronic-material-analysis.git
cd optoelectronic-material-analysis
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. Generate sample datasets

```bash
python src/generate_sample_data.py
```

This creates synthetic UV-Vis, PL, I-V, EQE, and material-property datasets.

### 2. Run Tauc plot and bandgap analysis

```bash
python src/bandgap_tauc_analysis.py
```

Output:

```text
outputs/figures/tauc_plot_bandgap.png
```

### 3. Run photoluminescence peak analysis

```bash
python src/pl_peak_analysis.py
```

Output:

```text
outputs/figures/pl_spectrum_peak.png
```

### 4. Run I-V device analysis

```bash
python src/iv_device_analysis.py
```

Output:

```text
outputs/figures/iv_characteristics.png
```

### 5. Run EQE response analysis

```bash
python src/eqe_analysis.py
```

Output:

```text
outputs/figures/eqe_response.png
```

### 6. Run ML-based bandgap prediction

```bash
python src/ml_bandgap_prediction.py
```

Output:

```text
outputs/figures/ml_bandgap_prediction.png
outputs/figures/ml_feature_importance.png
```

---

## Example Results

The project generates plots for:

- Optical absorbance spectrum
- Tauc plot for bandgap estimation
- Photoluminescence peak position
- Solar-cell-like I-V curve
- EQE response curve
- Machine learning predicted vs actual bandgap
- Feature importance for bandgap prediction

---

## Methods Used

### Tauc Plot Bandgap Estimation

For a direct bandgap semiconductor, the Tauc relation is commonly written as:

```text
(alpha * hν)^2 = A(hν - Eg)
```

where:

- `alpha` is the absorption coefficient
- `hν` is photon energy
- `Eg` is the optical bandgap
- `A` is a material-dependent constant

A linear fit is performed near the absorption edge. The x-axis intercept gives the estimated bandgap.

### ML Bandgap Prediction

A Random Forest Regressor is trained using synthetic material descriptors such as:

- Composition fraction
- Lattice constant
- Electronegativity difference
- Atomic radius difference
- Defect density
- Annealing temperature

The trained model predicts the optical bandgap and reports error metrics.

---

## Skills Demonstrated

- Python programming for scientific data analysis
- Data preprocessing and visualization
- Numerical modeling and curve fitting
- Semiconductor material characterization
- Optoelectronic device analysis
- Machine learning for materials science
- Clean research-oriented GitHub documentation

---




## Future Improvements

- Add real experimental UV-Vis and PL datasets
- Include uncertainty estimation in bandgap extraction
- Extend ML model to predict device efficiency
- Add support for perovskite and oxide semiconductor datasets
- Build a Streamlit dashboard for interactive analysis

---

## Disclaimer

The datasets included in this repository are synthetic and created for learning, demonstration, and reproducible workflow development. The same analysis pipeline can be applied to real experimental data after replacing the sample CSV files.
