## 🧠 Project: OOP Stock Market Analysis with PostgreSQL

This project teaches Object-Oriented Programming (Unit 6) and Design Patterns (Unit 12) using real stock market data stored in a PostgreSQL database hosted on Supabase.

---

### 📂 Project Overview
- Connect to a Supabase PostgreSQL database
- Read stock and company data from tables
- Use OOP to model companies and stock prices
- Apply Strategy, Factory, Singleton, and Repository Patterns
- Use GUI input to generate PDF reports

---

### 🗃️ Database Schema (What the DB Carries)

#### Table: `company_info`
| Column         | Description                            |
|----------------|----------------------------------------|
| Symbol         | Ticker symbol (e.g. AAPL)              |
| Company_Name   | Full name of the company               |
| Industry       | Industry category (e.g. Technology)    |
| Market_Cap     | Market capitalization (numeric/float) |

#### Table: `stock_market_data`
| Column         | Description                            |
|----------------|----------------------------------------|
| Date           | Trading date (YYYY-MM-DD)             |
| Open           | Opening price                          |
| High           | Highest price that day                |
| Low            | Lowest price that day                 |
| Close          | Closing price                         |
| Adj_Close      | Adjusted close for splits/dividends   |
| Volume         | Number of shares traded               |
| Name           | Ticker symbol (same as Symbol)        |
| Company_Name   | Full name of the company              |

---

### ✅ Prerequisites
- Python 3.8 or higher
- PostgreSQL database hosted on Supabase
- Access to `.env` file with `DATABASE_URL`

---

### 📦 Required Libraries
Create a file called `requirements.txt` and paste:

```txt
psycopg2-binary
pandas
python-dotenv
fpdf
tqdm
```

Then run:
```bash
pip install -r requirements.txt
```

---

### ⚙️ Setup Instructions
1. Clone the repository or copy the project folder.
2. Create a `.env` file in the root directory with:

```env
DATABASE_URL=postgresql://username:password@host:port/dbname
```

3. Ensure your database has the two tables as described above.

4. Run the project:
```bash
python main.py
```

---

### 🎯 Learning Goals by Unit
- **Unit 6**: Class design, constructors, methods
- **Unit 8**: Exception handling with `try/except`
- **Unit 9**: Regex input validation
- **Unit 10**: Filtering/sorting data
- **Unit 11**: Tkinter GUI input
- **Unit 12**: Factory, Singleton, Repository, and Strategy patterns

---

### 📄 Output
- Console logs of activity
- `PDF` report showing average price and stock history

---

Happy coding and learning! 🚀