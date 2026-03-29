import pandas as pd


def get_temperature_column(file_name):
    #df = pd.read_excel(file_name)
    df = pd.read_excel(file_name, engine="openpyxl")

    if "Temperature" not in df.columns:
        print("Temperature column missing!")
        return []

    return df["Temperature"]


def clean_data(temp_data):
    temp_data = temp_data.dropna()
    temp_data = pd.to_numeric(temp_data, errors='coerce')
    temp_data = temp_data.dropna()

    return temp_data.tolist()


def remove_duplicates(values):
    return list(set(values))


def sort_values(values):
    return sorted(values)


def calculate_results(values):
    min_val = min(values)
    max_val = max(values)
    avg_val = round(sum(values) / len(values), 2)

    critical = 0
    for v in values:
        if v > 100:
            critical += 1

    return min_val, max_val, avg_val, critical


def print_output(sorted_vals, min_v, max_v, avg_v, critical):
    print("\n--- Sensor Data Report ---")
    print("Sorted Unique Values:", sorted_vals)
    print("Min Temp:", min_v)
    print("Max Temp:", max_v)
    print("Average Temp:", avg_v)
    print("Critical Count (>100):", critical)


def main():
    #file_name = r"C:\Users\HP\Python automation\Sensor_Data_Assignment\sensor_readings.xlsx"
    file_name = r"C:\Users\HP\Documents\Interview questions\sensor.xlsx"

    data = get_temperature_column(file_name)

    if len(data) == 0:
        print("No data found!")
        return

    clean_vals = clean_data(data)
    unique_vals = remove_duplicates(clean_vals)
    sorted_vals = sort_values(unique_vals)

    min_v, max_v, avg_v, critical = calculate_results(sorted_vals)

    print_output(sorted_vals, min_v, max_v, avg_v, critical)


if __name__ == "__main__":
    main()
