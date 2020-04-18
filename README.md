# RPM spec files for the tools required to run XooNIps.
This repository maintains the packaging files to build packages on the Fedora Copr.

https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips/

## Installation Instructions of Fedora Copr build packages
Currently, Copr repository is provided only CentOS 7 packages.
```
$ sudo dnf install dnf-plugins-core
$ sudo dnf copr enable orrisroot/xoonips
$ sudo dnf install epel-release
$ sudo dnf install xoonips-utils
```
