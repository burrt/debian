#include <error.h>
#include <string.h>
#include <stdlib.h>
#include "fifo_queue.h"

// Global variables
fifo fifo_queue = NULL;
node *head = NULL;
node *tail = NULL;


void insert_item(int data)
{
    // Check if we have an empty FIFO
    if (fifo_queue == NULL)
    {
        fifo_queue = (fifo) malloc(sizeof(struct node));
        assert(fifo_queue != NULL);
        fifo_queue->data = data;
        fifo_queue->next = NULL;
        head = fifo_queue;
        tail = fifo_queue;
        printf("Created FIFO: %d\n", data);
    }
    else
    {
        node *new_node = (node *)malloc(sizeof(struct node));
        assert(new_node != NULL);
        new_node->data = data;
        new_node->next = NULL;

        // Update tail to be the new node
        tail->next = new_node;
        tail = new_node;
        printf("New node: %d\n", data);
    }

}


void remove_item()
{
    assert(head != NULL);
    node *to_pop = head;
    head = head->next;
    fifo_queue = head;

    to_pop->next = NULL;
    free(to_pop);
}


void remove_fifo()
{
    assert(fifo_queue != NULL && head != NULL);
    while (head != NULL)
    {
        remove_item();
    }
}
