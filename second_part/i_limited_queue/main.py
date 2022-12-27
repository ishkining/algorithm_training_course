class MyQueueSized:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def push(self, value):
        if len(self.queue) < self.size:
            self.queue.append(value)
        else:
            print('error')

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def get_size(self):
        return len(self.queue)


def main():
    num_commands = int(input())
    input_size = int(input())
    queue = MyQueueSized(input_size)

    for _ in range(num_commands):
        command = input()
        if command == 'peek':
            print(queue.peek())
        elif command == 'pop':
            print(queue.pop())
        elif command == 'size':
            print(queue.get_size())
        elif command.split(' ')[0] == 'push':
            queue.push(command.split(' ')[1])


if __name__ == '__main__':
    main()
