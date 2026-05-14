"""Train a simple ML model for bandgap prediction from material descriptors."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "processed" / "material_bandgap_dataset.csv"
FIG_DIR = ROOT / "outputs" / "figures"


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_FILE)
    target = "bandgap_ev"
    features = [col for col in df.columns if col != target]
    x = df[features]
    y = df[target]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42
    )

    model = RandomForestRegressor(n_estimators=250, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    plt.figure(figsize=(6, 6))
    plt.scatter(y_test, y_pred, s=45)
    lim_min = min(y_test.min(), y_pred.min()) - 0.05
    lim_max = max(y_test.max(), y_pred.max()) + 0.05
    plt.plot([lim_min, lim_max], [lim_min, lim_max], linestyle="--", linewidth=2)
    plt.xlabel("Actual bandgap (eV)", fontsize=12)
    plt.ylabel("Predicted bandgap (eV)", fontsize=12)
    plt.title(f"Bandgap Prediction: MAE = {mae:.3f} eV, R² = {r2:.3f}", fontsize=13)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "ml_bandgap_prediction.png", dpi=300)
    plt.close()

    importance = pd.Series(model.feature_importances_, index=features).sort_values()
    plt.figure(figsize=(7, 5))
    plt.barh(importance.index, importance.values)
    plt.xlabel("Feature importance", fontsize=12)
    plt.title("Material Descriptor Importance for Bandgap Prediction", fontsize=13)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "ml_feature_importance.png", dpi=300)
    plt.close()

    print(f"Mean absolute error: {mae:.3f} eV")
    print(f"R2 score: {r2:.3f}")


if __name__ == "__main__":
    main()
