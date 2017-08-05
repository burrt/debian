#include <error.h>
#include <string.h>
#include <stdlib.h>
#include "fifo_queue.h"


fifo *create_fifo()
{
    fifo *new_fifo = (fifo *)malloc(sizeof(fifo));
    assert(new_fifo != NULL);

    new_fifo->head = NULL;
    new_fifo->tail = NULL;
    new_fifo->size = 0;
    printf("Created Fifo\n");

    return new_fifo;
}

void insert_item(fifo *f, int data)
{
    node *new_node = (node *)malloc(sizeof(struct node));
    assert(new_node != NULL);

    new_node->data = data;
    new_node->next = NULL;

    if (f->size == 0)
    {
        f->head = new_node;
        f->tail = new_node;
    }
    else
    {
        f->tail->next = new_node;
        f->tail = new_node;
    }
    f->size++;
    printf("New node: %d\n", data);
}


void remove_item(fifo *f)
{
    node *to_remove = NULL;
    if (f->size == 0)
    {
        printf("Error: Fifo is already empty!\n");
        return;
    }
    f->size--;
    to_remove = f->head;

    if (f->size == 0)
    {
        f->head = NULL;
        f->tail = NULL;
    }
    else
    {
        f->head = f->head->next;
    }
    to_remove->next = NULL;
    free(to_remove);
    printf("Removed head\n");
}


void remove_fifo(fifo *f)
{
    if (f == NULL)
    {
        printf("Error: Fifo doesn't exist!\n");
        return;
    }
    while (f->head != NULL)
        remove_item(f);
    free(f);
    printf("Fifo has been removed\n");
}
