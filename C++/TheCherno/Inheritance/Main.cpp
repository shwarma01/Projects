#include <iostream>

class Entity {
public:
	float x, y;

	void move(float xa, float ya) {
		x += xa;
		y += ya;
	}
};

class Player : public Entity {
public:
	const char* name;

	void printName() {
		std::cout << name << std::endl;
	}
};

int main() {
	Player player;
	player.move(1, 1);

	return 0;
}