#include <iostream>

#define LOG(x) std::cout << x << std::endl;

class Player {
public:
	int x, y;
	int speed;

	void Move(int xa, int ya) {
		x += xa * speed;
		y += ya * speed;
	}
};

int main() {
	Player player;
	player.x = 5;
	player.y = 5;

	player.Move(1, -1);

	return 0;
}