class StackMaxEffective:
    def __init__(self):
        self.values = []

    def get_max(self):
        if len(self.values) > 0:
            return self.values[-1][1]
        else:
            return None

    def pop(self):
        if len(self.values) > 0:
            self.values.pop()
        else:
            print('error')

    def push(self, value):
        if len(self.values) == 0:
            max_for_now = value
        else:
            max_for_now = self.values[-1][1]
            if max_for_now < value:
                max_for_now = value
        self.values.append((value, max_for_now))


def main():
    num_commands = int(input())
    our_stack = StackMaxEffective()
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