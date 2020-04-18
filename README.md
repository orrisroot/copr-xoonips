# RPM spec files for the tools required to run XooNIps.
This repository maintains the packaging files to build packages on the Fedora Copr.

https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips/

## Installation Instructions of Fedora Copr build packages
This Copr repository is provided for CentOS 7 and CentOS 8.

### CentOS 7
```
$ sudo yum install yum-plugin-copr
$ sudo yum copr enable orrisroot/xoonips
$ sudo yum install epel-release
$ sudo yum install xoonips-utils
```

### CentOS 8
```
$ sudo dnf install dnf-plugins-core
$ sudo dnf copr enable orrisroot/xoonips
$ sudo dnf install epel-release
$ sudo dnf install xoonips-utils
```

## Providing Packages
* wv : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips/package/wv/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips/package/wv/)
  * epel-7-x86_64
    * wv-1.2.9-21.1.el7.ors.src.rpm
    * wv-1.2.9-21.1.el7.ors.x86_64.rpm
    * wv-debuginfo-1.2.9-21.1.el7.ors.x86_64.rpm
    * wv-devel-1.2.9-21.1.el7.ors.x86_64.rpm
  * epel-8-x86_64
    * wv-1.2.9-21.1.el8.ors.src.rpm
    * wv-1.2.9-21.1.el8.ors.x86_64.rpm
    * wv-debuginfo-1.2.9-21.1.el8.ors.x86_64.rpm
    * wv-devel-1.2.9-21.1.el8.ors.x86_64.rpm
