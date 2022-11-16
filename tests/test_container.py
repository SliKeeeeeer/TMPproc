from container import (
    container_add,
    container_read_from,
    container_write_to,
    container_clear,
    container_sort,
    Container
)


def test_clear():
    container = Container()
    for i in range(10):
        container_add(container, i)

    container_clear(container)

    assert container.size == 0


def test_len():
    container = Container()
    for i in range(10):
        container_add(container, i)

    assert container.size == 10


def test_read_from():
    container = Container()

    with open('input.txt', 'r') as file:
        container_read_from(container, file)

    assert container.size != 0


def test_write_to():
    container = Container()

    with open('input.txt', 'r') as file:
        container_read_from(container, file)

    with open('output.txt', 'w') as file:
        container_write_to(container, file)

    file_obs = open("output.txt", "r")
    file_exp = open("output_test_write.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()


def test_sort():
    container = Container()

    with open('input.txt', 'r') as file:
        container_read_from(container, file)

    container_sort(container)
    with open("output_test_sort.txt", "w") as file:
        container_write_to(container, file)

    file_obs = open("output_sort.txt", "r")
    file_exp = open("output_test_sort.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()


def test_write_procedure_to():
    container = Container()

    with open('input.txt', 'r') as file:
        container_read_from(container, file)

    with open("output_test_write_procedure_to.txt", "w") as file:
        container_write_to(container, file)

    file_obs = open("output_write_procedure.txt", "r")
    file_exp = open("output_test_write_procedure_to.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()