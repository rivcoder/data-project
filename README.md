# Health360: Comprehensive Healthcare Risk & Disease Analytics

An interactive Tableau analytics project that helps healthcare teams spot high-risk patients early and understand how age, BMI, clinical indicators and lifestyle habits relate to heart disease, diabetes and stroke.

**Author:** Rashika Kaushal Jain
**Program:** Data Analytics with Tableau (SkillWallet)

## Live Links

| | |
|---|---|
| Tableau Public Story | https://public.tableau.com/app/profile/rashika.jain8238/viz/Book1_17931080330870/Story1 |
| Demo video | _add link here_ |

## Problem Statement

Chronic diseases such as heart disease, diabetes and stroke are often detected late, which raises treatment costs and worsens outcomes. Manual review of patient records makes it hard to see patterns quickly. This project turns patient data into interactive dashboards so clinicians, analysts and public health researchers can identify vulnerable groups and act earlier.

## Dashboards (one per scenario)

| Dashboard | User | What it answers |
|---|---|---|
| **Clinical Risk Assessment** | Dr. Michael Carter, Clinical Risk Assessment Officer | Who is high risk, and how do blood pressure and cholesterol relate to disease? |
| **Lifestyle & Disease Analysis** | Emily Rodriguez, Healthcare Data Analyst | How do exercise and symptoms relate to disease across age groups? |
| **Population Health** | Dr. Priya Nair, Public Health Researcher | Which age and BMI groups are most vulnerable, and how does glucose change with age? |

A **Story** (4 scenes) walks through all three dashboards and ends with key takeaways.

## Visualizations

| Sheet | Chart type |
|---|---|
| Disease by Age Group | Bar chart |
| Disease by BMI | Bar chart |
| Risk Level Split | Pie chart |
| Exercise vs Age Heatmap | Heatmap |
| BP vs Cholesterol | Scatter plot |
| Glucose by Age | Line chart |
| Symptoms | Horizontal bar (Measure Values) |

## Calculated Fields

| Field | Purpose |
|---|---|
| Age Group | Buckets age into 18-29, 30-44, 45-59, 60+ |
| BMI Category | Underweight, Normal, Overweight, Obese |
| Any Disease | 1 if the patient has heart disease, diabetes or stroke |
| Risk Score | Count of risk factors: BP >= 140, cholesterol >= 240, glucose >= 126, BMI >= 30, smoker (0-5) |
| Risk Level | Low (0-1), Medium (2-3), High (4-5) |
| Prevalence % | Patients with any disease divided by total patients |

## Dataset

`data/health360_dataset.csv` (also provided as `.xlsx`)

- **1,500 patients, 16 columns:** Patient ID, Age, Gender, BMI, Blood Pressure, Cholesterol, Glucose, Smoking, Alcohol, Exercise Level, Fatigue, Chest Pain, Dizziness, Heart Disease, Diabetes, Stroke
- **Synthetic data.** It was generated to mimic well-known clinical risk relationships (disease likelihood rises with age, BMI, blood pressure and smoking). It contains no real patient information, and the findings illustrate the dashboards; they are not medical conclusions.

## Key Insights

- Overall, about 11.5% of patients have at least one of the three diseases.
- Disease prevalence rises steeply with age, from about 6% in the 18-29 group to about 22% in the 60+ group.
- Obese patients show the highest prevalence (about 18%), against about 8-9% for the Normal BMI group.
- The highest-risk segment is 60+ patients with low exercise levels (about 28% prevalence).
- Average glucose rises steadily with age.

## Web Integration (Flask)

The Tableau dashboards and Story are embedded in a small Flask app using the Tableau Embedding API.

```bash
cd flask_app
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

Routes: `/` (home), `/dashboard/clinical`, `/dashboard/lifestyle`, `/dashboard/population`, `/story`.
To change an embedded view, edit the URLs in `app.py`.

## Performance Notes

| Item | Value |
|---|---|
| Data loaded | 1,500 rows x 16 columns (about 80 KB) |
| Calculated fields | 6 |
| Worksheets | 7 |
| Dashboards | 3 |
| Story scenes | 4 |
| Filters | Measure Names filter plus dashboard "Use as Filter" actions on the charts |
| Dashboard size | Fixed 1200 x 800 desktop layout |

## Repository Structure

```
Health360/
├── README.md
├── data/
│   ├── health360_dataset.csv
│   └── health360_dataset.xlsx
├── tableau/
│   └── Health360.twbx
├── flask_app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
├── screenshots/
└── docs/
    └── Health360_Project_Report.docx
```

## Tools Used

Tableau Public, Python (Flask), Excel / CSV, GitHub