#ifndef FIFO_QUEUE

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct node
{
    int data;
    struct node *next;
} node;
typedef node *fifo;

extern fifo fifo_queue;
extern node *head;
extern node *tail;

void insert_item(int data);
void remove_item();
void remove_fifo();

#endif
