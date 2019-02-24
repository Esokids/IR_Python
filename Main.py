import InformationRetrieval

if __name__ == '__main__':
    print('function 1 is Inverted Index')
    print('function 2 is Positional Index')
    print('function 3 is Binary Search Tree')
    print('function 4 is Hash Dictionary')
    cmd = int(input('Enter function do you want to run: '))

    if cmd == 1:
        InformationRetrieval.invertedIndex()
    if cmd == 2:
        InformationRetrieval.positionalIndex()
    if cmd == 3:
        InformationRetrieval.binarySearchTree()
    if cmd == 4:
        InformationRetrieval.hash_Dictionary()
