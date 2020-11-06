#include <iostream>

int Multiply(int a, int b) {
	return a * b;
}

void MultiplyAndLog(int a, int b) {
	std::cout << Multiply(a, b) << std::endl;
}

int main() {
	std::cout << Multiply(1, 2) << std::endl;
	MultiplyAndLog(8, 5);
}