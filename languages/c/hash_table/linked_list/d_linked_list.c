/* d_linked_list.c -- Doubly linked list
 * A simple implementation of a doubly linked list in C.
 * Actually, some extra features were implemented to support
 * the hash table I also implemented e.g. tuples
 *
 * Actually, now that I've implemented in C, I really want to
 * do this in Java since the OO with sub-classing, method overriding
 * and inheritance is almost essential...
 *
 * Author: Geoff <geoffchoy@outlook.com>
 *
 * TODO:
 * - find a better way without all these horrible #ifdef
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "d_linked_list.h"

d_linked_list *ll_create()
{
    d_linked_list *linked_list = (d_linked_list *)malloc(sizeof(d_linked_list));
    assert(linked_list);
    linked_list->size = 0;
    return linked_list;
}

void ll_destroy(d_linked_list *llist)
{
    dnode *curr = llist->head;
    dnode *prev = curr;
    while (curr != NULL) {
        curr = curr->next;
        free(prev);
        prev = curr;
    }
}

dnode *ll_create_node(char *key, int key_len, int value)
{
    dnode *new_node = (dnode *)malloc(sizeof(dnode));
    assert(new_node);
    new_node->value = value;
    new_node->key = (char *)malloc(sizeof(char)*key_len);
    assert(new_node->key);
    if (key)
        strncpy(new_node->key, key, (size_t) key_len);
    return new_node;
}

/**
 * ll_append: Appends item to the tail of the linked list
 * @llist: doubly linked list pointer
 * @key: key string
 * @key_len: key string length
 * @val: value of item
 *
 */
void ll_append(d_linked_list **llist, char *key, int key_len, int val)
{
    dnode *new_node = ll_create_node(key, key_len, val);
    (*llist)->size++;

    dnode *curr = (*llist)->tail;
    if (curr == NULL) {
        /* check if list is empty */
        new_node->prev = NULL;
        new_node->next = NULL;
        (*llist)->head = new_node;
        (*llist)->tail = new_node;
#if defined(LL_DEBUG) || !defined(HASH_TABLE)
        printf("Empty list\nHead: %d\n", new_node->value);
#endif
    } else {
        /* append current node to end of linked list */
        new_node->next = NULL;
        new_node->prev = (*llist)->tail;
        (*llist)->tail->next = new_node;
        (*llist)->tail = new_node;
#if defined(LL_DEBUG) || !defined(HASH_TABLE)
        printf("Appended new node: %d\n", new_node->value);
#endif
    }
}

/**
 * ll_insert - Inserts item at the specified index into the linked list
 * @llist: doubly linked list pointer
 * @index: index at which to insert item
 * @key: key string
 * @key_len: key string length
 * @param val: value of item
 *
 * Desciption:
 * The key-value pair is an extension for the hash table.
 * To ignore it, simply use (NULL, 0)
 */
void ll_insert(d_linked_list **llist, int index, char *key, int key_len, int val)
{
    dnode *new_node = ll_create_node(key, key_len, val);
    dnode *curr = (*llist)->head;
    int i = 1;
    for (; curr != NULL && curr->next != NULL && i < index; i++) {
        curr = curr->next;
    }

    if (index > (*llist)->size) {
        free(new_node);
    } else if (curr == NULL) {
        /* check if we have an empty list */
        new_node->next = NULL;
        new_node->prev = NULL;
        (*llist)->head = new_node;
        (*llist)->tail = new_node;
        (*llist)->size++;
    } else if (curr->next == NULL) {
        /* check if llist->size == 1 or at tail */
        curr->next = new_node;
        new_node->prev = curr;
        new_node->next = NULL;
        (*llist)->tail = new_node;
        (*llist)->size++;
    } else {
#if defined(LL_DEBUG) || !defined(HASH_TABLE)
        printf("Inserting at index: %d, val: %d\n"
               " -> between (i: %d, val: %d) - (i: %d, val: %d)\n",
               index, val, i-1, curr->value, i, curr->next->value);
#endif
        dnode *old_next = curr->next;
        curr->next = new_node;
        new_node->prev = curr;
        new_node->next = old_next;
        old_next->prev = new_node;
        (*llist)->size++;
    }
}

/**
 * ll_update - Update the item value of a node in the linked list
 * @llist: doubly linked list pointer
 * @index: index of the linked list to update at
 * @value: value to replace if found
 *
 */
void ll_update(d_linked_list *llist, int index, int value)
{
    dnode *curr = llist->head;
    int i = 0;
    for (; curr != NULL && i < index; i++) {
        curr = curr->next;
    }
    if (curr != NULL && i == index) {
        curr->value = value;
    }
}

/**
 * ll_search_key - Searches the linked list for a key match
 * @llist: doubly linked list pointer
 * @key: key string
 * @key_len: key string length
 *
 * Description:
 * This is hash table specific since a key will always be unique
 * in the linked list - returns negative if not found.
 */
int ll_search_key(d_linked_list *llist, char *key, int key_len)
{
    if (llist) {
        /* check if llist is a valid pointer - hash table specific */
        dnode *curr = llist->head;
        for (int i = 0; curr != NULL; i++) {
            if (strncmp(key, curr->key, (size_t) key_len) == 0)
                return i;
            curr = curr->next;
        }
    }
    return -1;
}

/**
 * ll_reverse - Reverse the doubly linked list pointers
 * @llist: doubly linked list pointer
 *
 * Description:
 * This was originally for a singly linked list haha..
 */
void ll_reverse(d_linked_list **llist)
{
    dnode *curr = (*llist)->head;
    dnode *before = curr;
    while (curr != NULL) {
        if (curr->prev != NULL) {
            before->next = before->prev;
            before->prev = curr;
        }
        before = curr;
        curr = curr->next;
    }
    before->next = before->prev;
    before->prev = NULL;

    dnode *prev_head = (*llist)->head;
    dnode *prev_tail = (*llist)->tail;
    /* need to NULL the end pointers */
    (*llist)->head = prev_tail;
    (*llist)->head->prev = NULL;
    (*llist)->tail = prev_head;
    (*llist)->tail->next = NULL;
}

/**
 * ll_pop - Remove and return the tail element of llist
 * @llist: pointer to doubly linked list
 * @err: if error, return negative else positive
 *
 * Description:
 * Returns the last element of the linked list, if it isn't found,
 * both value and err are negative.
 */
int ll_pop(d_linked_list **llist, int *err)
{
    dnode *curr = (*llist)->tail;
    int val = -1;  /* default error */
    *err = 1;  /* default no error */

    if (curr == NULL) {
        /* empty list */
        *err = -1;
    } else if (curr->prev == NULL) {
        /* check if we only have one entry */
        val = curr->value;
        free(curr);
        (*llist)->head = NULL;
        (*llist)->tail = NULL;
        (*llist)->size--;
   } else {
        val = curr->value;
        curr = curr->prev;  /* back-track one */
        free(curr->next);   /* now free tail */
        curr->next = NULL;
        (*llist)->tail = curr;
        (*llist)->size--;
   }
   return val;
}

/**
 * ll_delete - Remove node at index from the linked list
 * @llist: doubly linked list pointer
 * @index: index at which to remove node
 *
 * TODO:
 * - the #ifdefs look HORRIBLE - need to change this!
 *
 */
void ll_delete(d_linked_list **llist, int index)
{
    dnode *curr = (*llist)->head;
    int i = 1;
    for (; curr != NULL && curr->next != NULL && i < index; i++) {
        curr = curr->next;
    }

    if (index > (*llist)->size
            || i != index
            || curr == NULL) {
#if defined(LL_DEBUG) || !defined(HASH_TABLE)
        printf("Unable to delete at index: %d, list size = %d\n",
               index, (*llist)->size);
#endif
    } else if (curr->next == NULL) {
#if defined(LL_DEBUG) || !defined(HASH_TABLE)
        printf("Node to delete - i: %d, val: %d\n", i, curr->next->value);
#endif
        free(curr);
        (*llist)->head = NULL;
        (*llist)->tail = NULL;
        (*llist)->size--;
    } else {
#if defined(LL_DEBUG) || !defined(HASH_TABLE)
        printf("Node to delete - i: %d, val: %d\n", i, curr->next->value);
#endif
        dnode *end = curr->next->next;
        free(curr->next);
        curr->next = end;
        end->prev = curr;
        (*llist)->size--;
    }
}

void ll_print(d_linked_list *llist)
{
    dnode *curr = llist->head;
    for (int i = 0; curr != NULL; i++) {
        printf("i: %d, val: %d\n", i, curr->value);
        curr = curr->next;
    }
}

#ifndef HASH_TABLE
int main(int argc, char **argv)
{
    d_linked_list *llist = ll_create();

    printf("\n-----------------------------------------------------------\n");
    printf("Inserting into linked list - loop\n");
    printf("-----------------------------------------------------------\n");
    for (int i = 0; i < 8; i++) {
        ll_append(&llist, NULL, 0, i);
    }

    printf("\n-----------------------------------------------------------\n");
    printf("Printing out linked list\n");
    printf("-----------------------------------------------------------\n");
    ll_print(llist);

    printf("\n-----------------------------------------------------------\n");
    printf("Manually deleting from linked list\n");
    printf("-----------------------------------------------------------\n");
    ll_delete(&llist, 4);
    ll_delete(&llist, 1000);

    printf("\n-----------------------------------------------------------\n");
    printf("Printing out linked list\n");
    printf("-----------------------------------------------------------\n");
    ll_print(llist);

    printf("\n-----------------------------------------------------------\n");
    printf("Manually inserting into linked list\n");
    printf("-----------------------------------------------------------\n");
    /* ll_insert(llist, index, key, key_len, value); */
    ll_insert(&llist, 3, NULL, 0, 99);

    printf("\n-----------------------------------------------------------\n");
    printf("Printing out linked list\n");
    printf("-----------------------------------------------------------\n");
    ll_print(llist);

    printf("\n-----------------------------------------------------------\n");
    printf("Reversing linked list\n");
    printf("-----------------------------------------------------------\n");
    ll_reverse(&llist);

    printf("\n-----------------------------------------------------------\n");
    printf("Printing out linked list\n");
    printf("-----------------------------------------------------------\n");
    ll_print(llist);

    printf("\n-----------------------------------------------------------\n");
    printf("Pop all items in linked list - tail\n");
    printf("-----------------------------------------------------------\n");
    for (int err = 1; err == 1;) {
        int val = ll_pop(&llist, &err);
        if (err == 1)
            printf("val: %d\n", val);
    }

    ll_destroy(llist);

    return 0;
}
#endif