%define lang or
%define langrelease 1

Name: hunspell-or
Summary: Oriya hunspell dictionaries
Version: 0.03
Epoch:   1
Release: 1%{?dist}
Group:          Applications/Text
License:        GPLv2+
URL:            http://aspell.net/
Source0:        ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  aspell >= 12:0.60
BuildRequires:  hunspell-devel
Requires:       hunspell
BuildArch: noarch

%description
Oriya hunspell dictionaries.This package
contains the efforts of aspell-or that converted by
wordlist2hunspell.


%prep
%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}
prezip-bin -d < or.cwl > or.txt

iconv -f ISO-8859-1 -t UTF-8 Copyright > Copyright.utf8
mv Copyright.utf8 Copyright

%build
export LANG=or_IN.utf8
wordlist2hunspell or.txt or_IN


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING Copyright
%{_datadir}/myspell/*

%changelog
* Mon Mar 22 2010 Parag <pnemade AT redhat.com> - 1:0.03-1
- Resolves:rh#575666:-[or_IN] Update upstream source

* Fri Feb 19 2010 Parag <pnemade AT redhat.com> - 20050726-5
- Resolves: rh#566398: License tag doesn't matches the actual license.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20050726-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20050726-2
- Added Copyright

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20050726-1
- Initial Fedora release
