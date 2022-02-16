from flask import Flask, request, jsonify

from matching.matching import get_match_results

app = Flask(__name__)

@app.route('/match', methods=['POST']) 
def do_matching():
    if request.json:
        final_results = get_match_results(request.json)
        return jsonify(final_results)
    else:
        return {}

# run the app.
# if __name__ == "__main__":
#     # Setting debug to True enables debug output. This line should be
#     # removed before deploying a production app.
#     app.debug = True
#     app.run()