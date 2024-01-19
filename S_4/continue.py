# instrukcja

# for element in sequence:
#     if condition:
#         continue
#     # Kod do wykonania dla każdego elementu
#     # (jeśli warunek nie jest spełniony)

for i in range(10):
    if i == 6:
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 == 1:
        continue
    print(i)

# %%
sample = "Python Course"
for char in sample:
    if char == " ":
        continue
    print(char)

# %%
hashtags = "#summer#holiday#free"
result = " "

for char in hashtags:
    if char == "#":
        print(result)
        result = " "
        continue
    result = result + char
print(result)

# %% ZADANIA

missions = [
    {
        "name": "Apollo 11",
        "date": "20.07.1969",
        "status": "completed",
    },
    {
        "name": "Mars Pathfinder",
        "date": "04.07.1997",
        "status": "completed",
    },
    {
        "name": "Chang'e 4",
        "date": "03.01.2019",
        "status": "in progress",
    },
    {
        "name": "Cassini",
        "date": "15.10.1997",
        "status": "completed",
    },
]

for mission in missions:
    if mission["status"] == "in progress":
        continue
    print("Mission", mission["name"], "took place on", mission["date"])

# %%

trainings = [
    {"name": "Basic marksmanship", "rank": "Private"},
    {"name": "Infantry tactics", "rank": "Corporal"},
    {"name": "Art of war", "rank": "Sergeant"},
    {"name": "Heavy weapons specialist", "rank": "Captain"},
    {"name": "Advanced first aid", "rank": "Private"},
    {"name": "Combat engineering", "rank": "Corporal"},
    {"name": "Field intelligence", "rank": "Sergeant"},
    {"name": "Military law", "rank": "Captain"},
    {"name": "Parachuting", "rank": "Private"},
    {"name": "Amphibious assault", "rank": "Corporal"},
    {"name": "Counterterrorism", "rank": "Sergeant"},
    {"name": "Military diplomacy", "rank": "Captain"},
]

military_rank = "Sergeant"

for training in trainings:
    if training["rank"] != military_rank:
        continue
    print("Training for rank", military_rank, "is:", training["name"])
