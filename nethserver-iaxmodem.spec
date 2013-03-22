Summary: NethServer module to configure IAX modems
Name: nethserver-iaxmodem
Version: @@VERSION@@
Release: @@RELEASE@@
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Packager: Giacomo Sanchietti <giacomo.sanchietti@nethesis.it>
BuildArch: noarch
Requires: iaxmodem
Requires: nethserver-hylafax
BuildRequires: nethserver-devtools
AutoReq: no

%description
NethServer module to configure IAX modems


%prep
%setup

%pre

%post
source /etc/nethserver/rpm_hook_functions
event_queue add %{name}-update

%preun
source /etc/nethserver/rpm_hook_functions
signal_event  %{name}-uninstall $1

%postun

%build
perl createlinks

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist  $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(0644,root,root)

%changelog
