# Financial Earnings Report Presentation

## Overview
This project contains an interactive financial presentation for a quarterly earnings report, based on movie revenue data. The presentation is built using [Reveal.js](https://revealjs.com/), a modern presentation framework.

## Dataset
The data used in this presentation is `Movie Revenue Data.csv`, sourced from [Kaggle](https://www.kaggle.com/datasets/wahaba/movie-revenue-data/data).

## Data Analysis
The financial analysis is performed using Python. The script `analyze_data.py` processes the CSV file and generates `data.js`, which is consumed by the presentation.

To regenerate the data:
1. Ensure Python 3 and pandas are installed (`pip install pandas`).
2. Run the script:
   ```bash
   python3 analyze_data.py
   ```

## Features
- **Interactive Slides**: Built with HTML/CSS/JavaScript.
- **Markdown Support**: Includes slides written in Markdown.
- **Code Highlighting**: Demonstrates code blocks with syntax highlighting.
- **Mathematical Formulas**: Uses MathJax for rendering financial formulas.
- **Animations**: Elements appear using fragments.
- **Speaker Notes**: Includes notes for the presenter.

## Setup and Usage
1.  Clone the repository.
2.  Open `index.html` in a web browser to view the presentation.

## GitHub Pages Deployment
To publish this presentation on GitHub Pages:
1.  Go to the repository settings on GitHub.
2.  Navigate to the **Pages** section.
3.  Under **Source**, select `main` (or `master`) branch and `/ (root)` folder.
4.  Click **Save**. The presentation will be available at the provided URL.

## Contact
- **Email**: 23f2005452@ds.study.iitm.ac.in
