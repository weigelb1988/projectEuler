#include <stdio.h>

int main(){
	int count = 1;
	unsigned long tri_num = 1;
	int i = 1;
	int x = 1;
	while (count <= 500){
		count = 2;
		for(x=1;x<tri_num/2;x++){
			if(tri_num%x == 0){
				count += 1;
			}
		}
		if(count >= 500){
			printf("ANSWER: %lu", tri_num);
		}
		i += 1;
		tri_num += i;
	}

}
