import java.util.LinkedList;

class Solution {
	public int[] solution(int m, int n, int[][] picture) {
		int numberOfArea = 0;
		int maxSizeOfOneArea = 0;
		boolean[][] visited = new boolean[m][n];
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (!visited[i][j] && picture[i][j] != 0) {
					int group = picture[i][j];
					// BFS
					LinkedList<int[]> queue = new LinkedList<int[]>();
					queue.add(new int[] { i, j });
					numberOfArea++;
					int size = 0;
					while (!queue.isEmpty()) {
						int[] pos = queue.pop();
						if (visited[pos[0]][pos[1]]) {
							continue;
						}
						size++;
						visited[pos[0]][pos[1]] = true;
						for (int y = pos[0] - 1; y <= pos[0] + 1; y++) {
							if (y < 0) {
								continue;
							}
							if (y >= m) {
								break;
							}
							for (int tempX = pos[1] - 1; tempX <= pos[1] + 1; tempX++) {
								if (tempX < 0) {
									continue;
								}
								if (tempX >= n) {
									break;
								}
								int x = 0;
								if (y == pos[0]) {
									x = tempX;
								} else {
									x = pos[1];
									tempX = n;
								}
								if (group == picture[y][x]) {
									queue.add(new int[] { y, x });
								}
							}
						}
					}
					maxSizeOfOneArea = size > maxSizeOfOneArea ? size : maxSizeOfOneArea;
				}
			}
		}

		int[] answer = new int[2];
		answer[0] = numberOfArea;
		answer[1] = maxSizeOfOneArea;
		return answer;
	}
}