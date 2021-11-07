if __name__ == '__main__':
    # Завдання до розділу 2
    second_in_minute = 60
    minute_in_hour = 60
    second_per_hour = second_in_minute * minute_in_hour
    print(" В годині: {} секунд".format(second_per_hour))
    second_per_day = second_per_hour * 24
    print(" В добі: {} секунд".format(second_per_day))
    print(second_per_day / second_per_hour)
    print(second_per_day // second_per_hour)
