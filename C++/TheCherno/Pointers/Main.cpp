#include <iostream>

#define LOG(x) std::cout << x << std::endl;

int main() {
	int* ptr = nullptr;
	int var = 8;
	LOG(ptr);

	ptr = &var;
	LOG(ptr);

	return 0;
}