# RPM spec files for the tools required to run XooNIps.
This repository maintains the packaging files to build packages on the Fedora Copr.

https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips-support/

## Installation Instructions of Fedora Copr build packages
This Copr repository is provided for CentOS 7 and CentOS 8.

### CentOS 7
```
$ sudo yum install epel-release
$ sudo yum install yum-utils yum-plugin-copr
$ sudo yum install https://rpms.remirepo.net/enterprise/remi-release-7.rpm
$ sudo yum-config-manager --enable remi-php73
$ sudo yum copr enable orrisroot/xoonips-support
$ sudo yum install xoonips-support
```

### CentOS 8
```
$ sudo dnf install epel-release
$ sudo dnf install dnf-plugins-core
$ sudo dnf config-manager --set-enabled PowerTools
$ sudo dnf install https://rpms.remirepo.net/enterprise/remi-release-8.rpm
$ sudo dnf module enable php:remi-7.3
$ sudo dnf copr enable orrisroot/xoonips-support
$ sudo dnf install xoonips-support
```

## Providing Packages
* xoonips-support : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips-support/package/xoonips-support/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips-support/package/xoonips-support/)
  * epel-7-x86_64
    * xoonips-support-0.0.1-1.el7.ors.noarch.rpm
    * xoonips-support-0.0.1-1.el7.ors.src.rpm
  * epel-8-x86_64
    * xoonips-support-0.0.1-1.el8.ors.noarch.rpm
    * xoonips-support-0.0.1-1.el8.ors.src.rpm
* xlhtml : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips-support/package/xlhtml/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips-support/package/xlhtml/)
  * epel-7-x86_64
    * xlhtml-0.5.1.p1-2.el7.ors.src.rpm
    * xlhtml-0.5.1.p1-2.el7.ors.x86_64.rpm
    * xlhtml-debuginfo-0.5.1.p1-2.el7.ors.x86_64.rpm
  * epel-8-x86_64
    * xlhtml-0.5.1.p1-2.el8.ors.src.rpm
    * xlhtml-0.5.1.p1-2.el8.ors.x86_64.rpm
    * xlhtml-debuginfo-0.5.1.p1-2.el8.ors.x86_64.rpm
    * xlhtml-debugsource-0.5.1.p1-2.el8.ors.x86_64.rpm	
* wv : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips-support/package/wv/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/xoonips-support/package/wv/)
  * epel-7-x86_64
    * wv-1.2.9-21.1.el7.ors.src.rpm
    * wv-1.2.9-21.1.el7.ors.x86_64.rpm
    * wv-debuginfo-1.2.9-21.1.el7.ors.x86_64.rpm
    * wv-devel-1.2.9-21.1.el7.ors.x86_64.rpm
  * epel-8-x86_64
    * wv-1.2.9-21.1.el8.ors.src.rpm
    * wv-1.2.9-21.1.el8.ors.x86_64.rpm
    * wv-debuginfo-1.2.9-21.1.el8.ors.x86_64.rpm
    * wv-debugsource-1.2.9-21.1.el8.ors.x86_64.rpm
    * wv-devel-1.2.9-21.1.el8.ors.x86_64.rpm
