line = [1,1,1,0,0,1]
arrival = [(3,5,50,1090)]
next_call = [1,4,38]
arrival_time = 1050
call_in_process = [(1,3,1055),(2,6,1099)]
clock_time = 1035
link = 3
use_in = 2
complete = 40
block = 20
busy = 20
update = []

while call_in_process:
    #update clock time
    for x in range(len(call_in_process)):
        update.append(call_in_process[x][2])
    if len(arrival)>0:
        for y in range(len(arrival)):
            update.append(arrival[y][3])
    if arrival_time>0:
        update.append(arrival_time)

    clock_time = min(update)
    update.sort(reverse=True)
    update.pop()

    #block or busy or intsert
    if clock_time == arrival_time:
        if link == use_in:
            block += 1

        elif line[next_call[0]-1] == 1 or line[next_call[1]-1]:
            busy +=1
            next_call.clear()
            arrival_time = 0

        else:
            temp_n = next_call.pop()
            next_call.append(arrival_time+temp_n)
            call_in_process.append(tuple(next_call))
            next_call.clear()
            arrival_time = 0
            use_in +=1

    #insert into next call:
    if len(arrival)>0:
        for x in range(len(arrival)):
            if clock_time == arrival[x][3]:
                next_call.append(arrival[x][0])
                next_call.append(arrival[x][1])
                next_call.append(arrival[x][2])
                arrival_time = arrival[x][3]

                del arrival[x]
                break

    #complete:
    for x in range(len(call_in_process)):
        if clock_time == call_in_process[x][2]:
            complete +=1

            del line[call_in_process[x][0]-1]
            line.insert(call_in_process[x][0]-1, 0)

            del line[call_in_process[x][1] - 1]
            line.insert(call_in_process[x][1] - 1, 0)

            del call_in_process[x]
            use_in -=1
            break

    #Calculate process:
    process = complete + block + busy

print("process: ",process)
print("complete: ",complete)
print("block: ", block)
print("busy: ",busy)
