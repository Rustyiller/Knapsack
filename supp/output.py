def outputData(solution_items, goal, time, f_name):
    f = open(f"{f_name}.txt", "w")
    f.write(str(solution_items) + "\n" + "wartosc : " + str(goal) + "\n" + "czas : " + str(time))
