cmake_minimum_required(VERSION 3.12)
# https://dominikberner.ch/cmake-interface-lib/

project(
    "cppy"
    VERSION 1.1.0
    HOMEPAGE_URL "https://github.com/nucleic/cppy")

set(libname "cppy")

add_library(${libname} INTERFACE)
# add alias so the project can be uses with add_subdirectory
add_library(${libname}::${libname} ALIAS ${libname})

include(GNUInstallDirs)

target_include_directories(
  ${libname}
  INTERFACE $<BUILD_INTERFACE:${${libname}_SOURCE_DIR}/lib>
            $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

target_compile_features(${libname} INTERFACE cxx_std_11)

install(TARGETS ${libname}
        EXPORT ${libname}_Targets
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    "${libname}ConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion)

configure_package_config_file(
  "${PROJECT_SOURCE_DIR}/cmake/${libname}Config.cmake.in"
  "${PROJECT_BINARY_DIR}/${libname}Config.cmake"
  INSTALL_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/${libname}/cmake)

install(EXPORT ${libname}_Targets
    FILE ${libname}Targets.cmake
    NAMESPACE ${libname}::
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${libname}/cmake)

install(FILES "${PROJECT_BINARY_DIR}/${libname}Config.cmake"
    "${PROJECT_BINARY_DIR}/${libname}ConfigVersion.cmake"
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${libname}/cmake)

install(DIRECTORY ${PROJECT_SOURCE_DIR}/cppy/include/cppy DESTINATION include)

set(CPACK_RESOURCE_FILE_LICENSE "${PROJECT_SOURCE_DIR}/LICENSE")

include(CPack)
