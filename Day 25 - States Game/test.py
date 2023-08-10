import pandas

my_dict = {}
data = pandas.read_csv("50_states.csv")

# def test(x):
#     print(f"Here is the x {x}")
#
# names = data["state"].tolist()
# print(names)
#
# print(data[data["state"] == "Alabama"])
# state = data[data["state"] == "Alabama"]
# print("Watch this \n")
# print(state.x)
# test(state.x)

# print(data)
# print(data.index)
# print(data.columns)
# print(data[data["state"] == "Arizona"].x)
print(data.state[2])
name = data.state[2]
print(data[data.x == -203])
print(type(data[data.x == -203]))
print(data[data.x == -203].x)
print(type(data[data.x == -203].x))
