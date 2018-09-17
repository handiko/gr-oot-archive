INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_IGATE igate)

FIND_PATH(
    IGATE_INCLUDE_DIRS
    NAMES igate/api.h
    HINTS $ENV{IGATE_DIR}/include
        ${PC_IGATE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    IGATE_LIBRARIES
    NAMES gnuradio-igate
    HINTS $ENV{IGATE_DIR}/lib
        ${PC_IGATE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(IGATE DEFAULT_MSG IGATE_LIBRARIES IGATE_INCLUDE_DIRS)
MARK_AS_ADVANCED(IGATE_LIBRARIES IGATE_INCLUDE_DIRS)

