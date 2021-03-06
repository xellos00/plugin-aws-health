
__all__ = ['PluginLogsResponse']

from spaceone.api.core.v1 import plugin_pb2
from spaceone.api.monitoring.plugin import log_pb2
from spaceone.core.pygrpc.message_type import *


def PluginAction(action_data):
    info = {
        'method': action_data['method'],
    }
    if 'options' in action_data:
        info.update({'options': change_struct_type(action_data['options'])})
    return plugin_pb2.PluginAction(**info)


def LogsInfo(result):
    info = {'logs': change_list_value_type(result['logs'])}
    return log_pb2.LogsInfo(**info)


def PluginLogsResponse(resource_dict):
    result = {
        'resource_type': resource_dict['resource_type'],
        'result': LogsInfo(resource_dict['result'])
    }

    if resource_dict.get('actions'):
        result['actions'] = list(map(PluginAction, resource_dict['actions']))

    return log_pb2.PluginLogsResponse(**result)
