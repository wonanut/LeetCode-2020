/*
 * 字节校园编程题0217 - 挖宝
 * 分析：看M和N的范围，应该是dfs没错吧，可以做一点点小优化：只从墙角出发，能降低遍历的次数
 */

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool check(vector<vector<int>>& map, int row, int col) {
	int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	int counter = 0;
	for(int i = 0; i < 4; i++) {
		int row_ = row + directions[i][0];
		int col_ = col + directions[i][1];
		if (row_ >= 0 && row_ < map.size() && col_ >= 0 && col_ < map[0].size() && map[row_][col_] > 0) counter++;
	}
	return counter <= 1;
}

int dfs(vector<vector<int>>& map, vector<vector<int>>& visited, int row, int col, int val) {
	int max_val = val;
	int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	for(int i = 0; i < 4; i++) {
		int row_ = row + directions[i][0];
		int col_ = col + directions[i][1];
		if (row_ >= 0 && row_ < map.size() && col_ >= 0 && col_ < map[0].size() && visited[row_][col_] == 0 && map[row_][col_] > 0) {
			visited[row_][col_] = 1;
			int ret = dfs(map, visited, row_, col_, val + map[row_][col_]);
			max_val = max(max_val, ret);
			visited[row_][col_] = 0;
		}
	}
	return max_val;
}

int main() {
	int N, M;
	cin >> N >> M;
	
	vector<vector<int>> map(N);
	vector<vector<int>> visited(N);
	for(int i = 0; i < N; i++) { 
		map[i].resize(M); 
		visited[i].resize(M);
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
		}
	}

	int ans = 0;
	for(int i = 0; i < N; i++) {
		for(int j = 0; j < M; j++) {
			// 寻找可能的出发点，为了降低复杂度，只选择墙角的通路作为出发点。
			if (map[i][j] > 0 && check(map, i, j)) {
				visited[i][j] = 1;
				int ret = dfs(map, visited, i , j, map[i][j]);
				ans = max(ans, ret);
				visited[i][j] = 0;
			}
		}
	}

	cout << ans;
	system("pause");

	return 0;
}