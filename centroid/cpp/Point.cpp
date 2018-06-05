#include "stdafx.h"
#include "Point.h"

int Point::size() const
{
	return 2;
}

const double & Point::operator[](int index) const
{
	if (index == 0) {
		return m_x;
	}

	if (index == 1) {
		return m_y;
	}
}

const double & Point::distance(Point & other) const
{
	auto d_x = std::pow((this->m_x - other.m_x), 2);
	auto d_y = std::pow((this->m_y - other.m_y), 2);
	return std::sqrt(d_x + d_y);
}

Point::~Point()
{
}

std::ostream & operator<<(std::ostream & os, const Point & point)
{
	os << "(" << point[0] << "," << point[1] << ")";
	return os;
}
