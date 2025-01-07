from botasaurus import *

@browser()
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.google_get("https://www.g2.com/products/github/reviews")
    heading = driver.text('h1')
    print(heading)
    return heading

scrape_heading_task()