import os
import ruamel.yaml

templates = ["base-template.yaml"]
for root, dirs, files in os.walk("./functions"):
    for file in files:
        if file.endswith(".yaml"):
            templates.append(os.path.join(root, file))

data = None

for file_name in templates:
    d = ruamel.yaml.round_trip_load(open(file_name, "rb"))
    if data is None:
        data = d
        continue

    for k in d:
        data["Resources"].update(d[k])

print(ruamel.yaml.round_trip_dump(data, indent=4, explicit_end=True))

with open("template.yaml", "w") as f:
    data = ruamel.yaml.round_trip_dump(data, f, indent=4)
