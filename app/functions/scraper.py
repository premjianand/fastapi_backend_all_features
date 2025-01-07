from functools import wraps
from botasaurus import *
# from botasaurus.driver import AntiDetectDriver
# from botasaurus import 


# def browser(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # Initialize the AntiDetectDriver (a customized Selenium driver)
#         driver = AntiDetectDriver()
#         try:
#             # Call the decorated function, passing the driver as an argument
#             result = func(driver, *args, **kwargs)
#         except Exception as e:
#             # Handle errors and optionally log them
#             print(f"An error occurred: {e}")
#             raise
#         finally:
#             # Ensure the driver is properly closed
#             driver.quit()
#         return result
#     return wrapper



# @browser()
# def scraper(driver: AntiDetectDriver, data: dict):

#     # navigate to the target website
#     driver.google_get("https://opensea.io")