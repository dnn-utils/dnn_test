from dnn_utils.model import BaseModel
#from dnn_utils.preprocessing import BasePreprocessor
from dnn_utils.preprocessing import DefaultPreprocessor
from dnn_utils import dnn_learn

#class MyModel(BaseModel) :
#
#    def print_name(self) :
#        print("MyModel::print_name")
#
#model = MyModel()
#model.print_name()

import sys, os
import argparse

def main() :

    parser = argparse.ArgumentParser(description = "Run some sandbox DNN tests")
    parser.add_argument("-c", "--config", required = True,
        help = "Provide the DNN configuration JSON file"
    )
    args = parser.parse_args()

    processor = DefaultPreprocessor(args.config)

    # start the learnin'
    actors = [processor]
    dnn_learn.learn(actors = actors)

if __name__ == "__main__" :
    main()
