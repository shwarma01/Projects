#include <iostream>

enum Example : unsigned char { // makes all the elements take unsigned char amount of memory
	A = 5, B, C // A = 5, B = 6, C = 7
};

int main() {
	Example value = B;

	return 0;
}