#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

listint_t *reverse_list(listint_t *head);
listint_t *find_middle(listint_t **head);
int compare_lists(listint_t *list1, listint_t *list2);
void reconnect_list(listint_t *middle, listint_t *second_half);

#endif /* LISTS_H */
