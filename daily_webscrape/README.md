# Readme

The purpose of this is to daily scrape the prices that will be needed for machine learning.

## Progress

Successful use of https://github.com/jairovadillo/pychromeless, with some help from https://robertorocha.info/setting-up-a-selenium-web-scraper-on-aws-lambda-with-python/ and https://stackoverflow.com/questions/49939123/scrape-dynamic-contents-created-by-javascript-using-python to set up web scraping. The challenge was that selenium was needed first to render the page, then the info could be scraped from it.

## Future work

* Set up alerts if data fails to be scraped
* Handle changes that regularly occur on the websites to allow continual scraping