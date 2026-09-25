# 🧴 AI Skin Consultant

> **Personalized skincare recommendations based on your skin type and skincare concerns.**

AI Skin Consultant is a **Streamlit-based skincare recommendation app** that uses categorized skincare data to suggest products based on a user's **skin type** and **main concern**.

## ✨ Features

* 🧑‍🔬 Select from **5 skin types**

  * Oily
  * Dry
  * Combination
  * Normal
  * Sensitive
* 🎯 Choose from **5 skincare concerns**

  * Acne
  * Pigmentation
  * Hydration
  * Sun Protection
  * Dark Spots
* 🔎 Filters products based on the selected profile
* 🖼️ Displays product images
* 🔗 Provides direct product-page links
* 📋 Shows up to **6 personalized recommendations**
* ⚡ Interactive interface built with Streamlit
* 💾 Uses cached data loading for improved performance

## 🧠 How It Works

```text
👤 User
   │
   ├── Skin Type
   │
   └── Main Concern
          │
          ▼
   ┌───────────────────┐
   │  Indian Skincare  │
   │      Dataset      │
   └─────────┬─────────┘
             │
             ▼
      🔎 Data Filtering
             │
             ▼
   🧴 Matching Products
             │
       ┌─────┴─────┐
       ▼           ▼
    Product      Product
     Image         Link
```

The application filters the dataset by matching the selected **Skin type** and **Concern** columns, then displays the matching products.

## 🖥️ App Interface

```text
┌─────────────────────────────────────┐
│        🧴 AI Skin Consultant        │
├─────────────────────────────────────┤
│                                     │
│  ✨ Your Skin Profile               │
│                                     │
│  Skin Type                           │
│  [ Oily ▼ ]                         │
│                                     │
│  Main Concern                       │
│  [ Acne ▼ ]                         │
│                                     │
│       [ Generate My Routine ]       │
│                                     │
├─────────────────────────────────────┤
│  Your Personalized Recommendations │
│                                     │
│  🧴 Product 1                       │
│  Best For: Acne                     │
│  🔗 View Product Page               │
│                                     │
└─────────────────────────────────────┘
```

## 🗂️ Dataset

The project contains two CSV datasets:

### `indian_skincare_dataset.csv`

The primary dataset used by the Streamlit application.

It contains:

| Column        | Description                 |
| ------------- | --------------------------- |
| `Skin type`   | Suitable skin type          |
| `Product`     | Product name                |
| `Concern`     | Associated skincare concern |
| `product_url` | Product page                |
| `product_pic` | Product image               |

### `skincare_products_clean.csv`

A separate cleaned skincare product dataset containing information such as:

* Product name
* Product URL
* Product type
* Ingredients
* Price

> The current Streamlit application uses `indian_skincare_dataset.csv` for recommendations.

## 🛠️ Tech Stack

```text
Python
│
├── Streamlit  → Interactive Web App
├── Pandas     → Data Loading & Filtering
└── CSV        → Skincare Product Data
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/manavupadhyay1/AI-Skincare-Recommendation.git
cd AI-Skincare-Recommendation
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate it

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install streamlit pandas
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL provided by Streamlit, usually:

```text
http://localhost:8501
```

## 📁 Project Structure

```text
AI-Skincare-Recommendation/
│
├── 📄 app.py
├── 📊 indian_skincare_dataset.csv
├── 📊 skincare_products_clean.csv
├── 🚫 .gitignore
└── 📄 README.md
```

## 🔍 Recommendation Logic

The recommendation process is intentionally simple and transparent:

```python
filtered = df[
    (df['Skin type'].str.contains(stype, case=False, na=False)) &
    (df['Concern'].str.contains(sconcern, case=False, na=False))
]
```

The application:

**Skin Type + Concern → Dataset Filtering → Product Recommendations**

This makes the recommendation logic easy to understand and extend.

## 🎯 Future Improvements

* [ ] 🤖 Machine-learning-based recommendations
* [ ] 🧴 Product category filtering
* [ ] 🧪 Ingredient-based recommendations
* [ ] 💰 Price-based filtering
* [ ] ⭐ Product rating system
* [ ] 📊 Recommendation scoring
* [ ] 🧠 Personalized skincare routine generation
* [ ] 📱 Mobile-friendly interface
* [ ] 📈 Recommendation analytics
* [ ] 🚀 Deploy the application online

## 💡 Project Goal

The goal of AI Skin Consultant is to make skincare product discovery **simpler and more personalized** by connecting a user's skin profile with structured skincare product data.

> **Choose your skin profile. Discover products that match. 🧴✨**

## 👨‍💻 Author

**Manav Upadhyay**
BTech Information Techn
