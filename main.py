import sys

sys.stdout.write('stdout ness\n')

print(sys.platform)

print('in yokohama module')


def main():
    print("hi from yokohama")


if __name__ == '__main__':
    print(sys.argv[1:])
    main()
