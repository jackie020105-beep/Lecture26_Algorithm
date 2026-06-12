def hash():
    r = 31
    M = 1234567891
    alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpa_input_dic= []
    alpa_input = input(f'알파벳을 입력하시오 : ').lower()
    alpa_input_dic.extend(alpa_input)
    hash_value = 0
    target_no = 0
    for target in alpa_input_dic:
        if target in alpa:
            alpa_no = alpa.index(target) + 1
            hash_value += alpa_no * (r ** target_no)
            target_no += 1
    return hash_value % M

a = hash()
print(a)