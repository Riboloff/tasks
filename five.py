#5.3 flip bit to win

bits = (1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1)

before_zero = 0
current_ones = 0
max_ones = 0

for bit in bits:
    if (bit == 0):
        current_ones = before_zero
        before_zero = 0
    else:
        before_zero += 1;

    current_ones += 1;
    if current_ones > max_ones:
        max_ones = current_ones

print max_ones 
