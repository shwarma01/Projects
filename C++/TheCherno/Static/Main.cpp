#include <iostream>

//extern int s_variable; // get rid of static in "static" in Static.cpp

void function() {

}

struct Entity {
	static int x, y;

	void print() { // if you make the methods static then they can only access static variables
		// If you want to access non static variables then you need to pass an instance of the class into the method
		std::cout << x << y << std::endl;
	}
};

// this is only needed if you have static variables;
int Entity::x;
int Entity::y;

int main() {
	Entity e;
	e.x = 2;
	e.y = 3;

	//Entity r = { 5, 8 }; use this if x and y aren't static
	Entity r;
	r.x = 5;
	r.y = 8;

	e.print();
	r.print();

	return 0;
}