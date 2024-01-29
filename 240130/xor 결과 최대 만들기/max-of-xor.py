n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = []
max_xor = 0

def power(a, n):
    if n == 0:
        return 1
    x = power(a, n//2)
    if n % 2 == 0:
        return x * x
    else:
        return x * x * a
    
def dec_to_bin(dec):
    bin_arr = []
    while True:
        if dec == 0:
            break
        bin_arr.append(dec % 2)
        dec = dec // 2 
    return bin_arr

def bin_to_dec(bin_num):
    dec = 0
    for i in range(len(bin_num)):
        dec += int(bin_num[i]) * power(2, i)
    return dec
    
def cal_xor():
    global max_xor
    if len(answer) == 1:
        xor_bin = []
        bin1 = dec_to_bin(answer[0])
        for i in range(1, len(bin1) + 1):
            xor_bin.append(bin1[-i])
        max_xor = max(bin_to_dec(xor_bin), max_xor)
        
    bin1 = dec_to_bin(answer[0])
    for i in range(1, m):
        xor_bin = []
        bin2 = dec_to_bin(answer[i])
        bin1_len = len(bin1)
        bin2_len = len(bin2)
        max_len = max(bin1_len, bin2_len)
        for j in range(0, max_len):
            if j >= bin1_len:
                if bin2[j] == 1:
                    xor_bin.append(1)
                else:
                    xor_bin.append(0)
            elif j >= bin2_len:
                if bin1[j] == 1:
                    xor_bin.append(1)
                else:
                    xor_bin.append(0)
            elif bin1[j] != bin2[j]:
                xor_bin.append(1)
            else:
                xor_bin.append(0)
        bin1 = xor_bin
    max_xor = max(bin_to_dec(xor_bin), max_xor)


def choose(pos, idx):
    if pos == m + 1:
        # print_answer()
        cal_xor()
        return
    
    for i in range(idx, n):
        answer.append(nums[i])
        choose(pos + 1, i + 1)
        answer.pop()
    return


choose(1, 0)
print(max_xor)