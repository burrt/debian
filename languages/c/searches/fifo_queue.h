#ifndef FIFO_QUEUE

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>


typedef struct node
{
    int data;
    struct node *next;
} node;

typedef struct queue
{
    int size;
    struct node *head;
    struct node *tail;
} fifo;


fifo *create_fifo();
void insert_item(fifo *f, int data);
void remove_item(fifo *f);
void remove_fifo(fifo *f);

#endif
