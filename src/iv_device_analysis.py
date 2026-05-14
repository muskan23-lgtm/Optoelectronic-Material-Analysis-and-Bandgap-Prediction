"""Analyze current-voltage characteristics of a solar-cell-like device."""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "raw" / "iv_characteristics.csv"
FIG_DIR = ROOT / "outputs" / "figures"


def interpolate_x_at_y(x: np.ndarray, y: np.ndarray, target: float = 0.0) -> float:
    idx = np.where(np.diff(np.signbit(y - target)))[0]
    if len(idx) == 0:
        return float("nan")
    i = idx[0]
    return float(np.interp(target, [y[i], y[i + 1]], [x[i], x[i + 1]]))


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_FILE)
    voltage = df["voltage_v"].to_numpy()
    current = df["current_density_mA_cm2"].to_numpy()

    jsc = float(np.interp(0.0, voltage, current))
    voc = interpolate_x_at_y(voltage, current, 0.0)
    power = voltage * current
    max_power_idx = int(np.argmax(power))
    vmp = voltage[max_power_idx]
    jmp = current[max_power_idx]
    fill_factor = (vmp * jmp) / (voc * jsc) if voc > 0 and jsc > 0 else float("nan")

    plt.figure(figsize=(7, 5))
    plt.plot(voltage, current, linewidth=2, label="J-V curve")
    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)
    plt.scatter([vmp], [jmp], s=55, label="Maximum power point")
    plt.xlabel("Voltage (V)", fontsize=12)
    plt.ylabel("Current density (mA/cm²)", fontsize=12)
    plt.title("Device Current-Voltage Characteristics", fontsize=14)
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "iv_characteristics.png", dpi=300)
    plt.close()

    print(f"Short-circuit current density Jsc: {jsc:.2f} mA/cm^2")
    print(f"Open-circuit voltage Voc: {voc:.2f} V")
    print(f"Fill factor: {fill_factor:.2f}")


if __name__ == "__main__":
    main()
