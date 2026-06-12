def online_j():
    member_list = []
    total_input_member = int(input())
    for _ in range(total_input_member):
        age, name = input().split()
        member_list.append([int(age), name])
    
    # key=lambda member_list: member_list[0] <-- [나이, 이름] 중에 0번째인 나이를 기준으로 정렬
    member_list.sort(key=lambda member_list: member_list[0])

    for member in range(0,total_input_member):
        print(member_list[member][0], member_list[member][1])
        #print(나이, 이름)

online_j()