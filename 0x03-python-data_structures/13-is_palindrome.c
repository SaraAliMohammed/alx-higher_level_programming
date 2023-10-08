#include "lists.h"
/**
 * chk_palindrome - checksif is a palindrome.
 * @head: head pointer
 * @end: end poiter
 *
 * Return: 0 if it is not a palindrome,
 *      1 if it is a palindrome
 */
int chk_palindrome(listint_t **head, listint_t *end)
{
	if (!end)
		return (1);
	if (chk_palindrome(head, end->next) && ((*head)->n == end->n))
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head pointer
 *
 * Return: 0 if it is not a palindrome,
 *      1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	return (chk_palindrome(head, *head));
}
