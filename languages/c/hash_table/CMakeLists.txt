cmake_minimum_required(VERSION 3.9)
project(hashtable)

set(CMAKE_CXX_STANDARD 11)

# set preprocessor flags
add_definitions(-DHASH_TABLE)
add_definitions(-DDEBUG)
# add_definitions(-DHT_DEBUG)

add_executable(hashtable
        hash/hash.c
        hash/hash.h
        hashtable/hashtable.c
        linked_list/d_linked_list.c
        linked_list/d_linked_list.h)
