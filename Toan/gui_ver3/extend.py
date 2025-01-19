from pathlib import Path
def get_path_img():
    path=Path(__file__).parent.resolve()
    final_path=str(path.as_posix())+'/img/'
    return final_path



from pathlib import Path
def get_path_img():
    path=Path(__file__).parent.resolve()
    final_path=str(path.as_posix())+'/img/'
    return final_path

array_load_bank = [{'id':1, 'kw': 1, 'port':0x01},
       {'id': 2, 'kw': 2, 'port':0x02},
       {'id': 3, 'kw': 3, 'port': 0x03},
       {'id': 4, 'kw': 5, 'port': 0x04},
       {'id': 5, 'kw': 5, 'port': 0x05},
       {'id': 6, 'kw': 5, 'port': 0x06},
       {'id': 7, 'kw': 10, 'port': 0x07},
       {'id': 8, 'kw': 10, 'port': 0x08},
       {'id': 9, 'kw': 10, 'port': 0x09},
       {'id': 10, 'kw': 20, 'port': 0x0A},
       {'id': 11, 'kw': 20, 'port': 0x0B},
       {'id': 12, 'kw': 20, 'port': 0x0C},]

print(array_load_bank[11]['port'])
print(type(array_load_bank[0]['port']))

def number_of_objects(input_kw):
    cnt = {20:3, 10:3, 5:3, 3:1, 2:1, 1:1}
    ans = 0
    num = 0
    val = 0
    # id = -1
    id = len(array_load_bank)-1
    stores = []
    sum_kw = 0
    for k,v in cnt.items():
        sum_kw += k * v
    if sum_kw < input_kw:
        return -1
    else:
        total_port = 0
        while input_kw > 0:
            for i in range(id, -1, -1):
                curr_val = array_load_bank[i]['kw']
                # print('cv ', curr_val)
                if input_kw >= curr_val:
                    num = input_kw // curr_val
                    num = min(num, cnt[curr_val])
                    val = curr_val
                    id=i
                    break
            input_kw -= num * val
            ans += num
            for i in range(id, id-num, -1):
                stores.append(array_load_bank[i])
            id -= num
        for i in stores:
            total_port += i['port']
    return stores, total_port

print(number_of_objects(68))