if __name__ == '__main__':
    # 1
    years_list = [1994, 1995, 1996, 1997, 1998, 1999]
    # 2
    print("3-й др був у {} році".format(years_list[3]))
    # 3
    print("Найбільше років було у {}".format(years_list[4:-1]))  # виведе останній елемент списку з 5 елементів
    # 4
    things = ["mozzarella", "cinderella", "salmonella"]
    # 5
    things[1] = "Cinderella"
    print(things)
    # 6
    things[0] = things[0].upper()
    print(things)
    # 7
    things.remove("salmonella")
    print(things)
    # 8
    surprise = ["Groucho", "Chico", "Harpo"]
    surprise[2] = (surprise[2].lower()).title()
    print(surprise)
    # 10
    e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
    print(e2f.get("walrus"))

    #11
    f2e = e2f.items()
    print(f2e)
