/*
 * 0301-最大连续子列和
 * 在线处理
 */

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int func0301() {
	int N;
	vector<int> vec;

	cin >> N;
	int inp;
	for (int i = 0; i < N; ++i) {
		cin >> inp;
		vec.push_back(inp);
	}

	int ret = 0, temp_sum = 0;
	for (int i = 0; i < N; i++) {
		temp_sum += vec[i];
		if (temp_sum < 0) temp_sum = 0;
		if (temp_sum > ret) ret = temp_sum; 
	}
	return ret;
}

int main() {
	cout << func0301();
	system("pause");
	return 0;
}