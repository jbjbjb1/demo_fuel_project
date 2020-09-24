# Goal
Goal is to web scrape daily and save to DynamoDB table. Aim is to do in free tier of AWS as a learning project.

## Setup
* A venv has been created with the requried packages


## Steps
1. Follow this tutorial https://medium.com/@kagemusha_/scraping-on-a-schedule-with-aws-lambda-and-cloudwatch-caf65bc38848
2. Do this DynamoDB tutorial https://aws.amazon.com/getting-started/hands-on/create-nosql-table/
3. To get oil price will need to do this tutorial to get data that is javascript generated https://robertorocha.info/setting-up-a-selenium-web-scraper-on-aws-lambda-with-python/

## More on serverless
* `serverless deploy`
* `serverless invoke -f fuel-scrape   # --aws_profile serverless`

## Up to
getting access denied error (see tutorial)