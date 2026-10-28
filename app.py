from flask import Flask, render_template

app = Flask(__name__)

# Paste your Tableau Public URLs here after publishing.
# Format: https://public.tableau.com/views/<WorkbookName>/<SheetName>
# For a Story, use the story sheet's name.
DASHBOARDS = {
    "clinical": {
        "title": "Clinical Risk Assessment",
        "persona": "Dr. Michael Carter, Clinical Risk Assessment Officer",
        "url": "https://public.tableau.com/views/Book1_17931080330870/ClinicalRisk",
    },
    "lifestyle": {
        "title": "Lifestyle & Disease Analysis",
        "persona": "Emily Rodriguez, Healthcare Data Analyst",
        "url": "https://public.tableau.com/views/Book1_17931080330870/Lifestyle",
    },
    "population": {
        "title": "Population Health",
        "persona": "Dr. Priya Nair, Public Health Researcher",
        "url": "https://public.tableau.com/views/Book1_17931080330870/Population",
    },
}

STORY = {
    "title": "Health360 Story",
    "url": "https://public.tableau.com/views/Book1_17931080330870/Story1",
}


@app.route("/")
def home():
    return render_template("index.html", dashboards=DASHBOARDS, story=STORY)


@app.route("/dashboard/<key>")
def dashboard(key):
    d = DASHBOARDS.get(key)
    if not d:
        return "Dashboard not found", 404
    return render_template("viz.html", d=d, dashboards=DASHBOARDS)


@app.route("/story")
def story():
    return render_template("viz.html", d=STORY | {"persona": "All three scenarios"}, dashboards=DASHBOARDS)


if __name__ == "__main__":
    app.run(debug=True)
