# File Name : CSVUtilities
# Student Name: Asfia Siddiqui, Zoha Iqbal
# email:  siddiqaf@mail.uc.edu, iqbalza@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Cleans out data to give cleaner data
# Brief Description of what this module does. Cleans out duplicates
# Citations: chatgpt.com
# Anything else that's relevant:
import requests
import time

class FuelDataCleaner:
    def __init__(self, api_key):
        self.api_key = api_key

    def remove_duplicates_and_format_price(self, data):
        """
        Removes duplicate rows and formats 'Gross Price' to two decimals as a string.
        """
        seen = set()
        cleaned = []

        for row in data:
            row_key = tuple(row.items())
            if row_key not in seen:
                seen.add(row_key)

                try:
                    price = float(row.get("Gross Price", "0"))
                    row["Gross Price"] = "{:.2f}".format(price)
                except:
                    row["Gross Price"] = "0.00"

                cleaned.append(row)

        return cleaned

    def fill_missing_zip_codes(self, data):
        """
        Fills ZIP codes for up to 5 rows where 'Zip' is missing.
        """
        lookup_limit = 5
        lookup_count = 0

        for row in data:
            if "Zip" not in row or not row["Zip"]:
                if lookup_count >= lookup_limit:
                    break

                full_address = row.get("Full Address", "")
                try:
                    parts = [p.strip() for p in full_address.split(",")]
                    city = parts[-2] if len(parts) >= 2 else ""
                    state_raw = parts[-1] if len(parts) >= 2 else ""
                    state = state_raw.split()[0]
                except Exception as e:
                    print(f" Error parsing address: {full_address} - {e}")
                    continue

                if not city or not state:
                    print(f" Skipping row with missing city/state - {full_address}")
                    continue

                zip_code = self.lookup_zip_code(city, state)
                if zip_code:
                    row["Zip"] = zip_code
                    lookup_count += 1
                    print(f"ZIP filled for {city}, {state}: {zip_code}")
                else:
                    print(f" ZIP not found for {city}, {state}")

                time.sleep(1)

        print(f"Total ZIPs filled: {lookup_count}")
        return data

    def lookup_zip_code(self, city, state):
        """
        Uses Zipcodebase API to look up ZIP codes by city and state.
        """
        try:
            url = "https://app.zipcodebase.com/api/v1/code/city"
            params = {
                "apikey": self.api_key,
                "city": city,
                "state": state,
                "country": "US"
            }

            print(f" API Request: {url} with {params}")
            response = requests.get(url, params=params, timeout=5)

            print(f"Response Status: {response.status_code}")
            print(f" Response Body: {response.text}")

            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                if isinstance(results, list) and results:
                    return results[0]
        except Exception as e:
            print(f"API Error for {city}, {state}: {e}")
        return ""


