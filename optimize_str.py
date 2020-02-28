char_limit = 8

def optimize_str(str_list, chunk_size, start):
    count = 0
    if chunk_size == 1:
        return str_list

    for i in range(chunk_size):
        count += len(str_list[start+i].strip(' '))

    if count <= char_limit:
        str_list[start:start+chunk_size] = [''.join(str_list[start:start+chunk_size])]
    if start + chunk_size >= len(str_list):
        return optimize_str(str_list, chunk_size - 1, 0)
    else:
        return optimize_str(str_list, chunk_size, start + 1)

string = [' aa', ' bbbb', 'c', 'ddd', ' eeeeee', 'ffff', 'ggggggggggg', 'hh', 'iii', 'j', 'k', 'lllllll', 'm']
str_op = optimize_str(string, len(string), 0)
print(str_op)
