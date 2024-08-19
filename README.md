This script automates the process of collecting information about the latest videos from a specific YouTube channel using the Selenium and BeautifulSoup libraries in Python. Here's a breakdown of what the script does:

1. Setup and Configuration
Libraries Imported: The script imports necessary libraries: BeautifulSoup for parsing HTML, Selenium for browser automation, webdriver_manager to manage the ChromeDriver installation, time for pauses, and pandas for data manipulation and exporting.
Chrome WebDriver Setup: The script sets up a Chrome WebDriver with options to ignore certain SSL errors and disable logging. It uses webdriver_manager to automatically install the ChromeDriver.
2. Open YouTube Channel
Navigate to YouTube Channel: The script opens a YouTube channel (in this case, @ZyoniK) by navigating to the channel's videos page.
3. Handle Cookies
Handle Cookie Consent: If a cookie consent popup appears (with an option to "Reject all"), the script clicks on the button to dismiss it. If no such popup appears, it continues without interruption.
4. Scrolling to Load Videos
Fast Scrolling: The script scrolls down the page repeatedly to load more videos. This is necessary because YouTube loads additional videos dynamically as you scroll down. The scrolling pauses briefly (0.5 seconds) between each scroll.
Stop After Loading 50 Videos: The script stops scrolling once it has loaded at least 50 video entries.
5. Extract Video Data
Parse HTML with BeautifulSoup: After scrolling, the script extracts the HTML content of the page using BeautifulSoup.
Find Video Details: It locates all the video elements on the page and extracts relevant information for each video:
Title: The title of the video.
URL: The URL link to the video.
Views: The number of views the video has.
Age: The time since the video was uploaded (e.g., "2 days ago", "1 month ago").
Limit to 50 Videos: The script then limits the list to the first 50 videos, regardless of how many were loaded.
6. Convert and Clean Data
Convert Views to Numeric Format: A helper function convert_views converts view counts from a string format with suffixes like "K" (thousands) or "M" (millions) into numeric values for easier analysis.
7. Save to CSV
Export Data to CSV: The script converts the collected video data into a Pandas DataFrame and saves it to a CSV file named "Youtube_list_zionik.csv".
8. Cleanup
Close the Browser: Finally, the script closes the Chrome browser session to free up resources.
Summary:
The script automates the collection of video data from a YouTube channel, specifically focusing on the latest 50 videos. It scrapes video titles, URLs, view counts, and upload times, then processes this data into a structured format and saves it to a CSV file.
