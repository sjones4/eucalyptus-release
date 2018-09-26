Name:           eucalyptus-release
Version:        4.1
Release:        2.el6
Summary:        Eucalyptus release files

License:        GPLv3
URL:            http://www.eucalyptus.com/

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
* Tue Sep 25 2018 Steve Jones <steve.jones@appscale.com> - 4.1-2
- Backport for eucalyptus 4.1

* Wed Jan 21 2015 Eucalyptus Release Engineering <support@eucalyptus.com> - 4.1-1
- Updated for eucalyptus 4.1

* Thu May 22 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 4.0-1
- Recreated from scratch
