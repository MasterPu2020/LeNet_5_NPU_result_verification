
from PIL import Image

# number = input("select the number of the processed image\n")
number = '11'
number = int(number)
img = Image.open("./processed_image/" + "p_" + str(number) + ".png")
Pixel = []
for row in range(32):
    Pixel.append([])
    for col in range(32):
        pixel = img.getpixel((row, col))
        Pixel[row].append(pixel)

Filter = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

result_weight = [[[0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]],
                 [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]],
                 [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 1, 0]],
                 [[0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0]],
                 [[0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]],
                 [[0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 1, 1, 1, 0]],
                 [[0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]],
                 [[0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]],
                 [[0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]],
                 [[0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0]]]

s2 = []
total = 0
for F_row in range(28):
    s2.append([])
    for F_col in range(28):
        total = 0
        for row in range(5):
            for col in range(5):
                total = total + Pixel[F_row + row][F_col + col] * Filter[row][col]
        s2[F_row].append(total)

# Show S2 Data in hex form
s2_str = ''
for row in range(28):
    for col in range(28):
        if s2[row][col] <= 16:
            s2_str = s2_str + '000' + (str(hex(s2[row][col]))[2:]).upper()
        elif 16 < s2[row][col] <= 16 * 16:
            s2_str = s2_str + '00' + (str(hex(s2[row][col]))[2:]).upper()
        elif 16 * 16 < s2[row][col] <= 16 * 16 * 16:
            s2_str = s2_str + '0' + (str(hex(s2[row][col]))[2:]).upper()
        else:
            s2_str = s2_str + (str(hex(s2[row][col]))[2:]).upper()

c3 = []
for F_row in range(14):
    c3.append([])
    for F_col in range(14):
        Max = 0
        for row in range(2):
            for col in range(2):
                if s2[F_row * 2 + row][F_col * 2 + col] >= Max:
                    Max = s2[F_row * 2 + row][F_col * 2 + col]
        c3[F_row].append(Max)

c3_str = ''
n = 4
for row in range(14):
    for col in range(14):
        # for i in range(0, n):
        #     if (16 ** i) < c3[row][col] <= (16 ** (i + 1)):
        #         c3_str = c3_str + ('0' * (n - i)) + ' ' + (str(hex(c3[row][col]))[2:]).upper()
        if c3[row][col] <= 16:
            c3_str = c3_str + '000' + (str(hex(c3[row][col]))[2:]).upper()
        elif 16 < s2[row][col] <= 16 * 16:
            c3_str = c3_str + '00' + (str(hex(c3[row][col]))[2:]).upper()
        elif 16 * 16 < s2[row][col] <= 16 * 16 * 16:
            c3_str = c3_str + '0' + (str(hex(c3[row][col]))[2:]).upper()
        else:
            c3_str = c3_str + (str(hex(c3[row][col]))[2:]).upper()

s4 = []
total = 0
for F_row in range(10):
    s4.append([])
    for F_col in range(10):
        total = 0
        for row in range(5):
            for col in range(5):
                total = total + c3[F_row + row][F_col + col] * Filter[row][col]
        s4[F_row].append(total)

s4_str = ''
for row in range(10):
    for col in range(10):
        if s4[row][col] <= 16:
            s4_str = s4_str + '0000000' + (str(hex(s4[row][col]))[2:]).upper()
        elif 16 < s2[row][col] <= 16 * 16:
            s4_str = s4_str + '000000' + (str(hex(s4[row][col]))[2:]).upper()
        elif 16 * 16 < s2[row][col] <= 16 * 16 * 16:
            s4_str = s4_str + '00000' + (str(hex(s4[row][col]))[2:]).upper()
        elif 16 * 16 * 16 < s2[row][col] <= 16 * 16 * 16 * 16:
            s4_str = s4_str + '0000' + (str(hex(s4[row][col]))[2:]).upper()
        elif 16 * 16 * 16 * 16 < s2[row][col] <= 16 * 16 * 16 * 16 * 16:
            s4_str = s4_str + '000' + (str(hex(s4[row][col]))[2:]).upper()
        elif 16 * 16 * 16 * 16 * 16 < s2[row][col] <= 16 * 16 * 16 * 16 * 16 * 16:
            s4_str = s4_str + '00' + (str(hex(s4[row][col]))[2:]).upper()
        elif 16 * 16 * 16 * 16 * 16 * 16 < s2[row][col] <= 16 * 16 * 16 * 16 * 16 * 16 * 16:
            s4_str = s4_str + '0' + (str(hex(s4[row][col]))[2:]).upper()
        else:
            s4_str = s4_str + (str(hex(s4[row][col]))[2:]).upper()

c5 = []
Max = 0
for F_row in range(5):
    c5.append([])
    for F_col in range(5):
        Max = 0
        for row in range(2):
            for col in range(2):
                if s4[F_row * 2 + row][F_col * 2 + col] >= Max:
                    Max = s4[F_row * 2 + row][F_col * 2 + col]
        c5[F_row].append(Max)

c5_str = ''
n = 4
for row in range(5):
    for col in range(5):
        # for i in range(0, n):
        #     if (16 ** i) < c3[row][col] <= (16 ** (i + 1)):
        #         c3_str = c3_str + ('0' * (n - i)) + ' ' + (str(hex(c3[row][col]))[2:]).upper()
        if c5[row][col] <= 16:
            c5_str = c5_str + '0000000' + (str(hex(c5[row][col]))[2:]).upper()
        elif 16 < c5[row][col] <= 16 * 16:
            c5_str = c5_str + '000000' + (str(hex(c5[row][col]))[2:]).upper()
        elif 16 * 16 < c5[row][col] <= 16 * 16 * 16:
            c5_str = c5_str + '00000' + (str(hex(c5[row][col]))[2:]).upper()
        elif 16 * 16 * 16 < c5[row][col] <= 16 * 16 * 16 * 16:
            c5_str = c5_str + '0000' + (str(hex(c5[row][col]))[2:]).upper()
        elif 16 * 16 * 16 * 16 < c5[row][col] <= 16 * 16 * 16 * 16 * 16:
            c5_str = c5_str + '000' + (str(hex(c5[row][col]))[2:]).upper()
        elif 16 * 16 * 16 * 16 * 16 < c5[row][col] <= 16 * 16 * 16 * 16 * 16 * 16:
            c5_str = c5_str + '00' + (str(hex(c5[row][col]))[2:]).upper()
        elif 16 * 16 * 16 * 16 * 16 * 16 < c5[row][col] <= 16 * 16 * 16 * 16 * 16 * 16 * 16:
            c5_str = c5_str + '0' + (str(hex(c5[row][col]))[2:]).upper()
        else:
            c5_str = c5_str + (str(hex(c5[row][col]))[2:]).upper()

result_possibility = []
total = 0
for number in range(10):
    total = 0
    for F_row in range(5):
        for F_col in range(5):
            total = total + c5[F_row][F_col] * result_weight[number][F_row][F_col]
    result_possibility.append(total)

# Show filter in hex form
filter_string_8bit = ''
filter_string_16bit = ''
# (+1) F: 16 FF:256(8bit)  FFF:4096  Fx4:65536(16bit)  Fx5:1048576  Fx6:16777216 Fx7:268435456 Fx8:4294967296(32bit)
for row in range(5):
    for col in range(5):
        if Filter[row][col] <= 16:
            filter_string_8bit = filter_string_8bit + '0' + (str(hex(Filter[row][col]))[2:]).upper()
            filter_string_16bit = filter_string_16bit + '000' + (str(hex(Filter[row][col]))[2:]).upper()
        elif 16 < Filter[row][col] <= 256:
            filter_string_8bit = filter_string_8bit + (str(hex(Filter[row][col]))[2:]).upper()
            filter_string_16bit = filter_string_16bit + '00' + (str(hex(Filter[row][col]))[2:]).upper()
        elif 256 < Filter[row][col] <= 4096:
            filter_string_16bit = filter_string_16bit + '0' + (str(hex(Filter[row][col]))[2:]).upper()
        else:
            filter_string_16bit = filter_string_16bit + (str(hex(Filter[row][col]))[2:]).upper()

# Show C5 weight in hex form
result_weight_string = ''  #
for number in range(10):
    for row in range(5):
        for col in range(5):
            if result_weight[number][row][col] <= 16:
                result_weight_string = result_weight_string + '0000000' + (str(hex(result_weight[number][row][col]))[2:]).upper()
            elif 16 < result_weight[number][row][col] <= 256:
                result_weight_string = result_weight_string + '000000' + (str(hex(result_weight[number][row][col]))[2:]).upper()
            elif 256 < result_weight[number][row][col] <= 4096:
                result_weight_string = result_weight_string + '00000' + (str(hex(result_weight[number][row][col]))[2:]).upper()
            elif 4096 < result_weight[number][row][col] <= 65536:
                result_weight_string = result_weight_string + '0000' + (str(hex(result_weight[number][row][col]))[2:]).upper()
            elif 65536 < result_weight[number][row][col] <= 1048576:
                result_weight_string = result_weight_string + '000' + (str(hex(result_weight[number][row][col]))[2:]).upper()
            elif 1048576 < result_weight[number][row][col] <= 16777216:
                result_weight_string = result_weight_string + '00' + (str(hex(result_weight[number][row][col]))[2:]).upper()
            elif 16777216 < result_weight[number][row][col] <= 268435456:
                result_weight_string = result_weight_string + '0' + (str(hex(result_weight[number][row][col]))[2:]).upper()
            else:
                result_weight_string = result_weight_string + (str(hex(result_weight[number][row][col]))[2:]).upper()

# Show result in hex form
hex_form_result = ''
for row in range(10):
    if result_possibility[row] <= 16:
        hex_form_result = hex_form_result + '000000000000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 16 < result_possibility[row] <= 16 * 16:
        hex_form_result = hex_form_result + '00000000000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 16 * 16 < result_possibility[row] <= 16 * 16 * 16:
        hex_form_result = hex_form_result + '0000000000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 16 * 16 * 16 < result_possibility[row] <= 16 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '000000000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 16 * 16 * 16 * 16 < result_possibility[row] <= 16 * 16 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '00000000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 16 * 16 * 16 * 16 * 16 < result_possibility[row] <= 16 * 16 * 16 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '0000000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 16 * 16 * 16 * 16 * 16 * 16 < result_possibility[row] <= 16 * 16 * 16 * 16 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '000000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 16 * 16 * 16 * 16 * 16 * 16 * 16 < result_possibility[row] <= 16 * 16 * 16 * 16 * 16 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '00000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 268435456 * 16 < result_possibility[row] <= 268435456 * 16 * 16:
        hex_form_result = hex_form_result + '0000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 268435456 * 16 * 16 < result_possibility[row] <= 268435456 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '000000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 268435456 * 16 * 16 * 16 < result_possibility[row] <= 268435456 * 16 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '00000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 268435456 * 16 * 16 * 16 * 16 < result_possibility[row] <= 268435456 * 16 * 16 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '0000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 268435456 * 16 * 16 * 16 * 16 * 16 < result_possibility[row] <= 268435456 * 16 * 16 * 16 * 16 * 16 * 16:
        hex_form_result = hex_form_result + '000' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 268435456 * 16777216 < result_possibility[row] <= 268435456 * 16777216 * 16:
        hex_form_result = hex_form_result + '00' + (str(hex(result_possibility[row]))[2:]).upper()
    elif 268435456 * 16777216 * 16 < result_possibility[row] <= 268435456 * 16777216 * 16 * 16:
        hex_form_result = hex_form_result + '0' + (str(hex(result_possibility[row]))[2:]).upper()
    else:
        hex_form_result = hex_form_result + (str(hex(result_possibility[row]))[2:]).upper()

# Show image data in hex form
hex_form_image = ''
for row in range(32):
    for col in range(32):
        bit_pixel = int(Pixel[row][col])
        if bit_pixel <= 16:
            hex_form_image = hex_form_image + '0' + (str(hex(bit_pixel))[2:]).upper()
        else:
            hex_form_image = hex_form_image + (str(hex(bit_pixel))[2:]).upper()


print('Filter in 8 bit: ' + filter_string_8bit)
print('Bit length: ' + str(len(filter_string_8bit) * 4))

print('Filter in 16 bit: ' + filter_string_16bit)
print('Bit length: ' + str(len(filter_string_16bit) * 4))

print('C5 (Filter) weight: ' + result_weight_string)
print('Bit length: ' + str(len(result_weight_string) * 4))

print('Image in hex form: ' + hex_form_image)
print('Bit length: ' + str(len(hex_form_image) * 4))

print('img28: ' + s2_str)
print('Bit length: ' + str(len(s2_str) * 4))

print('img14: ' + c3_str)
print('Bit length: ' + str(len(c3_str) * 4))

print('img10: ' + s4_str)
print('Bit length: ' + str(len(s4_str) * 4))

print('img5: ' + c5_str)
print('Bit length: ' + str(len(c5_str) * 4))

print('Result: ' + hex_form_result)
print('Bit length: ' + str(len(hex_form_result) * 4))

# print("Most resemble to " + str(max_row) + " at " + str(Max))
# print(result_possibility)
