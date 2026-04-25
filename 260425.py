class Calc {
    int cc(int a, int b) {
        return a + b; 
    }
    int cc(char a, char b) {
        return a -b; 
    }
    int cc(char c) {
        return c; 
    }
}

public class Test {
    public static void main(String[] args) {
        Calc calc = new Calc(); 
        int r1 = calc.cc(5, 4); 
        int r2 = calc.cc('c','a'); 
        char r3 = (char) cal.cc('3'); 
        System.out.println(r1 + r2 + "2" + r3); 
    }
}