from enum import Enum


def language_read_from(stream, line):
    k = int(line)

    language = Language()
    language.year = int(stream.readline().rstrip('\n'))

    if k == 1:
        language.key = Type.procedure
        language.obj = Procedure()
        procedure_read_from(language.obj, stream)
    elif k == 2:
        language.key = Type.object_oriented
        language.obj = ObjectOriented()
        object_oriented_read_from(language.obj, stream)
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
    else:
        stream.write('Error type\n')

    stream.write(f'Year: {language.year}\n')
    stream.write(f'Years passed: {years_passed(language)}\n')


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


class Language:
    def __init__(self):
        self.year = None

        self.key = None
        self.obj = None


class Procedure:
    def __init__(self):
        self.has_abstract_type = None


class ObjectOriented:
    def __init__(self):
        self.inheritance_type = None


class Type(Enum):
    procedure = 1
    object_oriented = 2
