import java.io.*;
import java.util.*;

public class Main {
  public static void display(int[] a) {
    StringBuilder sb = new StringBuilder();

    for (int val : a) {
      sb.append(val + "\n");
    }
    System.out.println(sb);
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    int[] a = new int[n];
    for (int i = 0; i < n; i++) {
      a[i] = Integer.parseInt(br.readLine());
    }

    int[] span = solve(a);
    display(span);
  }

  public static int[] solve(int[] arr) {
    int n = arr.length;
    int[] res = new int[n];
    Arrays.fill(res, 1);
    Stack<Integer> st = new Stack<>();

    for (int i  = 0; i < n ; i++) {
      while (st.size() > 0  && arr[st.peek()] <  arr[i] ) {
        st.pop();
      }
      if (st.size() != 0) {
        res[i] = i-st.peek();
      }else{
        res[i] = i+ 1;
      }
        int curMax = arr[i];
        st.push(i);

      }
      return res;
    }

  }
