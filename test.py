from dnn_utils.model import BaseModel

class MyModel(BaseModel) :

    def print_name(self) :
        print("MyModel::print_name")

model = MyModel()
model.print_name()
