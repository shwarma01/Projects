#include <iostream>

#define LOG(x) std::cout << x << std::endl;

void increment(int& value) {
	value++:
}

int main() {
	int a = 5;
	int& ref = a;
	increment(a);
	LOG(a);
	
	return 0;
}