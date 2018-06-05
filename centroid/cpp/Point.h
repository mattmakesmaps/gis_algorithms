#pragma once
#include <ostream>
#include <cmath>

class Point
{
public:
	Point(double x, double y) :
		m_x(x), m_y(y)
	{
	}

	// __len__(self)
	int size() const;

	// __getitem__(self, i)
	// The const method returning a const reference
	// allows for "read-only" access.
	const double& operator[] (int index) const;

	const double & distance(Point & other) const;

	~Point();

private:
	double m_x;
	double m_y;
};

// __str__ and __repr__
std::ostream& operator<<(std::ostream& os, const Point& probe);