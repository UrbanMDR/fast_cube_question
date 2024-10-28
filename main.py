import struct

#计算一个浮点数的立方根，不使用库函数。
#保留一位小数。
#目前问题 1 我该怎么样复现 i =  * ( long * ) &y;  这样的操作
#2 我该如何实现32位数的算术位移 struct 模块转换过来的整数似乎并不是32位符号整数(long)


def fast_cube_root(num: float) -> float:
    abs_num = abs(num)
    x = abs(num)
    i = struct.unpack('I', struct.pack('f', abs_num))[0] # evil floating point bit level hacking
    i = (i >> 2) + (i >> 4) + (i >> 6) + (i >> 8) + (i >> 10) + (i >> 12)+ 0x2a555555 # what the fuck?
    y = struct.unpack('f', struct.pack('I', i))[0]

    y = (2 * y + x / (y * y)) *0.3332 # 1st iteration
    # y = (2 * y + x / (y * y)) *0.3332 # 2nd iteration, this can be removed
    y =-y if num < 0 else y
    return round(y,1)


print(fast_cube_root(float(input())))
