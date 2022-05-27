# stack overflow: https://stackoverflow.com/questions/9330946/how-to-convert-a-decimal-base-10-to-a-negabinary-base-2
# wiki: https://en.wikipedia.org/wiki/Negative_base#Calculation


def to_negtive_base(num, base):
    if num == 0:
        return '0'

    result = []

    while num != 0:
        num, remainder = divmod(num, base)

        if remainder < 0:
            num += 1
            remainder -= base

        result.append(remainder)

    return result


print(to_negtive_base(-23, -2))
