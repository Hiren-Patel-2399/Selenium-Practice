#function level
#test function
"""
def testcompose():
    print("composing a mail")
"""
"""
>pytest -vs pyconcept.py
collected 1 item

pyconcept.py::testcompose composing a mail

PASSED
"""
#non-test function

"""
def compose_test():
    print("compose test case")
"""

"""
>pytest -vs pyconcept.py
collected 0 items
"""
#multiple test function

"""def test_login():
    print("login testcase")
def test_signup():
    print("signup testcase")
def test_register():
    print("register testcase")"""

"""
>pytest -vs pyconcept.py
collected 3 items

pyconcept.py::test_login login testcase
PASSED
pyconcept.py::test_signup signup testcase
PASSED
pyconcept.py::test_register register testcase
PASSED
"""

#combination of test and normal function

"""def test_login():
    print("login testcase")
def signup():
    print("signup testcase")
def test_register():
    print("register testcase")
"""

"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::test_login login testcase
PASSED
pyconcept.py::test_register register testcase
PASSED
"""
#normal/non test function

"""def login():
    print("login testcase")
def signup():
    print("signup testcase")
def register():
    print("register testcase")"""

"""
>pytest -vs pyconcept.py
collected 0 items
"""
###########################################################################################################
#class and method level
#testclass and test method

"""class Test_Gmail:
    def test_TC1(self):
        print("Testcase1")
    def test_TC2(self):
        print("testcase2")"""

"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::Test_Gmail::test_TC1 Testcase1
PASSED
pyconcept.py::Test_Gmail::test_TC2 testcase2
PASSED
"""

#normal class and test method

"""class Gmail:
    def test_TC1(self):
        print("Testcase1")
    def test_TC2(self):
        print("testcase2")"""

"""
>pytest -vs pyconcept.py
collected 0 items
"""

#test class with normal and test method

"""class TestGmail:
    def TC1(self):
        print("Testcase1")
    def test_TC2(self):
        print("testcase2")"""

"""
>pytest -vs pyconcept.py
collected 1 item

pyconcept.py::TestGmail::test_TC2 testcase2
PASSED
"""

#test class with normal method

"""class TestGmail:
    def TC1(self):
        print("Testcase1")
    def TC2(self):
        print("testcase2")"""

"""
>pytest -vs pyconcept.py
collected 0 items
"""

#test class with normal and test method and constructor

"""class Test_FB:
    def __init__(self):
        print("in a constructor")
    def test_login(self):
        print("login page")"""

"""
>pytest -vs pyconcept.py
collected 0 items
PytestCollectionWarning: cannot collect test class 'Test_FB' because it has a __init__ constructor (from: pyconcept.py)
"""
#the above we are gerring error because a class consist of constructor, constructor will get execute
#only when we create a object, but test class is impicitly callable we no need to create an object.

#multiple test class with test method
"""
class Test_Fb:
    def test_tc1(self):
        print("fb testcase1")

class Test_Gmail:
    def test_tc2(self):
        print("gmail testcase")
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::Test_Fb::test_tc1 fb testcase1
PASSED
pyconcept.py::Test_Gmail::test_tc2 gmail testcase
PASSED
"""

#multiple test class with test method and normal method
"""
class Test_Fb:
    def test_tc1(self):
        print("fb testcase1")

class Test_Gmail:
    def tc2(self):
        print("gmail testcase")
    def test_tc3(self):
        print("gmail testcase3")
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::Test_Fb::test_tc1 fb testcase1
PASSED
pyconcept.py::Test_Gmail::test_tc3 gmail testcase3
PASSED
"""

#multiple class with test method
"""
class Fb:
    def test_tc1(self):
        print("fb testcase1")

class Gmail:
    def test_tc2(self):
        print("gmail testcase")
    def test_tc3(self):
        print("gmail testcase3")
"""
"""
>pytest -vs pyconcept.py
collected 0 items
"""
#13-09-2023
#module level
"""
def test_tc1():
    print("test function")

class Test_App:
    def test_tc2(self):
        print("test method1")
    def tc3(self):
        print("test method2")

class Demo:
    def test_tc3(self):
        print("test method3")
"""
"""
>pytest -vs pyconcept.py
collected 2 items

pyconcept.py::test_tc1 test function
PASSED
pyconcept.py::Test_App::test_tc2 test method1
PASSED
"""