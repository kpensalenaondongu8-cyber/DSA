
# def add_tag(profile, tag):
#     updated = profile.copy()
#     all = updated["tags"][:]
#     updated["tags"] = all
#     all.append(tag)
#     return updated

#  new_list = {"name":profile["name"], "tags":[tag],}
#     for tag in profile["tags"]:
#       new_list["tags"].append(tag)
   
#     return new_list
# original = {"name": "Ada", "tags": ["python", "key"]}
# changed = add_tag(original, "testing")

# print(original)
# print(changed)
# print(original["tags"])
# print(changed["tags"])
# print(changed is original)
# print(changed["tags"] is original["tags"])
# assert original["tags"] == ["python"]
# assert changed["tags"] == ["python", "testing"]
# assert set(changed["tags"]) == {"python", "testing"}

# changed["tags"].append("more")
# assert original["tags"] == ["python"]


def ticket_total(price, quantity):
    total = price * quantity
    print(total)
amount = ticket_total("7", 3)
print(amount)
