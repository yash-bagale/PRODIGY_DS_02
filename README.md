# 🚢 Titanic Data Cleaning & Exploratory Data Analysis (EDA)

---

## 📌 Project Overview

This project performs **Data Cleaning** and **Exploratory Data Analysis (EDA)** on the  
**Titanic - Machine Learning from Disaster** dataset from Kaggle.

The objective is to analyze passenger data and identify patterns that influenced survival.

---

## 🎯 Problem Statement

The Titanic dataset contains passenger demographic and travel information.  
The goal of this project is to:

- Clean the dataset
- Handle missing values
- Explore relationships between variables
- Identify survival trends
- Generate meaningful insights using visualization

---

## 📂 Dataset Information

Dataset Source: Kaggle  
File Used: `train.csv`

### 🔎 Features in Dataset

| Feature | Description |
|----------|------------|
| PassengerId | Unique passenger ID |
| Pclass | Ticket class (1, 2, 3) |
| Name | Passenger name |
| Sex | Gender |
| Age | Age of passenger |
| SibSp | Siblings/Spouses aboard |
| Parch | Parents/Children aboard |
| Ticket | Ticket number |
| Fare | Ticket fare |
| Cabin | Cabin number |
| Embarked | Port of embarkation |
| Survived | Survival status (0 = No, 1 = Yes) |

---

## 🧹 Data Cleaning Process

- Filled missing **Age** values using median
- Filled missing **Embarked** values using mode
- Dropped **Cabin** column due to excessive missing values
- Verified dataset integrity after cleaning

---

## 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

-  Survival distribution
-  Survival by gender
-  Survival by passenger class
-  Age distribution
-  Fare distribution
-  Correlation analysis between numerical features

---

## 🔎 Key Insights

- Female passengers had significantly higher survival rates.
- 1st class passengers had higher survival probability.
- Higher ticket fares correlated positively with survival.
- Majority of passengers were aged between 20–40 years.
- Overall survival rate was lower than non-survival rate.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib

---

## 📁 Project Structure

```
Titanic-EDA-Project/
│
├── train.csv
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yash-bagale/PRODIGY_DS_02.git
cd Titanic-EDA-Project
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install pandas matplotlib
```

---

## ▶️ How to Run

Make sure `train.csv` is in the project folder.

Run:

```bash
python main.py
```

The script will:
- Clean the dataset
- Generate visualizations
- Print correlation analysis
- Display key findings






