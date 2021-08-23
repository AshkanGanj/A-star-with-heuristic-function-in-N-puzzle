
def get_mis_tiles(arr,goal):
    count = 0
    for i in range(len(arr)):
        if arr[i] != goal[i]:
            count = count + 1
    return count - 1
        
def write_data(data,file):
    with open(file, 'w') as f:
        for item in data:
            f.write(str(item))
            f.write('\n')

