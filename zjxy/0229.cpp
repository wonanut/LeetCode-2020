/*
 * 0229-找零钱
 * 假定我们有若干种不同面额的硬币，希望在给出要找零的钱数以及可用的硬币面额及其数量之后，可以找出所需的最少的硬币个数的方案。
 * 思路：动态规划
 */

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> func0229() {
	int arr[] = {1, 2, 5, 10, 50};
	int amount = 38;
	vector<int> coins(begin(arr), end(arr));
	vector<int> dp(amount + 1, 0);

    for (int i = 1; i < amount + 1; i++) {
        dp[i] = amount + 1;
        for (int j = 0; j < coins.size(); j++) {
            if (i - coins[j] >= 0) {
                dp[i] = min(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }
        
    vector<int> ans;
    int pre = amount;
    int pre_coins = dp[amount];
    for (int i = amount; i >= 0; i--) {
        if (dp[i] == pre_coins - 1) {
            pre_coins --;
            ans.push_back(pre - i);
            pre = i;
        }
    }

    return ans;

}

int main() {
	func0229();
	system("pause");
	return 0;
}
