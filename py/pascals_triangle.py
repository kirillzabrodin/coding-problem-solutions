def generate(numRows):
        if numRows == 1:
            row = [1]
            return [row]
        else:
            previous_rows = generate(numRows - 1)
            row = [None] * numRows
            row[0], row[-1] = 1, 1
            for i in range(len(row) - 2):
                row[i + 1] = previous_rows[-1][i] + previous_rows[-1][i + 1]
        print(previous_rows)
        return previous_rows + [row]
    
print(generate(8))