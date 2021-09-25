// https://programmers.co.kr/learn/courses/30/lessons/1829?language=java

import java.util.LinkedList;

class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        boolean[][] visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) {
                    if (picture[i][j] != 0) {
                        int group = picture[i][j];
                        int y = i;
                        int x = j;
                        // BFS ㄱ
                        int nodeNumber = 0;
                        LinkedList<Integer> queue = new LinkedList<Integer>();
                        queue.add(nodeNumber);
                        while (queue.isEmpty()) {
                            if (y == 0) {
                                if (x == 0) {

                                }
                            }
                        }
                    }
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}

[
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]