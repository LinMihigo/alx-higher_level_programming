#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *middle, *second_half;
	int result;

	middle = find_middle(head);
	second_half = reverse_list(middle->next);

	result = compare_lists(*head, second_half);

	second_half = reverse_list(second_half);
	reconnect_list(middle, second_half);

	return (result);
}

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * find_middle - Finds the middle node of a linked list
 * @head: Double pointer to the head of the list
 * Return: Pointer to the middle node
 */
listint_t *find_middle(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		return (slow);
	return (prev);
}

/**
 * compare_lists - Compares two linked lists
 * @list1: First list
 * @list2: Second list
 * Return: 1 if lists are identical, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	return (1);
}

/**
 * reconnect_list - Reconnects the reversed second half of the list
 * @middle: Pointer to the middle node
 * @second_half: Pointer to the head of the second half
 */
void reconnect_list(listint_t *middle, listint_t *second_half)
{
	if (middle->next == NULL)
	{
		middle->next = second_half;
	}
	else
	{
		middle->next = second_half;
	}
}
