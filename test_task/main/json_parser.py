import json
import logging
import os
import ast
from main.definitions import ROOT_DIR, TEST_FOLDER_PATH

logger = logging.getLogger('test_task')


def _load_json_data_from_file(file_name):
    """
    :param file_name: File name to be read
    :return:
    """
    try:
        with open(file_name) as data_file:
            if data_file:
                data = json.load(data_file)
                return data
            else:
                logger.error('No file found at location:{%s}', file_name)
    except (IOError, ValueError) as error:
        logger.exception(error)
    return None


def pytest_generate_tests(metafunc):
    module_name = metafunc.module.__name__
    if 'jsontestdata' in metafunc.fixturenames:
        data_set_for_execution = get_test_data_for(module_name, metafunc.function.__name__)
        if not data_set_for_execution:
            logger.error("No test data for :Mod[%s]  Method[%s]", module_name, metafunc.function.__name__)
        metafunc.parametrize('json_data_parse', data_set_for_execution, scope='function')


def get_test_data_file_name(module_name):
    path_to_file = module_name .split('.')
    if path_to_file:
        if path_to_file[1] in ['tests','test']:
            path_to_file.pop(1)
            path_to_file.pop(0)
        path_to_file[-1] += '.json'
    logger.debug('Test Module Name:[%s] Resolved TestData location:%s',module_name,path_to_file)
    path = os.path.join(ROOT_DIR, TEST_FOLDER_PATH, *path_to_file)
    logger.debug(
            'Trying to locate testdata file in sub-folder location: [%s]   Is present [%s]', path, os.path.isfile(path))
    if not os.path.isfile(path):
        logger.warning('Test data file not in sub-folder..')
        path = os.path.join(ROOT_DIR, TEST_FOLDER_PATH, path_to_file[-1])
        logger.info('Test data file is present %s', os.path.isfile(path))
    logger.info('Test Data:[%s]', path)
    return path


def get_test_data_for(module_name, method_name):
    '''
    BUILD PARAMS = fetched from CLI : (priority, component etc)
    '''
    logger.debug(
        '<Test data Set-up> For Module:[%s],Method:[%s]', module_name, method_name)
    list_of_test_data = list()
    count = 0
    negative_count = 0
    test_method_data = dict()
    if module_name:
        file_path = get_test_data_file_name(module_name)
        logger.debug('Test data File location:%s', file_path)
        loaded_data = _load_json_data_from_file(os.path.join(file_path))
        if loaded_data:
            logger.debug('Json data loaded..')

            for module, module_child_nodes in loaded_data.items():
                logger.debug(module_name.split('.')[-1])
                if module == module_name.split('.')[-1]:
                    logger.debug(
                        'Validate module/file_name:[%s] with root-node key:[%s] --> Passed', module_name, module)

                    if method_name in module_child_nodes.keys():
                        logger.debug('method in module {} in {}'.format(method_name, module_child_nodes.keys()))
                        if 'test_data_set' in module_child_nodes.get(method_name).keys():
                            for key, test_data in module_child_nodes.get(method_name).get('test_data_set').items():
                                if (key == 'positive' or key == 'negative') and isinstance(test_data, list):
                                    for data_entry in test_data:
                                        try:
                                            data_entry = ast.literal_eval(json.dumps(data_entry))
                                        except:
                                            pass

                                        count = count + 1
                                        if key == 'negative':
                                            negative_count = negative_count + 1
                                            data_entry['negative_scenario'] = 'True'
                                        #validated_test_data = validate_user_data(data_entry)

                                        list_of_test_data.append(data_entry)
                                else:
                                    logger.debug(
                                        'Ignoring unknown key:[%s] in \'test_data-set \' node...', key)
                        else:
                            logger.debug(
                                'No data found under node:%s', 'test_data_set')
                        logger.debug(
                            'Found entry for test_method:%s ', method_name)
                    else:
                        logger.exception(
                            'Method node:[%s] not found in input file:[%s]', method_name, file_path)
                else:
                    logger.exception(
                        'JSON validation failed: Module Name:[%s] is not the root element input file:[%s]', module_name,
                        module)
        else:
            logger.exception(
                'No data found for input [Module_name=%s]', module_name)
    else:
        logger.exception(
            'Module_name:[%s] Method_name:[%s] are mandatory!!', module_name, method_name)

    logger.debug('Size of Resolved test data set : {}'.format(count))
    if list_of_test_data:
        logger.info('No of executions [%s] ', len(list_of_test_data))
        test_data_entry_size = 1
        for test_data_entry in list_of_test_data:
            logger.info(' ========== Test data for method : [%s] at index : [%s] ==============',method_name,
                        str(test_data_entry_size))
            logger.info(test_data_entry)
    else:
        logger.info('Skipping execution for test: [%s]..', method_name)
    logger.info('========= End of Data generation =========')
    return list_of_test_data
