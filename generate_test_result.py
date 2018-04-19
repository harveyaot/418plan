#!/bin/env python
import sys
import random

def load_test_data(infile):
    with open(infile) as fin:
        # skipe first line.
        fin.readline()
        for line in fin:
            g = line.strip('\n').split(',')
            yield g

def predict(indata):
    for sample in indata:
        y = predict_one(sample)
        y = format_score(y)
        yield sample + [y]

def predict_one(sample):
    return random.uniform(0, 1)

def output_predicts(predicts, outfile):
    header = "aid,uid"
    with open(outfile, 'w') as fout:
        fout.write(header + '\n')
        for predict in predicts:
            fout.write(",".join(predict) + "\n")

def format_score(y):
    return "%.8f" % y

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    test_data = load_test_data(infile)
    predicts = predict(test_data)
    output_predicts(predicts, outfile)
