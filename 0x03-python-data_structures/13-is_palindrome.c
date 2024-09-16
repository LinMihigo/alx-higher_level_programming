#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 *
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the pointer of the head of the list.
 *
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *first_half, *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	/* Find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse the second half of the list */
	second_half = reverse_list(slow);
	first_half = *head;

	/* Compare the first and the reversed second half */
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			reverse_list(second_half); /* Restore the list */
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	reverse_list(slow); /* Restore the list */
	return (1);
}
