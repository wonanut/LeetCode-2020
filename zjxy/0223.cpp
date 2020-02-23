/*
 * 字节校园编程题：0223
 * 分析：这是一道经典的动态规划题目，最短路径即曼哈顿距离，从起点出发后只向右和向下移动即可
 * 由于不能穿过对角线，上半三角和下半三角的路径是镜像的，因此只用考虑上半个三角中的路线，得到的结果×2即可。
 */

#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;


int main() {
	vector<vector<int>> dp;
	int N;
	cin >> N;
	dp.resize(N + 1);
	for (int i = 0; i < N + 1; i++ ) dp[i].resize(N + 1);
	dp[1][1] = 1;
	for (int i = 1; i < N + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			// 往下走
			if (i > 1 && i <= j) dp[i][j] += dp[i - 1][j];
			// 往右走
			if (j > 1 && i <= j) dp[i][j] += dp[i][j - 1];
		}
	}

	return dp[N][N] * 2;
}