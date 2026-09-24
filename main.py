def summarise_amounts(raw_values):
    total = 0
    rejected = 0

    for raw in raw_values:
          
        try:
            all = int(raw)
            if all < 0:
                rejected += 1
            else:
                total += all   
        except ValueError:
            rejected += 1

    return {"total": total, "rejected": rejected}

result = ["10", " 5 ", "bad", "-3", "0", ""]
print(summarise_amounts(result))