import requests
import time
from datetime import datetime

# Function to fetch and format the price
def fetch_and_format_price():
    url = "https://api.spot-hinta.fi/JustNow?lookForwardHours=0"
    response = requests.get(url)
    price_in_euros = response.json()['PriceWithTax']
    price_in_cents = price_in_euros * 100
    formatted_price = "{:.2f}".format(price_in_cents)
    return formatted_price

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Electricity Price</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Current Electricity Price:</h1>
    <p id="price">{}</p>
</body>
</html>
"""

# Path to save HTML file
html_file_path = "index.html"

# Initial check when the script starts
initial_price = fetch_and_format_price()
print(f"Initial check completed. Current price: {initial_price} c/kWh")

# Main loop to continuously update HTML
while True:
    # Get the current time
    current_time = datetime.now().strftime("%H:%M")

    # Check if the current time is the desired update time (e.g., at the start of each hour)
    if current_time.endswith(":00"):
        # Fetch and format the price
        formatted_price = fetch_and_format_price()

        # Update HTML template with the latest price
        html_content = html_template.format(formatted_price)

        # Write HTML content to file
        with open(html_file_path, "w") as html_file:
            html_file.write(html_content)
            print(f"Updated HTML at {current_time} with price: {formatted_price} c/kWh")

        # Wait for 1 hour before updating again
        time.sleep(3600)  # 3600 seconds = 1 hour
    else:
        # Wait for 1 minute before checking the time again
        time.sleep(60)  # 60 seconds = 1 minute
