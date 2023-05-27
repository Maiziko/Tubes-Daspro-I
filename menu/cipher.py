from menu.function import list_to_string_1_line

def cipher(string, reverse):
    string_list = [letter for letter in string]
    old_ord = [ord(letter) for letter in string]
    new_ord = [num for num in old_ord]
    if not reverse:
        for i in range(len(string_list)):
            if (old_ord[i] >= ord('A'))&(old_ord[i] <= ord('Z')):
                new_ord[i] = (((old_ord[i]-ord('A'))+(i+1)**2)%26)+ord('A')
            elif (old_ord[i] >= ord('a'))&(old_ord[i] <= ord('z')):
                new_ord[i] = (((old_ord[i]-ord('a'))+(i+1)**2)%26)+ord('a')
            elif (old_ord[i] >= ord('0'))&(old_ord[i] <= ord('9')):
                new_ord[i] = (((old_ord[i]-ord('0'))+(i+1)**2)%10)+ord('0')
    else:
        for i in range(len(string_list)):
            if (old_ord[i] >= ord('A'))&(old_ord[i] <= ord('Z')):
                new_ord[i] = (((old_ord[i]-ord('A'))-(i+1)**2)%26)+ord('A')
            elif (old_ord[i] >= ord('a'))&(old_ord[i] <= ord('z')):
                new_ord[i] = (((old_ord[i]-ord('a'))-(i+1)**2)%26)+ord('a')
            elif (old_ord[i] >= ord('0'))&(old_ord[i] <= ord('9')):
                new_ord[i] = (((old_ord[i]-ord('0'))-(i+1)**2)%10)+ord('0')
    new_string_list = [chr(i) for i in new_ord]
    new_string = list_to_string_1_line(new_string_list)
    return new_string