Name:           eucalyptus-release
Version:        5
Release:        1%{?dist}
Summary:        Eucalyptus release files

License:        GPLv3
URL:            https://eucalyptus.cloud/

BuildArch:      noarch

Source0:       %{tarball_basedir}.tar.xz


%description
This package contains release files, such as yum configs and various
/etc files that define a Eucalyptus release.


%prep
%setup -q -n %{tarball_basedir}


%build
./configure \
    --with-rpm-repository-url=%{rpm_repo_url}


%install
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
cp -p eucalyptus.repo $RPM_BUILD_ROOT/etc/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp -p RPM-GPG-KEY-eucalyptus-release* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/


%files
/etc/pki/rpm-gpg/RPM-GPG-KEY-eucalyptus-release*
%config(noreplace) /etc/yum.repos.d/eucalyptus.repo


%changelog
* Tue Sep 11 2018 Steve Jones <steve.jones@appscale.com> - 5-1
- Updated for appscale eucalyptus 5.x

* Wed Feb 14 2018 Steve Jones <steve.jones@appscale.com> - 4.4-2
- Updated for appscale eucalyptus 4.4

* Tue Mar 07 2017 Garrett Holmstrom <gholms@hpe.com> - 4.4-1
- Updated for eucalyptus 4.4

* Tue Apr 26 2016 Garrett Holmstrom <gholms@hpe.com> - 4.3-1
- Updated for eucalyptus 4.3

* Fri Oct 16 2015 Eucalyptus Release Engineering <support@eucalyptus.com> - 4.2-1
- Updated for eucalyptus 4.2

* Wed Jan 21 2015 Eucalyptus Release Engineering <support@eucalyptus.com> - 4.1-1
- Updated for eucalyptus 4.1

* Thu May 22 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 4.0-1
- Recreated from scratch
