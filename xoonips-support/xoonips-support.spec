Name:       xoonips-support
Version:    0.0.1
Release:    1%{?dist}.ors
Summary:    Meta-package for XooNIps
License:    MIT
BuildArch:  noarch

Requires:   epel-release, remi-release
Requires:   poppler-utils, elinks, wv, xlhtml
Requires:   php-common >= 7.3
Requires:   php-bcmath, php-cli, php-gd, php-intl, php-json, php-mbstring
Requires:   php-mysqlnd, php-opcache, php-pdo, php-pecl-apcu, php-soap
Requires:   php-process, php-xml, php-zip

%description
Meta-package for XooNIps

%prep

%build

%install

%files

%changelog
* Sun Apr 19 2020 Yoshihiro OKUMURA <orrisroot@gmail.com> - 0.0.1-1
- Rebuild for CentOS 7 and 8

