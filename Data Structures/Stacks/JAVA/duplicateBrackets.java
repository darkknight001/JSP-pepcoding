import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner s  = new Scanner(System.in);
        
        String exp = s.nextLine();
        
        Stack<Character> stk = new Stack<>();
        boolean flag=false;
        for(int i  = 0; i < exp.length(); i++){
            char ch = exp.charAt(i);
            
            if(ch!=')'){
                stk.push(ch);
            }
            
            else{
                // if(stk.size()==0){
                //     System.out.println("false");
                // }
                int c = 0;
                while(stk.peek()!='('){
                    char n = stk.pop();
                    c++;
                }
                stk.pop();
                if(c==0){
                    flag = true;
                    break;
                }
            }
        
        }
        if(flag==true){
            System.out.println("true");
        }
        else{
            System.out.println("false");
        }
        
    }

}