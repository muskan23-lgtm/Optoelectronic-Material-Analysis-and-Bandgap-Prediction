"""Analyze photoluminescence spectrum and identify peak wavelength."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "raw" / "photoluminescence_spectrum.csv"
FIG_DIR = ROOT / "outputs" / "figures"


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_FILE)
    peak_idx = df["pl_intensity_au"].idxmax()
    peak_wavelength = df.loc[peak_idx, "wavelength_nm"]
    peak_intensity = df.loc[peak_idx, "pl_intensity_au"]

    plt.figure(figsize=(7, 5))
    plt.plot(df["wavelength_nm"], df["pl_intensity_au"], linewidth=2)
    plt.scatter([peak_wavelength], [peak_intensity], s=55, label=f"Peak = {peak_wavelength:.1f} nm")
    plt.xlabel("Wavelength (nm)", fontsize=12)
    plt.ylabel("PL intensity (a.u.)", fontsize=12)
    plt.title("Photoluminescence Spectrum", fontsize=14)
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "pl_spectrum_peak.png", dpi=300)
    plt.close()
    print(f"PL peak wavelength: {peak_wavelength:.2f} nm")


if __name__ == "__main__":
    main()
