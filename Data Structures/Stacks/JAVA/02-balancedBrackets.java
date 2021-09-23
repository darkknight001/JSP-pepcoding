import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner s  = new Scanner(System.in);
        
        String exp = s.nextLine();
        
        Stack<Character> stk = new Stack<>();
        boolean flag=true;
        for(int i  = 0; i < exp.length(); i++){
            char ch = exp.charAt(i);
            
            if(ch=='(' || ch=='{' || ch=='['){
                stk.push(ch);
            }
            
            if(ch==')' || ch=='}' || ch==']'){
                if(stk.size()==0){
                    flag = false;
                    break;
                }
                if (ch==')'){
                   if(stk.peek()!='('){
                        flag = false;
                        break;
                    } 
                    stk.pop();
                }
                else if (ch=='}'){
                   if(stk.peek()!='{'){
                        flag = false;
                        break;
                    } 
                    stk.pop();
                }
                else{
                   if(stk.peek()!='['){
                        flag = false;
                        break;
                    } 
                    stk.pop();
                }
                
            }
        
        }
        if(flag==true && stk.size()==0){
            System.out.println("true");
        }
        else{
            System.out.println("false");
        }
    }

}