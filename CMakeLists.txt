

1.create file CMakeLists.txt
2.cmake ./  to create Makefile
3.make    to generate bin


//////////////CMakeLists.txt

cmake_minimum_required(VERSION 3.5)

project(lwm2mclient)

set(CMAKE_CXX_STANDARD 98)

add_definitions(-DLOG_DEBUG -DLWM2M_CLIENT)

set(SOURCES a.cpp  b.cpp  c.cpp)

add_executable(${PROJECT_NAME}  ${SOURCES} )
