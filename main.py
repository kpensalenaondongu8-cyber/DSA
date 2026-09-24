def summarise_amounts(raw_values):
    total = 0
    rejected = 0

    for raw in raw_values:
          
        try:
            total += int(raw)
            if total < 0:
                rejected += total
            else:
                total += int(raw)    
            return total
        except ValueError:
            rejected += raw

    return {"total": total, "rejected": rejected}

result = ["10", " 5 ", "bad", "-3", "0", ""]
print(summarise_amounts(result))