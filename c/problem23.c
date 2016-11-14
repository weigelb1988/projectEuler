/*
 * A perfect number is a number for which the sum of its proper divisors is exactly equal
 *  to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
 *  which means that 28 is a perfect number.
 *
 * A number n is called deficient if the sum of its proper divisors is less
 * than n and it is called abundant if this sum exceeds n.
 *
 * As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
 * that can be written as the sum of two abundant numbers is 24. By mathematical
 * analysis, it can be shown that all integers greater than 28123 can be written as the
 * sum of two abundant numbers. However, this upper limit cannot be reduced any further
 * by analysis even though it is known that the greatest number that cannot be
 * expressed as the sum of two abundant numbers is less than this limit.
 *
 * Find the sum of all the positive integers which cannot be written as the sum of
 * two abundant numbers.
 *
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct node_s {
	int data;
	struct node_s *next;
} node;

#define MAX_NON_ABUNDANT 28123 /* see above */

unsigned int sum_divisors(unsigned int num);
unsigned int is_abundant(unsigned int num);

/*
 * Returns the sum of the proper divisors of the passed in number
 */
unsigned int sum_divisors(unsigned int num) {
	int i = 0;
	unsigned int a_sum = 1;
	for (i = 2; i * i < num; ++i) {
		int p = 1;
		while (num % i == 0) {
			p = p * i + 1;
			num = num / i;
		}
		a_sum = a_sum * p;
	}
	if (num > 1) {
		a_sum = a_sum * (1 + num);
	}
	return a_sum;
}
/*
 * Checks it see if the number is abundant.
 * A number is called abundant if this sum of divisors exceeds the passed in number
 *
 * Returns:
 * 		1 if it is abundant
 * 		0 if it is not.
 *
 */
unsigned int is_abundant(unsigned int num) {
	int i = 0;
	unsigned int sum = sum_divisors(num);
	if (num < sum) {
		return 1;
	}
	return 0;
}

struct test_struct {
	int val;
	struct test_struct *next;
};

struct test_struct *head = NULL;
struct test_struct *curr = NULL;

struct test_struct* create_list(int val) {
	printf("\n creating list with headnode as [%d]\n", val);
	struct test_struct *ptr = (struct test_struct*) malloc(
			sizeof(struct test_struct));
	if (NULL == ptr) {
		printf("\n Node creation failed \n");
		return NULL;
	}
	ptr->val = val;
	ptr->next = NULL;

	head = curr = ptr;
	return ptr;
}

struct test_struct* add_to_list(int val) {
	if (NULL == head) {
		return (create_list(val));
	}

	struct test_struct *ptr = (struct test_struct*) malloc(
			sizeof(struct test_struct));
	if (NULL == ptr) {
		printf("\n Node creation failed \n");
		return NULL;
	}
	ptr->val = val;
	ptr->next = NULL;

	ptr->next = head;
	head = ptr;
	return ptr;
}

struct test_struct* search_in_list(int val, struct test_struct **prev) {
	struct test_struct *ptr = head;
	struct test_struct *tmp = NULL;
	int found = 0;

	while (ptr != NULL) {
		if (ptr->val == val) {
			found = 1;
			break;
		} else {
			tmp = ptr;
			ptr = ptr->next;
		}
	}

	if (1 == found) {
		if (prev)
			*prev = tmp;
		return ptr;
	} else {
		return NULL;
	}
}

int delete_from_list(int val) {
	struct test_struct *prev = NULL;
	struct test_struct *del = NULL;

	del = search_in_list(val, &prev);
	if (del == NULL) {
		return -1;
	} else {
		if (prev != NULL)
			prev->next = del->next;

		if (del == curr) {
			curr = prev;
		} else if (del == head) {
			head = del->next;
		}
	}

	free(del);
	del = NULL;

	return 0;
}

void print_list(void) {
	struct test_struct *ptr = head;

	printf("\n -------Printing list Start------- \n");
	while (ptr != NULL) {
		printf("\n [%d] \n", ptr->val);
		ptr = ptr->next;
	}
	printf("\n -------Printing list End------- \n");

	return;
}

unsigned int sum_list() {
	struct test_struct *ptr = head;
	unsigned int total = 0;
	while (ptr != NULL) {
		total = total + ptr->val;
		ptr = ptr->next;
	}
	return total;
}

/**
 * main function
 */
int main() {
	unsigned int i = 0;
	unsigned int x = 0;
	long total = 0;

	/* fill a linked list with all the possible numbers to add up*/
	for (i = 0; i < MAX_NON_ABUNDANT; i++) {
		add_to_list(i);
	}
	for (i = 0; i < MAX_NON_ABUNDANT; i++) {
		if (is_abundant(i) == 1) { // abundant
			for (x = 0; x <= i; x++) {
				if (is_abundant(x) == 1) {
					/* remove sum of 2 abundant numbers */
					delete_from_list((x + i));
				}
			}
		}
		if(i%200==0){
			printf("%d\n", i);
		}
	}
	printf("\nTOTAL: %d\n", sum_list());
	return 0;
}
