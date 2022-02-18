import json


def read_json(json_data, max_rank):
    preferences = {}
    num_interests = json_data["num_interests"]

    for user_id, user_interests in json_data.items():

        if user_id == "num_interests" or len(user_interests) < num_interests:
            continue

        interest_ids = []
        for interest in user_interests:
            interest_ids.append(int(str(interest).split("'")[1]))

        sorted_interest_ids = sorted(interest_ids)
        preferences[user_id] = []

        for interest_id in sorted_interest_ids:
            for _, interest in enumerate(user_interests):
                interest_id_loop = int(str(interest).split("'")[1])
                if interest_id_loop == interest_id:
                    interest_value = str(interest)[-2:-1]
                    if interest_value.isnumeric() and 0 < int(interest_value) <= max_rank:
                        preferences[user_id].append(int(interest_value))
                    else:
                        preferences[user_id].append(1)
                    break

    num_users = len(preferences)
    return preferences, num_interests, num_users


if __name__ == "__main__":
    rank_range = 5

    with open("input_test_data/input_test_data_1.json") as json_file:
        json_dict = json.load(json_file)

    print("Attempting to read the JSON file...")
    read_json(json_dict, rank_range)