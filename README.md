# Smart Web Scraper Dashboard

An end-to-end **Python Web Scraping Dashboard** built with **Streamlit**, **BeautifulSoup**, **SQLite** and **Plotly**. This application allows users to scrape website data, store it in a database, visualize the results, search and filter records and export the data in multiple formats.

---

## Features

- Scrape data from a user-provided website URL
- Store scraped data in a SQLite database
- Interactive dashboard with visual analytics
- Search and filter scraped records
- View charts and statistics
- Maintain scraping history
- Export data to CSV, Excel, and JSON
- Duplicate record prevention
- Modern Streamlit user interface

---

## Screenshots


## Project Structure

```text
SmartWebScraperDashboard/

│── app.py
│── scraper.py
│── database.py
│── scheduler.py
│── export.py
│── requirements.txt

├── database/
│      scraper.db

├── pages/
│      Dashboard.py
│      History.py
│      Export.py

├── utils/
│      helper.py

├── assets/
│      logo.png

└── README.md
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | User Interface |
| Requests | HTTP Requests |
| BeautifulSoup | HTML Parsing |
| SQLite | Database |
| Pandas | Data Processing |
| Plotly | Interactive Charts |
| OpenPyXL | Excel Export |
| APScheduler | Automated Scraping |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/universal-web-scraper-dashboard.git
```

---

### 2. Navigate into the project

```bash
cd smart-web-scraper-dashboard
```

---

### 3. Create a virtual environment (Recommended)

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## Database

The project uses **SQLite** for storing scraped data.

## Dashboard

The dashboard provides

- Total Records
- Total Authors
- Search
- Filters
- Recent Scraped Data

---

## Export Options

Users can export scraped data as

- CSV
- Excel (.xlsx)
- JSON

---

## Workflow

```text
          Website URL
                │
                ▼
      BeautifulSoup Scraper
                │
                ▼
          SQLite Database
                │
                ▼
     Streamlit Dashboard
                │
      ┌─────────┼─────────┐
      ▼         ▼         ▼
 Dashboard   History    Export
```

---

## Future Improvements

- Support multiple website templates
- AI-powered content summarization
- Scheduled scraping
- User authentication
- Docker support
- REST API integration
- Dark mode
- Email notifications
- Cloud deployment
- Keyword alerts

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---


## 👨‍💻 Author

**Aditya Sharma**

GitHub: https://github.com/AdityaSh11-11

LinkedIn: https://www.linkedin.com/in/sharma11aditya/

---

## Support

If you found this project useful,

Star this repository

Fork it

Share it with others

---

### Thank you for visiting this project!
