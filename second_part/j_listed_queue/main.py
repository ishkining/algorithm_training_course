class MyListedQueue:
    def __init__(self):
        self.queue = []

    def get(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return 'error'

    def put(self, value):
        self.queue.append(value)

    def size(self):
        return len(self.queue)


def main():
    num_commands = int(input())
    queue = MyListedQueue()
    for _ in range(num_commands):
        command = input()
        if command == 'get':
            print(queue.get())
        elif command == 'size':
            print(queue.size())
        elif command.split(' ')[0] == 'put':
            queue.put(int(command.split(' ')[1]))


if __name__ == '__main__':
    main()