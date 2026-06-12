def hash():
    r = 31
    M = 1234567891
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_input_dic= []
    alpha_input = input(f'알파벳을 입력하시오 : ').lower()
    alpha_input_dic.extend(alpha_input)
    hash_value = 0
    target_no = 0
    for target in alpha_input_dic:
        if target in alpha:
            alpha_no = alpha.index(target) + 1
            hash_value += alpha_no * (r ** target_no)
            target_no += 1
    return hash_value % M

a = hash()
print(a)