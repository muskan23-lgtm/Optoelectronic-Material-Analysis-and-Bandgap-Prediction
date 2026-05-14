"""Visualize external quantum efficiency response."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "raw" / "eqe_response.csv"
FIG_DIR = ROOT / "outputs" / "figures"


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_FILE)
    max_idx = df["eqe_percent"].idxmax()
    max_wavelength = df.loc[max_idx, "wavelength_nm"]
    max_eqe = df.loc[max_idx, "eqe_percent"]

    plt.figure(figsize=(7, 5))
    plt.plot(df["wavelength_nm"], df["eqe_percent"], linewidth=2)
    plt.scatter([max_wavelength], [max_eqe], s=55, label=f"Max EQE = {max_eqe:.1f}%")
    plt.xlabel("Wavelength (nm)", fontsize=12)
    plt.ylabel("EQE (%)", fontsize=12)
    plt.title("External Quantum Efficiency Response", fontsize=14)
    plt.ylim(0, 100)
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "eqe_response.png", dpi=300)
    plt.close()
    print(f"Maximum EQE: {max_eqe:.2f}% at {max_wavelength:.1f} nm")


if __name__ == "__main__":
    main()
