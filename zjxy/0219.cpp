/*
 * 字节校园编程题：0219-信息解密
 * 分析：这是一道经典的动态规划题目，最短路径即曼哈顿距离，从起点出发后只向右和向下移动即可
 * 由于不能穿过对角线，上半三角和下半三角的路径是镜像的，因此只用考虑上半个三角中的路线，得到的结果×2即可。
 */

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

string func() {
	vector<int> ans;
	int N, K;
	string S;
	cin >> N >> K;
	cin >> S;
	
	int temp = S[0] - '0';
	for (int i = 0;i < N; i++) {
		if (i > 0) {
			// xor S[i] 并去掉xor S[i-1]
			temp = temp ^ S[i - 1] ^ S[i];
			// xor ans[i-1]
			temp ^= ans[i - 1];
		}
		if (i >= K) {
			temp ^= ans[i - K];
		}
		ans.push_back(temp);
	}
	stringstream ss;
	string res;
	copy(ans.begin(),ans.end(),ostream_iterator<int>(ss,""));
	return ss.str();;
}