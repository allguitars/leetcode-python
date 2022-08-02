'''
1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/

* foodpand online test

#easy

Solution from discussion board
'''


def max_number_of_ballons(text):
    # Here is my brute force solution during the online test
    # letter_count = {}
    # # O(n)
    # for c in text:
    #     letter_count[c] = letter_count.get(c, 0) + 1

    # count_b = letter_count.get('b', 0)
    # count_a = letter_count.get('a', 0)
    # count_l = letter_count.get('l', 0)
    # count_o = letter_count.get('o', 0)
    # count_n = letter_count.get('n', 0)

    # # O(k)
    # res = 0
    # while (count_b >= 1 and
    #        count_a >= 1 and
    #        count_l >= 2 and
    #        count_o >= 2 and
    #        count_n >= 1):
    #     res += 1
    #     count_b -= 1
    #     count_a -= 1
    #     count_l -= 2
    #     count_o -= 2
    #     count_n -= 1
    # return res

    # # Here is the solution from leetcode duscussion -- Fast!
    # # O(5n) = O(n)
    count_b = text.count('b')
    count_a = text.count('a')
    count_l = text.count('l')
    count_o = text.count('o')
    count_n = text.count('n')

    # Constant time!! No while loop!
    return min(count_b, count_a, count_l // 2, count_o // 2, count_n)


# text = 'nlaebolko'         # 1
text = 'loonbalxballpoon'    # 2
# text = 'leetcode'          # 0

print(max_number_of_ballons(text))
