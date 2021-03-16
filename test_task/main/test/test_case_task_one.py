import pytest
from main.api import CuboidCalci
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('test_tail_for_file_content')


def test_for_exactly_three_input_values(jsontestdata):
    logger.info(jsontestdata['test_description'])
    edges = jsontestdata['edges']
    cmd = 'CuboidCalci.py' + edges
    parse_arg = CuboidCalci.parse_args(cmd.split())
    case = CuboidCalci.cuboid_app(parse_arg)
    expected = jsontestdata['expected_result']
    assert case, expected


def test_for_less_than_three_input_values(jsontestdata):
    logger.info(jsontestdata['test_description'])
    edges = jsontestdata['edges']
    cmd = 'CuboidCalci.py' + edges
    parse_arg = CuboidCalci.parse_args(cmd.split())
    case = CuboidCalci.cuboid_app(parse_arg)
    expected = jsontestdata['expected_result']
    assert case, expected


def test_more_than_three_inputs(jsontestdata):
    logger.info(jsontestdata['test_description'])
    edges = jsontestdata['edges']
    cmd = 'CuboidCalci.py' + edges
    parse_arg = CuboidCalci.parse_args(cmd.split())
    case = CuboidCalci.cuboid_app(parse_arg)
    expected = jsontestdata['expected_result']
    assert case, expected


def test_with_invalid_input(jsontestdata):
    logger.info(jsontestdata['test_description'])
    edges = jsontestdata['edges']
    cmd = 'CuboidCalci.py' + edges
    parse_arg = CuboidCalci.parse_args(cmd.split())
    case = CuboidCalci.cuboid_app(parse_arg)
    expected = jsontestdata['expected_result']
    assert case, expected
