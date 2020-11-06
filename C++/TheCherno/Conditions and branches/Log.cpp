#include <iostream>
#include "Log.h"

void Log(const char* msg) {
	std::cout << msg << std::endl;
}

void InitLog() {
	Log("Initializing Log");
}