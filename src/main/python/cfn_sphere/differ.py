from cfn_sphere.aws.cfn import CloudFormation
from cfn_sphere.exceptions import CfnSphereException
import dictdiffer


class StackDiffer(object):

    def __init__(self, region, stack):
        self.cfn = CloudFormation(region)
        self.stack = stack

    def get_parameters_diff_string(self):
        pass

    def get_template_diff_string(self):
        pass


def get_diff_string(old_dict, new_dict):
    diff_string = ""
    diff = dictdiffer.diff(old_dict, new_dict)
    for difference in diff:
        diff_string = diff_string + get_modification_string(difference) + "\n"

    return diff_string


def get_modification_string(difference_tuple):
    change_type = difference_tuple[0]
    key = difference_tuple[1]
    modification = difference_tuple[2]

    if change_type == "change":
        return "Modify  {0}: '{1}' -> '{2}'".format(key, modification[0], modification[1])
    elif change_type == "add":
        return "Add     {0}.{1}".format(key, modification[0][0])
    elif change_type == "remove":
        return "Remove  {0}.{1}".format(key, modification[0][0])
    else:
        raise CfnSphereException("Unknown diff modification type: {0}".format(change_type))
