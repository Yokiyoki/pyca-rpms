%define pyca /
#%define perl_lib %{blocket}/lib/%(perl -MConfig -le 'print "$Config{package}/$Config{version}"')
%define cwd %(pwd)
%define branchid 1_20031118
#%define bpvschema bpv
#%define __spec_install_post /usr/lib/rpm/brp-compress
Summary: PyCA
Name: pyca
Version: 1

Release: 20031118
License: GPL2
Group: System Utilities
URL: http://www.pyca.de

BuildRoot: %{cwd}/dest/%{name}-root
BuildArch: noarch

Requires: openssl httpd python vixie-cron MTA

%description
Manage a CA with a web interface

%install
make DESTDIR=%{pyca} INSTALLROOT=$RPM_BUILD_ROOT%{pyca} install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config %{pyca}/etc/cron.hourly/pyca
%config %{pyca}/etc/httpd/conf.d/pyca
%config %{pyca}/etc/pyca/cacert_AuthCerts.cnf
%config %{pyca}/etc/pyca/cacert_CodeSigning.cnf
%config %{pyca}/etc/pyca/cacert_EmailCerts.cnf
%config %{pyca}/etc/pyca/cacert_Root.cnf
%config %{pyca}/etc/pyca/cacert_ServerCerts.cnf
%config %{pyca}/etc/pyca/openssl.cnf
%config %{pyca}/etc/pyca/ssl_server_csr.cnf
%{pyca}/usr/bin/ca2ldif.py
%{pyca}/usr/bin/certs2ldap.py
%{pyca}/usr/bin/copy-cacerts.py
%{pyca}/usr/bin/ldap2certs.py
%{pyca}/usr/bin/ns-jsconfig.py
%{pyca}/usr/bin/print-cacerts.py
%{pyca}/usr/sbin/ca-certreq-mail.py
%{pyca}/usr/sbin/ca-cycle-priv.py
%{pyca}/usr/sbin/ca-cycle-pub.py
%{pyca}/usr/sbin/ca-make.py
%{pyca}/usr/sbin/ca-revoke.py
%{pyca}/usr/sbin/pickle-cnf.py
%{pyca}/usr/share/pyca/browser-check.py
%{pyca}/usr/share/pyca/ca-index.py
%{pyca}/usr/share/pyca/cert-query.py
%{pyca}/usr/share/pyca/client-enroll.py
%{pyca}/usr/share/pyca/get-cert.py
%{pyca}/usr/share/pyca/ns-check-rev.py
%{pyca}/usr/share/pyca/ns-revoke.py
%{pyca}/usr/share/pyca/pycacnf.py
%{pyca}/usr/share/pyca/scep.py
%{pyca}/usr/share/pyca/view-cert.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/certhelper.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/cgiforms.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/cgihelper.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/cgissl.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/charset.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/htmlbase.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/ipadr.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/ldapbase.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/ldif.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/openssl/__init__.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/openssl/cert.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/openssl/cnf.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/openssl/db.py
%{pyca}/usr/lib/python2.4/site-packages/pycalib/vbs.py
%{pyca}/usr/share/doc/pyca/htdocs/changes.html
%{pyca}/usr/share/doc/pyca/htdocs/config.html
%{pyca}/usr/share/doc/pyca/htdocs/demo.html
%{pyca}/usr/share/doc/pyca/htdocs/download.html
%{pyca}/usr/share/doc/pyca/htdocs/faq.html
%{pyca}/usr/share/doc/pyca/htdocs/features.html
%{pyca}/usr/share/doc/pyca/htdocs/feedback.html
%{pyca}/usr/share/doc/pyca/htdocs/files.html
%{pyca}/usr/share/doc/pyca/htdocs/help/client-enroll.html.de
%{pyca}/usr/share/doc/pyca/htdocs/help/client-enroll.html.en
%{pyca}/usr/share/doc/pyca/htdocs/install.html
%{pyca}/usr/share/doc/pyca/htdocs/news.html
%{pyca}/usr/share/doc/pyca/htdocs/overview.html
%{pyca}/usr/share/doc/pyca/htdocs/pyca.html
%{pyca}/usr/share/doc/pyca/htdocs/related.html
%{pyca}/usr/share/doc/pyca/htdocs/roadmap.html
%{pyca}/usr/share/doc/pyca/htdocs/security.html
%{pyca}/usr/share/doc/pyca/htdocs/ssi/footer.html
%{pyca}/usr/share/doc/pyca/htdocs/ssi/head.html
%{pyca}/usr/share/doc/pyca/htdocs/ssi/navigation.html
