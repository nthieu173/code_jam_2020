def vestifium(): 
    num_cases = int(input().strip())
    for case_num in range(num_cases):
        trace = 0
        repeated_rows = 0
        repeated_cols = 0
        num_lines = int(input().strip())
        matrix = [[] for col in range(num_lines)]
        for line_num in range(num_lines):
            row = list(map(lambda s : int(s), input().strip().split()))
            trace += row[line_num]
            row_set = set(row)
            repeated_rows += 1 if len(row) > len(row_set) else 0
            for i, num in enumerate(row):
                matrix[i].append(num)
        for col in matrix:
            col_set =set(col)
            repeated_cols += 1 if len(col) > len(col_set) else 0
        print("Case #{}: {} {} {}".format(case_num + 1, trace, repeated_rows, repeated_cols))

def nesting_depth():
    num_cases = int(input().strip())
    for case_num in range(num_cases):
        print("Case #{}: ".format(case_num + 1), end="")
        curr = 0
        line = input().strip()
        for num in map(lambda c: int(c), line):
            delta = num - curr
            if delta > 0:
                for _ in range(delta):
                    print("(", end="")
            elif delta < 0:
                for _ in range(-delta):
                    print(")", end="")
            print(num, end="")
            curr = num
        for _ in range(curr):
            print(")", end="")
        print()
        
def parenting_partnering():
    num_cases = int(input().strip())
    for case_num in range(num_cases):
        schedule = {}
        parents = {"C":0,"J":0}
        num_tasks = int(input().strip())
        tasks = {}
        for i in range(num_tasks):
            task = map(lambda s: int(s), input().strip().split())
            start = next(task)
            end = next(task)
            tasks[i] = (start, end)
        impossible = False
        for num, (start, end) in sorted(tasks.items(), key= lambda t: t[1][1]):
            ok = False
            for p,c in sorted(parents.items(), key= lambda t: t[1], reverse=True):
                if c <= start:
                    parents[p] = end
                    schedule[num] = p
                    ok = True
                    break
            if not ok:
                print("Case #{}: {}".format(case_num + 1, "IMPOSSIBLE"))
                impossible = True
                break
        if not impossible:
            output = ""
            for num in sorted(schedule.keys()):
                output += schedule[num]
            print("Case #{}: {}".format(case_num + 1, output))

def query(bit_num):
    print(bit_num) 
    return int(input().strip())

def esab_atad():
    info = map(lambda s: int(s), input().strip().split())
    num_cases = next(info)
    num_bits = next(info)
    for _ in range(num_cases):
        bits = {}
        if num_bits <= 10:
            output = ""
            for i in range(num_bits, 0, -1):
                output += str(query(i))
            print(output)
            _ = input()
            continue
        queried = 0
        if num_bits % 2 != 0:
            bits[num_bits // 2 + 1] = query(num_bits // 2 + 1)
            query(1)#To get even queried number
            queried += 2
        next_index = 1
        while len(bits) < num_bits and next_index <= num_bits // 2:
            # the next query will be a change
            if queried % 10 == 0 and queried != 0:
                #setting up indicative bits
                indicative = {}
                for i in range(1,len(bits) // 2 + 1):
                    first = bits[i]
                    second = bits[num_bits - i + 1]
                    if "same" not in indicative and first == second:
                        indicative["same"] = i
                    if "diff" not in indicative and first != second:
                        indicative["diff"] = i
                    if "same" in indicative and "diff" in indicative:
                        break
                change_type = "UNKNOWN"
                #Probing change type
                if len(indicative) == 1: #Cant be 0
                    for t in indicative:
                        query(1) #To get even queried number
                        if bits[indicative[t]] == query(indicative[t]):
                            change_type = "NONE"
                        else:
                            change_type = "COMP"
                        queried += 2
                else:
                    same_change = bits[indicative["same"]] != query(indicative["same"])
                    diff_change = bits[indicative["diff"]] != query(indicative["diff"])
                    queried += 2
                    if same_change and diff_change:
                        change_type = "COMP"
                    elif not same_change and diff_change:
                        change_type = "SWAP"
                    elif same_change and not diff_change:
                        change_type = "BOTH"
                    else:
                        change_type = "NONE"
                print(change_type)
                if change_type == "COMP":
                    for k in bits:
                        bits[k] = 1 if bits[k] == 0 else 0
                elif change_type == "SWAP":
                    print("swapped")
                    for i in range(1, next_index):
                        temp = bits[i]
                        bits[i] = bits[num_bits - i + 1]
                        bits[num_bits - i + 1] = temp
                elif change_type == "BOTH":
                    for i in range(1, next_index):
                        temp = bits[i]
                        bits[i] = 1 if bits[num_bits - i + 1] == 0 else 0
                        bits[num_bits - i + 1] = 1 if temp == 0 else 0
            else:
                bits[next_index] = query(next_index)
                bits[num_bits - next_index + 1] = query(num_bits - next_index + 1)
                next_index += 1
                queried += 2
        output = ""
        for i in range(num_bits, 0, -1):
            output += str(bits[i])
        print(output)
        _ = input()
