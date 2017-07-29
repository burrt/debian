#include <stdio.h>
#include <stdlib.h>
#include "fifo_queue.h"

int main(int argc, char **argv)
{
    node *curr = NULL;

    insert_item(1);
    insert_item(2);
    insert_item(3);
    insert_item(4);
    insert_item(5);

    remove_item();

    curr = fifo_queue;
    while (curr != NULL)
    {
        printf("[%d]->", curr->data);
        curr = curr->next;
    }
    printf("NULL\n");

    remove_fifo();
    printf("Removed FIFO\n");

    return 0;
}
