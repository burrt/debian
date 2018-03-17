/* hashtable.c -- Hash table implementation
 *
 * Hash table implementation with separate chaining with
 * linked lists using Paul Hsieh's hash function which
 * can be found here:
 *   http://www.azillionmonkeys.com/qed/hash.html
 *
 * I did this for fun so there's heaps of ways to improve this!
 * I'm open to any suggestions too.
 *
 * Author: Geoff <geoffchoy@outlook.com>
 *
 *
 * TODO:
 * - support open addressing option
 * - support singly linked list option
 * - use CMake or not
 * - agree on a C style...
 * - cleaner use of #ifdef
 * - better printing
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "../hash/hash.h"
#include "../linked_list/d_linked_list.h"


/*
 * Hash table sizes should account for load factor:
 *
 * L = n/k
 *
 * n = number of keys we want to hash
 * k = number of buckets/possible keys
 *
 * L ~ 0.75 generally ideal for O(1)
 *
 * To test for hash collisions - reduce hash table size
 * and increase the number of keys so L >> 1
 *
 */
#define HASHTABLE_CAPACITY 5


/* Hash table entry */
typedef struct entry {
    d_linked_list *llist;
} entry;

typedef struct hash_table {
    int num_values;
    int num_keys;
    entry **ht_array;
} hashtable;

typedef hashtable *hash_table;

/* Tuple for a key-value pair */
typedef struct tuple {
    char *key;
    int value;
} tuple;


hash_table hm_create()
{
    hash_table ht = (hash_table) malloc(sizeof(struct hash_table));
    assert(ht);

    ht->num_values = 0;
    ht->num_keys = 0;
    ht->ht_array = (entry **) malloc(sizeof(entry *) * HASHTABLE_CAPACITY);
    assert(ht->ht_array);
    for (int i = 0; i < HASHTABLE_CAPACITY; i++) {
        ht->ht_array[i] = (entry *) malloc(sizeof(entry));
        assert(ht->ht_array[i]);
    }
    return ht;
}

void hm_destroy(hash_table ht)
{
    for (int i = 0; i < HASHTABLE_CAPACITY; i++) {
        if (ht->ht_array[i]->llist != NULL) {
            ll_destroy(ht->ht_array[i]->llist);
        }
        free(ht->ht_array[i]);
    }
    free(ht);
}

/**
 * hm_get_index - Returns the index for indexing the hash table
 * @key: key string
 * @len: key length
 *
 */
int hm_get_index(char *key, int len)
{
    int hash_val = (int) super_fast_hash(key, len);
    hash_val = (hash_val < 0) ? -hash_val : hash_val;
    return hash_val % HASHTABLE_CAPACITY;
}

/**
 * hm_get_keys - Return all keys in the hash table
 * @values: array of pointers to point to the hash table keys
 *
 * Description:
 * Returns the values in the hash table via the array passed in.
 * Values are unordered and unsorted.
 */
void hm_get_keys(hash_table ht, char **keys)
{
    for (int i = 0, k = 0; i < HASHTABLE_CAPACITY && k < ht->num_keys; i++) {
        if (ht->ht_array[i]->llist != NULL) {
            dnode *curr = ht->ht_array[i]->llist->head;
            while (curr != NULL) {
                keys[k++] = curr->key;
                curr = curr->next;
            }
        }
    }
}

/**
 * hm_get_values - Return all values in the hash table
 * @values: array to store the hash table values
 *
 * Description:
 * Returns the values in the hash table via the array passed in.
 * Values are unordered and unsorted.
 */
void hm_get_values(hash_table ht, int *values)
{
    for (int i = 0, v = 0; i < HASHTABLE_CAPACITY && v < ht->num_values; i++) {
        if (ht->ht_array[i]->llist != NULL) {
            dnode *curr = ht->ht_array[i]->llist->head;
            while (curr != NULL) {
                values[v++] = curr->value;
                curr = curr->next;
            }
        }
    }
}

/**
 * hm_search_ky - Checks if a key exists in the hash table
 * @ht: hash table pointer
 * @search_key: key string to search for
 * @key_len: length of key string
 *
 */
int hm_search_key(hash_table ht, char *search_key, int key_len)
{
    int index = hm_get_index(search_key, key_len);
    if (ht->ht_array[index]->llist != NULL) {
        return (ll_search_key(ht->ht_array[index]->llist,
                              search_key,
                              key_len) != -1) ? 1 : 0;
    }
    return 0;
}

/**
 * hm_delete_key - Delete the key from the hash table
 * @ht: hash table pointer
 * @key: key string to delete
 * @key_len: length of key string
 *
 */
void hm_delete_key(hash_table ht, char *key, int key_len)
{
    int index = hm_get_index(key, key_len);
    if (ht->ht_array[index]->llist != NULL) {
        int i = ll_search_key(ht->ht_array[index]->llist,
                              key,
                              key_len);
        if (i != -1)
            ll_delete(&(ht->ht_array[index]->llist), i);
    }
}

/**
 * hm_insert - Insert a key-value into the hash table
 * @ht: hash table pointer
 * @key_value: tuple for key-value pair
 *
 * Description:
 * There are a few cases when inserting into the hash table:
 * - no hash collision
 * - hash collision (same index in hash table)
 *
 * No hash collision:
 * 1. if the key doesn't exist - insert (easy)
 * 2. if the key exists - replace its value
 *
 * Hash collision:
 * 1. if the key doesn't exist - append to the linked list (easy)
 * 2. if the key exists in the linked list - search and replace value
 */
int hm_insert(hash_table ht, tuple key_value)
{
    int key_len = sizeof(key_value.key);
    int index = hm_get_index(key_value.key, key_len);

    printf("New entry k: %s, data: %d\n", key_value.key, key_value.value);

    if (ht->ht_array[index]->llist != NULL) {
        int search_index = ll_search_key(ht->ht_array[index]->llist,
                                         key_value.key,
                                         key_len);
        if (search_index == -1) {
#ifdef HT_DEBUG
            printf("- hash collision - append to list\n\n");
#endif
            ll_append(&(ht->ht_array[index]->llist),
                      key_value.key,
                      key_len,
                      key_value.value);
            ht->num_keys++;
            ht->num_values++;
        } else {
#ifdef HT_DEBUG
            printf("- hash collision - replace existing key-value\n\n");
#endif
            ll_update(ht->ht_array[index]->llist,
                      search_index,
                      key_value.value);
        }
    } else {
        // no collision - create a new entry in the hash table
        // linked-list is empty
        d_linked_list *new_llist = ll_create();
        ll_append(&new_llist, key_value.key, key_len, key_value.value);
        ht->ht_array[index]->llist = new_llist;
        ht->num_keys++;
        ht->num_values++;
    }
    return index;
}

/**
 * hm_get_value - Return the value found at the key in the hash table
 * @ht: pointer to hash table
 * @key: string key
 * @key_len: key length
 * @found: check if key doesn't exist in hash table
 *
 */
int hm_get_value(hash_table ht, char *key, int key_len, int *found)
{
    int index = hm_get_index(key, key_len);
    int search_index = ll_search_key(ht->ht_array[index]->llist,
                                     key,
                                     key_len);
    if (search_index != -1) {
        dnode *curr = ht->ht_array[index]->llist->head;
        for (int i = 0; curr != NULL && i < search_index; i++) {
            curr = curr->next;
        }
        *found = 1;
        return curr->value;
    }
    *found = 0;
    return -1;
}

void print_hash_table(hash_table ht)
{
    for (int i = 0, k = 0; i < HASHTABLE_CAPACITY && k < ht->num_keys; i++) {
        if (ht->ht_array[i]->llist != NULL) {
            dnode *curr = ht->ht_array[i]->llist->head;
            for (int j = 0; curr != NULL; j++) {
                if (!j)
                    printf("[%s] = %d\n", curr->key, curr->value);
                else
                    printf(" --> [%s] = %d\n", curr->key, curr->value);
                curr = curr->next;
            }
        }
    }
}

void print_string_array(char **array, int array_len)
{
    int i = 0;
    printf("keys = [");
    for (; i < array_len - 1; i++) {
        printf("%s, ", array[i]);
    }
    printf("%s]\n", array[i]);
}

void print_int_array(int *array, int array_len)
{
    int i = 0;
    printf("values = [");
    for (; i < array_len - 1; i++) {
        printf("%d, ", array[i]);
    }
    printf("%d]\n", array[i]);
}

#ifdef HASH_TABLE
int main(int argc, char **argv)
{
    int i = 0;
    hash_table ht = hm_create();

    tuple key_values[] = {
            {"k1", 1},
            {"k2", 2},
            {"k3", 3},
            {"k4", 4},
            {"k5", 5},  /* test for duplicate keys */
            {"k5", 6},
            {"k6", 6},
            {"k7", 7}
    };
    int num_tuples = sizeof(key_values) / sizeof(key_values[0]);

    printf("\n-----------------------------------------------------------\n");
    printf("Inserting keys-values\n");
    printf("-----------------------------------------------------------\n");
    for (i = 0; i < num_tuples; i++) {
        hm_insert(ht, key_values[i]);
    }

    printf("\n-----------------------------------------------------------\n");
    printf("Getting keys - values from our input tuple array\n");
    printf("-----------------------------------------------------------\n");
    int found = 0;
    int data = 0;
    for (i = 0; i < num_tuples; i++) {
        data = hm_get_value(ht,
                            key_values[i].key,
                            sizeof(key_values[i].key),
                            &found);
        if (found)
            printf("Key: %s - Value: %d\n", key_values[i].key, data);
        else
            printf("Key: %s - Not found!\n", key_values[i].key);
    }

    printf("\n-----------------------------------------------------------\n");
    printf("Getting list of keys\n");
    printf("-----------------------------------------------------------\n");
    char *ht_keys[ht->num_keys];
    hm_get_keys(ht, ht_keys);
    print_string_array(ht_keys, ht->num_keys);

    printf("\n-----------------------------------------------------------\n");
    printf("Getting list of values\n");
    printf("-----------------------------------------------------------\n");
    int ht_values[ht->num_values];
    hm_get_values(ht, ht_values);
    print_int_array(ht_values, ht->num_values);

    printf("\n-----------------------------------------------------------\n");
    printf("Printing out hash table\n");
    printf("-----------------------------------------------------------\n");
    print_hash_table(ht);

    hm_destroy(ht);

    return 0;
}
#endif