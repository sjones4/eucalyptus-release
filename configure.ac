AC_INIT([eucalyptus-release], 4.1)
RPM_REPO_URL="${RPM_REPO_URL}"
AC_ARG_WITH(rpm-repository-url,
        [  --with-rpm-repository-url=<url>      where rpm packages are located],
        [RPM_REPO_URL="${withval}"])
if test x$RPM_REPO_URL = "x" ; then
    AC_MSG_ERROR([rpm-repository-url must be provided.])
fi
AC_CONFIG_FILES([eucalyptus.repo])
AC_SUBST(RPM_REPO_URL)
AC_OUTPUT
