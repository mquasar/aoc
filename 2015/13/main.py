import time
from itertools import permutations
from parse import compile

def resolve(part2=False):
    start_time = time.time()

    with open('input') as fin:
        lines = [line.rstrip() for line in fin.readlines()]

    p = compile("{} would {} {:d} happiness units by sitting next to {}.")

    happy_dict = {}
    guests = []
    for line in lines:
        temp = p.parse(line).fixed
        happiness = temp[2] if temp[1] == 'gain' else -1 * temp[2]
        happy_dict[(temp[0][0]+temp[3][0]).lower()] = happiness
        if (temp[0][0]).lower() not in guests:
            guests.append((temp[0][0]).lower())

    #part 2
    # add combinations for new guest and happiness = 0
    # then add the 'new' guest to the guests
    if part2:
        for guest in guests:
            happy_dict[guest+'i'] = 0
            happy_dict['i'+guest] = 0

        guests.append('i')

    pos_list = []
    happy_list = []
    guest_pers = list(permutations(guests))  # 8! = 40320 permutations

    for per in guest_pers:
        str_per = []
        for first, second in zip(per, per[1:]):
            str_per.append(first + second)

        max_idx = len(str_per) - 1
        str_per.append(str_per[max_idx][1] + str_per[0][0])
        pos_list.append(str_per)          # 7! = 5040 different layouts

    for pos in pos_list:
        happiness = 0
        for couple in pos:
            for k, v in happy_dict.items():
                if couple == k or couple == k[::-1]:
                    happiness += v

        happy_list.append(happiness)

    print("The highest change in happiness is:", max(happy_list))
    print(f"{time.time() - start_time}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'part2':
        resolve(part2=True)
    else:
        resolve()
