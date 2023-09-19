import os
import shutil
import json

from speaker_recognition_util import delete_profile

prof_dict = {}
if os.path.isfile("profiles.json"):
    with open('profiles.json', 'r', encoding='utf-8') as f:
        prof_dict = json.load(f)
else:
    print("There are no profiles to delete!")
    exit(0)

# Delete profiles from Microsoft
for prof_id in prof_dict.keys():
    delete_profile(prof_id)

# Delete folders with audio recordings related to the profiles
for elem in os.listdir():
    if elem in prof_dict.keys():
        shutil.rmtree(elem)

# Remove the profiles file
os.remove("profiles.json")

