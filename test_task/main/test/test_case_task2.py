import pytest
import requests
import json
import yaml
from config_v2 import *
import expected_output_v2


def test_all_int_edges(url=f'http://{web_service_ip}', edge_list=all_int_edges,
                       expected_output=expected_output_v2.all_int_edges):
    final_url = url+'cuboid/calculate'
    print(final_url)
    json_data = {"cuboid_edges": edge_list}
    print('json_data=', json_data)
    response = requests.post(url=final_url, data=json_data, json=json_data)
    #response = requests.post(final_url, json_data)
    print(response)
    print(response.status_code)
    json_response = json.loads(response.text)
    assert (response.status_code == 200 and json_response['error'] is None and json_response['success'] is True and
           expected_output['surface_area'] == json_response['surface_area'] and
           expected_output['volume'] == json_response['volume'] and
           expected_output['sum_of_edges'] == json_response['sum_of_edges']), \
        f'Cuboid Calculation with all int value as edge parameter did not work'

"""
def test_all_float_edges(url=f'http://{web_service_ip}', edge_list=all_float_edges,
                         expected_output=expected_output_v2.all_float_edges):
    final_url = url+'cuboid/calculate'
    json_data = {"cuboid_edges": edge_list}
    response = requests.post(final_url, json_data)
    json_response = response.json()
    assert (response.status_code == 200 and json_response['error'] is None and json_response['success'] is True and
           expected_output['surface_area'] == json_response['surface_area'] and
           expected_output['volume'] == json_response['volume'] and
           expected_output['sum_of_edges'] == json_response['sum_of_edges']), \
        f'Cuboid Calculation with all float value as edge parameter did not work'


def test_edges_with_zero(url=f'http://{web_service_ip}', edge_list=edges_with_zero,
                         expected_output=expected_output_v2.edges_with_zero):
    final_url = url+'cuboid/calculate'
    json_data = {"cuboid_edges": edge_list}
    response = requests.post(final_url, json_data)
    json_response = response.json()
    assert (response.status_code == 400 and json_response['error'] == expected_output['error'] and 
            json_response['success'] is False), \
        f'Cuboid Calculation with edges having zero value processed'


def test_edges_with_non_int_or_float(url=f'http://{web_service_ip}', edge_list=edges_with_non_int_or_float,
                                     expected_output=expected_output_v2.edges_with_non_int_or_float):
    final_url = url+'cuboid/calculate'
    json_data = {"cuboid_edges": edge_list}
    response = requests.post(final_url, json_data)
    json_response = response.json()
    assert (response.status_code == 400 and json_response['error'] == expected_output['error'] and
            json_response['success'] is False), \
        f'Cuboid Calculation when edges having non int or float value is processed'


def test_more_than_3_edges(url=f'http://{web_service_ip}', edge_list=more_than_3_edges,
                           expected_output=expected_output_v2.more_than_3_edges):
    final_url = url+'cuboid/calculate'
    json_data = {"cuboid_edges": edge_list}
    response = requests.post(final_url, json_data)
    json_response = response.json()
    assert (response.status_code == 400 and json_response['error'] == expected_output['error'] and
            json_response['success'] is False), \
        f'Cuboid Calculation when more than 3 edges are given is processed'


def test_less_than_3_edges(url=f'http://{web_service_ip}', edge_list=less_than_3_edges,
                           expected_output=expected_output_v2.less_than_3_edges):
    final_url = url+'cuboid/calculate'
    json_data = {"cuboid_edges": edge_list}
    response = requests.post(final_url, json_data)
    json_response = response.json()
    assert (response.status_code == 400 and json_response['error'] == expected_output['error'] and
            json_response['success'] is False), \
        f'Cuboid Calculation when less than 3 edges are given is processed'

"""

def test_get_all_entries_from_db(url=f'http://{web_service_ip}'):
    final_url = url + '/cuboid/result'
    # final_url = url
    print('final_url=', final_url)
    response = requests.get(final_url)
    print('response=', response)
    print(response.status_code)
    json_response = response.json()
    print(json_response)
    # compare the len(data) and result from db

"""
test_get_all_entries_from_db(url='http://85.215.232.182')

"""

test_all_int_edges(url='http://85.215.232.182/', edge_list=[2, 3, 4],
                       expected_output={'surface_area': '52.0', 'volume': '24.0', 'sum_of_edges': '36.0'})
