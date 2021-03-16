import pytest
from main.json_parser import get_test_data_for
import logging
from datetime import datetime
from html_table_parser import HTMLTableParser as Html

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('test_task')

html = Html()


@pytest.fixture(scope='function')
def jsontestdata(json_data_parse):
    yield json_data_parse


def pytest_generate_tests(metafunc):
    module_name = metafunc.module.__name__
    if 'jsontestdata' in metafunc.fixturenames:
        data_set_for_execution = get_test_data_for(module_name, metafunc.function.__name__)
        if not data_set_for_execution:
            logger.error("No test data for :Mod[%s]  Method[%s]", module_name, metafunc.function.__name__)
        metafunc.parametrize('json_data_parse', data_set_for_execution, scope='function')


