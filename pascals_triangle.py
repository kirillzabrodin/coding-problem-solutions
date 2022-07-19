from multiprocessing.dummy import Array


def generate(numRows):
        for i in range(numRows):
            row = Array[i]
            total += generateRow(i)