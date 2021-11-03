// https://programmers.co.kr/learn/courses/30/lessons/42583


import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> bridge = new LinkedList<>();
        for(int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }
        int nowWeight = 0;
        
        for (int i = 0; i < truck_weights.length; i++) {
            answer++;
            int truck = truck_weights[i];
            nowWeight -= bridge.poll();
            while (nowWeight + truck > weight) {
                answer++;
                nowWeight -= bridge.poll();
                bridge.offer(0);
            }
            bridge.offer(truck);
            nowWeight += truck;
        }
        answer += bridge_length;
        return answer;
    }
}
