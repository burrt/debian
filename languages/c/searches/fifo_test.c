#include <stdio.h>
#include <stdlib.h>
#include "fifo_queue.h"

int main(int argc, char **argv)
{
    fifo *fifo_queue = create_fifo();

    insert_item(fifo_queue, 1);
    insert_item(fifo_queue, 2);
    insert_item(fifo_queue, 3);
    insert_item(fifo_queue, 4);
    insert_item(fifo_queue, 5);

    remove_item(fifo_queue);

    node *curr = fifo_queue->head;
    while (curr != NULL)
    {
        printf("[%d]->", curr->data);
        curr = curr->next;
    }
    printf("NULL\n");

    remove_fifo(fifo_queue);

    return 0;
}
