import pytest
from main.api import CuboidCalci
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('test_tail_for_file_content')


def test_with_three_input_values(jsontestdata):
    logger.info(jsontestdata['test_description'])
    edges = jsontestdata['edges']
    cmd = 'CuboidCalci.py' + edges
    parse_arg = Cu.parse_args(cmd.split())
    case = tail.tail(parse_arg.filename)
    expected = jsontestdata['expected_result']
    assert case, expected


def test_for_less_than_three_inputs(jsontestdata):
    logger.info(jsontestdata['test_description'])
    filename = jsontestdata['filename']
    cmd = 'tail.py -f'+ filename
    parse_arg= tail.parse_args(cmd.split())
    case = tail.tail(parse_arg.filename)
    expected = jsontestdata['expected_result']
    assert case, expected


def test_more_than_three_inputs(jsontestdata):
    logger.info(jsontestdata['test_description'])
    filename = jsontestdata['filename']
    cmd = 'tail.py -f' + filename
    parse_arg= tail.parse_args(cmd.split())
    case = tail.tail(parse_arg.filename)
    expected = jsontestdata['expected_result']
    assert case, expected


def test_with_invalid_inputs(jsontestdata):
    logger.info(jsontestdata['test_description'])
    filename = jsontestdata['filename']
    cmd = 'tail.py -f' + filename
    parse_arg= tail.parse_args(cmd.split())
    case = tail.tail(parse_arg.filename)
    expected = jsontestdata['expected_result']
    assert case, expected


def test_content_less_than_five_lines(jsontestdata):
    logger.info(jsontestdata['test_description'])
    filename = jsontestdata['filename']
    cmd = 'tail.py -f' + filename
    parse_arg = tail.parse_args(cmd.split())
    case = tail.tail(parse_arg.filename)
    expected = jsontestdata['expected_result']
    assert case, expected
