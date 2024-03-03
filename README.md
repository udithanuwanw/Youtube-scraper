<!DOCTYPE html>
<html>

<body>
    <h1>YouTube Scraper</h1>
    <p>This script is designed to scrape YouTube for specific information about channels based on search queries.</p>
    <h2>Requirements</h2>
    <ul>
        <li>Python</li>
        <li>Selenium</li>
        <li>PyTube</li>
    </ul>
    <h2>Usage</h2>
    <ol>
        <li>Install the required Python packages:</li>
        <pre><code>pip install selenium pytube</code></pre>
        <li>Run the script:</li>
        <pre><code>python main.py</code></pre>
        <li>Follow the instructions provided in the script's prompts.</li>
    </ol>
    <h2>Features</h2>
    <ul>
        <li>Scrapes YouTube search results for channels.</li>
        <li>Retrieves channel information such as channel ID, name, URL, view count, subscriber count, video count, etc.</li>
        <li>Detects if channels have emails and extracts emails from channel descriptions.</li>
        <li>Extracts social media links from channel pages.</li>
        <li>Outputs the data to a CSV file for further analysis.</li>
    </ul>
    <h2>License</h2>
    <p>This project is licensed under the MIT License. Feel free to modify and distribute it according to the terms of the license.</p>
</body>
</html>
