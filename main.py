def expogo():
    def gen_steps(max_num):
        count = 1
        while count <= max_num:
            yield count
            count *= 2

    num_cases = int(input().strip())
    for case_num in range(1, num_cases + 1):
        coord = input().strip().split()
        x, y = (int(coord[0]), int(coord[1]))
        if abs(x) % 2 + abs(y) % 2 != 1:
            print("Case #{}: IMPOSSIBLE".format(case_num))
            continue
        steps = reversed(list(gen_steps(abs(x) + abs(y))))
        x_temp = x
        y_temp = y
        jump = ""
        for step in steps:
            if abs(x_temp) >= abs(y_temp):
                if x_temp > 0:
                    jump = "E" + jump
                    x_temp -= step
                else:
                    jump = "W" + jump
                    x_temp += step
            else:
                if y_temp > 0:
                    jump = "N" + jump
                    y_temp -= step
                else:
                    jump = "S" + jump
                    y_temp += step
        if x_temp == 0 and y_temp == 0:
            print("Case #{}: {}".format(case_num, jump))
        else:
            print("Case #{}: IMPOSSIBLE".format(case_num))


def overexited_fan():
    num_cases = int(input().strip())
    for case_num in range(1, num_cases + 1):
        peppurr = input().strip().split()
        p_x = int(peppurr[0])
        p_y = int(peppurr[1])
        if abs(p_x) + abs(p_y) == 0:
            print("Case #{}: {}".format(case_num, 0))
            continue
        moves = peppurr[2]
        reachable = False
        minutes = 0
        for i, m in enumerate(moves):
            x_move = 0
            y_move = 0
            if m == "N":
                y_move = 1
            elif m == "E":
                x_move = 1
            elif m == "S":
                y_move = -1
            elif m == "W":
                x_move = -1
            p_x += x_move
            p_y += y_move
            if abs(p_x) + abs(p_y) <= i + 1:
                reachable = True
                minutes = i + 1
                break
        if reachable:
            print("Case #{}: {}".format(case_num, minutes))
        else:
            print("Case #{}: IMPOSSIBLE".format(case_num))


def overrandomized():
    import string
    import math

    num_cases = int(input().strip())
    for case_num in range(1, num_cases + 1):
        num_digits = int(input().strip())
        num_queries = 0
        mapping = {}
        while len(mapping) < 10:
            num_queries += 1
            query = input().strip().split()
            response = query[1]
            for c in response:
                mapping[c] = 0
        while num_queries < 10000:
            num_queries += 1
            query = input().strip().split()
            upper_bound = int(query[0])
            max_digits = int(math.log10(upper_bound)) + 1
            response = query[1]
            if len(response) == max_digits:
                limited_digit = int(upper_bound / pow(10, max_digits - 1))
                if mapping[response[0]] == 0:
                    mapping[response[0]] = limited_digit
                elif limited_digit < mapping[response[0]]:
                    mapping[response[0]] = limited_digit
        final = ["?" for i in range(10)]
        for char, num in mapping.items():
            final[num] = char
        print("Case #{}: {}".format(case_num, "".join(final)))


def oversized_pancake():
    from collections import Counter
    from itertools import product

    num_cases = int(input().strip())
    for case_num in range(1, num_cases + 1):
        info = input().strip().split()
        num_diners = int(info[1])
        highest_slice_count = 1
        slices_count = Counter([int(s) for s in input().strip().split()])
        for slice_size, slice_count in slices_count.items():
            if highest_slice_count < slice_count:
                highest_slice_count = slice_count
        if highest_slice_count >= num_diners:
            print("Case #{}: {}".format(case_num, 0))
            continue
        # One cut land

        for cut in range(1, num_diners):
            if cut == num_diners - 1:
                print("Case #{}: {}".format(case_num, cut))
                break
            most_slices = cut + 1
            for s1, s2 in product(slices_count, slices_count):
                max_extra = 0
                if s1 == s2:
                    continue
                if s2 % s1 == 0:
                    if cut + 1 < s2 / s1 and cut > max_extra:
                        max_extra = cut
                    elif cut + 1 >= s2 / s1 and s2 / s1 > max_extra:
                        max_extra = s2 / s1
                if slices_count[s1] + max_extra > most_slices:
                    most_slices = slices_count[s1] + max_extra
            if most_slices >= num_diners:
                print("Case #{}: {}".format(case_num, cut))
                break


oversized_pancake()
