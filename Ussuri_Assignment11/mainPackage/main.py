# File Name : main.py
# Student Name: Asfia Siddiqui, Zoha Iqbal
# email:  siddiqaf@mail.uc.edu, iqbalza@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Cleans out data to give cleaner data
# Brief Description of what this module does. Imports everythings from the cvs and class to create the output
# Citations: chatgpt.com
# Anything else that's relevant:
import os
from CSVUtilitiesPackage.CSVUtilities import CSVUtilities
from dataProcessingPackage.fuelDataCleaner import FuelDataCleaner
from pepsiPackage.pepsifilter import filter_pepsi_anomalies

if __name__ == "__main__":
    API_KEY = "fb7a0790-162e-11f0-bcb8-730c5a4cfe14"
    INPUT_FILE = "data/fuelPurchaseData.csv"
    CLEANED_FILE = "data/cleanedData.csv"
    ANOMALY_FILE = "data/dataAnomalies.csv"

    os.makedirs("data", exist_ok=True)

    csv_util = CSVUtilities()
    data = csv_util.load_csv_to_dict_list(INPUT_FILE)

    cleaner = FuelDataCleaner(api_key=API_KEY)
    data = cleaner.remove_duplicates_and_format_price(data)
    cleaned_data, anomalies = filter_pepsi_anomalies(data)
    cleaned_data = cleaner.fill_missing_zip_codes(cleaned_data)

    csv_util.write_dict_list_to_csv(cleaned_data, CLEANED_FILE)
    csv_util.write_dict_list_to_csv(anomalies, ANOMALY_FILE)

    print(" Done! Cleaned and anomaly files saved.")

