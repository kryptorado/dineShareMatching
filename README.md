# dineShareMatching

A Flask web server to run our matching algorithm

## Installation

First, you need to clone this repository:

```bash
$ git clone https://github.com/dineShare/dineShareMatching.git
```

Then change into the `dineShareMatching` folder:

```bash
$ cd dineShareMatching
```

Now, we will need to create a virtual environment and install all the dependencies:

```bash
$ python3 -m venv venv  # on Windows, use "python -m venv venv" instead
$ . venv/bin/activate  # on Windows, use "venv\Scripts\activate" instead
$ pip install -r requirements.txt
```

## How to run the web server?

To run the web server, go to the root director and execute the following command

```bash
$ python application.py
```

The applications will always running on http://localhost:5000.

## Access the deployed API
```
https://dineshare-matching.herokuapp.com/match

```
this path accepts a POST request with content-type=json
and the body of the request must be in this format: https://github.com/dineShare/dineShareAPI/blob/recommendation_engine/Recommendation_Engine/python/operation.txt
