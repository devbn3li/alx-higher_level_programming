#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * 
 * @list: ptr to the list
 *
 * Return: 0 if there is no cycle, 1 if there
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
