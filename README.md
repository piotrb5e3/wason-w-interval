# About
Conduct Peter Wason's selection task experiment with random interval generation as a secondary task.

# Disclaimer
This application is a proof of concept.
It's not suitable for use in production - it has not been properly tested.
If you want to use it in production, please contact me at piotrb5e3@gmail.com

# Requirements
* Git
* Python 3 with pip
* Qt5 GPL

# Setup
* Optionally create and activate a python virtualenv
* `git clone https://github.com/piotrb5e3/wason-w-interval.git`
* `cd wason-w-interval`
* `pip install -r requirements.txt`

# Running:
* Configuration editor: `python configure.py`
* Experiment runner: `python start_experiment.py`
* Export to CSV: `python csv_export.py`
