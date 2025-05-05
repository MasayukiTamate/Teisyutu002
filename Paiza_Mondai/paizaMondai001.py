s = []
input_line = input()
#input_line = "7 2 4"
s.append(input_line.split(' '))


N = s[0][0]
H = s[0][1]
W = s[0][2]

s = []
input_line = input()
s.append(input_line.split(' '))


sy = int(s[0][0])
sx = int(s[0][1])

#input_line = input()
#input_line = "RFLLLBR"
#sinkou = input_line
sinkou = input()


zaseki = []
for i in range(int(H)):
    zaseki.append(input().split(' '))
input_line = "0 1 2 3","4 5 0 7"

for aruki in sinkou:
    if aruki == "F":
        sy = sy - 1
    elif aruki == "B":
        sy = sy + 1
    elif aruki == "L":
        sx = sx - 1
    elif aruki == "R":
        sx = sx + 1
    
    print(zaseki[sy-1][sx-1])
        

#print(f"{N=} {H=} {W=} {sy=} {sx=} {sinkou=} {zaseki=}")

