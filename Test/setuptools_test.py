from setuptools import setup, find_packages

setup(
    test_suites="tests", #unit test
    tests_require=['pytest'] # pytestを使う場合
    ''' pytestを使う場合 > setup.cfg
    [aliases]
    test=pytest

    [tool:pytest]
    python_files = tests/*
    '''
)