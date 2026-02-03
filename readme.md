# NoVacancy (
**Campus Parking Occupancy Predictor & Visualizer for UNC Charlotte**

NoVacancy is a Python-based project designed to give UNC Charlotte students quick insights into campus building occupancy and space availability.  
It scrapes and analyzes occupancy data to provide live updates, historical trends, and forecasted crowd levels.

---

### 🚀 Features
- **Occupancy Forecasting** – Predicts building crowd levels using machine learning models.  
- **Historical Trends** – Interactive, zoomable graphs let you browse occupancy history and usage patterns.  
- **Live Updates** –  Parking data refreshes in real-time every 3 minutes. 
- **Data-driven Insights** – Data analysis finds patterns in campus usage, providing glanceable insights into usage patterns and best times to leave for a particular deck.  

---

### 🧰 Tech Stack
- **Languages:** Python  
- **Libraries:** pandas, Plotly, Facebook Prophet
- **Web Framework:** Flask *(planned)*  
- **Frontend:** React, JavaScript, CSS *(planned)*  

---

### 🗂️ File Structure
```
novacancy/
│
├── forecastModels/ # Forecasting scripts and ML models
├── data/ # Collected occupancy data
├── static/ # Planned assets (CSS/JS)
├── templates/ # Planned web templates
├── forecast_model.py
└── README.md
```



---

### 📍 Roadmap
This is my most complex project to date, so certain features may be in development for a while.
Features to be implemented:

- **Phase 1 - Data Collection & Processing**
    - [x] Data scraping for deck occupancy.
    - [x] Store live data in CSV.
    - [ ] Collect 1-2 months of data.

- **Phase 2 - Data Analysis & Exploration**
    - [x] Set up simple graph script for displaying CSV data.
    - [ ] Create web dashboard for viewing graphs

- **Phase 3 - Forecasting and Modeling**
    - [ ] Develop simple ML forecasting model with Facebook Prophet

- **Phase 4 - Deployment and Website**
    - [ ] Local host runs the entire stack successfully.
    - [ ] Create React frontend
    - [ ] Connect frontend to API


---

### 📄 License
This project is for educational and personal research use.  
Developed at UNC Charlotte by Michael Onate.
</file>
