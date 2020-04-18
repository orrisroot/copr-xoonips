Name:           xlhtml
Summary:        Excel 95/97 and PowerPoint to HTML converter
Version:        0.5.1.p1
Release:        2%{?dist}.ors

License:        GPLv2+
Group:          Applications/Text
Source0:        http://dl.sf.net/xoonips/xlhtml-%{version}.tar.gz
URL:            http://chicago.sourceforge.net/xlhtml/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The xlhtml program will take an Excel 95, or 97 file as input and
convert it to HTML. The output is via standard out so it can be
re-directed to files or piped to filters or used as a gateway to the
internet. pptHtml program converts PowerPoint files to HTML.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc xlhtml/contrib xlhtml/{README,THANKS,TODO,ChangeLog}
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Apr 18 2020 Yoshihiro OKUMURA <orrisroot@gmail.com> - 0.5.1.p1-2
- Rebuild for CentOS 7 and 8

* Thu Mar 12 2009 Yoshihiro OKUMURA <orrisroot@gmail.com> - 0.5.1.p1-1
- updated to upstream 0.5.1
- applied debian's 0.5.1-6 patches
- supported to build mingw32 msys environment
- assigned new version 0.5.1-p1 to these patched sources

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5-8
- Autorebuild for GCC 4.3

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.5-7
- fix license tag
- rebuild for BuildID

* Thu Aug 31 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.5-6
- rebuild

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.5-5
- rebuild for FC5

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.5-4
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Jun 25 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.5-0.fdr.2
- cleanup spec file

* Thu May 13 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.5-0.fdr.1
- initial Fedora RPM (from PLD)
