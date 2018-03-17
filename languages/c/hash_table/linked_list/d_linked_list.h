
/* Doubly-linked-list node */
typedef struct node {
    char *key;  /* hash table specific */
    int value;
    struct node *prev;
    struct node *next;
} dnode;

typedef struct d_linked_list {
    dnode *head;
    dnode *tail;
    int size;
} d_linked_list;


d_linked_list *ll_create();

void ll_destroy(d_linked_list *llist);

dnode *ll_create_node(char *key, int key_len, int value);

void ll_append(d_linked_list **llist, char *key, int key_len, int val);

void ll_insert(d_linked_list **llist, int index, char *key, int key_len, int val);

void ll_update(d_linked_list *llist, int index, int value);

int ll_pop(d_linked_list **llist, int *err);

void ll_delete(d_linked_list **llist, int index);

void ll_reverse(d_linked_list **llist);

void ll_print(d_linked_list *llist);

/* Hash table specific */
int ll_search_key(d_linked_list *llist, char *key, int key_len);
