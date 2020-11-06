#include <iostream>

class Entity {
public:
	int X, Y;

	Entity() {
		X = 0;
		Y = 0;
	}

	Entity(int x, int y) {
		X = x;
		Y = y;
	}

	void print() {
		std::cout << X << ", " << Y << std::endl;
	}
};

int main() {
	Entity e1;
	e1.print();

	Entity e2(10, 5);
	e2.print();

	return 0;
}