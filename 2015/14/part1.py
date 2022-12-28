from parse import compile

with open('input') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

p = compile("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.")

tpl_list = []
for line in lines:
    tpl_list.append(p.parse(line).fixed)

distance = 0
end_time = 2503

for tpl in tpl_list:
    distance = 0
    for t in range(tpl[2], end_time, tpl[3] + tpl[2]):
        distance += tpl[1] * tpl[2]
    print(f"Reindeer {tpl[0]} has flown {distance}")
