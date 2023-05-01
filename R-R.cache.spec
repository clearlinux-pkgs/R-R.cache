#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R.cache
Version  : 0.16.0
Release  : 28
URL      : https://cran.r-project.org/src/contrib/R.cache_0.16.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/R.cache_0.16.0.tar.gz
Summary  : Fast and Light-Weight Caching (Memoization) of Objects and
Group    : Development/Tools
License  : LGPL-2.1
Requires: R-R.methodsS3
Requires: R-R.oo
Requires: R-R.utils
Requires: R-digest
BuildRequires : R-R.methodsS3
BuildRequires : R-R.oo
BuildRequires : R-R.utils
BuildRequires : R-digest
BuildRequires : buildreq-R

%description
This directory structure was created by the R package 'R.cache'
available on CRAN [https://cran.r-project.org/package=R.cache].
It holds cache files containing results memoized by various
R packages that utilize the R.cache package.  It is safe to
delete all or part of these files at any time.  By definition,
if memoized results are missing, they are recalculated by the
R package who needs them/created them in the first place.

%prep
%setup -q -c -n R.cache
cd %{_builddir}/R.cache

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658433153

%install
export SOURCE_DATE_EPOCH=1658433153
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.cache
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.cache
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.cache
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc R.cache || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R.cache/DESCRIPTION
/usr/lib64/R/library/R.cache/INDEX
/usr/lib64/R/library/R.cache/Meta/Rd.rds
/usr/lib64/R/library/R.cache/Meta/features.rds
/usr/lib64/R/library/R.cache/Meta/hsearch.rds
/usr/lib64/R/library/R.cache/Meta/links.rds
/usr/lib64/R/library/R.cache/Meta/nsInfo.rds
/usr/lib64/R/library/R.cache/Meta/package.rds
/usr/lib64/R/library/R.cache/NAMESPACE
/usr/lib64/R/library/R.cache/NEWS.md
/usr/lib64/R/library/R.cache/R/R.cache
/usr/lib64/R/library/R.cache/R/R.cache.rdb
/usr/lib64/R/library/R.cache/R/R.cache.rdx
/usr/lib64/R/library/R.cache/WORDLIST
/usr/lib64/R/library/R.cache/_Rcache/README.txt
/usr/lib64/R/library/R.cache/help/AnIndex
/usr/lib64/R/library/R.cache/help/R.cache.rdb
/usr/lib64/R/library/R.cache/help/R.cache.rdx
/usr/lib64/R/library/R.cache/help/aliases.rds
/usr/lib64/R/library/R.cache/help/paths.rds
/usr/lib64/R/library/R.cache/html/00Index.html
/usr/lib64/R/library/R.cache/html/R.css
/usr/lib64/R/library/R.cache/tests/DEPRECATED.R
/usr/lib64/R/library/R.cache/tests/Object.getChecksum.R
/usr/lib64/R/library/R.cache/tests/StaticMethodsAndNamespaces.R
/usr/lib64/R/library/R.cache/tests/addMemoization.R
/usr/lib64/R/library/R.cache/tests/assertDigest.R
/usr/lib64/R/library/R.cache/tests/clearCache.R
/usr/lib64/R/library/R.cache/tests/evalWithMemoization.R
/usr/lib64/R/library/R.cache/tests/findOSCachePath.R
/usr/lib64/R/library/R.cache/tests/getCachePath.R
/usr/lib64/R/library/R.cache/tests/getCacheRootPath.R
/usr/lib64/R/library/R.cache/tests/loadCache.R
/usr/lib64/R/library/R.cache/tests/memoizedCall.R
/usr/lib64/R/library/R.cache/tests/readCacheHeader.R
/usr/lib64/R/library/R.cache/tests/setCachePath.R
/usr/lib64/R/library/R.cache/tests/setCacheRootPath.R
/usr/lib64/R/library/R.cache/tests/textPrompt.R
