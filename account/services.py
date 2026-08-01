from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

handinfo_path = BASE_DIR / "datasets" / "HandInfo.csv"
tarot_path = BASE_DIR / "datasets" / "tarot_card_meanings.csv"

hand_df = pd.read_csv(handinfo_path)
tarot_df = pd.read_csv(tarot_path)