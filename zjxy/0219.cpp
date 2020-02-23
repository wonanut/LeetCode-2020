/*
 * 字节校园编程题：0219-信息解密
 * 分析：异或的应用，分析后编程实现即可。
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