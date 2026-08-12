# Copyright Contributors to the Open Shading Language project.
# SPDX-License-Identifier: BSD-3-Clause
# https://github.com/AcademySoftwareFoundation/OpenShadingLanguage

set ( oslc_srcs oslcmain.cpp )

# don't want to link oslexec but oslcomp uses these symbols
if (NOT BUILD_SHARED_LIBS)
    list (APPEND oslc_srcs
         ../liboslexec/oslexec.cpp
         ../liboslexec/typespec.cpp)
endif ()

add_executable ( oslc ${oslc_srcs} )
target_include_directories ( oslc  BEFORE PRIVATE ${OpenImageIO_INCLUDES})
target_link_libraries ( oslc PRIVATE oslcomp ${CMAKE_DL_LIBS})
install_targets (oslc)
add_custom_command(TARGET oslc POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        $<TARGET_RUNTIME_DLLS:oslc>
        $<TARGET_FILE_DIR:oslc>
    COMMAND_EXPAND_LISTS
)

# TARGET_RUNTIME_DLLS above only sees dependencies CMake knows about via the
# target graph. tbb12.dll and boost_thread are runtime deps buried inside
# OpenImageIO_Util.dll itself, invisible to that mechanism, so copy them
# explicitly using the root paths their own rez packages export.
if (WIN32 AND DEFINED ENV{TBB_ROOT})
    add_custom_command(TARGET oslc POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "$ENV{TBB_ROOT}/bin/tbb12.dll"
            $<TARGET_FILE_DIR:oslc>
    )
endif ()

if (WIN32 AND DEFINED ENV{BOOST_ROOT})
    file (GLOB _boost_thread_dll
          "$ENV{BOOST_ROOT}/lib/boost_thread-*.dll"
          "$ENV{BOOST_ROOT}/bin/boost_thread-*.dll")
    if (_boost_thread_dll)
        add_custom_command(TARGET oslc POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E copy_if_different
                ${_boost_thread_dll}
                $<TARGET_FILE_DIR:oslc>
        )
    endif ()
endif ()
