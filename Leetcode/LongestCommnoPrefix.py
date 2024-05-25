
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    print(prefix)

    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print(result)

