from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com")

wait = WebDriverWait(driver, 10)

all_books = []
page = 1

while True:
    print(f"\n--- Scraping page {page} ---")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_pod")))

    # Get all books on current page
    books = driver.find_elements(By.CLASS_NAME, "product_pod")

    for book in books:
        title  = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        price  = book.find_element(By.CLASS_NAME, "price_color").text
        rating = book.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split()[-1]
        all_books.append({"title": title, "price": price, "rating": rating})
        print(f"  {title[:40]} | {price} | {rating} stars")

    # Check if there's a next page
    try:
        next_btn = driver.find_element(By.CLASS_NAME, "next")
        next_btn.find_element(By.TAG_NAME, "a").click()
        page += 1
        time.sleep(2)

        # Stop after 3 pages for demo
        if page > 3:
            print("\nStopping at page 3 for demo...")
            break
    except:
        print("\nNo more pages!")
        break

print(f"\n=== Total books scraped: {len(all_books)} ===")
print(f"Price range: {min(b['price'] for b in all_books)} - {max(b['price'] for b in all_books)}")

# Find most common rating
from collections import Counter
ratings = Counter(b['rating'] for b in all_books)
print(f"Ratings breakdown: {dict(ratings)}")

driver.quit()