#include <iostream>

int main() {

	for (int i = 0; i < 5; i++) {
		std::cout << "Hello" << std::endl;
	}

	int i = 0;

	while (i < 5) {
		std::cout << "World" << std::endl;
		i++;
	}

	i = 0;

	do {
		std::cout << "!" << std::endl;
		i++;
	} while (i < 5);

	return 0;
}