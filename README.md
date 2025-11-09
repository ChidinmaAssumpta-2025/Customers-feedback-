
# 🧾 QuickSupply ETL Pipeline — End-to-End Data Engineering Project

## 📊 Project Overview

**QuickSupply** is a small business that supplies essential goods (like beverages, cleaning products, and food items) to local shops across different towns.

Recently, the company has been facing:

* Frequent **stockouts** on certain items
* Excess inventory of **slow-moving products**
* **Supplier reliability** concerns

The management suspects that:

* Demand differs across locations
* Some products are overstocked or understocked
* Certain suppliers are inconsistent

This project provides a **data-driven solution** by building an **end-to-end ETL (Extract, Transform, Load)** pipeline to collect, process, and store customer feedback data from **KoboToolbox** into **PostgreSQL** for analysis and decision-making.

---

## 🚀 Project Goals

1. Collect feedback data from field agents using **KoboToolbox forms**.
2. Automate data extraction using Python and environment variables (.env).
3. Transform and clean the collected CSV data.
4. Load the processed data into a **PostgreSQL database** for analysis.
5. Enable QuickSupply management to identify:

   * High-demand vs. low-demand products
   * Stock imbalance across regions
   * Supplier performance patterns

---

## 🛠️ Tech Stack

| Component                  | Technology                                 |
| -------------------------- | ------------------------------------------ |
| **Data Source**            | KoboToolbox                                |
| **Language**               | Python                                     |
| **Database**               | PostgreSQL                                 |
| **Environment Management** | `.env` file via `python-dotenv`            |
| **Libraries**              | `pandas`, `requests`, `psycopg2`, `dotenv` |

---

## 🧩 ETL Pipeline Breakdown

### 1️⃣ Extract

* Fetches live data from **KoboToolbox API** using secure authentication (via `.env` file).

### 2️⃣ Transform

* Reads CSV data, handles missing/invalid rows using `pandas`.

### 3️⃣ Load

* Automatically creates schema and table in **PostgreSQL**.
* Inserts all transformed records into the target table (`customers_feedback`).

---

## 🔐 Environment Variables

Create a `.env` file in your project root.
---

## ▶️ How to Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/customers-feedback-etl.git
   cd customers-feedback-etl
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** and fill in your credentials.

4. **Run the ETL pipeline**

   ```bash
   python main.py
   ```

5. ✅ Once complete, your data will be available in PostgreSQL under:
   **Schema:** `Chidinma_1`
   **Table:** `customers_feedback`

---

## 📈 Business Impact

This project enables **QuickSupply** to:

* Monitor customer satisfaction by region.
* Detect stock management issues early.
* Improve supplier reliability decisions.
* Reduce stockouts and overstocking through data insights.

---

## 💡 Key Highlights

* Fully **automated ETL pipeline** (no manual data entry).
* Uses **best practices** for credential management (`.env` file).
* Demonstrates an **end-to-end data engineering workflow** — from data collection to storage.
* Scalable and adaptable for other data sources or schemas.

---

## 👩‍💻 Author

**Chidinma Assumpta Nnadi**
Data Engineer | Analyst | Problem Solver
📧 *[[your.email@example.com](mailto:your.email@example.com)]*
🔗 *[LinkedIn or GitHub Profile]*

---

Would you like me to include a **`requirements.txt`** section (listing the Python dependencies) in the README as well? It helps users easily reproduce your setup.
