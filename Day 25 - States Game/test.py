import pandas

my_dict = {}
data = pandas.read_csv("50_states.csv")

def test(x):
    print(f"Here is the x {x}")

names = data["state"].tolist()
print(names)

print(data[data["state"] == "Alabama"])
state = data[data["state"] == "Alabama"]
print("Watch this \n")
print(state.x)
test(state.x)

