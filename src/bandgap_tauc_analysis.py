"""Estimate optical bandgap using a direct-transition Tauc plot."""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "raw" / "uv_vis_absorbance.csv"
FIG_DIR = ROOT / "outputs" / "figures"


def estimate_bandgap(df: pd.DataFrame) -> tuple[float, float, float]:
    energy = df["photon_energy_ev"].to_numpy()
    absorbance = df["absorbance_au"].to_numpy()
    alpha = absorbance / absorbance.max()
    tauc_y = (alpha * energy) ** 2

    # Choose a linear region near the absorption edge.
    mask = (energy >= 1.65) & (energy <= 2.05)
    slope, intercept, r_value, _, _ = linregress(energy[mask], tauc_y[mask])
    bandgap = -intercept / slope
    return bandgap, slope, intercept


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_FILE)
    energy = df["photon_energy_ev"].to_numpy()
    absorbance = df["absorbance_au"].to_numpy()
    alpha = absorbance / absorbance.max()
    tauc_y = (alpha * energy) ** 2

    bandgap, slope, intercept = estimate_bandgap(df)
    fit_energy = np.linspace(1.55, 2.15, 120)
    fit_y = slope * fit_energy + intercept

    plt.figure(figsize=(7, 5))
    plt.plot(energy, tauc_y, linewidth=2, label="Tauc data")
    plt.plot(fit_energy, fit_y, linestyle="--", linewidth=2, label="Linear fit")
    plt.axvline(bandgap, linestyle=":", linewidth=2, label=f"Estimated Eg = {bandgap:.2f} eV")
    plt.xlabel("Photon energy, hν (eV)", fontsize=12)
    plt.ylabel("(αhν)² (a.u.)", fontsize=12)
    plt.title("Tauc Plot for Optical Bandgap Estimation", fontsize=14)
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "tauc_plot_bandgap.png", dpi=300)
    plt.close()
    print(f"Estimated optical bandgap: {bandgap:.3f} eV")


if __name__ == "__main__":
    main()
