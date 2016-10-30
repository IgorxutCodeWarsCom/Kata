def tickets(people):
    purse = {"25": 0, "50": 0, "100": 0}
    result = "YES"

    while people:
        tmp = people.pop(0)
        purse[str(tmp)] += 1

        if tmp == 25:
            continue

        else:

            if purse["25"] == 0:
                result = "NO"
                break

            if tmp == 50:
                purse["25"] -= 1

            if tmp == 100:

                if purse["50"] >= 1:
                    purse["50"] -= 1
                    purse["25"] -= 1

                elif purse["25"] >= 3:
                    purse["25"] -= 3

                else:
                    result = "NO"
                    break

    return result
