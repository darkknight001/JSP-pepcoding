import java.io.*;
import java.util.*;

public class Main {


  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }

    int[] nsr = new int[n];
    int[] nsl = new int[n];

    Stack<Integer> st1 = new Stack<>();
    Stack<Integer> st2 = new Stack<>();
    
    for (int i  = 0; i < n; i++) {
      if (st1.size() != 0) {
        while (st1.size() > 0  && arr[st1.peek()] >= arr[i] ) {
          st1.pop();

        }
      }
      if (st1.size() != 0) {
        nsl[i] = st1.peek();
      }else{
        nsl[i] = -1;  
      }
      int curMax = arr[i];
      st1.push(i);

    }
    
    for (int i  = n-1; i >= 0; i--) {
      if (st1.size() != 0) {
        while (st2.size() > 0  && arr[st2.peek()] >= arr[i] ) {
          st2.pop();

        }
      }
      if (st2.size() != 0) {
        nsr[i] = st2.peek();
      }else{
        nsr[i] = n;  
      }
      
      int curMax = arr[i];
      st2.push(i);

    }
    
    int maxArea = 0;
    for (int i = 0; i < n; i++) {
        int temp = arr[i]*(nsr[i]-nsl[i]-1);
        if (temp>maxArea){
            maxArea = temp;
        }
    }
    
    System.out.println(maxArea);
    
  }
}