# Readme
This is a machine learning project. It is using data on fuel price, exhange rate and oil price to predict the fuel price in advance.

## Progress
* I have an active web scraper collecting the 3 main sources of data (see below). See folder /daily_webscrape for details of this.

## Next steps
* Create machine learning algorithm to predicte fuel price
* Run this on lambda weekly
* Create a user friendly. page that is updated weekly based on the above

## Sources of data:
* SINGAPORE MOGAS 95 UNLEADED - https://www.tradingview.com/symbols/NYMEX-AV02%21/
* Singapore exchange rate - https://www.rba.gov.au/statistics/frequency/exchange-rates.html
* South of river, Perth, best ULP fuel price - https://www.fuelwatch.wa.gov.au/fuelwatch/pages/home.jspx
* [maybe] Brent oil price
* [maybe] WTI oil price
* [maybe] NY harbour gasoline oil price
* [maybe] AUD-USD exchange rate as oil is traded in this too

## Info sources on factors impacting fuel price
* What impacts fuel prices? https://www.accc.gov.au/consumers/petrol-diesel-lpg/about-fuel-prices
* In the long-run petrol prices are mainly determined by Tapis crude oil and Singapore petrol prices https://ro.uow.edu.au/cgi/viewcontent.cgi?article=1073&context=aabfj

## Approaches to machine learning to predict fuel price
1. Four ways to sync time series data https://towardsdatascience.com/four-ways-to-quantify-synchrony-between-time-series-data-b99136c4a9c9
2. Mistakes not to make when syncing time series data https://www.linkedin.com/pulse/how-use-machine-learning-time-series-forecasting-vegard-flovik-phd-1f/?trk=related_artice_How%20(not)%20to%20use%20Machine%20Learning%20for%20time%20series%20forecasting%3A%20The%20sequel_article-card_title
3. Masters thesis on good way to sync time series data https://pdfs.semanticscholar.org/8824/fb4ef14f94f96a9d6799551e99a612fa7cf3.pdf
4. Google search on the topic https://www.google.com/search?safe=strict&rlz=1C1CHBF_en-GBAU903AU903&sxsrf=ALeKk01rANBO4IOZu4cAVc_L6gK3IDZ_xg%3A1595502105744&ei=GW4ZX4mJLbnE4-EP_MyOyA4&q=machine+learning+how+to+find+relationship+between+two+curves+time+series&oq=machine+learning+how+to+find+relationship+between+two+curves+time+series&gs_lcp=CgZwc3ktYWIQAzIECCEQCjoECCMQJ1DKQFjKU2CIVGgBcAB4AIABzQKIAb0YkgEGMi0xMS4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwjJ-YDCnOPqAhU54jgGHXymA-kQ4dUDCAw&uact=5
5. When models have been made, test on things like sin(x) vs sin(2x) or 2*sin(x) to test how well they work
6. Maybe the seasonal/weekly trends have to be removed from the data before using the comparisons etc.a

## More data sources
* AUD/SGD: https://au.investing.com/currencies/aud-usd-historical-data
* AUD/SGD: https://au.investing.com/currencies/aud-sgd-historical-data
* Brent Oil: https://www.eia.gov/dnav/pet/hist/RBRTED.htm
* WTI Oil: https://www.eia.gov/dnav/pet/hist/RWTCD.htm
* For daily oil prices: https://www.reuters.com/quote/CLc1
* Fuelprices WA SoR: https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/historicalFileDownloadRetail.jspx