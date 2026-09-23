
def add_tag(profile, tag):
    updated = profile.copy()
    all = updated["tags"][:]
    updated["tags"] = all
    all.append(tag)
    return updated

#  new_list = {"name":profile["name"], "tags":[tag],}
#     for tag in profile["tags"]:
#       new_list["tags"].append(tag)
   
#     return new_list
original = {"name": "Ada", "tags": ["python", "key"]}
changed = add_tag(original, "testing")

print(original)
print(changed)
print(original["tags"])
print(changed["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])