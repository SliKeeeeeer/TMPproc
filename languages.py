from enum import Enum


def language_read_from(stream, line):
    k = int(line)

    language = Language()
    language.year = int(stream.readline().rstrip('\n'))
    language.references = int(stream.readline().rstrip('\n'))

    if k == 1:
        language.key = Type.procedure
        language.obj = Procedure()
        procedure_read_from(language.obj, stream)
    elif k == 2:
        language.key = Type.object_oriented
        language.obj = ObjectOriented()
        object_oriented_read_from(language.obj, stream)
    elif k == 3:
        language.key = Type.functional
        language.obj = Functional()
        functional_read_from(language.obj, stream)
    else:
        return 0

    return language


def language_write_to(language, stream):
    if language.key == Type.procedure:
        stream.write('[Procedure language]\n')
        procedure_write_to(language.obj, stream)
    elif language.key == Type.object_oriented:
        stream.write('[OOP language]\n')
        object_oriented_write_to(language.obj, stream)
    elif language.key == Type.functional:
        stream.write('[Functional language]\n')
        functional_write_to(language.obj, stream)
    else:
        stream.write('Error type\n')

    stream.write(f'Year: {language.year}\n')
    stream.write(f'Years passed: {years_passed(language)}\n')
    stream.write(f'References: {language.references}\n')


def procedure_read_from(language, stream):
    language.has_abstract_type = bool(stream.readline())


def procedure_write_to(language, stream):
    stream.write(f'Has abstract type: {language.has_abstract_type}\n')


def object_oriented_read_from(language, stream):
    language.inheritance_type = int(stream.readline())


def object_oriented_write_to(language, stream):
    stream.write(f'Inheritance type: {language.inheritance_type}\n')


def years_passed(language):
    return 2022 - language.year


def compare(self, other):
    return years_passed(self) < years_passed(other)


def functional_read_from(language, stream):
    language.typification = int(stream.readline())
    language.has_lazy_evaluation = bool(stream.readline())


def functional_write_to(language, stream):
    stream.write(f'Inheritance type: {language.typification}\n')
    stream.write(f'Has lazy evaluation: {language.has_lazy_evaluation}\n')


class Language:
    def __init__(self):
        self.year = None
        self.references = None

        self.key = None
        self.obj = None


class Procedure:
    def __init__(self):
        self.has_abstract_type = None


class ObjectOriented:
    def __init__(self):
        self.inheritance_type = None


class Functional:
    def __init__(self):
        self.typification = None
        self.has_lazy_evaluation = None


class Type(Enum):
    procedure = 1
    object_oriented = 2
    functional = 3
