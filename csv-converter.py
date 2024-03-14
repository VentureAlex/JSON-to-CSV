import json
import csv

# Example usage
json_file_path = './Input/data.json'  # Path to the JSON file
csv_file_path = './Output/data.csv'     # Path to the output CSV file

# Function to convert a JSON file to a CSV file
def json_to_csv(json_file_path, csv_file_path):
    # Open the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        # Load the JSON data
        data = json.load(json_file)
        
        # Ensure the data is a list of records
        if not isinstance(data, list):
            data = [data]
        
        # Open the CSV file for writing
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)
            
            # Write the header (column names) to the CSV file
            # Assuming all dictionaries have the same structure
            headers = data[0].keys()
            csv_writer.writerow(headers)
            
            # Write the JSON data to the CSV file
            for record in data:
                csv_writer.writerow(record.values())

# Convert JSON to CSV
json_to_csv(json_file_path, csv_file_path)

print(f"Conversion completed. The CSV file is saved as '{csv_file_path}'.")
