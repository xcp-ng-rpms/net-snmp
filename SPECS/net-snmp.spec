%global package_speccommit b6ea450d730666c343f0f5485a2eb258dc842129
%global usver 5.7.2
%global xsver 52
%global xsrel %{xsver}%{?xscount}%{?xshash}

# use nestnmp_check 0 to speed up packaging by disabling 'make test'
%{!?netsnmp_check: %global netsnmp_check 1}

Summary: A collection of SNMP protocol tools and libraries
Name: net-snmp
Version: 5.7.2
Release: %{?xsrel}%{?dist}
Epoch: 1
License: BSD
Group: System Environment/Daemons
URL: http://net-snmp.sourceforge.net/

Source0: net-snmp-5.7.2-noapsl.tar.gz
Source1: net-snmp.redhat.conf
Source2: net-snmpd.init
Source3: net-snmptrapd.init
Source4: net-snmp-config.h
Source5: net-snmp-config
Source6: net-snmp-trapd.redhat.conf
Source7: net-snmpd.sysconfig
Source8: net-snmptrapd.sysconfig
Source9: net-snmp-tmpfs.conf
Source10: snmpd.service
Source11: snmptrapd.service
Source12: snmpd.xs.conf
Patch0: net-snmp-5.5-dir-fix.patch
Patch1: net-snmp-5.6-multilib.patch
Patch2: net-snmp-5.6-test-debug.patch
Patch3: net-snmp-5.7.2-systemd.patch
Patch4: net-snmp-5.7.2-fips.patch
Patch5: net-snmp-5.7-skip-ipv6-tests.patch
Patch6: net-snmp-5.7-relro.patch
Patch7: net-snmp-5.7-smux-reqid.patch
Patch8: net-snmp-5.7-agentx-crash.patch
Patch9: net-snmp-5.7.2-exec-cmdline.patch
Patch10: net-snmp-5.7.2-clientaddr-port.patch
Patch11: net-snmp-5.5-getnext-loop.patch
Patch12: net-snmp-5.7-dsktable-cache.patch
Patch13: net-snmp-5.7.2-python-ipaddress-size.patch
Patch14: net-snmp-5.7.2-create-user-multilib.patch
Patch15: net-snmp-5.5-extend-realloc-leak.patch
Patch16: net-snmp-5.5-man-config-path.patch
Patch17: net-snmp-5.7.2-kernel-threads.patch
Patch18: net-snmp-5.7.2-agentx-disconnect-crash.patch
Patch19: net-snmp-5.7.2-dskTable-dynamic.patch
Patch20: net-snmp-5.5-extTable-crash.patch
Patch21: net-snmp-5.7.2-dot3stats-log.patch
Patch22: net-snmp-5.7.2-soname.patch
Patch23: net-snmp-5.5-ber-int-size.patch
Patch24: net-snmp-5.5-ber-int-size2.patch
Patch25: net-snmp-5.7.2-hrStorage-fs.patch
Patch26: net-snmp-5.7.2-btrfs.patch
Patch27: net-snmp-5.7.2-trigger-crash.patch
Patch28: net-snmp-5.5-python-retcodes.patch
Patch29: net-snmp-5.7.2-icmp-mib.patch
Patch30: net-snmp-5.7.2-ipCidrRouteTable-duplicates.patch
Patch31: net-snmp-5.7.2-hrProcessorLoad-many-cpus.patch
Patch32: net-snmp-5.5-mvfs.patch
Patch33: net-snmp-5.7.2-clientaddr-error-msg.patch
Patch34: net-snmp-5.7.2-proxy-getnext.patch
Patch35: net-snmp-5.7.2-extend-reload.patch
Patch36: net-snmp-5.7.2-trap-vartypes.patch
Patch37: net-snmp-5.5-storageUseNFS.patch
Patch38: net-snmp-5.5-trap-forward-reqid.patch
Patch39: net-snmp-5.5-hrStorage-31bits.patch
Patch40: net-snmp-5.7.2-udp6-clientaddr.patch
Patch41: net-snmp-5.7.2-smux-logging.patch
Patch42: net-snmp-5.7.2-udpTable-index.patch
Patch43: net-snmp-5.7.2-client-write-var.patch
Patch44: net-snmp-5.7.2-smux-invalid-headers.patch
Patch45: net-snmp-5.7.2-diskio-whitelist.patch
Patch46: net-snmp-5.7.2-systemstats-ipv4.patch
Patch47: net-snmp-5.7.2-incomplete-parse.patch
Patch48: net-snmp-5.7.2-hrFSTable-read-write.patch
Patch49: net-snmp-5.5-sensors-duplicate.patch
Patch50: net-snmp-5.7.2-extend-close.patch
Patch51: net-snmp-5.7.2-python-addr-size.patch
Patch52: net-snmp-5.7.2-dot3-leak.patch
Patch53: net-snmp-5.7.2-max-msg-size.patch
Patch54: net-snmp-5.7.2-response-too-long.patch
Patch55: net-snmp-5.7.2-agentx-disconnect-crash-part2.patch
Patch56: net-snmp-5.7.2-client-udp6.patch
Patch57: net-snmp-5.7.2-ipAddress-faster-load.patch
Patch58: net-snmp-5.7.2-large-fdset.patch
Patch59: net-snmp-5.7.2-duplicate-ipAddress.patch
Patch60: net-snmp-5.5-SCTP-parser.patch
Patch61: net-snmp-5.7.2-strstr.patch
Patch62: net-snmp-5.7.2-documentation.patch
Patch63: net-snmp-5.7.2-iterator-fix.patch
Patch64: net-snmp-5.7.2-autofs.patch
Patch65: net-snmp-5.7.2-leak-backport.patch
Patch66: net-snmp-5.7.2-acfs.patch
Patch67: net-snmp-5.7.2-fsync.patch
Patch68: net-snmp-5.7.2-zfs-support.patch
Patch69: net-snmp-5.7.2-man-page.patch
Patch70: net-snmp-5.7.2-key-leak-backport.patch
Patch71: net-snmp-5.7.2-snmpd-log-once.patch
Patch72: net-snmp-5.7.2-MYSQL-LIBS.patch
Patch73: net-snmp-5.7.2-expand-SNMPCONFPATH.patch
Patch74: net-snmp-5.7.2-traptomail.patch
Patch75: net-snmp-5.7.2-null-magic.patch
Patch76: net-snmp-5.7.2-v3-forward.patch
Patch77: net-snmp-5.7.2-memory.patch
Patch78: net-snmp-5.7.2-glusterfs.patch
Patch79: net-snmp-5.7.2-ifTable-interface_fadeout.patch
Patch80: net-snmp-5.7.2-icmp.patch
Patch81: net-snmp-5.7.2-pass_common.patch
Patch82: net-snmp-5.7.2-CVE-2018-18066.patch
Patch83: net-snmp-5.7.2-counter64.patch
Patch84: net-snmp-5.7.2-SHA-fix.patch
Patch85: net-snmp-5.7.2-sec-counter.patch
Patch86: net-snmp-5.7.2-memory-leak.patch
Patch87: net-snmp-5.7.2-flood-messages.patch
Patch88: net-snmp-5.7.2-proc-whitespace.patch
Patch89: net-snmp-5.7.2-CVE-2020-15862.patch
Patch90: net-snmp-5.7.2-bulk.patch
Patch91: 0001-CHANGES-snmpd-fix-bounds-checking-in-NET-SNMP-AGENT-.patch

Requires(post): chkconfig
Requires(preun): chkconfig
# for /sbin/service
Requires(preun): initscripts
# for /bin/rm
Requires(preun): coreutils
Requires: %{name}-libs = %{epoch}:%{version}-%{release}
Requires: %{name}-agent-libs = %{epoch}:%{version}-%{release}
Requires: mysql-libs

BuildRequires: openssl-devel, bzip2-devel, elfutils-devel
BuildRequires: libselinux-devel, elfutils-libelf-devel, rpm-devel
BuildRequires: perl-devel, perl(ExtUtils::Embed), gawk, procps
BuildRequires: python-devel, python-setuptools
BuildRequires: chrpath
BuildRequires: mysql-devel
# for netstat, needed by 'make test'
BuildRequires: net-tools
# for make test
BuildRequires: perl(TAP::Harness)
BuildRequires: systemd-units
%{?_cov_buildrequires}


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
Group: Applications/System
Summary: Network management utilities using SNMP, from the NET-SNMP project
Requires: %{name}-libs = %{epoch}:%{version}-%{release}

%description utils
The net-snmp-utils package contains various utilities for use with the
NET-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol. You will also need to install the net-snmp
package.

%package devel
Group: Development/Libraries
Summary: The development environment for the NET-SNMP project
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-libs = %{epoch}:%{version}-%{release}
Requires: %{name}-agent-libs = %{epoch}:%{version}-%{release}
Requires: elfutils-devel, rpm-devel, elfutils-libelf-devel, openssl-devel
# pull perl development libraries, net-snmp agent libraries may link to them
Requires: perl-devel%{?_isa}

%description devel
The net-snmp-devel package contains the development libraries and
header files for use with the NET-SNMP project's network management
tools.

Install the net-snmp-devel package if you would like to develop
applications for use with the NET-SNMP project's network management
tools. You'll also need to have the net-snmp and net-snmp-utils
packages installed.

%package perl
Group: Development/Libraries
Summary: The perl NET-SNMP module and the mib2c tool
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-libs = %{epoch}:%{version}-%{release}, perl
Requires: %{name}-agent-libs = %{epoch}:%{version}-%{release}
Requires: %{name}-devel = %{epoch}:%{version}-%{release}
BuildRequires: perl

%description perl
The net-snmp-perl package contains the perl files to use SNMP from within
Perl.

Install the net-snmp-perl package, if you want to use mib2c or SNMP
with perl.

%package gui
Group: Applications/System
Summary: An interactive graphical MIB browser for SNMP
Requires: perl-Tk, net-snmp-perl = %{epoch}:%{version}-%{release}

%description gui
The net-snmp-gui package contains tkmib utility, which is a graphical user
interface for browsing the Message Information Bases (MIBs). It is also
capable of sending or retrieving the SNMP management information to/from
the remote agents interactively.

Install the net-snmp-gui package, if you want to use this interactive utility.

%package libs
Group: Development/Libraries
Summary: The NET-SNMP runtime client libraries

%description libs
The net-snmp-libs package contains the runtime client libraries for shared
binaries and applications.

%package agent-libs
Group: Development/Libraries
Summary: The NET-SNMP runtime agent libraries
# the libs link against libperl.so:
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: %{name}-libs = %{epoch}:%{version}-%{release}

%description agent-libs
The net-snmp-agent-libs package contains the runtime agent libraries for shared
binaries and applications.

%package python
Group: Development/Libraries
Summary: The Python 'netsnmp' module for the Net-SNMP
Requires: %{name}-libs = %{epoch}:%{version}-%{release}

%description python
The 'netsnmp' module provides a full featured, tri-lingual SNMP (SNMPv3,
SNMPv2c, SNMPv1) client API. The 'netsnmp' module internals rely on the
Net-SNMP toolkit library.

%package sysvinit
Group: System Environment/Daemons
Summary: Legacy SysV init scripts for Net-SNMP daemons
Requires: %{name} = %{epoch}:%{version}-%{release}

%description sysvinit
The net-snmp-sysvinit package provides SysV init scripts for Net-SNMP daemons.


%prep
%autosetup -p1 -n %{name}-%{version}
%{?_cov_prepare}

%build
MIBS="host agentx smux \
     ucd-snmp/diskio tcp-mib udp-mib mibII/mta_sendmail \
     ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
     ip-mib/ipAddressPrefixTable/ipAddressPrefixTable \
     ip-mib/ipDefaultRouterTable/ipDefaultRouterTable \
     ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
     sctp-mib rmon-mib etherlike-mib"

%configure \
    --disable-static --enable-shared \
    --with-cflags="$RPM_OPT_FLAGS -D_RPM_4_4_COMPAT" \
    --with-ldflags="-Wl,-z,relro -Wl,-z,now" \
    --with-sys-location="Unknown" \
    --with-logfile="/var/log/snmpd.log" \
    --with-persistent-directory="/var/lib/net-snmp" \
    --with-mib-modules="$MIBS" \
    --sysconfdir=%{_sysconfdir} \
    --enable-ipv6 \
    --enable-ucd-snmp-compatibility \
    --with-openssl \
    --with-pic \
    --enable-embedded-perl \
    --enable-as-needed \
    --with-perl-modules="INSTALLDIRS=vendor" \
    --enable-mfd-rewrites \
    --enable-local-smux \
    --with-temp-file-pattern=/var/run/net-snmp/snmp-tmp-XXXXXX \
    --with-transports="DTLSUDP TLSTCP" \
    --with-security-modules=tsm  \
    --with-mysql \
    --with-systemd \
    --with-sys-contact="root@localhost" <<EOF
EOF

# store original libtool file, we will need it later
cp libtool libtool.orig
# remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# the package is not %%_smp_mflags safe
%{?_cov_wrap} make

# remove rpath from compiled perl libs
find perl/blib -type f -name "*.so" -print -exec chrpath --delete {} \;

# compile python module
pushd python
%{__python2} setup.py --basedir="../" build
popd


%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp
install -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp/snmpd.conf.example
install -m 644 %SOURCE6 ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp/snmptrapd.conf

install -m 644 %SOURCE12 ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp/snmpd.xs.conf

install -d ${RPM_BUILD_ROOT}%{_initrddir}
install -m 755 %SOURCE2 ${RPM_BUILD_ROOT}%{_initrddir}/snmpd
install -m 755 %SOURCE3 ${RPM_BUILD_ROOT}%{_initrddir}/snmptrapd

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -m 644 %SOURCE7 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/snmpd
install -m 644 %SOURCE8 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/snmptrapd

# prepare /var/lib/net-snmp
install -d ${RPM_BUILD_ROOT}%{_localstatedir}/lib/net-snmp
install -d ${RPM_BUILD_ROOT}%{_localstatedir}/lib/net-snmp/mib_indexes
install -d ${RPM_BUILD_ROOT}%{_localstatedir}/lib/net-snmp/cert_indexes
install -d ${RPM_BUILD_ROOT}%{_localstatedir}/run/net-snmp

# remove things we don't want to distribute
rm -f ${RPM_BUILD_ROOT}%{_bindir}/snmpinform
ln -s snmptrap ${RPM_BUILD_ROOT}/usr/bin/snmpinform
rm -f ${RPM_BUILD_ROOT}%{_bindir}/snmpcheck
rm -f ${RPM_BUILD_ROOT}/%{_bindir}/fixproc
rm -f ${RPM_BUILD_ROOT}/%{_mandir}/man1/fixproc*
rm -f ${RPM_BUILD_ROOT}/%{_bindir}/ipf-mod.pl
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.la
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/libsnmp*

# remove special perl files
find $RPM_BUILD_ROOT -name perllocal.pod \
    -o -name .packlist \
    -o -name "*.bs" \
    -o -name Makefile.subs.pl \
    | xargs -ri rm -f {}
# remove docs that do not apply to Linux
rm -f README.aix README.hpux11 README.osX README.Panasonic_AM3X.txt README.solaris README.win32

# copy missing mib2c.conf files
install -m 644 local/mib2c.*.conf ${RPM_BUILD_ROOT}%{_datadir}/snmp

# install python module
pushd python
%{__python2} setup.py --basedir=.. install -O1 --skip-build --root $RPM_BUILD_ROOT
popd

find $RPM_BUILD_ROOT -name '*.so' | xargs chmod 0755

# trim down massive ChangeLog
dd bs=1024 count=250 if=ChangeLog of=ChangeLog.trimmed

# convert files to UTF-8
for file in README COPYING; do
    iconv -f 8859_1 -t UTF-8 <$file >$file.utf8
    mv $file.utf8 $file
done

# remove executable bit from documentation samples
chmod 644 local/passtest local/ipf-mod.pl

# dirty hack for #603243, until it's fixed properly upstream
install -m 755 -d $RPM_BUILD_ROOT/usr/include/net-snmp/agent/util_funcs
install -m 644  agent/mibgroup/util_funcs/*.h $RPM_BUILD_ROOT/usr/include/net-snmp/agent/util_funcs

# systemd stuff
install -m 755 -d $RPM_BUILD_ROOT/%{_tmpfilesdir}
install -m 644 %SOURCE9 $RPM_BUILD_ROOT/%{_tmpfilesdir}/net-snmp.conf
install -m 755 -d $RPM_BUILD_ROOT/%{_unitdir}
install -m 644 %SOURCE10 %SOURCE11 $RPM_BUILD_ROOT/%{_unitdir}/

%{?_cov_install}


%check
%if %{netsnmp_check}
# restore libtool, for unknown reason it does not work with the one without rpath
cp -f libtool.orig libtool
# temporary workaround to make test "extending agent functionality with pass" working
chmod 755 local/passtest

LD_LIBRARY_PATH=${RPM_BUILD_ROOT}/%{_libdir} make test
%endif


%post
%systemd_post snmpd.service snmptrapd.service

%preun
%systemd_preun snmpd.service snmptrapd.service

%postun
%systemd_postun_with_restart snmpd.service snmptrapd.service

%posttrans
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post agent-libs -p /sbin/ldconfig

%postun agent-libs -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%doc COPYING ChangeLog.trimmed EXAMPLE.conf FAQ NEWS TODO
%doc README README.agent-mibs README.agentx README.krb5 README.snmpv3
%doc local/passtest local/ipf-mod.pl
%doc README.thread AGENT.txt PORTING local/README.mib2c
%dir %{_sysconfdir}/snmp
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/snmp/snmpd.conf.example
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/snmp/snmptrapd.conf
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/snmp/snmpd.xs.conf
%{_bindir}/snmpconf
%{_bindir}/agentxtrap
%{_bindir}/net-snmp-create-v3-user
%{_sbindir}/*
%attr(0644,root,root) %{_mandir}/man[58]/snmp*d*
%attr(0644,root,root) %{_mandir}/man5/snmp_config.5.gz
%attr(0644,root,root) %{_mandir}/man5/variables*
%attr(0644,root,root) %{_mandir}/man1/net-snmp-create-v3-user*
%attr(0644,root,root) %{_mandir}/man1/snmpconf.1.gz
%dir %{_datadir}/snmp
%{_datadir}/snmp/snmpconf-data
%dir %{_localstatedir}/run/net-snmp
%{_tmpfilesdir}/net-snmp.conf
%{_unitdir}/snmp*
%config(noreplace) %{_sysconfdir}/sysconfig/snmpd
%config(noreplace) %{_sysconfdir}/sysconfig/snmptrapd

%files utils
%{_bindir}/encode_keychange
%{_bindir}/snmp[^c-]*
%attr(0644,root,root) %{_mandir}/man1/snmp[^-]*.1*
%attr(0644,root,root) %{_mandir}/man1/encode_keychange*.1*
%attr(0644,root,root) %{_mandir}/man1/agentxtrap.1*
%attr(0644,root,root) %{_mandir}/man5/snmp.conf.5.gz
%attr(0644,root,root) %{_mandir}/man5/variables.5.gz

%files devel
%{_libdir}/lib*.so
/usr/include/*
%attr(0644,root,root) %{_mandir}/man3/*.3.*
%attr(0755,root,root) %{_bindir}/net-snmp-config*
%attr(0644,root,root) %{_mandir}/man1/net-snmp-config*.1.*

%files perl
%{_bindir}/mib2c-update
%{_bindir}/mib2c
%{_bindir}/snmp-bridge-mib
%{_bindir}/net-snmp-cert
%dir %{_datadir}/snmp
%{_datadir}/snmp/mib2c*
%{_datadir}/snmp/*.pl
%{_bindir}/traptoemail
%attr(0644,root,root) %{_mandir}/man[15]/mib2c*
%attr(0644,root,root) %{_mandir}/man3/*.3pm.*
%attr(0644,root,root) %{_mandir}/man1/traptoemail*.1*
%attr(0644,root,root) %{_mandir}/man1/snmp-bridge-mib.1*
%{perl_vendorarch}/*SNMP*
%{perl_vendorarch}/auto/*SNMP*
%{perl_vendorarch}/auto/Bundle/*SNMP*

%files python
%doc python/README
%{python2_sitearch}/*

%files gui
%{_bindir}/tkmib
%attr(0644,root,root) %{_mandir}/man1/tkmib.1*

%files libs
%doc COPYING README ChangeLog.trimmed FAQ NEWS TODO
%{_libdir}/libnetsnmp.so.*
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/snmp/mibs/*
%dir %{_localstatedir}/lib/net-snmp
%dir %{_localstatedir}/lib/net-snmp/mib_indexes
%dir %{_localstatedir}/lib/net-snmp/cert_indexes

%files agent-libs
%{_libdir}/libnetsnmpagent*.so.*
%{_libdir}/libnetsnmphelpers*.so.*
%{_libdir}/libnetsnmpmibs*.so.*
%{_libdir}/libnetsnmptrapd*.so.*

%files sysvinit
%{_initrddir}/snmpd
%{_initrddir}/snmptrapd


%{?_cov_results_package}


%changelog
* Wed Jul 31 2024 Deli Zhang <deli.zhang@cloud.com> - 5.7.2-52
- CA-393002: Fix CVE-2022-24805 and CVE-2022-24809 issues

* Wed Oct 25 2023 Deli Zhang <deli.zhang@cloud.com> - 5.7.2-51
- CP-44170: Update default settings
- CP-44169: Add XenServer SNMP Agent so

* Tue Sep 12 2023 Deli Zhang <deli.zhang@cloud.com> - 5.7.2-50
- CP-44429: Move snmpd.xs.conf from xenserver-release
- CP-44429: Improve service config

* Tue Sep 05 2023 Deli Zhang <deli.zhang@cloud.com> - 5.7.2-49
- CP-44429: Import net-snmp 5.7.2-49
