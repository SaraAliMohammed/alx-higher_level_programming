#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_nb_objects_private(self):
        '''Check if Base has private nb_objects class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_init(self):
        '''Checks if nb_objects has initialization value of zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_constructor_args_2(self):
        '''Tests constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_id_synced(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_id_synced_more(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_custom_id_int(self):
        '''Tests custom int id.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_custom_id_str(self):
        '''Tests custom int id.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_id_keyword(self):
        '''Tests id passed as keyword arg.'''
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_to_json_None(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        msg = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), msg)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        o = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(o)),
                         len(str(o)))
        o = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(o)),
                         len(str(o)))
        o = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(o),
                         '[{"foobarrooo": 989898}]')

        o = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(o),
                         '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

        o = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(o)),
                         len(str(o)))
        o = [{}]
        self.assertEqual(Base.to_json_string(o),
                         '[{}]')
        o = [{}, {}]
        self.assertEqual(Base.to_json_string(o),
                         '[{}, {}]')

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dict = [r1.to_dictionary(), r2.to_dictionary(),
                r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dict)
        dict = str(dict)
        dict = dict.replace("'", '"')
        self.assertEqual(dict, json_dictionary)

    def test_from_json_string(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        st = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), st)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        st = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        dict = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
                {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
                'height': 34340}]
        self.assertEqual(Base.from_json_string(st), dict)

        dict = [{}, {}]
        st = '[{}, {}]'
        self.assertEqual(Base.from_json_string(st), dict)
        dict = [{}]
        st = '[{}]'
        self.assertEqual(Base.from_json_string(st), dict)

        dict = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        st = '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(st), dict)

        dict = [{"foobarrooo": 989898}]
        st = '[{"foobarrooo": 989898}]'
        self.assertEqual(Base.from_json_string(st), dict)

        dict = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        st = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(st), dict)

        dict = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
                'height': 34340}]
        st = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(st), dict)

        list_in = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_out = Rectangle.from_json_string(
            Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)

        # ----------------- Tests for #16 ------------------------
    def test_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except Exception:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    def test_create(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        '''Tests load_from_file() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))


if __name__ == "__main__":
    unittest.main()
