//https://programmers.co.kr/learn/courses/30/lessons/1835
// 경우의 수가 8! 이기 때문에 DFS 돌리면 가능
// 8중 for 문 사용 역시 가능하지만 시간복잡도상 손해
// 좀 더 공부해야 할 것
class Solution {
	private int answer = 0;
	private String[] member = { "A", "C", "F", "J", "M", "N", "R", "T" };

	public int solution(int n, String[] data) {
		boolean[] isVisited = new boolean[8];
		dfs("", isVisited, data);
		return answer;
	}

	private void dfs(String names, boolean[] isVisited, String[] datas) {
		if (names.length() == 7) {
			if (check(names, datas)) { // 조건만족 체크
				answer++;
			}
			return;
		}
		for (int i = 0; i < 8; i++) { // 조합
			if (!isVisited[i]) {
				isVisited[i] = true;
				String name = names + member[i];
				dfs(name, isVisited, datas);
				isVisited[i] = false;
			}
		}
	}

	// 조건대로 섰는지 체크
	private boolean check(String names, String[] datas) {
		for (String data : datas) {
			int position1 = names.indexOf(data.charAt(0));
			int position2 = names.indexOf(data.charAt(2));
			char op = data.charAt(3);
			int index = data.charAt(4) - '0';
			if (op == '=') {
				if (!(Math.abs(position1 - position2) == index + 1)) {
					return false;
				}
			} else if (op == '>') {
				if (!(Math.abs(position1 - position2) > index + 1)) {
					return false;
				}
			} else if (op == '<') {
				if (!(Math.abs(position1 - position2) < index + 1)) {
					return false;
				}
			}
		}
		return true;
	}
}