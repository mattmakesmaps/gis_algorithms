#include "stdafx.h"
#include "Point.h"
#include <vector>
#include <iostream>

/*
Port of Listing 2.4 GIS Algorithms, Xiao.
*/

std::pair<double, Point> centroid(std::vector<Point> & pgon) {
	/*
	Calculates the centroid and area of a polygon.
	Input
		pgon: a vector of Point objects representing a valid polygon.
	Output
		std::pair<double, Point>: double is the area, Point is the centroid
	*/

	auto numvert = pgon.size();
	double A = 0;
	double xmean = 0;
	double ymean = 0;
	for (auto i = 0; i < (numvert - 1); ++i)
	{
		auto ai = pgon[i][0] * pgon[i + 1][1] - pgon[i + 1][0] * pgon[i][1];
		A += ai;

		// Accessing `x` and `y` via subscript rather then named params.
		xmean += (pgon[i + 1][0] + pgon[i][0]) * ai;
		ymean += (pgon[i + 1][1] + pgon[i][1]) * ai;
	}
	A = A / 2.0;
	auto C = Point(xmean / (6 * A), ymean / (6 * A));
	return std::pair<double, Point>(A, C);
}

int main() {
	std::vector<Point> polygon = {
		Point(0,10), Point(5,0), Point(10,10), Point(15,0), Point(20,10), 
		Point(25,0), Point(30,20), Point(40,20), Point(45,0), Point(50,50), 
		Point(40,40), Point(30,50), Point(25,20), Point(20,50), Point(15,10), 
		Point(10,50), Point(8,8), Point(4,50), Point(0,10)
	};
	auto result = centroid(polygon);
	std::cout << result.first << ", " << result.second;
	std::cout << std::endl;
}