"""
A utility module that can host utilities that will be used by more than
one type of distro and not common to all of them
"""
from megdc.util import pkg_managers


def install_yum_priorities(distro, _yum=None):
    """
    
    The name of the package changed back and forth (!) since CentOS 4:

    From the CentOS wiki::

        Note: This plugin has carried at least two differing names over time.
        It is named yum-priorities on CentOS-5 but was named
        yum-plugin-priorities on CentOS-4. CentOS-6 has reverted to
        yum-plugin-priorities.

    :params _yum: Used for testing, so we can inject a fake yum
    """
    yum = _yum or pkg_managers.yum
    package_name = 'yum-plugin-priorities'

    if distro.normalized_name == 'centos':
        if distro.release[0] != '6':
            package_name = 'yum-priorities'
    yum(distro.conn, package_name)
