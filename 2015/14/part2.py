from parse import compile

with open('input') as fin:
    lines = [line.rstrip() for line in fin.readlines()]

p = compile("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.")

tpl_list = []
for line in lines:
    tpl_list.append(p.parse(line).fixed)

print(tpl_list)

#dist_dict = { 'Vixen': 0, 'Rudolph': 0, 'Donner': 0, 'Blitzen': 0, 'Comet': 0, 'Cupid': 0, 'Dasher': 0, 'Dancer': 0, 'Prancer': 0 }
#tpl_list = [(19, 7, 124), (3, 15, 28), (19, 9, 164), (19, 9, 158), (13, 7, 82), (25, 6, 145), (14, 3, 38), (3, 16, 37), (25, 6, 143)]
end_time = 2503
score = [0, 0, 0, 0, 0, 0, 0, 0, 0]
distance = [0, 0, 0, 0, 0, 0, 0, 0, 0]
cycle = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for tt in range(1, end_time + 1):
    print('Second: %d, Cycle: %s' %(tt, str(cycle)))
    for idx, tpl in enumerate(tpl_list):
        factor = cycle[idx] * (tpl[2] + tpl[3])
        if factor <= tt <= factor + tpl[2]:
            distance[idx] += tpl[1]
        print('Deer %d, Distance: %d' %(idx+1, distance[idx]))
        if tt % (tpl[2] + tpl[3]) == 0:
            cycle[idx] += 1
    m = max(distance)
    idx_max = [i for i, j in enumerate(distance) if j == m]
    for idx in idx_max: score[idx] += 1
    print('Score: %s' %str(score))
    print('----------------------')
