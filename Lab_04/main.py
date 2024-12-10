from deque import Deque


def wordToDeque(s: str) -> Deque:
    deque = Deque()
    for i in s:
        deque.push(i)

    return deque


def testWordToDeque(test_string, test_deque):
    temp = test_deque
    for i in range(len(test_string)):
        if temp.front == None or test_string[i] != temp.front.item:
            return False
        else:
            temp.front = temp.front.next
    if temp.front != None:
        return False
    return True


def OffByOne(a: chr, b: chr) -> bool:
    return ord(a) - ord(b) == 1 or ord(b) - ord(a) == 1


def OffByN(a: chr, b: chr, n: int) -> bool:
    return ord(a) - ord(b) == n or ord(b) - ord(a) == n


if __name__ == '__main__':
    test1_string = "hello"
    test1_deque = wordToDeque(test1_string)
    print(testWordToDeque(test1_string, test1_deque))  # Should return True

    char1 = 'c'
    char2 = 'd'
    print(OffByOne(char1, char2))  # print True

    char1 = 'b'
    char2 = 'e'
    N = 3
    print(OffByN(char1, char2, N))  # Prints True
