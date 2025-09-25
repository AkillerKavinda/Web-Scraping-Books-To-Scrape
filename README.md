# Web Scraping: Books to Scrape

This project uses [Scrapy](https://scrapy.org/) to collect book data (titles, prices, and ratings) from [books.toscrape.com](http://books.toscrape.com). It includes a scraping pipeline, a cleaned dataset saved as a CSV file, and a Jupyter notebook for analyzing the data with clear visualizations.

---

## Project Overview

This project:
- Scrapes book data using two Scrapy spiders:
  - `books.py`: Collects titles, prices, and star ratings.
  - `books-rating-num.py`: Converts star ratings to numbers (e.g., "One" to 1).
- Saves the scraped data to `books.csv`.
- Analyzes the data in a Jupyter notebook (`books-analysis.ipynb`) with:
  - Price distribution histogram
  - Rating vs. price scatter plots
  - Violin and box plots for price trends
  - Correlation heatmaps to show data relationships
- Focuses on simple, clean code and clear visualizations.

---

## Project Structure

```
Web-Scraping-Books-To-Scrape/
├── books-analysis.ipynb        # Jupyter notebook for data analysis
├── books.csv                  # Scraped dataset
├── books/                     # Scrapy project folder
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       ├── books.py           # Spider for basic scraping
│       ├── books-rating-num.py # Spider with numeric rating mapping
│       └── books.csv          # Optional output file
├── scrapy.cfg                 # Scrapy configuration
├── requirements.txt           # Python dependencies
└── .gitignore                # Excludes unnecessary files
```

---

## How to Run the Spider

Make sure you're in the project directory and have Scrapy installed:

```bash
scrapy crawl books
```

Or to run the spider with numeric rating mapping:

```bash
scrapy crawl books-rating-num
```

---

## Dependencies

The project requires the following Python packages (listed in `requirements.txt`):
- `scrapy`
- `jupyter`
- `pandas`
- `matplotlib`
- `seaborn`
- `numpy`

---

## Author

**Akilla Kavinda Herath**  
Focused on clean scraping logic, reproducible analysis, and clear visualizations. Built to be simple.

---