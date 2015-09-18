from urlparse import urlparse

#from ceph_deploy.util.paths import gpg
#from ceph_deploy.hosts.common import map_components

NON_SPLIT_COMPONENTS = ['megam-nilavu', 'megam-common']

def install(distro, version_kind, version, **kw):
    
     packages = map_components(
        NON_SPLIT_COMPONENTS,
        kw.pop('components', [])
    )
    codename = distro.codename
    machine = distro.machine_type

    if version_kind in ['stable']:
        key = 'release'
    else:
        key = 'autobuild'

    distro.packager.install('ca-certificates')
    
    distro.packager.clean()

    # TODO this does not downgrade -- should it?
    if packages:
        distro.packager.install(
            packages,
            extra_install_flags=['-o', 'Dpkg::Options::=--force-confnew']
        )
    


