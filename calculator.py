def add(num, sec_num):
    return num + sec_num

def sub(num, sec_num):
    return num - sec_num

def mult(num, sec_num):
    return num * sec_num

def div(num, sec_num):
    if sec_num != 0:
        return num / sec_num
    return "Zero division error"