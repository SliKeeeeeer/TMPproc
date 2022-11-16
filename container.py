from languages import language_read_from, language_write_to, compare, Type, Language, Procedure, Functional, ObjectOriented


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


def container_sort(container):
    if container.start_node is None:
        print('Empty list')
    else:
        n1 = container.start_node
        n2 = container.start_node
        while n1 is not None:
            while n2 is not None:
                if compare(n1.data, n2.data):
                    n1.data, n2.data = n2.data, n1.data
                n2 = n2.next
            n1 = n1.next
            n2 = container.start_node


def container_write_to_procedure(container, stream):
    stream.write('Only procedure languages\n')

    n = container.start_node
    while n is not None:
        if n.data.key == Type.procedure:
            language_write_to(n.data, stream)
        n = n.next


def container_check_languages(container):
    languages_1 = []
    n = container.start_node
    while n is not None:
        languages_1.append(n.data)
        n = n.next

    languages_2 = languages_1.copy()

    for language_1 in languages_1:
        for language_2 in languages_2:
            check_languages(language_1, language_2)


def check_languages(language_1, language_2):
    match language_1.obj, language_2.obj:
        case Procedure(), Procedure():
            print("Languages are the same type: Procedure and Procedure")

        case Procedure(), Functional():
            print("Languages are different type: Procedure and Functional")

        case Procedure(), ObjectOriented():
            print("Languages are different type: Procedure and ObjectOriented")

        case Functional(), Procedure():
            print("Languages are different type: Functional and Procedure")

        case Functional(), Functional():
            print("Languages are the same type: Functional and Functional")

        case Functional(), ObjectOriented():
            print("Languages are different type: Functional and ObjectOriented")

        case ObjectOriented(), Procedure():
            print("Languages are different type: ObjectOriented and Procedure")

        case ObjectOriented(), Functional():
            print("Languages are different type: ObjectOriented and Functional")

        case ObjectOriented(), ObjectOriented():
            print("Languages are the same type: ObjectOriented and ObjectOriented")

        case _:
            print('Unknown type')
            return

    print(f"First: {language_1}, second: {language_2}")
    print()