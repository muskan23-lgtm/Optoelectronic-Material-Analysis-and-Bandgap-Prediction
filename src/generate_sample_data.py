"""Generate synthetic datasets for optoelectronic material analysis.

The generated data is only for demonstration. Replace these CSV files
with real experimental datasets when available.
"""

from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"


def make_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def generate_uv_vis(seed: int = 7) -> None:
    rng = np.random.default_rng(seed)
    wavelength_nm = np.linspace(350, 850, 501)
    photon_energy_ev = 1240 / wavelength_nm
    eg_true = 1.62
    edge = np.maximum(photon_energy_ev - eg_true, 0)
    absorbance = 0.08 + 0.95 * edge**1.8 + 0.02 * rng.normal(size=wavelength_nm.size)
    absorbance = np.clip(absorbance, 0, None)
    df = pd.DataFrame(
        {
            "wavelength_nm": wavelength_nm,
            "photon_energy_ev": photon_energy_ev,
            "absorbance_au": absorbance,
        }
    )
    df.to_csv(RAW_DIR / "uv_vis_absorbance.csv", index=False)


def generate_pl(seed: int = 11) -> None:
    rng = np.random.default_rng(seed)
    wavelength_nm = np.linspace(500, 850, 500)
    peak_center = 720
    peak_width = 32
    intensity = 1200 * np.exp(-0.5 * ((wavelength_nm - peak_center) / peak_width) ** 2)
    intensity += 120 * np.exp(-0.5 * ((wavelength_nm - 650) / 60) ** 2)
    intensity += 25 * rng.normal(size=wavelength_nm.size)
    intensity = np.clip(intensity, 0, None)
    df = pd.DataFrame({"wavelength_nm": wavelength_nm, "pl_intensity_au": intensity})
    df.to_csv(RAW_DIR / "photoluminescence_spectrum.csv", index=False)


def generate_iv(seed: int = 21) -> None:
    rng = np.random.default_rng(seed)
    voltage_v = np.linspace(-0.1, 1.05, 400)
    jsc = 21.5
    voc = 0.88
    current_density = jsc * (1 - np.exp((voltage_v - voc) / 0.095))
    current_density += 0.25 * rng.normal(size=voltage_v.size)
    df = pd.DataFrame({"voltage_v": voltage_v, "current_density_mA_cm2": current_density})
    df.to_csv(RAW_DIR / "iv_characteristics.csv", index=False)


def generate_eqe(seed: int = 31) -> None:
    rng = np.random.default_rng(seed)
    wavelength_nm = np.linspace(350, 900, 500)
    rise = 1 / (1 + np.exp(-(wavelength_nm - 410) / 18))
    fall = 1 / (1 + np.exp((wavelength_nm - 790) / 25))
    eqe = 82 * rise * fall + 2.0 * rng.normal(size=wavelength_nm.size)
    eqe = np.clip(eqe, 0, 100)
    df = pd.DataFrame({"wavelength_nm": wavelength_nm, "eqe_percent": eqe})
    df.to_csv(RAW_DIR / "eqe_response.csv", index=False)


def generate_material_dataset(seed: int = 51) -> None:
    rng = np.random.default_rng(seed)
    n = 180
    composition_fraction = rng.uniform(0, 1, n)
    lattice_constant_a = rng.normal(5.6, 0.25, n)
    electronegativity_diff = rng.uniform(0.1, 1.8, n)
    atomic_radius_diff = rng.uniform(0.0, 0.35, n)
    defect_density_log = rng.uniform(13, 17, n)
    annealing_temperature_c = rng.uniform(80, 450, n)

    bandgap_ev = (
        1.15
        + 0.75 * composition_fraction
        + 0.22 * electronegativity_diff
        - 0.18 * atomic_radius_diff
        - 0.035 * (lattice_constant_a - 5.6)
        + 0.00055 * (annealing_temperature_c - 250)
        + 0.025 * (defect_density_log - 15)
        + rng.normal(0, 0.06, n)
    )

    df = pd.DataFrame(
        {
            "composition_fraction": composition_fraction,
            "lattice_constant_a": lattice_constant_a,
            "electronegativity_diff": electronegativity_diff,
            "atomic_radius_diff": atomic_radius_diff,
            "defect_density_log_cm3": defect_density_log,
            "annealing_temperature_c": annealing_temperature_c,
            "bandgap_ev": bandgap_ev,
        }
    )
    df.to_csv(PROCESSED_DIR / "material_bandgap_dataset.csv", index=False)


def main() -> None:
    make_dirs()
    generate_uv_vis()
    generate_pl()
    generate_iv()
    generate_eqe()
    generate_material_dataset()
    print("Sample datasets generated successfully.")


if __name__ == "__main__":
    main()
