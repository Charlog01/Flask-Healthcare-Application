# Income Spending Survey System (Final Project)

**Course:** BAN6420 – Programming in R and Python  
**Student:** Charles Orji  
**Institution:** Nextford University  
**Date:** 13th February, 2026  

---

## Assignment Overview

This final project implements a **web-based survey and data analytics system** designed to collect and analyze participants’ income and spending behavior in preparation for a **healthcare industry product launch**.

The solution integrates **Flask web development**, **MongoDB data storage**, **Object-Oriented Programming (OOP)** in Python, **CSV data processing**, **Jupyter Notebook data analysis**, **data visualization**, and **cloud deployment readiness on AWS**.

---

## Requirements Checklist

| Requirement | Status | Notes |
|-----------|--------|------|
| Flask web application for data collection | Completed | User-friendly survey form |
| MongoDB data storage | Completed | Stores demographics & expenses |
| Expense categories with checkboxes and amount fields | Completed | Utilities, entertainment, school fees, shopping, healthcare |
| Python class named `User` | Completed | Used during CSV export |
| Loop MongoDB data into CSV | Completed | `responses.csv` generated |
| Load CSV into Jupyter Notebook | Completed | Pandas-based analysis |
| Visualization: ages with highest income | Completed | Bar chart |
| Visualization: gender spending distribution | Completed | Stacked bar chart |
| Export charts for PowerPoint | Completed | High-resolution PNG |
| AWS deployment readiness | Completed | Elastic Beanstalk compatible |
| ZIP submission with documentation | Completed | This package |

---

## Project Structure

```text
income-spending-survey/
│
├── application.py              # Flask application (AWS-ready)
├── config.py                   # Environment-based configuration
├── export_to_csv.py            # User class & CSV export
├── requirements.txt            # Python dependencies
├── Procfile                    # Gunicorn startup (AWS)
├── runtime.txt                 # Python version
├── .env.example                # Environment variable template
├── README.md                   # Project documentation
│
├── templates/
│   ├── base.html
│   ├── index.html              # Survey form
│   └── success.html
│
├── data/
│   └── responses.csv           # Generated CSV output
│
├── notebooks/
│   └── analysis.ipynb          # Data analysis & visualization
│
└── static/
    └── charts/
        ├── top_ages_income.png
        └── gender_spend_by_category.png
```
---

## How to Run (Local Environment)

1. **Ensure Python 3.11+ is installed**
2. Open a terminal in the project directory
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
   Update `.env` with your MongoDB connection string.

6. Start the Flask application:
   ```bash
   flask --app application run --debug
   ```
7. Open a browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Data Processing & Visualization

1. **Export MongoDB data to CSV**
   ```bash
   python export_to_csv.py
   ```
   This creates `data/responses.csv`.

2. **Run the Jupyter Notebook**
   - Open `notebooks/analysis.ipynb`
   - Run all cells

3. **Generated Outputs**
   - `static/charts/top_ages_income.png`
   - `static/charts/gender_spend_by_category.png`  
   (High-resolution, PowerPoint-ready)

---

## AWS Deployment

This project is configured for **Amazon Web Services (Elastic Beanstalk)**.

Required AWS environment variables:
- `MONGO_URI`
- `SECRET_KEY`
- `DB_NAME`
- `COLLECTION_NAME`

Included deployment files:
- `application.py`
- `Procfile`
- `requirements.txt`
- `runtime.txt`

---

## Conclusion

This final project successfully demonstrates the **end-to-end development of a data-driven survey and analytics system**, combining web development, database management, object-oriented programming, data analysis, visualization, and cloud deployment.
All assignment requirements have been fully implemented following best practices in **Python development, data engineering, and documentation**.
