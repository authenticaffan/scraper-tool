import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [website, setWebsite] = useState('');
  const [targetElement, setTargetElement] = useState('');
  const [scrapedData, setScrapedData] = useState('');
  const [error, setError] = useState('');

  const handleScrape = async () => {
    setError(''); // Clear previous errors

    if (!website || !targetElement) {
      setError('Please enter both website URL and target element.');
      return;
    }

    try {
      const response = await axios.post('http://localhost:8000/scrape/', {
        website,
        targetElement
      });

      if (response.status !== 200) {
        throw new Error('Failed to scrape website.');
      }

      setScrapedData(response.data.scraped_data);
      setError('');
    } catch (err) {
      console.error(err);
      setError(err.response && err.response.data ? err.response.data.error : 'An error occurred while scraping the website.');
    }
  };

  return (
    <div className="App">
      <h1>Web Scraper</h1>
      <div>
        <label htmlFor="website">Website URL:</label>
        <input
          type="text"
          id="website"
          value={website}
          onChange={(e) => setWebsite(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="target">Target Element:</label>
        <select
          id="target"
          value={targetElement}
          onChange={(e) => setTargetElement(e.target.value)}
        >
          <option value="">Select an element</option>
          <option value="h1">H1</option>
          <option value="p">Paragraph</option>
          <option value=".title">Class: Title</option>
          <option value="#main">ID: Main</option>
          <option value="div">DIV</option>
          <option value="span">SPAN</option>
          {/* Add more options as needed */}
        </select>
      </div>
      <button onClick={handleScrape}>Scrape</button>
      {error && <div className="error">{error}</div>}
      {scrapedData && <div className="scraped-data">Scraped Data: {scrapedData}</div>}
    </div>
  );
}

export default App;
