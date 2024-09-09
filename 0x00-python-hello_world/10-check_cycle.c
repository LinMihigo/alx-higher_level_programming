#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the linked list struct
 * Return: 0 (No cycle), 1 (There is a cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *ahead;

	if (!list || !list->next)
		return (0);

	current = list;
	ahead = list->next;
	while (current != ahead)
	{
		if (!ahead || !ahead->next)
			return (0);
		current = current->next;
		ahead = ahead->next->next;
	}
	return (1);
}
