/*
 * 字节校园编程题：0225 - 需求安排
 * 贪心算法
 */

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Work {
public:
	int start;
	int last;
	int end;
	Work(int l) : start(0), last(l) ,end(0) {}
};

// 比较函数，结束时间早的在前面
bool cmp(Work& work1, Work& work2) {
	return work1.end <= work2.end;
}

int main() {
	vector<Work> work_list;
	int inp;
	while(cin >> inp) {
		work_list.push_back(Work(inp));
		char c = cin.get();
		if (c == '\n') break;
	}
	for (int i = 0; i < work_list.size(); ++i) {
		int end;
		cin >> end;
		work_list[i].end = end;
		work_list[i].start = end - work_list[i].last + 1;
	}

	// 对需求按deadline日期进行升序排序
	sort(work_list.begin(), work_list.end(), cmp);

	int ans = 0;
	int next_start = 0;
	for (int i = 0; i < work_list.size(); ++i) {
		if (work_list[i].start >= next_start) {
			ans++;
			next_start = work_list[i].end + 1;
		}
	}
	cout << ans;
	system("pause");
	return 0;
}