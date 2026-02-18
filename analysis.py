# student_analysis_styled_2025.py
import pandas as pd
import os
import kagglehub
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------
# 1️⃣ Download dataset
# ------------------------------
path = kagglehub.dataset_download(
    "alhamdulliah123/student-placement-and-skills-analytics-dataset-2025"
)
print("Dataset downloaded to:", path)

files = os.listdir(path)
df = pd.read_csv(os.path.join(path, files[0]))
print("First 5 rows:")
print(df.head())

# ------------------------------
# 2️⃣ Modern Green Theme Setup
# ------------------------------
sns.set_style("whitegrid")  # clean background
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['figure.facecolor'] = '#f5f5f5'  # light gray background

green_palette = ["#2E7D32", "#66BB6A"]  # consistent Yes/No palette

# ------------------------------
# 3️⃣ Placement Distribution
# ------------------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Placement_Offer", palette=green_palette)
plt.title("Placement Distribution 2025", fontsize=16, weight='bold')
plt.xlabel("Placement Status", fontsize=14)
plt.ylabel("Number of Students", fontsize=14)
plt.tight_layout()
plt.savefig("placement_distribution_2025.png")
plt.show()

# ------------------------------
# 4️⃣ GPA vs Placement
# ------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Placement_Offer", y="CGPA", palette=green_palette)
plt.title("CGPA vs Placement 2025", fontsize=16, weight='bold')
plt.xlabel("Placement Status", fontsize=14)
plt.ylabel("CGPA", fontsize=14)
plt.tight_layout()
plt.savefig("cgpa_vs_placement_2025.png")
plt.show()

# ------------------------------
# 5️⃣ Technical Skills vs Placement
# ------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Placement_Offer", y="Technical_Skills_Score_100", palette=green_palette)
plt.title("Technical Skills vs Placement 2025", fontsize=16, weight='bold')
plt.xlabel("Placement Status", fontsize=14)
plt.ylabel("Technical Skills Score", fontsize=14)
plt.tight_layout()
plt.savefig("technical_skills_vs_placement_2025.png")
plt.show()

# ------------------------------
# 6️⃣ Degree vs Placement
# ------------------------------
plt.figure(figsize=(8,5))
num_degrees = len(df['Degree'].unique())
degree_palette = sns.light_palette("#2E7D32", n_colors=num_degrees)
sns.countplot(data=df, x="Degree", hue="Placement_Offer", palette=degree_palette)
plt.title("Degree vs Placement 2025", fontsize=16, weight='bold')
plt.xlabel("Degree", fontsize=14)
plt.ylabel("Number of Students", fontsize=14)
plt.legend(title="Placement Status")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("degree_vs_placement_2025.png")
plt.show()

# ------------------------------
# 7️⃣ Degree vs Placement Percentage
# ------------------------------
total_per_degree = df.groupby("Degree")["Student_ID"].count()
placed_per_degree = df[df["Placement_Offer"] == "Yes"].groupby("Degree")["Student_ID"].count()
placement_percentage = (placed_per_degree / total_per_degree * 100).round(2)

print("\nPlacement Percentage by Degree 2025:")
print(placement_percentage)

plt.figure(figsize=(8,5))
sns.barplot(x=placement_percentage.index, y=placement_percentage.values, palette=degree_palette)
plt.title("Placement Percentage by Degree 2025", fontsize=16, weight='bold')
plt.xlabel("Degree", fontsize=14)
plt.ylabel("Placement Percentage (%)", fontsize=14)
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("degree_placement_percentage_2025.png")
plt.show()

# ------------------------------
# 8️⃣ Internships vs Placement per Degree
# ------------------------------
plt.figure(figsize=(10,6))

# Aggregate: average internships per degree & placement status
internship_avg = df.groupby(['Degree', 'Placement_Offer'])['Internships_Count'].mean().reset_index()

# Barplot
sns.barplot(
    data=internship_avg,
    x='Degree',
    y='Internships_Count',
    hue='Placement_Offer',
    palette={"Yes": "#2E7D32", "No": "#66BB6A"}
)

# Titles & labels
plt.title("Average Number of Internships vs Placement per Degree 2025", fontsize=16, weight='bold')
plt.xlabel("Degree / Major", fontsize=14)
plt.ylabel("Average Number of Internships", fontsize=14)
plt.xticks(rotation=45, ha='right')

# Annotate bars with values
for p in plt.gca().patches:
    height = p.get_height()
    plt.gca().annotate(f'{height:.2f}',
                       (p.get_x() + p.get_width() / 2., height),
                       ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.legend(title="Placement Status")
sns.despine(top=True, right=True)
plt.tight_layout()
plt.savefig("internships_vs_placement_per_degree_2025.png", dpi=300)
plt.show()

