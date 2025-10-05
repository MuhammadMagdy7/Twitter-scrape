# Twitter Hashtag Scraper

## Project Overview

This script is a powerful tool designed to scrape data from Twitter based on a predefined hashtag. It utilizes the `snscrape` library to gather comprehensive details about tweets and the profiles of the users who posted them. The collected data is then neatly organized and saved into three distinct CSV files for further analysis.

The primary goal of this tool is to create structured datasets from public Twitter activity related to a specific topic or trend.

## Features

-   **Hashtag-Based Scraping**: Scrapes all tweets associated with a specified hashtag.
-   **Comprehensive Data Collection**:
    -   **Tweet Details**: Captures tweet content, URL, ID, source, date, language, and engagement counts (replies, retweets, likes).
    -   **User Profile Details**: Captures username, display name, user ID, bio/description, follower/following counts, account creation date, and location.
-   **Organized Output**: Saves the scraped data into three separate, well-structured CSV files:
    1.  `subject.csv`: Contains all tweet-related data.
    2.  `profile.csv`: Contains all user profile-related data.
    3.  `correlation.csv`: Maps User IDs to the Tweet IDs they authored.
-   **Data Preprocessing**: Includes helper functions to clean up tweet content (e.g., remove media links) and parse the tweet source.

## How It Works

1.  **Configuration**: The script is initialized with a hardcoded list of hashtags to search for (in the `query` variable).
2.  **Scraping**: It iterates through each hashtag and uses `snscrape.modules.twitter.TwitterSearchScraper` to fetch tweets.
3.  **Data Extraction**: For each tweet found, the script extracts dozens of data points related to the tweet itself and its author.
4.  **Data Storage**: The extracted data is appended to corresponding lists (`json_opje` for tweets, `profile_det` for profiles).
5.  **File Output**: After the scraping process is complete, the script writes the contents of the lists into three CSV files in the `hash/` directory.

## Output Files

The script will create a directory named `hash/` and generate the following files inside it:

1.  **`hash/subject.csv`**: Contains detailed information about each tweet.
    -   **Columns include**: `Hashtag`, `Username`, `Content`, `Has Photo`, `Id of tweet`, `Url of tweet`, `Source`, `Date`, `Count of replies`, `Count of retweet`, `Count of likes`, etc.

2.  **`hash/profile.csv`**: Contains detailed information about each unique user profile.
    -   **Columns include**: `Username`, `profile name`, `Id of user`, `description`, `verified`, `created`, `Count of followers`, `Count of following`, `Location`, etc.

3.  **`hash/correlation.csv`**: Links users to the tweets they posted.
    -   **Columns**: `User ID`, `Tweet ID`.

## Prerequisites

-   Python 3.x
-   Required Python libraries.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install the required Python packages:**
    The script relies on `snscrape` and `playwright`. It's recommended to install the development version of `snscrape` for better compatibility with Twitter.

    ```bash
    pip install pandas codecs
    pip install git+[https://github.com/JustAnotherArchivist/snscrape.git](https://github.com/JustAnotherArchivist/snscrape.git)
    pip install playwright
    ```
3.  **Install Playwright browsers:**
    (Required even though the Playwright code is commented out, as it's still imported).
    ```bash
    playwright install
    ```

## Usage

1.  **Configure the Hashtag**:
    Open the script and modify the `query` list to include the hashtag(s) you want to scrape.
    ```python
    # a.py
    query = ['#YourHashtagHere']
    ```

2.  **Run the Script**:
    Execute the script from your terminal.
    ```bash
    python a.py
    ```

3.  **Check the Output**:
    Once the script finishes, a `hash/` directory will be created in the same folder, containing the `subject.csv`, `profile.csv`, and `correlation.csv` files.

## Important Notes

* **Playwright Code**: The script contains a large, commented-out block of code that uses the `Playwright` library. This was likely an alternative method for logging into Twitter and searching for hashtags. This functionality is **not active** in the current version.
* **API Changes**: Twitter frequently changes its internal structure, which can break third-party scrapers like `snscrape`. If the script stops working, you may need to check for an updated version of the `snscrape` library.
* **Disclaimer**: This script is for educational purposes. Please be responsible and respect Twitter's Terms of Service when scraping data. Avoid making too many requests in a short period to prevent being rate-limited or blocked.
