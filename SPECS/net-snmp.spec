%global package_speccommit 1cbf2cf791a16cd1453776f9e4aaba0924269439
%global usver 5.9.3
%global xsver 8
%global xsrel %{xsver}%{?xscount}%{?xshash}

# use nestnmp_check 0 to speed up packaging by disabling 'make test'
%{!?netsnmp_check: %global netsnmp_check 1}

# Arches on which we need to prevent arch conflicts on net-snmp-config.h
%global multilib_arches %{ix86} ia64 ppc ppc64 s390 s390x x86_64 sparc sparcv9 sparc64 aarch64

# actual soname version
%global soname  40

Summary:    A collection of SNMP protocol tools and libraries
Name:       net-snmp
Version:    5.9.3
Release:    %{?xsrel}.1%{?dist}
%if 0%{?xenserver} < 9
Epoch:      1
%global     epoch_str %{epoch}:
%endif

License:    BSD
URL:        http://net-snmp.sourceforge.net/
Source0: net-snmp-5.9.3.tar.gz
Source1: net-snmp.redhat.conf
Source2: net-snmp-config.h
Source3: net-snmp-config
Source4: net-snmp-trapd.redhat.conf
Source5: net-snmpd.sysconfig
Source6: net-snmptrapd.sysconfig
Source7: net-snmp-tmpfs.conf
Source8: snmpd.service
Source9: snmptrapd.service
Source10: IETF-MIB-LICENSE.txt
Source11: snmpd.xs.conf
Patch0: net-snmp-5.9-pie.patch
Patch1: net-snmp-5.9-dir-fix.patch
Patch2: net-snmp-5.9-multilib.patch
Patch3: net-snmp-5.9-test-debug.patch
Patch4: net-snmp-5.7.2-cert-path.patch
Patch5: net-snmp-5.9-cflags.patch
Patch6: net-snmp-5.8-Remove-U64-typedef.patch
Patch7: net-snmp-5.7.3-iterator-fix.patch
Patch8: net-snmp-5.9-autofs-skip.patch
Patch9: net-snmp-5.9-coverity.patch
Patch10: net-snmp-5.8-expand-SNMPCONFPATH.patch
Patch11: net-snmp-5.8-duplicate-ipAddress.patch
Patch12: net-snmp-5.9-memory-reporting.patch
Patch13: net-snmp-5.8-man-page.patch
Patch14: net-snmp-5.8-ipAddress-faster-load.patch
Patch15: net-snmp-5.8-rpm-memory-leak.patch
Patch16: net-snmp-5.9-aes-config.patch
Patch17: net-snmp-5.8-clientaddr-error-message.patch
Patch18: net-snmp-5.9-intermediate-certs.patch
Patch19: net-snmp-5.9.1-autoconf.patch
Patch20: net-snmp-libs-misunderstanding.patch
Patch21: net-snmp-5.8-modern-rpm-api.patch
Patch22: net-snmp-5.9-python3.patch

# XCP-ng patches
Source100: net-snmp-5.7.2-no-XENSERVER-MIB.xcp-ng.patch
Patch1001: net-snmp-5.7.2-CVE-2022-44793-1.patch
Patch1002: net-snmp-5.7.2-CVE-2022-44793-2.patch
Patch1003: net-snmp-5.7.2-CVE-2022-44793-3.patch

Requires:        %{name}-libs = %{?epoch_str}%{version}-%{release}
Requires:        %{name}-agent-libs = %{?epoch_str}%{version}-%{release}
# This is actually needed for the %%triggerun script but Requires(triggerun)
# is not valid.  We can use %%post because this particular %%triggerun script
# should fire just after this package is installed.
%{?systemd_requires}
BuildRequires:   make
BuildRequires:   systemd
BuildRequires:   gcc
BuildRequires:   openssl-devel, bzip2-devel, elfutils-devel
BuildRequires:   elfutils-libelf-devel, rpm-devel
BuildRequires:   procps
BuildRequires:   python3-devel, python3-setuptools
# needed by 'make test'
BuildRequires:   iproute
# for make test
BuildRequires:   lm_sensors-devel >= 3
BuildRequires:   autoconf, automake

%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management. The NET-SNMP project includes various SNMP tools:
an extensible agent, an SNMP library, tools for requesting or setting
information from SNMP agents, tools for generating and handling SNMP
traps, a version of the netstat command which uses SNMP, and a Tk/Perl
mib browser. This package contains the snmpd and snmptrapd daemons,
documentation, etc.

You will probably also want to install the net-snmp-utils package,
which contains NET-SNMP utilities.

%package utils
Summary:  Network management utilities using SNMP, from the NET-SNMP project
Requires: %{name}-libs = %{?epoch_str}%{version}-%{release}

%description utils
The net-snmp-utils package contains various utilities for use with the
NET-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol. You will also need to install the net-snmp
package.

%package devel
Summary:  The development environment for the NET-SNMP project
Requires: %{name}-libs = %{?epoch_str}%{version}-%{release}
Requires: %{name}-agent-libs = %{?epoch_str}%{version}-%{release}
Requires: elfutils-devel, rpm-devel, elfutils-libelf-devel, openssl-devel
%if 0%{?xenserver} < 9
Requires: redhat-rpm-config
%else
Requires: xenserver-config-rpm
%endif
Requires: lm_sensors-devel

%description devel
The net-snmp-devel package contains the development libraries and
header files for use with the NET-SNMP project's network management
tools.

Install the net-snmp-devel package if you would like to develop
applications for use with the NET-SNMP project's network management
tools. You'll also need to have the net-snmp and net-snmp-utils
packages installed.

%package libs
Summary: The NET-SNMP runtime client libraries

%description libs
The net-snmp-libs package contains the runtime client libraries for shared
binaries and applications.

%package agent-libs
Summary:   The NET-SNMP runtime agent libraries
# the libs link against libperl.so:
Requires:  %{name}-libs = %{?epoch_str}%{version}-%{release}

%description agent-libs
The net-snmp-agent-libs package contains the runtime agent libraries for shared
binaries and applications.

%package -n python3-net-snmp
%{?python_provide:%python_provide python3-net-snmp}
# Remove before F30
Provides:  %{name}-python = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:   The Python 'netsnmp' module for the Net-SNMP
Requires:  %{name}-libs = %{?epoch_str}%{version}-%{release}

%description -n python3-net-snmp
The 'netsnmp' module provides a full featured, tri-lingual SNMP (SNMPv3,
SNMPv2c, SNMPv1) client API. The 'netsnmp' module internals rely on the
Net-SNMP toolkit library.

%prep
%setup -q
cp %{SOURCE10} .
%autopatch -p1

# xs8 uses different version of autoconf
%if 0%{?xenserver} < 9
rm testing/fulltests/default/T000configure_simple
%endif

# disable failing test - see https://bugzilla.redhat.com/show_bug.cgi?id=680697
rm testing/fulltests/default/T200*

%build

# Autoreconf to get autoconf 2.69 for ARM (#926223)
autoreconf

MIBS="host agentx smux \
     ucd-snmp/diskio tcp-mib udp-mib mibII/mta_sendmail \
     ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
     ip-mib/ipAddressPrefixTable/ipAddressPrefixTable \
     ip-mib/ipDefaultRouterTable/ipDefaultRouterTable \
     ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
     sctp-mib rmon-mib etherlike-mib"

# there are no lm_sensors on s390
MIBS="$MIBS ucd-snmp/lmsensorsMib"

%configure \
    --disable-static --enable-shared \
    --enable-as-needed \
    --enable-blumenthal-aes \
    --disable-embedded-perl \
    --disable-perl-cc-checks \
    --enable-ipv6 \
    --enable-local-smux \
    --enable-mfd-rewrites \
    --enable-ucd-snmp-compatibility \
    --disable-manuals \
    --sysconfdir=%{_sysconfdir} \
    --with-cflags="$RPM_OPT_FLAGS -fPIE" \
    --with-ldflags="$RPM_LD_FLAGS -lm" \
    --with-logfile="/var/log/snmpd.log" \
    --with-mib-modules="$MIBS" \
    --without-mysql \
    --with-openssl \
    --with-persistent-directory="/var/lib/net-snmp" \
    --without-perl-modules \
    --with-pic \
    --with-security-modules=tsm  \
    --with-sys-location="Unknown" \
    --with-systemd \
    --with-temp-file-pattern=/run/net-snmp/snmp-tmp-XXXXXX \
    --with-transports="DTLSUDP TLSTCP" \
    --with-sys-contact="root@localhost" \
    --without-pcre <<EOF
EOF

# store original libtool file, we will need it later
cp libtool libtool.orig
# remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# the package is not %%_smp_mflags safe
%{__make}

# compile python module
pushd python
%{__python3} setup.py --basedir="../" build
popd


%install
make install DESTDIR=%{buildroot}

# Determine which arch net-snmp-config.h is going to try to #include.
basearch=%{_arch}
%ifarch %{ix86}
basearch=i386
%endif

%ifarch %{multilib_arches}
# Do an net-snmp-config.h switcheroo to avoid file conflicts on systems where you
# can have both a 32- and 64-bit version of the library, as they each need
# their own correct-but-different versions of net-snmp-config.h to be usable.
mv %{buildroot}/%{_bindir}/net-snmp-config %{buildroot}/%{_bindir}/net-snmp-config-${basearch}
install -m 755 %SOURCE3 %{buildroot}/%{_bindir}/net-snmp-config
mv %{buildroot}/%{_includedir}/net-snmp/net-snmp-config.h %{buildroot}/%{_includedir}/net-snmp/net-snmp-config-${basearch}.h
install -m644 %SOURCE2 %{buildroot}/%{_includedir}/net-snmp/net-snmp-config.h
%endif

install -d %{buildroot}%{_sysconfdir}/snmp
install -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/snmp/snmpd.conf.example
install -m 644 %SOURCE4 %{buildroot}%{_sysconfdir}/snmp/snmptrapd.conf

install -m 644 %SOURCE11 %{buildroot}%{_sysconfdir}/snmp/snmpd.xs.conf

install -d %{buildroot}%{_sysconfdir}/sysconfig

# XCP-ng: patch /etc/sysconfig/snmpd
cp %SOURCE7 net-snmpd.sysconfig
patch -p1 < %SOURCE100
install -m 644 net-snmpd.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/snmpd
rm -f net-snmpd.sysconfig

install -m 644 %SOURCE6 %{buildroot}%{_sysconfdir}/sysconfig/snmptrapd

# prepare /var/lib/net-snmp
install -d %{buildroot}%{_localstatedir}/lib/net-snmp
install -d %{buildroot}%{_localstatedir}/lib/net-snmp/mib_indexes
install -d %{buildroot}%{_localstatedir}/lib/net-snmp/cert_indexes
install -d %{buildroot}%{_localstatedir}/run/net-snmp

# remove things we don't want to distribute
rm -f %{buildroot}%{_bindir}/snmpinform
ln -s snmptrap %{buildroot}/usr/bin/snmpinform
rm -f %{buildroot}%{_bindir}/snmpcheck
rm -f %{buildroot}/%{_bindir}/fixproc
rm -f %{buildroot}/%{_mandir}/man1/fixproc*
rm -f %{buildroot}/%{_bindir}/ipf-mod.pl
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/libsnmp*

# remove special perl files
find %{buildroot} -name perllocal.pod \
    -o -name .packlist \
    -o -name "*.bs" \
    -o -name Makefile.subs.pl \
    | xargs -ri rm -f {}
# remove docs that do not apply to Linux
rm -f README.aix README.hpux11 README.osX README.Panasonic_AM3X.txt README.solaris README.win32

# install python module
pushd python
%{__python3} setup.py --basedir=.. install -O1 --skip-build --root %{buildroot}
popd

find %{buildroot} -name '*.so' | xargs chmod 0755

# trim down massive ChangeLog
dd bs=1024 count=250 if=ChangeLog of=ChangeLog.trimmed

# convert files to UTF-8
for file in README COPYING; do
    iconv -f 8859_1 -t UTF-8 <$file >$file.utf8
    mv $file.utf8 $file
done

# remove executable bit from documentation samples
chmod 644 local/passtest

# systemd stuff
install -m 755 -d %{buildroot}/%{_tmpfilesdir}
install -m 644 %SOURCE7 %{buildroot}/%{_tmpfilesdir}/net-snmp.conf
install -m 755 -d %{buildroot}/%{_unitdir}
install -m 644 %SOURCE8 %SOURCE9 %{buildroot}/%{_unitdir}/

# remove gui files
rm -rf %{buildroot}%{_bindir}/tkmib
rm -rf %{buildroot}%{_mandir}/man1/tkmib.1*

# remove perl files
rm -rf %{buildroot}%{_bindir}/mib2c-update
rm -rf %{buildroot}%{_bindir}/mib2c
rm -rf %{buildroot}%{_bindir}/snmp-bridge-mib
rm -rf %{buildroot}%{_bindir}/net-snmp-cert
rm -rf %{buildroot}%{_bindir}/checkbandwidth
rm -rf %{buildroot}%{_datadir}/snmp/mib2c*
rm -rf %{buildroot}%{_datadir}/snmp/*.pl
rm -rf %{buildroot}%{_bindir}/traptoemail
rm -rf %{buildroot}%{_mandir}/man[15]/mib2c*
rm -rf %{buildroot}%{_mandir}/man3/*
rm -rf %{buildroot}%{_mandir}/man1/traptoemail*.1*
rm -rf %{buildroot}%{_mandir}/man1/snmp-bridge-mib.1*
rm -rf %{buildroot}%{perl_vendorarch}/*SNMP*
rm -rf %{buildroot}%{perl_vendorarch}/auto/*SNMP*
rm -rf %{buildroot}%{perl_vendorarch}/auto/Bundle/*SNMP*
rm -rf %{buildroot}%{perl_vendorarch}/Bundle/MakefileSubs.pm
rm -rf %{buildroot}%{_bindir}/snmpconf

%check
%if %{netsnmp_check}
%ifarch ppc ppc64
rm -vf testing/fulltests/default/T200snmpv2cwalkall_simple
%endif
# restore libtool, for unknown reason it does not work with the one without rpath
cp -f libtool.orig libtool
# temporary workaround to make test "extending agent functionality with pass" working
chmod 755 local/passtest

LD_LIBRARY_PATH=%{buildroot}/%{_libdir} make test

%endif


%post
%systemd_post snmpd.service snmptrapd.service

%preun
%systemd_preun snmpd.service snmptrapd.service


%postun
%systemd_postun_with_restart snmpd.service snmptrapd.service

%ldconfig_scriptlets libs
%ldconfig_scriptlets agent-libs

%files
%dir %{_sysconfdir}/snmp
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/snmp/snmpd.conf.example
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/snmp/snmptrapd.conf
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/snmp/snmpd.xs.conf
%{_bindir}/net-snmp-create-v3-user
%{_sbindir}/*
%dir %{_datadir}/snmp
%{_datadir}/snmp/snmpconf-data
%dir %{_localstatedir}/run/net-snmp
%{_tmpfilesdir}/net-snmp.conf
%{_unitdir}/snmp*
%config(noreplace) %{_sysconfdir}/sysconfig/snmpd
%config(noreplace) %{_sysconfdir}/sysconfig/snmptrapd
%{_bindir}/agentxtrap

%files utils
%{_bindir}/encode_keychange
%{_bindir}/snmp[^c-]*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%attr(0755,root,root) %{_bindir}/net-snmp-config*

%files -n python3-net-snmp
%doc README
%{python3_sitearch}/*

%files libs
%doc COPYING README ChangeLog.trimmed FAQ NEWS TODO
%doc IETF-MIB-LICENSE.txt
%{_libdir}/libnetsnmp.so.%{soname}*
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/snmp/mibs/*
%dir %{_localstatedir}/lib/net-snmp
%dir %{_localstatedir}/lib/net-snmp/mib_indexes
%dir %{_localstatedir}/lib/net-snmp/cert_indexes

%files agent-libs
%{_libdir}/libnetsnmpagent*.so.%{soname}*
%{_libdir}/libnetsnmphelpers*.so.%{soname}*
%{_libdir}/libnetsnmpmibs*.so.%{soname}*
%{_libdir}/libnetsnmptrapd*.so.%{soname}*

%changelog
* Thu Jan 22 2026 Philippe Coval <philippe.coval@vates.tech> - 5.9.3-8.1
- Rebuild for openssl-3
- Remove obsolete net-snmp-5.7.2-CVE-2022-24806.patch
- Rebase on 5.9.3-8
- *** Upstream changelog ***
  * Mon Jan 20 2025 Deli Zhang <deli.zhang@cloud.com> - 5.9.3-8
  - CP-50295: Add epoch 1 for XS 8

  * Fri Jan 17 2025 Chunjie Zhu <chunjie.zhu@cloud.com> - 5.9.3-7
  - CP-53263: Remove net-tools

  * Fri Jan 17 2025 Stephen Cheng <stephen.cheng@cloud.com> - 5.9.3-6
  - CP-53229: Remove chrpath

  * Thu Nov 21 2024 Stephen Cheng <stephen.cheng@cloud.com> - 5.9.3-5
  - CP-50538 Remove perl related packages
  - CP-50538 Remove selinux from BuildRequires

  * Fri Aug 23 2024 Deli Zhang <deli.zhang@cloud.com> - 5.9.3-4
  - CP-44169: Add XenServer SNMP Agent so
  - CP-44170: Update default settings
  - CP-44429: Move snmpd.xs.conf from xenserver-release
  - CP-44429: Improve service config

  * Tue Jul 30 2024 Deli Zhang <deli.zhang@cloud.com> - 5.9.3-3
  - CP-50122: Revert perl-srpm-macros require

  * Fri Jul 26 2024 Deli Zhang <deli.zhang@cloud.com> - 5.9.3-2
  - CP-50122: Replace redhat-rpm-config with xenserver-config-rpm in XS9

  * Mon Sep 04 2023 Lin Liu <lin.liu@citrix.com> - 5.9.3-1
  - First imported release

* Tue Mar 04 2025 Samuel Verschelde <stormi-xcp@ylix.fr> - 5.7.2-52.1
- Rebase on 5.7.2-52
- Replace our patch by upstream identical one
- *** Upstream changelog ***
  * Wed Jul 31 2024 Deli Zhang <deli.zhang@cloud.com> - 5.7.2-52
  - CA-393002: Fix CVE-2022-24805 and CVE-2022-24809 issues

* Mon Aug 12 2024 Thierry Escande <thierry.escande@vates.tech> - 5.7.2-51.3
- Backport patches for CVE-2022-24805, CVE-2022-24806, CVE-2022-24807,
  CVE-2022-24808, CVE-2022-24809, CVE-2022-24810, and CVE-2022-44793

* Fri Jul 05 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 5.7.2-51.2
- Add net-snmp-5.7.2-no-XENSERVER-MIB.xcp-ng.patch
- Remove XenServer-specific options from /etc/sysconfig/snmpd

* Mon Jun 03 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 5.7.2-51.1
- Rebase on XS8's 5.7.2-51
- Undo most changes from snmp.xs.conf, which are related to a proprietary implementation

* Wed Oct 25 2023 Deli Zhang <deli.zhang@cloud.com> - 5.7.2-51
- CP-44170: Update default settings
- CP-44169: Add XenServer SNMP Agent so

* Tue Sep 12 2023 Deli Zhang <deli.zhang@cloud.com> - 5.7.2-50
- CP-44429: Move snmpd.xs.conf from xenserver-release
- CP-44429: Improve service config

* Tue Sep 05 2023 Deli Zhang <deli.zhang@cloud.com> - 5.7.2-49
- CP-44429: Import net-snmp 5.7.2-49
