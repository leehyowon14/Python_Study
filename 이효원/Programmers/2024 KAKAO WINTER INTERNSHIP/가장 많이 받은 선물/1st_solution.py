# 기본적으로는 더 많이 준 사람이 받음.
# 근데 같으면 선물 지수 더 높은 사람이 받음.
# 선물지수: 선물_나-친 - 선물_친-나.
# 선물을 가장 많이 받을 친구가 받을 선물의 수는?
def solution(friends, gifts):
    # 받은 친구: {준 친구: 횟수}
    present_dict = {friend: 0 for friend in friends}
    received_dict, toss_dict, result_dict = present_dict.copy(
    ), present_dict.copy(), present_dict.copy()
    present_dict = {key: present_dict.copy() for key in present_dict}

    for gift in gifts:
        gift = gift.split(' ')
        present_dict[gift[1]][gift[0]] += 1

    # for key, value in present_dict.items():
    #     print(key, value)
    # print()

    # 친구: 준 횟수
    for gift_dict in present_dict.values():
        for name, num in gift_dict.items():
            toss_dict[name] += num

    # 친구: 받은 횟수
    for key, value in present_dict.items():
        received_dict[key] = sum(value.values())

    for current_friend in present_dict.keys():
        for target_friend, num in present_dict[current_friend].items():
            if current_friend == target_friend:
                continue
            elif present_dict[target_friend][current_friend] > num:
                result_dict[current_friend] += 1
            elif present_dict[target_friend][current_friend] < num:
                result_dict[target_friend] += 1
            # 준 횟수-받은 횟수 동일
            elif toss_dict[current_friend] - received_dict[current_friend] > toss_dict[target_friend] - received_dict[target_friend]:
                result_dict[current_friend] += 1
            else:
                result_dict[target_friend] += 1
        # print(current_friend, result_dict)

    return sorted(result_dict.values(), reverse=True)[0] // 2


# print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo",
#       "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
