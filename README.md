# Personality-Distribution-Analysis-in-AequorTech-CTRL
This project analyses the distribution of personality types among employees in AequorTech CTRL using Python. It utilizes a dataset of 350 employees, each assigned a random role and personality type. The primary goal is to provide an understanding of the overall distribution of personality types in the company and offer functions for retrieving personality information based on employee names or IDs
.
By: Fozan Ahmed
.
![personality_distribution](https://github.com/user-attachments/assets/602874f2-9f98-41f2-858f-2646777f5993)

Steps Involved:
1. Generating Sample Data:
The project begins by generating a synthetic dataset using random data to simulate the employee database. The following attributes are included in the dataset:
•	Employee ID: A unique ID for each employee (ranging from 1 to 350).
•	Name: The name of each employee, labelled as "Employee_1" through "Employee_350."
•	Role: The role of the employee, which is selected randomly from a predefined list of roles: Programmer, Engineer, Worker, Manager, Designer, Analyst, Technician, HR, Consultant.
•	Personality Type: The personality type of each employee, chosen randomly from a list of 16 personality types based on the Myers-Briggs Type Indicator (MBTI), such as INFP, ENFP, ISTP, etc.
The generated data is stored in a pandas DataFrame, making it easy to analyse and manipulate.
2. Analysing Personality Distribution:
The next step involves analyzing the distribution of personality types within the company. The value_counts() function is used to count the occurrences of each personality type. These counts are then converted to percentages to determine the relative proportion of each personality type in the dataset. This analysis is summarized in a DataFrame (summary_df), which includes the following columns:
•	Personality Type: The unique personality types found in the dataset.
•	Count: The number of employees assigned to each personality type.
•	Percentage: The percentage of employees with each personality type, calculated as (count / total number of employees) * 100.
3. Visualizing the Distribution:
To make the distribution analysis more accessible, a bar plot is generated using the Seaborn and Matplotlib libraries. The plot visualizes the percentage distribution of personality types in AequorTech CTRL. The following customizations are made:
•	A grid background for better readability.
•	The x-axis displays the different personality types.
•	The y-axis represents the percentage of employees in each personality type.
•	The chart is saved as a PNG file (personality_distribution.png) and also displayed on the screen.
4. Adding Lookup Functions:
To further enhance the functionality of the project, two lookup functions are added:
•	find_personality_by_name(name): This function allows the user to input an employee's name (e.g., "Employee_1") and retrieve their personality type.
•	find_personality_by_id(emp_id): This function takes an employee's ID (e.g., 1) and returns their personality type.
Both functions search the DataFrame for the corresponding employee and print their personality type. If the employee is not found, a message is displayed indicating that the employee does not exist in the dataset.
________________________________________
Example Usage:
1.	Looking up by Name:
o	To find the personality type of "Employee_1," the following code is used:
find_personality_by_("Employee_1")
Output:
Employee_1's Personality Type: INFP
2.	Looking up by ID:
o	To find the personality type of the employee with ID 1:
find_personality_by_id(1)
Output:
Employee ID 1's Personality Type: INFP

________________________________________
Conclusion:
This project provides a comprehensive analysis of the personality distribution within AequorTech CTRL. By utilizing random data generation, personality analysis, and visualization, it offers valuable insights into the company's employee dynamics. Additionally, the inclusion of lookup functions allows for easy access to individual employee personality information. This project can be expanded further to integrate real employee data and perform more advanced analyses.
________________________________________
Tools and Libraries Used:
•	pandas: For data manipulation and storage.
•	matplotlib: For creating visualizations.
•	seaborn: For creating aesthetically pleasing plots.
•	random: For generating random data.

________________________________________
Future Improvements:
•	Real Data Integration: Instead of using synthetic data, real employee data could be incorporated into the analysis for more accurate insights.
•	Interactive Dashboards: Implementing a web-based interactive dashboard using tools like Dash or Streamlit to allow users to query the dataset and visualize the results in real time.
•	Employee Role Analysis: Expanding the analysis to explore how personality types correlate with specific employee roles in the organization.
________________________________________
By:
Fozan Ahmed Memon
Data Analyst and Python Enthusiast

## Using Your Dataset (Volunteering Participants)
- The analysis now uses `PersonalityAnalysis/participants_mbti.csv` with columns: Name, Age, Gender, City, Country, MBTI, Occupation.
- The script reads this CSV and generates `participants_personality_distribution.png`.

## How to Run (Script)
- Install dependencies: `pip install -r PersonalityAnalysis/requirements.txt`
- Run analysis: `python PersonalityAnalysis/app.py`
- Output: `PersonalityAnalysis/participants_personality_distribution.png`

## How to Run (Notebook)
- Install Jupyter: `pip install notebook`
- Start notebook: `jupyter notebook PersonalityAnalysis/MBTI_Personality_Analysis.ipynb`
- The notebook visualizes the MBTI distribution and saves `notebook_participants_personality_distribution.png`.

## Notes
- MBTI codes are normalized to uppercase.
- You can adjust `participants_mbti.csv` to add more volunteers; rerun the script/notebook to update visuals.

## Quick Start
- Windows + Python 3.12 recommended (prebuilt wheels available).
- Install Python: `winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements --silent`
- Upgrade tooling: `"$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m pip install --upgrade pip setuptools wheel`
- Install deps: `"$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m pip install -r PersonalityAnalysis/requirements.txt`

## Run Options
- Script (generates plot): `"$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" PersonalityAnalysis/app.py`
- Notebook (EDA): `"$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m notebook PersonalityAnalysis/MBTI_Personality_Analysis.ipynb`
- Headless notebook: `"$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m notebook PersonalityAnalysis/MBTI_Personality_Analysis.ipynb --no-browser --port 8890`

## AI Research Context
- Goal: Explore MBTI distribution within volunteering participants to inform team composition, engagement strategies, and role alignment at AequorTech CTRL.
- Methodology:
  - Data ingestion from `participants_mbti.csv` with fields: Name, Age, Gender, City, Country, MBTI, Occupation.
  - Normalization of MBTI codes to uppercase; deterministic analysis (no random generation).
  - Descriptive analytics: counts and percentages per MBTI; bar chart visualization.
  - Lookup utilities for qualitative inspection (by name; by MBTI group).
- Research framing:
  - EDA-first pipeline suitable for AI/ML projects: curate dataset → clean/normalize → summarize → visualize → derive hypotheses.
  - The notebook extends toward cross-tabs (MBTI × Gender/Occupation) and age distributions, providing features and insights for downstream modeling.
- Potential ML extensions:
  - Predictive modeling if richer features are added (e.g., survey items, text notes). Examples: clustering participant profiles; predicting role fit or engagement from features.
  - Time-based monitoring: track distributions over cohorts to evaluate program changes.

## Reproducibility
- Deterministic pipeline using a fixed CSV; rerunning the script/notebook yields identical results.
- Environment: Python 3.12, `pandas`, `matplotlib`, `seaborn`, and Jupyter (versions pinned in `requirements.txt`).
- Artifacts: `participants_personality_distribution.png` (script) and `notebook_participants_personality_distribution.png` (notebook).

## Ethics & Limitations
- Small convenience sample; distributions are descriptive and not generalizable.
- MBTI is a self-report typology; use insights responsibly and avoid stereotyping or prescriptive decisions.
- Ensure voluntary participation, transparency, and privacy when expanding the dataset.

## Extending the Research
- Add more attributes (e.g., tenure, department, interests) to enable richer analysis.
- Implement cross-tabs in the notebook and compare cohorts (e.g., teams or time periods).
- Consider lightweight dashboards (e.g., Streamlit) for interactive exploration.
