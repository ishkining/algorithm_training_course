class StackMax:
    def __init__(self):
        self.values = []

    def get_max(self):
        if self.values:
            return max(self.values)
        else:
            return None

    def pop(self):
        self.values.pop()

    def push(self, value):
        self.values.append(value)


def main():
    num_commands = int(input())
    our_stack = StackMax()
    for _ in range(num_commands):
        command = input()
        if command == 'get_max':
            print(our_stack.get_max())
        elif command == 'pop':
            our_stack.pop()
        elif command.split(' ')[0] == 'push':
            our_stack.push(int(command.split(' ')[1]))


if __name__ == '__main__':
    main()
