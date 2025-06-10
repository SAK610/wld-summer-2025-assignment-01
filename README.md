### 1. Project description

U.S. Unemployment Rate Analysis

This project conducts a historical analysis of U.S. unemployment trends using publicly available data from the Federal Reserve Economic Data (FRED). It explores labor market patterns, the effects of major economic events, and decade-level statistics using Python. The analysis is implemented as a standalone script.

---

#### Project Structure

- `UNRATE.csv` – Source dataset from FRED
- `unemployment_analysis.py` – Python script containing all analysis and visualizations
- `requirements.txt` – List of required Python packages
- `README.md` – Project overview and instructions
- `results.txt` – Project results details

---



### 2. Create and activate a virtual environment
Use the terminal

uv venv --python 3.12
source .venv/bin/activate

uv pip install -r requirements.txt  


### 3. How to Run the Analysis
Ensure the virtual environment is activated.

Run the Python script
python unemployment_analysis.py


### 4. Key findings from analysis
The highest unemployment rate occurred in April 2020 at 14.8%, due to the COVID-19 pandemic.

The 2008 financial crisis peaked at 10.0% unemployment in October 2009.

The 1990s were the most stable decade, with a standard deviation of 1.05%, indicating a steady labor market.

The 1980s recorded the highest average unemployment rate at 7.27%.

Between 2015 and 2025, the unemployment rate decreased from 5.7% to 4.1%, reflecting post-crisis economic recovery.


### 5. Data source attribution

Federal Reserve Economic Data (FRED)
Series: UNRATE – Unemployment Rate
Provider: U.S. Bureau of Labor Statistics
Frequency: Monthly

### 6. GenAI usage
This project used Open AI's ChatGPT to form the structure of the readme file 

Git repository link
https://github.com/SAK610/wld-summer-2025-assignment-01.git
