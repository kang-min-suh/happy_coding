class A{
    String f(Object x) {
        return "1"; 
    }
    String g() {
        return f("a"); 
    }

}

class B extends A {
    String f(Object x) {
        return "2"; 
    }
    String f(String x) {
        return "3"; 
    }
}

public class Test {
    public static void main(String[] args) {
        A a = new B(); 
        System.out.pringln(a, g()); 
    }
}