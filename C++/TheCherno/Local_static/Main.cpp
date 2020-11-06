#include <iostream>

void function() {
	static int i = 0; // Every call of the function will refer to the same memory address of the first call of the function
	int j = 0;
	i++;
	j--;
	std::cout << i << " " << j << std::endl;
}

int main() {
	function();
	function();
	function();
	function();

	return 0;
}