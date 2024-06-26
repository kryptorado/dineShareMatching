import pandas as csv


def read_csv(file_name, rating_columns):
    csv_data = csv.read_csv(file_name + ".csv")
    preferences = {}

    for i, row in enumerate(csv_data.values):
        user_preferences = []
        for column in rating_columns:
            user_preferences.append(int(str(row[column])[0]))
        preferences[i + 1] = user_preferences

    num_interests = len(rating_columns)
    num_users = len(csv_data.values) - 1
    print(f"Interests: {num_interests}")
    print(f"Users: {num_users}")
    print(preferences)
    return preferences, num_interests, num_users


if __name__ == "__main__":
    csv_file_name = "input_test_data/sample_data"
    csv_rating_columns = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

    print("Attempting to read the CSV file...")
    read_csv(csv_file_name, csv_rating_columns)