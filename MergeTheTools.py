def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string) + 1, k):
        result = string[i:i + k-1]
        if len(result) == k-1:
            print(result)
        else:
            return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    print(merge_the_tools(string, max_width))
