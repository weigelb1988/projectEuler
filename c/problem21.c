/**
 *
 * Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 * If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
 *
 * For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
 *
 * Evaluate the sum of all the amicable numbers under 10000.
 *
 */

#include <stdio.h>


unsigned int sum_divisors(unsigned int num);
unsigned int is_amicable(unsigned int num);

/*
 * Returns the sum of the proper divisors of the passed in number
 */
unsigned int sum_divisors(unsigned int num) {
	int i = 0;
	int x = 0;
	unsigned int a_sum = 0;
	for (i = 1; i < num; i++) {
		if (num % i == 0) {
			a_sum = a_sum + i;
		}
	}
	return a_sum;
}
/**
 * check to see if the passed in number is amicable
 *
 * Returns:
 * 	0 is not amicable
 * 	1 if is amicable
 */
unsigned int is_amicable(unsigned int num) {
	unsigned int sumDiv = sum_divisors(num);
	unsigned int bSumDiv = sum_divisors(sumDiv);
	if (num == bSumDiv && bSumDiv != sumDiv) {
		return 1;
	}
	return 0;
}

int main() {
	unsigned int i = 0;
	unsigned int runningTot = 0;
	for (i = 1; i < 10000; i++) { //stay under 10000
		if (is_amicable(i) == 1) {
			runningTot = runningTot + i; //add to total
		}
	}
	printf("TOTAL: %d\n\n", runningTot);

	return 0;
}
