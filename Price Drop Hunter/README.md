# Price Drop Hunter

A desktop app that scrapes product prices, stores the price history in a
database, and highlights products whose price has dropped.

![screenshot](docs/screenshot.png)

## Features
- Scrapes book titles, prices, and links (2 pages, 40 products) with Playwright
- Stores every scrape with a timestamp in SQLite, building a price history
- Detects price drops by comparing the latest price with the previous one
- Tkinter GUI with search, summary cards, and green highlighting for drops
- Error handling: a failed scrape shows a message and keeps the old data

## Tech stack
Python, Playwright, SQLite, Tkinter

## How to run
1. pip install -r requirements.txt
2. playwright install chromium
3. python price_drop_hunter.py
4. Click Refresh. Click it again later to see price changes.

## How it works
Click Refresh -> scrape pages -> clean prices -> save to SQLite
-> compare latest vs previous price -> update the table

Database: `products` (id, name, url unique) and `prices` (id, product_id,
price, scraped_at). Keeping prices in their own table is what makes
price history possible.

## What I learned
- Scraping with pagination using Playwright
- Designing relational tables and avoiding duplicates with UNIQUE
- Handling None values and edge cases, and testing with fake data
- Closing database connections safely with try/except/finally

## Limitations and future work
- One website; the window freezes briefly while scraping (threading would fix this)
- Ideas: price history chart, a second site, email alerts, scheduled runs