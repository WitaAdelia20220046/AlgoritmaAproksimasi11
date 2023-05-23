import numpy as np

def scheduling_approx(tasks, deadlines, processing_times):
    n = len(tasks)
    order = []
    time_left = deadlines - processing_times

    while len(order) < n:
        ratios = time_left / processing_times
        i = np.argmax(ratios)
        order.append(tasks[i])
        time_left = np.delete(time_left, i)
        tasks = np.delete(tasks, i, axis=0)
        deadlines = np.delete(deadlines, i, axis=0)
        processing_times = np.delete(processing_times, i, axis=0)

    return order

tasks = np.array(['A', 'B', 'C', 'D', 'E'])[:, np.newaxis]
deadlines = np.array([7, 6, 8, 10, 11])[:, np.newaxis]
processing_times = np.array([3, 4, 2, 5, 6])[:, np.newaxis]

order = scheduling_approx(tasks, deadlines, processing_times)
print("Urutan tugas yang direkomendasikan:", order)
