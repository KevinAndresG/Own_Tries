#include <stdio.h>
#include <string.h>

int main(void)
{
	int list[] = {5, 1, 2, 3, 4, 6, 7, 8, 9, 100};
	int run, run2, save, list2;
	int length = sizeof(list) / sizeof(int);
	for (run = 0; run < length; run++)
	{
		save = list[run];
		for (run2 = 0; run2 < length; run2++)
		{
			if (list[run2] > save)
			{
				save = list[run2];
			}
		}
	}
	printf("%d\n", save);
	return (save);
}
