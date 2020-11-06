#include "Log.h"

int main() {
	int x = 5;
	bool comparisonResult = (x == 5);
	
	if (comparisonResult) {
		InitLog();
	}

	const char* ptr = nullptr;
	if (ptr) {
		Log("Hello World!");
	}
	else if (ptr == "Hello") {
		Log("Pointer is Hello");
	}
	else {
		Log("Pointer is null");
	}

	return 0;
}