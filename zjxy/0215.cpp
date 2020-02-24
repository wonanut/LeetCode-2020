/*
 * 字节校园编程题0217 - naive游戏
 * 模拟可能会超时，但这个模拟程序应该是对的
 * 如果不用模拟，应该是做>和<的括号匹配问题吧。
 */

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	vector<char> vec;
	vector<vector<int>> border; 
	int n, m, q;
	cin >> n >> m >> q;
	for (int i = 0; i < n; i++) { 
		char ch;
		cin >> ch;
		vec.push_back(ch);  
	}
	
	border.resize(q);
	for (int i = 0; i < q; i++) {
		int left, right;
		cin >> left >> right;
		border[i].push_back(left);
		border[i].push_back(right);
	}

	for (int i = 0; i < q; i++) {
		vector<char> gameMap(vec);
		int score = 0;
		int left = border[i][0];
		int right = border[i][1];
		int cur = left;
		char pre = -1;						// 记录上一个箭头符号的位置，上一个位置不是箭头符号置为-1
		int direction = 1;					// 1 向右,  -1 向左
		while (cur >= left && cur <= right) {
			if (gameMap[cur] <= '9' && gameMap[cur] >= '1') {
				score += int(gameMap[cur] - '0');
				gameMap[cur] -= 1;
				pre = -1;
			}
			else if (gameMap[cur] == '0') {
				gameMap[cur] = 'X';
				pre = -1;
			}
			else if (gameMap[cur] == '<') {
				direction = -1;
				if (pre != -1 && (gameMap[pre] == '<' || gameMap[pre] == '>')) gameMap[pre] = 'X';
				pre = cur;
			}
			else if (gameMap[cur] == '>') {
				direction = 1;
				if (pre != -1 && (gameMap[pre] == '<' || gameMap[pre] == '>')) gameMap[pre] = 'X';
				pre = cur;
			}
			cur += direction;
		}
		cout << score << endl;
	}
	system("pause");
	return 0;
}