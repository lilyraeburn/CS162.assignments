premium = []
standard = []
economy = []
packets = [
    "S Mary",
    "P Dee",
    "P Dee",
    "E Eileen",
    "E Mike",
    "E Joe",
    "P Dee",
    "E Vicky",
    "E George",
    "P Dee",
    "P Joe",
    "E Sally",
    "P Joe",
    "S Pete",
    "P Dee",
    "S Bill",
    "S Chase",
    "E Price",
    "P Dee",
    "E Sue"]
for packet in packets:
    if packet[0] == "P":
        premium.append(packet)
    elif packet[0] == "S":
        standard.append(packet)
    elif packet[0] == "E":
        economy.append(packet)
print("Premium Queue: ")
print(premium)
print("Standard Queue: ")
print(standard)
print("Economy Queue: ")
print(economy)
print("Priority Scheme: ")
output = []
while len(premium) > 0 or len(standard) > 0 or len(economy) >0:
    for i in range(3):
        if len(premium) > 0:
            output.append(premium.pop(0))
    for i in range(2):
        if len(standard) > 0:
            output.append(standard.pop(0))
    for i in range(1):
        if len(economy) > 0:
            output.append(economy.pop(0))
print(output)