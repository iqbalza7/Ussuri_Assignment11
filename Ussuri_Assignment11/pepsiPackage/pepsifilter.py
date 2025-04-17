# File Name : pepsifilter.py
# Student Name: Asfia Siddiqui, Zoha Iqbal
# email:  siddiqaf@mail.uc.edu, iqbalza@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   04/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Cleans out data to give cleaner data
# Brief Description of what this module does. filters pepsi data
# Citations: chatgpt.com
# Anything else that's relevant:
def filter_pepsi_anomalies(data):
    """
    Splits the data into two lists:
    - cleaned: rows that do NOT mention 'pepsi'
    - anomalies: rows that contain 'pepsi' in any field (case-insensitive)
    """
    cleaned = []
    anomalies = []

    for row in data:
        found = False
        for value in row.values():
            if isinstance(value, str) and "pepsi" in value.lower():
                found = True
                break

        if found:
            anomalies.append(row)
        else:
            cleaned.append(row)

    return cleaned, anomalies
