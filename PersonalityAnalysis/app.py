import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load participants dataset (volunteering management MBTI data)
DATA_PATH = os.path.join(os.path.dirname(__file__), "participants_mbti.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}. Please ensure participants_mbti.csv exists.")

# Read CSV
df = pd.read_csv(DATA_PATH)
# Add a simple Participant ID column
df.insert(0, "Participant ID", range(1, len(df) + 1))
# Normalize MBTI codes
df["MBTI"] = df["MBTI"].str.upper().str.strip()

# MBTI distribution
mbti_order = [
    "INFP", "ENFP", "ESFJ", "ISTP", "INFJ", "ENTP", "ENTJ", "ISFP",
    "INTP", "ESTP", "ESTJ", "ISFJ", "ISTJ", "ENFJ", "INTJ", "ESFP"
]
counts = df["MBTI"].value_counts()
percentages = (counts / len(df)) * 100
summary_df = (
    pd.DataFrame({"MBTI": counts.index, "Count": counts.values, "Percentage": percentages.values})
    .set_index("MBTI")
    .reindex(mbti_order)
    .dropna()
    .reset_index()
)

# Visualize distribution
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
sns.barplot(x="MBTI", y="Percentage", data=summary_df, palette="viridis")
plt.title("Personality Distribution (Volunteering Participants) in AequorTech CTRL", fontsize=16)
plt.xlabel("MBTI Type", fontsize=12)
plt.ylabel("Percentage (%)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

out_path = os.path.join(os.path.dirname(__file__), "participants_personality_distribution.png")
plt.savefig(out_path)
# Avoid interactive show in headless environments
# plt.show()

print(f"Saved distribution plot to: {out_path}")

# Lookup utilities

def find_personality_by_name(name: str):
    person = df[df["Name"].str.lower() == name.lower()]
    if not person.empty:
        mbti = person.iloc[0]["MBTI"]
        print(f"{name}'s MBTI: {mbti}")
    else:
        print(f"Participant {name} not found.")


def list_participants_by_mbti(mbti: str):
    mbti_clean = mbti.upper().strip()
    people = df[df["MBTI"] == mbti_clean][["Name", "Gender", "City", "Country", "Occupation"]]
    print(f"Participants with MBTI {mbti_clean} ({len(people)}):")
    print(people.to_string(index=False))


if __name__ == "__main__":
    # Example usage for quick verification
    find_personality_by_name("Fozan Ahmed")
    list_participants_by_mbti("INFP")
