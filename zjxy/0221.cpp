// 字节校园学习挑战赛-0221
// 感觉这道题就是背包问题的变形吧，没有测试用例不知道有没有什么毛病

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Game {
public:
	int a_i;
	int b_i;
	int w_i;
	Game(int a, int b, int w) : a_i(a), b_i(b), w_i(w) {}
};

int main() {
	// 输入数据
	int n, X;
	vector<Game> game_vector;
	cin >> n >> X;
	for (int i = 0; i < n; i++) {
		int a, b, w;
		cin >> a >> b >> w;
		game_vector.push_back(Game(a, b, w));
	}

	// 定义dp矩阵:dp[i][j]表示购买前i个游戏后剩余可购买'金额'
	vector<vector<int>> dp(n+1);
	for (int i = 0; i < n + 1; i++) { dp[i].resize(X + 1); }

	// 状态转移方程更新dp矩阵
	for (int i = 1; i < n + 1; i++) {
		for(int j = 1; j < X + 1; j++) {
			// 买不起就不买当前游戏
			int temp = max(game_vector[i - 1].a_i - game_vector[i - 1].b_i - game_vector[i - 1].w_i, 0);
			if (j < temp) { 
				dp[i][j] = dp[i - 1][j];
			} 
			// 如果买得起当前游戏，权衡一下取其大
			else {
				dp[i][j] = max(dp[i - 1][j - temp] + game_vector[i - 1].w_i, dp[i - 1][j]);
			}
		}
	}
	return dp[n][X];
}