n = int(input())
directory = []
size = pow(2, n)
answer = "no"
for i in range(n):
    line = input().split()
    power = int(line[1]) * int(line[2])
    if (line[0] == "acid"):
        directory.append(-1 * power)
    else:
        directory.append(power)

sik = False
for i in range(size):
    if (sik):
        break
    phase_calc = 0
    if(i == 0):
        continue
    key = 1
    for j in range(n):
        if (key & i != 0):
            phase_calc += directory[j]
        key = key * 2
    if (phase_calc == 0):
        answer = "yes"
        sik = True
        break
print(answer)
