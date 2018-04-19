set -x
python generate_test_result.py ./preliminary_contest_data/test1.csv ./submission/submission.csv &&
cd submission && zip submission.zip submission.csv
