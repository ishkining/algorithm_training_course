class MyDeck:
    def __init__(self, limit):
        self.limit = limit
        self.deck = []

    def push_front(self, value):
        if len(self.deck) <= self.limit:
            self.deck.insert(0, value)
        else:
            print('error')

    def push_back(self, value):
        if len(self.deck) <= self.limit:
            self.deck.append(value)
        else:
            print('error')

    def pop_front(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            return 'error'

    def pop_back(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return 'error'


def main():
    num_commands = int(input())
    our_size = int(input())
    my_deck = MyDeck(our_size)
    for _ in range(num_commands):
        command = input()
        if command == 'pop_back':
            print(my_deck.pop_back())
        elif command == 'pop_front':
            print(my_deck.pop_front())
        else:
            part = command.split(' ')
            if part[0] == 'push_front':
                my_deck.push_front(int(part[1]))
            elif part[1] == 'push_back':
                my_deck.push_back((int(part[1])))


if __name__ == '__main__':
    main()