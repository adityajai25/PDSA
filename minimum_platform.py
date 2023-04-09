def minimum_platform(train_schedule):
    max_plt_no = 0
    for i in range(len(train_schedule)):
        plt_no = 1
        for j in range(len(train_schedule[:i])):
            if train_schedule[i][1] < train_schedule[j][2]:
                plt_no += 1
        if plt_no > max_plt_no:
            max_plt_no = plt_no
    return max_plt_no
