#include "sort.h"

/**
 * insertion_sort_list - function that sorts in ascending order
 * @list: the array to be sorted
 * Return: this function doesn't return
 */

void insertion_sort_list(listint_t **list)
{
	listint_t *curr;

	if (!list)
		return;
	if ((*list)->next == NULL)
		return;
	curr = (*list)->next;
	while (list)
	{
		if (curr->next != NULL && curr->n < curr->prev->n)
		{
			curr->next = ;
		}
	}
	*list = (*list)->next;
	print_list(*list);
}
}
