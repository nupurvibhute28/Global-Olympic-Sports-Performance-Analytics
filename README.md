# Global Olympic Sports Performance Analytics (1992–2026)

## 📌 Project Overview
**Global Olympic Sports Performance Analysis** is an interactive data analytics and visualization project built using **Tableau Public** and integrated into a **Python Flask** web application. The project evaluates Olympic medal achievements, regional efficiency, sports category performance, and national sports investment trends from **1992 to 2026**.

---

## 📂 Datasets Used
The data model connects four structured CSV datasets in Tableau:
1. **`alltime_country_rankings.csv`** (60 rows, 13 columns) – Overall historical rankings, medal totals, and regional efficiency across 60 nations.
2. **`medal_results.csv`** (910 rows, 19 columns) – Edition-level medal counts, athlete participation, GDP tiers, and sports investment metrics.
3. **`athletes.csv`** (8,000 rows, 26 columns) – Individual athlete demographics, sport categories, training hours, and career performance.
4. **`games_summary.csv`** (18 rows, 10 columns) – Host cities, participating nations, and total medals awarded across 18 Olympic Games (1992–2026).

---

## 📊 Key Visualizations & Dashboards
* **Dashboard 1: Global Sports Performance Analytics Dashboard**
  * **KPI Banner:** Global Athlete Participation (`910`), Total Sports Categories Entered (`60`), Total Nations Represented (`18`).
  * **Total Medal Achievements Across Nations:** Interactive choropleth world map (`11` to `735` medals).
  * **Trend of Total Medals Awarded Over the Years:** Time-series line chart from `1992` to `2026`.
  * **Avg Medals per Athlete by Sport Category:** Horizontal bar chart across 21 sport categories (led by Rowing at `6.916` and Shooting at `6.731`).
  * **Global Performance Metrics by Country:** Top 10 vertical bar chart controlled by a dynamic `KPI Selector` parameter (`Total Medals`, `Total Gold`, `Total Silver`, `Total Bronze`).

* **Dashboard 2: Olympic Performance and Regional Efficiency Dashboard**
  * **KPI Banner:** Regional Performance Efficiency (`33.2%`), Countries Participating (`60`), Athlete Participation Count (`8,000`), Average Medal Efficiency (`31.8%`).
  * Regional efficiency comparisons, sports investment vs. medal output analysis, and cross-country medal breakdowns.

* **Story: Olympic Performance Story**
  * Multi-point guided narrative walking through historical trends, country dominance, sport category averages, and regional efficiency.

---

## 🛠️ Tech Stack & Web Integration
* **Data Visualization:** Tableau Public
* **Backend Framework:** Python (Flask)
* **Frontend:** HTML5, CSS3, Tableau JavaScript Embed API v1

---

## 🚀 How to Run Locally
1. Clone this repository or download the `Olympic_Sports_Analysis` folder.
2. Install Flask:
   ```bash
   py -m pip install flask
   
 Run the Flask server:py app.py

Open your browser and visit: https://global-olympic-sports-performance-xtdd.onrender.com

👤 Author
Nupur Vibhute
