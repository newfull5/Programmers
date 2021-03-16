// 자바는 진짜 이번학기만 끝나면 다신 안할거다.

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public static boolean ithas(ArrayList<Integer> arr, int num){

        for (int i = 0; i < arr.size(); i++){
            if (arr.get(i) == num){
                return true;
            }
        }
        return false;
    }
    
    public int[] solution(int[] numbers) {
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i = 0; i < numbers.length-1; i++){
            for (int j = i+1; j < numbers.length; j++){
                int sum = numbers[i] + numbers[j];
                if (!ithas(answer, sum)){
                    answer.add(sum);
                }

            }
        }

        int[] outputs = new int[answer.size()];
        
        for (int i = 0; i < outputs.length; i++){
            outputs[i] = answer.get(i);
        }

        Arrays.sort(outputs);
        
        return outputs;
    }
}
