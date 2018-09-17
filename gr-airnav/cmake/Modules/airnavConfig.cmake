INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_AIRNAV airnav)

FIND_PATH(
    AIRNAV_INCLUDE_DIRS
    NAMES airnav/api.h
    HINTS $ENV{AIRNAV_DIR}/include
        ${PC_AIRNAV_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    AIRNAV_LIBRARIES
    NAMES gnuradio-airnav
    HINTS $ENV{AIRNAV_DIR}/lib
        ${PC_AIRNAV_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(AIRNAV DEFAULT_MSG AIRNAV_LIBRARIES AIRNAV_INCLUDE_DIRS)
MARK_AS_ADVANCED(AIRNAV_LIBRARIES AIRNAV_INCLUDE_DIRS)

