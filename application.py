from flask import Flask

from utils.read_json import read_json
from utils.remap_ids import remap_ids
from matching.compatibility import calculate_compatibility
from matching.matching import solve_ip
import json
import sys

# TODO: call with actual user data
def do_matching():
    # Constants
    rank_range = 5
    threshold_compatibility = 0.2

    with open("input_test_data/input_test_data_1.json") as json_file:
        json_dict = json.load(json_file)

    user_preferences, num_interests, num_users = read_json(json_dict, rank_range)
    user_preferences, mapping = remap_ids(user_preferences, {}, True)
    user_compatibility_scores, num_users = calculate_compatibility(user_preferences, num_interests, num_users)
    score_max = pow(rank_range, 2) * num_interests
    matches = solve_ip(num_users, user_compatibility_scores, threshold_compatibility, score_max)

    final_results = remap_ids(matches, mapping, False)
    print(final_results)


    return '<p>Hello %s!</p>\n' % final_results


# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: do_matching()))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()