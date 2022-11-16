from languages import language_read_from, language_write_to


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Container:
    def __init__(self):
        self.start_node = None
        self.size = 0


def container_add(container, data):
    if container.start_node is None:
        container.start_node = Node(data)
    else:
        n = container.start_node
        while n.next is not None:
            n = n.next
        n.next = Node(data)

    container.size += 1


def container_clear(container):
    container.start_node = None
    container.size = 0


def container_read_from(container, stream):
    while line := stream.readline():
        item = language_read_from(stream, line)
        container_add(container, item)


def container_write_to(container, stream):
    stream.write(f'Container has {container.size} elements\n')

    if container.start_node != None:
        n = container.start_node
        while n is not None:
            language_write_to(n.data, stream)
            n = n.next